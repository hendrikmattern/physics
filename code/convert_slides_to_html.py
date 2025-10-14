import os


def convert_notebook_to_slides(input_path, output_path, curr_filtered_notebooks):
    for notebook in curr_filtered_notebooks:
        # convert notebook to HTML slides
        input_file = os.path.join(input_path, notebook)
        output_file = os.path.join(output_path, notebook.replace(".ipynb", ".slides.html"))
        command = (
            f"jupyter nbconvert {input_file} --to slides --no-input --no-prompt "
            f"--SlidesExporter.reveal_number='c/t' --SlidesExporter.reveal_scroll=True "
            #f"--SlidesExporter.reveal_height=800 --SlidesExporter.reveal_width=800 "
            f"--output-dir {output_path}"
        )
        os.system(command)       
        print("-------------> Conversion complete. HTML slides saved in", output_file)


# --- MAIN ---

# Determine project root (assuming this script is inside /code)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Define input and output directories relative to project root
physics1_folder = os.path.join(project_root, "physics1")
physics2_folder = os.path.join(project_root, "physics2")
html_slides_folder = os.path.join(project_root, "html_script")

# Ensure output folder exists
os.makedirs(html_slides_folder, exist_ok=True)

# List all files in the input directory
notebooks1 = [f for f in os.listdir(physics1_folder) if f.endswith(".ipynb")]
notebooks2 = [f for f in os.listdir(physics2_folder) if f.endswith(".ipynb")]

# Filter notebooks containing 'slides' or 'introduction'
filtered_notebooks1 = [nb for nb in notebooks1 if "slides" in nb.lower() or "introduction" in nb.lower()]
filtered_notebooks2 = [nb for nb in notebooks2 if "slides" in nb.lower() or "introduction" in nb.lower()]

# Convert filtered notebooks to HTML slides
convert_notebook_to_slides(physics1_folder, html_slides_folder, filtered_notebooks1)
#convert_notebook_to_slides(physics2_folder, html_slides_folder, filtered_notebooks2)


