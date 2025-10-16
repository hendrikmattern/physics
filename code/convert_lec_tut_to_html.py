import os
import subprocess
import shutil
import sys


def _resolve_jupyter_cmd(project_root: str):
    # Prefer project-local venv jupyter executables on Windows
    venv_scripts = os.path.join(project_root, ".venv", "Scripts")
    jupyter_nb = os.path.join(venv_scripts, "jupyter-nbconvert.exe")
    jupyter_exe = os.path.join(venv_scripts, "jupyter.exe")
    if os.path.exists(jupyter_nb):
        return [jupyter_nb]
    if os.path.exists(jupyter_exe):
        return [jupyter_exe, "nbconvert"]

    # Try PATH-resolved executables
    jup_path = shutil.which("jupyter")
    if jup_path:
        return [jup_path, "nbconvert"]
    jup_nb_path = shutil.which("jupyter-nbconvert")
    if jup_nb_path:
        return [jup_nb_path]

    # Fallback to Python module invocation in the current interpreter
    return [sys.executable, "-m", "jupyter", "nbconvert"]


def convert_notebook_to_slides(input_path, output_path, curr_filtered_notebooks):
    # Resolve base jupyter command once
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))
    jupyter_cmd = _resolve_jupyter_cmd(project_root)
    for notebook in curr_filtered_notebooks:
        # convert notebook to HTML slides
        input_file = os.path.join(input_path, notebook)
        output_file = os.path.join(output_path, notebook.replace(".ipynb", ".slides.html"))
        # Build command with argument list to safely handle spaces in paths
        cmd = jupyter_cmd + [
            input_file,
            "--to",
            "slides",
            "--no-input",
            "--no-prompt",
            "--SlidesExporter.reveal_number=c/t",
            "--SlidesExporter.reveal_scroll=True",
            # "--SlidesExporter.reveal_height=800",
            # "--SlidesExporter.reveal_width=800",
            "--output-dir",
            output_path,
        ]
        try:
            subprocess.run(cmd, check=True)
            print("-------------> Conversion complete. HTML slides saved in", output_file)
        except subprocess.CalledProcessError as e:
            print("Conversion failed for:", input_file)
            print("Command:", " ".join(cmd))
            print("Error:", e)


# --- MAIN ---

# Determine project root (assuming this script is inside /code)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Define input and output directories relative to project root
lec_tut_folder = os.path.join(project_root, "lecture_tutorials")
html_slides_folder = os.path.join(project_root, "html_lec_tut")

# Ensure output folder exists
os.makedirs(html_slides_folder, exist_ok=True)

# List all files in the input directory
notebooks = [f for f in os.listdir(lec_tut_folder) if f.endswith(".ipynb")]

# Filter notebooks containing 'slides' or 'introduction'
filtered_notebooks = [nb for nb in notebooks if ".ipynb" in nb.lower()]

# Convert filtered notebooks to HTML slides
convert_notebook_to_slides(lec_tut_folder, html_slides_folder, filtered_notebooks)



