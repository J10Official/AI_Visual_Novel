import re

def load_scenes(filename):
    """Split screenplay into scenes based on INT./EXT. markers."""
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    scenes = re.split(r'(?=(?:INT\.|EXT\.).*?\d+\s*\d*)', text)
    return [s.strip() for s in scenes if s.strip()]

def annotate_scene(scene_text):
    """Interactive manual annotation of one scene."""
    print("\n" + "="*60)
    print("SCENE RAW TEXT:\n")
    print(scene_text[:500] + ("..." if len(scene_text) > 500 else ""))
    print("="*60)

    location = input("LOCATION: ")
    mood = input("MOOD: ")
    characters = input("CHARACTERS (comma-separated): ")
    bg_image = input("BACKGROUND_IMAGE (filename.png): ")
    bg_edit = input("BACKGROUND_EDIT (short description): ")

    # Collect lines with manual expressions
    lines = []
    current_char = "Narrator"
    for line in scene_text.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.match(r"^[A-Z ]{2,}$", line) and len(line.split()) < 5:
            current_char = line.title()
        elif line.startswith("(") and line.endswith(")"):
            continue
        else:
            expr = input(f"Expression for '{line[:50]}...': ")
            lines.append((current_char, line, expr if expr else "null"))

    # Collect paths
    paths = []
    while True:
        add_path = input("Add a choice/path? (y/n): ").lower()
        if add_path != "y":
            break
        choice = input("CHOICE: ")
        target = input("TARGET: ")
        state_change = input("STATE_CHANGE (e.g. fear=+1): ")
        condition = input("CONDITION (or leave null): ")
        paths.append((choice, target, state_change, condition or "null"))

    # Convert to Markdown format
    md = []
    md.append("::SCENE::")
    md.append(f"LOCATION: {location}")
    md.append(f"MOOD: {mood}")
    md.append(f"CHARACTERS: {characters}")
    md.append(f"BACKGROUND_IMAGE: {bg_image}")
    md.append(f"BACKGROUND_EDIT: \"{bg_edit}\"\n")

    md.append("::SCRIPT::")
    for c, l, e in lines:
        md.append(f"- CHARACTER: {c}")
        md.append(f"  LINE: {l}")
        md.append(f"  EXPRESSION: {e}")

    md.append("\n::PATHS::")
    for choice, target, state, cond in paths:
        md.append(f"- CHOICE: \"{choice}\"")
        md.append(f"  TARGET: {target}")
        md.append(f"  STATE_CHANGE: {state}")
        md.append(f"  CONDITION: {cond}")

    return "\n".join(md)

def main():
    filename = input("Enter screenplay .txt filename: ")
    scenes = load_scenes(filename)
    annotations = []

    for i, scene in enumerate(scenes, 1):
        print(f"\n--- Annotating Scene {i}/{len(scenes)} ---")
        annotations.append(annotate_scene(scene))

    out_file = f"{filename}.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(annotations))

    print(f"\n✅ Annotation complete. Saved to {out_file}")

if __name__ == "__main__":
    main()
