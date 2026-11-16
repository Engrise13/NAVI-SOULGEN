import random

from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt  # noqa

from logic import *
from model_data import *

console = Console()
console.clear()

font = Figlet(font="ansi_shadow", width=100)
header = font.renderText("NAVI SOULGEN")

start_text = f"""
[bold green]{header}[/]
digital personality (LLM prompt) generator built with [bold cyan]Python[/]
creates an unique token that defines an exact personality (244M+ combinations)
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
            choices=["calibrate", "read", "quit"],
            default="calibrate",
        )

        if action == "quit":
            console.print("[red]Quit![/]")
            break

        elif action == "read":
            pass

        else:
            lang = Prompt.ask(
                "[bold green]language[/]", choices=["EN", "RU"], default="EN"
            )
            rand = Prompt.ask(
                "[bold green]random token generation:",
                choices=["NO", "YES"],
                default="NO",
            )

            if rand == "YES":
                soul = random.choices("12345", k=4)
                speech = random.choices("12345", k=4)
                mind = random.choices("12345", k=4)
                token = f"NAVI-{lang}-{''.join(soul)}-{''.join(speech)}-{''.join(mind)}"
                console.print(f"[bold green]your token is:[/] {token}")
            else:
                pass
    except KeyboardInterrupt:
        console.print("\n[red]Forcequit![/]")
        break

    except Exception as error:  # noqa: BLE001
        console.print(f"[red]{error}[/]")
