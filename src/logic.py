from model_data import *


def generate(soul: tuple, speech: tuple, mind: tuple, lang: str) -> str:
    rules_map = {
        "ru": (SOUL_RULES_RU, SPEECH_RULES_RU, MIND_RULES_RU),
        "en": (SOUL_RULES_EN, SPEECH_RULES_EN, MIND_RULES_EN),
    }

    personality = []

    # match by index: dict + tuple -> key in dict + value in tuple
    # 1st loop: pairs category dict with ratings tuple -> (SOUL_RULES, soul)
    # 2st loop QUALITY_RULES_RU/EN[KEY] (key in dict) - QUALITY[VALUE] (value in tuple)
    for rules, values in zip(rules_map[lang], (soul, speech, mind)):
        for key, value in zip(rules.keys(), values):
            personality.append(rules[key][value])

    return "\n".join(personality)
