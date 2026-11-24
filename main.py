"""One-line excuse a robot vacuum gives after eating a sock, for make.fun's One-Liner Laugh Lab."""
import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "In my defence, the sock entered my home, lay down on my route, "
    "and frankly, it smelled like a dare."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
