import json
from collections.abc import Sequence

import ollama

from model_data import (
    ANALYZE_PROMPT,
    MIND_RULES_EN,
    MIND_RULES_RU,
    SOUL_RULES_EN,
    SOUL_RULES_RU,
    SPEECH_RULES_EN,
    SPEECH_RULES_RU,
)

RULES_MAP = {
    "ru": (SOUL_RULES_RU, SPEECH_RULES_RU, MIND_RULES_RU),
    "en": (SOUL_RULES_EN, SPEECH_RULES_EN, MIND_RULES_EN),
}

REQUIRED_KEYS = {"archetype", "vibe", "strength", "weakness"}


def generate(
    soul: Sequence[str],
    speech: Sequence[str],
    mind: Sequence[str],
    lang: str,
) -> str:
    if lang not in RULES_MAP:
        raise ValueError(f"Unsupported language: {lang}")

    personality = [
        rules_value[value]
        for rules, values in zip(RULES_MAP[lang], (soul, speech, mind), strict=True)
        for rules_value, value in zip(rules.values(), values, strict=True)
    ]
    return "\n".join(personality)


def analyze(model: str, lang: str, user_prompt: str) -> dict[str, str]:
    if lang not in ANALYZE_PROMPT:
        raise ValueError(f"Unsupported language: {lang}")

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": ANALYZE_PROMPT[lang]},
                {"role": "user", "content": user_prompt},
            ],
            think=False,
            format="json",
            options={"temperature": 0.2, "num_ctx": 2048},
        )
    except ollama.ResponseError as err:
        raise RuntimeError(f"Ollama error ({model}): {err.error}") from err

    content = response["message"]["content"]
    try:
        data = json.loads(content)
    except json.JSONDecodeError as err:
        raise ValueError(f"{model}: invalid JSON response") from err

    if not isinstance(data, dict) or REQUIRED_KEYS != data.keys():
        raise ValueError(f"{model}: invalid JSON structure")

    return data
