import json
import os

CHAT_FILE = "data/chat_history.json"


def load_history():

    if os.path.exists(CHAT_FILE):

        with open(
            CHAT_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    return []


def save_history(messages):

    with open(
        CHAT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            messages,
            f,
            ensure_ascii=False,
            indent=2
        )