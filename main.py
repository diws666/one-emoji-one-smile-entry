# /output/entry.txt IS the whole entry: exactly one emoji, byte-identical,
# nothing else. U+1F31E SUN WITH FACE (🌞) — do not change it.
EMOJI = "🌞"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(EMOJI)
