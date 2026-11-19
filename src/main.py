import random
import re

import ollama  # noqa
import pyperclip
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

from logic import generate
from model_data import *

console = Console()
console.clear()

font = Figlet(font="ansi_shadow", width=100)
header = font.renderText("NAVI SOULGEN")

start_text = f"""
[bold green]{header}[/]
digital personality (LLM prompt) generator built with [bold cyan]Python[/]
creates a unique token that defines an exact personality (244M+ combinations)
[bold magenta]personality parts:[/]
[dim]{"─" * 42}[/]
• [bold green]SOUL[/]       personality, tone, and attitude
• [bold green]SPEECH[/]     delivery style and phrasing
• [bold green]MIND[/]       logic, reasoning, and initiative
"""

start_message = Panel(
    start_text,
    title="NAVI SOULGEN v1.0",
    border_style="bold green",
)

console.print(start_message)

while True:
    try:
        action = Prompt.ask(
            "[bold green]choose action[/]",
            choices=["calibrate", "inspect", "quit"],
            default="calibrate",
        )

        if action == "quit":
            console.print("[red]Quit![/]")
            break

        elif action == "inspect":
            token = Prompt.ask("[bold green]enter token[/]")
            pattern = r"^NAVI-(EN|RU)-([1-5]{4}-[1-5]{4}-[1-5]{4})$"
            match = re.match(pattern, token)
            if not match:
                console.print(
                    "[bold red]Invalid token! Expected: NAVI-(EN/RU)-XXXX-XXXX-XXXX[/]"
                )
            else:
                lang, numbers = match.groups()
                soul, speech, mind = map(tuple, numbers.split("-"))
                prompt = generate(soul, speech, mind, lang.lower())
                Prompt.ask(
                    "[bold green]select an option[/]",
                    choices=["analyze", "prompt"],
                    default="analyze",
                )
        else:
            lang = Prompt.ask(
                "[bold green]language[/]", choices=["EN", "RU"], default="EN"
            )
            rand = Confirm.ask(
                "[bold green]random token generation:[/]",
                default=False,
            )
            if rand:
                soul = tuple(random.choices("12345", k=4))
                speech = tuple(random.choices("12345", k=4))
                mind = tuple(random.choices("12345", k=4))
            else:
                console.print(
                    "[bold magenta]calibration levels:[/]\n"
                    "[bold cyan]1 (minimal)[/]: barely present, near-zero trace\n"
                    "[bold green]2 (low)[/]: subtle, restrained, understated presence\n"
                    "[bold yellow]3 (moderate)[/]: balanced, natural baseline level\n"
                    "[bold dark_orange]4 (high)[/]: strong, prominent, dominant trait\n"
                    "[bold red]5 (extreme)[/]: absolute maximum, peak intensity"
                )
                traits = {
                    "warmth": "empathy and emotional involvement",
                    "sharpness": "degree of sarcasm and irony",
                    "chaos": "non-linear thinking and associative leaps",
                    "ego": "level of confidence and conversational dominance",
                    "verbosity": "text length and depth of detail",
                    "formality": "speech register from slang to legalese",
                    "expressiveness": "emotional intensity and tonal vividness",
                    "pedantry": "precision of terms and attention to detail",
                    "proactivity": "initiative and tendency to ask follow-ups",
                    "caution": "focus on risks, pitfalls, and safety",
                    "metaphor": "use of analogies, imagery, and allegories",
                    "skepticism": "critical scrutiny of premises and contradictions",
                }

                vals = []
                for name, desc in traits.items():
                    answer = Prompt.ask(
                        f"[bold green]{name} ({desc})[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )
                    vals.append(answer)

                soul, speech, mind = tuple(vals[:4]), tuple(vals[4:8]), tuple(vals[8:])

            token = f"NAVI-{lang}-{''.join(soul)}-{''.join(speech)}-{''.join(mind)}"
            prompt = generate(soul, speech, mind, lang.lower())

            console.print(f"[bold green]your token is:[/] {token}")
            clipboard = Prompt.ask(
                "[bold green]copy to clipboard[/]",
                choices=["prompt", "token", "none"],
                default="prompt",
            )
            if clipboard == "prompt":
                pyperclip.copy(prompt)
                console.print("[bold green]copied to clipboard![/]")
            elif clipboard == "token":
                pyperclip.copy(token)
                console.print("[bold green]copied to clipboard![/]")

    except KeyboardInterrupt:
        console.print("\n[bold red]Forcequit![/]")
        break

    except Exception as error:  # noqa: BLE001
        console.print(f"[bold red]{error}[/]")
