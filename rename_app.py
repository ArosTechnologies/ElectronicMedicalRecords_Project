import os

base_dir = "/Users/ivanvivas/Repositories/ElectronicMedicalRecords_Project/radiographxpress"

# 1. Update text content
replacements = {
    "radiographxpress": "medCloud",
    "Radiograph Xpress": "MedCloud",
    "RadiographXpress": "MedCloud"
}

def replace_in_file(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read()
            
        new_content = content
        for k, v in replacements.items():
            new_content = new_content.replace(k, v)
            
        if new_content != content:
            with open(filepath, "w") as f:
                f.write(new_content)
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Failed to read/write {filepath}: {e}")

# Walk through all text files in the project
for root, dirs, files in os.walk(base_dir):
    if "node_modules" in root or ".git" in root or "venv" in root or "__pycache__" in root:
        continue
    for file in files:
        if file.endswith(('.py', '.html', '.txt', '.sh', '.yml', '.yaml', '.md', '.env', '.env.example')):
            replace_in_file(os.path.join(root, file))

# 2. Rename logo
old_logo = os.path.join(base_dir, "core/static/core/assets/img/logos/radiographxpress_logo.png")
new_logo = os.path.join(base_dir, "core/static/core/assets/img/logos/medCloud_logo.png")
if os.path.exists(old_logo):
    os.rename(old_logo, new_logo)
    print(f"Renamed {old_logo} to {new_logo}")

# 3. Rename inner directory
inner_dir_old = os.path.join(base_dir, "radiographxpress")
inner_dir_new = os.path.join(base_dir, "medCloud")
if os.path.exists(inner_dir_old) and os.path.isdir(inner_dir_old):
    os.rename(inner_dir_old, inner_dir_new)
    print(f"Renamed {inner_dir_old} to {inner_dir_new}")
