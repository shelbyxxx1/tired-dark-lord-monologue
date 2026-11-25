import os


MONOLOGUE = (
    "Put that sword down. You'll chip a tooth. Not yours. His. I'm Edris. "
    "I fed your first king to this worm. For three hundred years I've picked "
    "bits of crown from its gums. Every night. With this bent nail. "
    "At dawn I'll loose it under the palace. All those soft little... "
    "The nail. Where's my... Oh. Still in my hand. Hold its lip up. Higher. "
    "My arm won't... there. No duel. I need both your hands for this. "
    "Take the nail. Start at the back. Yes, you may kill me.\n"
    "Just don't let go of the lip when you do."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(MONOLOGUE)
    print(f"Words: {len(MONOLOGUE.split())}; characters: {len(MONOLOGUE)}")


if __name__ == "__main__":
    main()
