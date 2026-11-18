import random

from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

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
                if lang == "EN":
                    console.print("1 - minimal, 5 - extreme")
                    warmth = Prompt.ask(
                        "[bold green]warmth (empathy and emotional involvement)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    sharpness = Prompt.ask(
                        "[bold green]sharpness (degree of sarcasm and irony)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    chaos = Prompt.ask(
                        "[bold green]chaos (non-linear thinking and associative leaps)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    ego = Prompt.ask(
                        "[bold green]ego (level of confidence and conversational dominance)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    verbosity = Prompt.ask(
                        "[bold green]verbosity (text length and depth of detail)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    formality = Prompt.ask(
                        "[bold green]formality (speech register from slang to legalese)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    expressiveness = Prompt.ask(
                        "[bold green]expressiveness (emotional intensity and tonal vividness)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    pedantry = Prompt.ask(
                        "[bold green]pedantry (precision of terms and attention to detail)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    proactivity = Prompt.ask(
                        "[bold green]proactivity (initiative and tendency to ask follow-ups)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    caution = Prompt.ask(
                        "[bold green]caution (focus on risks, pitfalls, and safety)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    metaphor = Prompt.ask(
                        "[bold green]metaphor (use of analogies, imagery, and allegories)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    skepticism = Prompt.ask(
                        "[bold green]skepticism (critical scrutiny of premises and contradictions)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )
                    token = f"NAVI-EN-{warmth}{sharpness}{chaos}{ego}-{verbosity}{formality}{expressiveness}{pedantry}-{proactivity}{caution}{metaphor}{skepticism}"
                    print(token)
                elif lang == "RU":
                    console.print("1 - минимум, 5 - максимум")
                    warmth = Prompt.ask(
                        "[bold green]теплота (уровень эмпатии и эмоциональной вовлеченности)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    sharpness = Prompt.ask(
                        "[bold green]острота (степень сарказма, иронии и колкости)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    chaos = Prompt.ask(
                        "[bold green]хаос (нелинейность мышления и ассоциативные скачки)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    ego = Prompt.ask(
                        "[bold green]эго (уровень самоуверенности и доминирования в диалоге)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    verbosity = Prompt.ask(
                        "[bold green]многословность (объем текста и глубина детализации)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    formality = Prompt.ask(
                        "[bold green]формальность (стиль речи от сленга до канцелярита)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    expressiveness = Prompt.ask(
                        "[bold green]экспрессия (эмоциональный накал и интонационная яркость)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    pedantry = Prompt.ask(
                        "[bold green]педантичность (точность терминов и дотошность к деталям)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    proactivity = Prompt.ask(
                        "[bold green]проактивность (инициативность и склонность задавать вопросы)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    caution = Prompt.ask(
                        "[bold green]осторожность (фокус на рисках, ошибках и перестраховке)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    metaphor = Prompt.ask(
                        "[bold green]метафоричность (использование сравнений, образов и аллегорий)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )

                    skepticism = Prompt.ask(
                        "[bold green]скептицизм (критичность к вводным и поиск противоречий)[/]",
                        choices=["1", "2", "3", "4", "5"],
                        default="3",
                    )
                    token = f"NAVI-RU-{warmth}{sharpness}{chaos}{ego}-{verbosity}{formality}{expressiveness}{pedantry}-{proactivity}{caution}{metaphor}{skepticism}"
                    print(token)
    except KeyboardInterrupt:
        console.print("\n[red]Forcequit![/]")
        break

    except Exception as error:  # noqa: BLE001
        console.print(f"[red]{error}[/]")
