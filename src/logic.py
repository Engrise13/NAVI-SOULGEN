import ollama  # noqa

from model_data import *


def generate(soul: tuple, speech: tuple, mind: tuple, lang: str) -> str:
    rules_map = {
        "ru": (SOUL_RULES_RU, SPEECH_RULES_RU, MIND_RULES_RU),
        "en": (SOUL_RULES_EN, SPEECH_RULES_EN, MIND_RULES_EN),
    }

    personality = []

    # match by index: dict + tuple -> key in dict + value in tuple
    for rules, values in zip(rules_map[lang], (soul, speech, mind)):
        for key, value in zip(rules.keys(), values):
            personality.append(rules[key][value])

    return "\n".join(personality)


def analyze(model: str, prompt: str) -> str:
    pass
