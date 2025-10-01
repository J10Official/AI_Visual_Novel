import re

def load_annotations_md(filename):
    """Parse the annotations.md into structured scenes."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by scene markers
    raw_scenes = content.split("::SCENE::")
    scenes = []

    for raw in raw_scenes:
        raw = raw.strip()
        if not raw:
            continue

        # Extract blocks
        parts = re.split(r"::SCRIPT::|::PATHS::", raw)
        if len(parts) < 2:
            continue

        header, script_block, *path_block = parts
        path_block = path_block[0] if path_block else ""

        # Parse header fields
        header_data = {}
        for line in header.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                header_data[key.strip()] = val.strip()

        # Parse script
        script = []
        current = {}
        for line in script_block.splitlines():
            line = line.strip()
            if line.startswith("- CHARACTER:"):
                if current:
                    script.append(current)
                current = {"CHARACTER": line.split(":", 1)[1].strip()}
            elif line.startswith("LINE:"):
                current["LINE"] = line.split(":", 1)[1].strip()
            elif line.startswith("EXPRESSION:"):
                current["EXPRESSION"] = line.split(":", 1)[1].strip()
        if current:
            script.append(current)

        # Parse paths
        paths = []
        current = {}
        for line in path_block.splitlines():
            line = line.strip()
            if line.startswith("- CHOICE:"):
                if current:
                    paths.append(current)
                current = {"CHOICE": line.split(":", 1)[1].strip().strip('"')}
            elif line.startswith("TARGET:"):
                current["TARGET"] = line.split(":", 1)[1].strip()
            elif line.startswith("STATE_CHANGE:"):
                current["STATE_CHANGE"] = line.split(":", 1)[1].strip()
            elif line.startswith("CONDITION:"):
                current["CONDITION"] = line.split(":", 1)[1].strip()
        if current:
            paths.append(current)

        scenes.append({
            "SCENE": header_data,
            "SCRIPT": script,
            "PATHS": paths
        })

    return scenes

def edit_scene(scene):
    """Interactive editing of one scene."""
    print("\n" + "="*60)
    print("Editing Scene")
    print("="*60)

    # Edit scene metadata
    for key, val in scene["SCENE"].items():
        new_val = input(f"{key} [{val}]: ").strip()
        if new_val:
            scene["SCENE"][key] = new_val

    # Edit script
    print("\n-- Script Lines --")
    for i, line in enumerate(scene["SCRIPT"]):
        print(f"{i+1}. {line['CHARACTER']}: {line['LINE']} ({line['EXPRESSION']})")
        new_line = input("  New LINE (blank=keep): ").strip()
        new_expr = input("  New EXPRESSION (blank=keep): ").strip()
        if new_line:
            scene["SCRIPT"][i]["LINE"] = new_line
        if new_expr:
            scene["SCRIPT"][i]["EXPRESSION"] = new_expr

    # Edit paths
    print("\n-- Paths --")
    for i, path in enumerate(scene["PATHS"]):
        print(f"{i+1}. Choice: {path['CHOICE']} → {path['TARGET']} ({path['STATE_CHANGE']})")
        for key in ["CHOICE", "TARGET", "STATE_CHANGE", "CONDITION"]:
            new_val = input(f"  {key} [{path[key]}]: ").strip()
            if new_val:
                scene["PATHS"][i][key] = new_val

    return scene

def save_annotations_md(scenes, filename):
    """Save scenes back to MD format."""
    md_scenes = []
    for sc in scenes:
        scene = sc["SCENE"]
        md = []
        md.append("::SCENE::")
        for k, v in scene.items():
            md.append(f"{k}: {v}")
        md.append("")

        md.append("::SCRIPT::")
        for l in sc["SCRIPT"]:
            md.append(f"- CHARACTER: {l['CHARACTER']}")
            md.append(f"  LINE: {l['LINE']}")
            md.append(f"  EXPRESSION: {l['EXPRESSION']}")

        md.append("")
        md.append("::PATHS::")
        for p in sc["PATHS"]:
            md.append(f"- CHOICE: \"{p['CHOICE']}\"")
            md.append(f"  TARGET: {p['TARGET']}")
            md.append(f"  STATE_CHANGE: {p['STATE_CHANGE']}")
            md.append(f"  CONDITION: {p['CONDITION']}")
        md_scenes.append("\n".join(md))

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n\n".join(md_scenes))

def main():
    filename = input("Enter annotations.md filename: ")
    scenes = load_annotations_md(filename)

    for i, scene in enumerate(scenes, 1):
        print(f"\n--- Scene {i}/{len(scenes)} ---")
        edit = input("Edit this scene? (y/n): ").lower()
        if edit == "y":
            scenes[i-1] = edit_scene(scene)

    save_annotations_md(scenes, filename)
    print(f"\n✅ Updated annotations saved to {filename}")

if __name__ == "__main__":
    main()
