import random
import re

import pyperclip
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

from logic import analyze, generate

console = Console()

TOKEN_PATTERN = re.compile(r"^NAVI-(EN|RU)-([1-5]{4}-[1-5]{4}-[1-5]{4})$")
LEVELS = ["1", "2", "3", "4", "5"]

TRAITS = {
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

CALIBRATION_HELP = (
    "[bold magenta]calibration levels:[/]\n"
    "[bold cyan]1 (minimal)[/]: barely present, near-zero trace\n"
    "[bold green]2 (low)[/]: subtle, restrained, understated presence\n"
    "[bold yellow]3 (moderate)[/]: balanced, natural baseline level\n"
    "[bold dark_orange]4 (high)[/]: strong, prominent, dominant trait\n"
    "[bold red]5 (extreme)[/]: absolute maximum, peak intensity"
)


def copy_to_clipboard(text: str, label: str = "copied") -> None:
    pyperclip.copy(text)
    console.print(f"[bold green]{label} to clipboard![/]")


def print_banner() -> None:
    console.clear()
    header = Figlet(font="ansi_shadow", width=100).renderText("NAVI SOULGEN")
    start_text = (
        f"\n[bold green]{header}[/]\n"
        "digital personality (LLM prompt) generator built with [bold cyan]Python[/]\n"
        "creates a unique token that defines an exact personality (244M+ combinations)\n"
        "[bold magenta]personality parts:[/]\n"
        f"[dim]{'─' * 42}[/]\n"
        "- [bold green]SOUL[/]       personality, tone, and attitude\n"
        "- [bold green]SPEECH[/]     delivery style and phrasing\n"
        "- [bold green]MIND[/]       logic, reasoning, and initiative\n"
    )
    console.print(
        Panel(start_text, title="NAVI SOULGEN v1.0", border_style="bold green")
    )


def handle_inspect() -> None:
    token = Prompt.ask("[bold green]enter token[/]").strip().upper()
    match = TOKEN_PATTERN.match(token)
    if not match:
        console.print(
            "[bold red]Invalid token! Expected: NAVI-(EN/RU)-XXXX-XXXX-XXXX[/]"
        )
        return

    lang, numbers = match.groups()
    soul, speech, mind = map(tuple, numbers.split("-"))
    prompt = generate(soul, speech, mind, lang.lower())

    choice = Prompt.ask(
        "[bold green]select an option[/]",
        choices=["analyze", "prompt"],
        default="analyze",
    )

    if choice == "prompt":
        copy_to_clipboard(prompt, "prompt copied")
        return

    model = Prompt.ask("[bold green]model[/]", default="qwen3.5:4b")
    with console.status("[bold green]analyzing personality...[/]", spinner="aesthetic"):
        result = analyze(model, lang.lower(), prompt)

    labels = (
        ("vibe", "strength", "weakness")
        if lang == "EN"
        else ("вайб", "сильная сторона", "слабая сторона")
    )
    result_text = (
        f"\n• [bold green]{labels[0]}:[/] {result['vibe']}"
        f"\n• [bold green]{labels[1]}:[/] {result['strength']}"
        f"\n• [bold green]{labels[2]}:[/] {result['weakness']}\n"
    )
    console.print(
        Panel(result_text, title=result["archetype"], border_style="bold green")
    )

    if Confirm.ask("[bold green]copy prompt to clipboard[/]"):
        copy_to_clipboard(prompt)


def handle_calibrate() -> None:
    lang = Prompt.ask("[bold green]language[/]", choices=["EN", "RU"], default="EN")
    is_random = Confirm.ask("[bold green]random token generation[/]", default=False)

    if is_random:
        vals = random.choices(LEVELS, k=12)
    else:
        console.print(CALIBRATION_HELP)
        vals = [
            Prompt.ask(
                f"[bold green]{name} ({desc})[/]",
                choices=LEVELS,
                default="3",
            )
            for name, desc in TRAITS.items()
        ]

    soul, speech, mind = tuple(vals[:4]), tuple(vals[4:8]), tuple(vals[8:])
    token = f"NAVI-{lang}-{''.join(soul)}-{''.join(speech)}-{''.join(mind)}"
    prompt = generate(soul, speech, mind, lang.lower())

    console.print(f"[bold green]your token is:[/] {token}")
    clipboard = Prompt.ask(
        "[bold green]copy to clipboard[/]",
        choices=["prompt", "token", "none"],
        default="prompt",
    )
    if clipboard != "none":
        target = prompt if clipboard == "prompt" else token
        copy_to_clipboard(target, f"{clipboard} copied")


def main() -> None:
    print_banner()
    actions = {
        "calibrate": handle_calibrate,
        "inspect": handle_inspect,
    }

    while True:
        try:
            action = Prompt.ask(
                "[bold green]choose action[/]",
                choices=[*actions.keys(), "quit"],
                default="calibrate",
            )
            if action == "quit":
                console.print("[red]Quit![/]")
                break
            actions[action]()

        except KeyboardInterrupt:
            console.print("\n[bold red]Forcequit![/]")
            break
        except Exception as error:  # noqa: BLE001
            console.print(f"[bold red]{error}[/]")


if __name__ == "__main__":
    main()
