import re
import emoji

emoji_map = { "😂":"laughing", "😭":"crying", "💀":"dead_funny", "😡":"angry", "💅":"sassy" }
slang_map = { "bruh":"bro", "lit":"amazing", "idk":"i dont know", "smh":"disappointed" }

def normalize_text(text):
    if not isinstance(text, str):
        text = str(text)
    for emo,meaning in emoji_map.items():
        text = text.replace(emo, f" {meaning} ")
    text = emoji.demojize(text)
    for slang,expanded in slang_map.items():
        text = re.sub(r"\b"+re.escape(slang)+r"\b", expanded, text, flags=re.IGNORECASE)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    return re.sub(r"\s+"," ", text).strip().lower()
