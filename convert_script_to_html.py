import os


def convert_notebook_to_slides(input_path, output_path):
    for notebook in filtered_notebooks2:
        # convert notebook to HTML slides
        input_file = os.path.join(input_path, notebook)
        output_file = os.path.join(output_path, notebook.replace(".ipynb", ".slides.html"))
        command = (
            f"jupyter nbconvert {input_file} --to html --no-input --no-prompt --output-dir {output_path}"
        )
        os.system(command)
        print("Conversion complete. HTML slides saved in", output_file)


# Define input and output directories
physics1_folder = "./physics1"
physics2_folder = "./physics2"
html_script_folder = "./html_script"

# Ensure output folder exists
os.makedirs(html_script_folder, exist_ok=True)

# List all files in the input directory
notebooks1 = [f for f in os.listdir(physics1_folder) if f.endswith(".ipynb")]
notebooks2 = [f for f in os.listdir(physics2_folder) if f.endswith(".ipynb")]

# Filter notebooks containing 'slides' or 'introduction'
filtered_notebooks1 = [nb for nb in notebooks1 if "script" in nb.lower() or "1_cheat_sheet" in nb.lower()]
filtered_notebooks2 = [nb for nb in notebooks2 if "script" in nb.lower() or "2_cheat_sheet" in nb.lower()]

# Convert filtered notebooks to HTML slides
#convert_notebook_to_slides(physics1_folder, html_script_folder)
convert_notebook_to_slides(physics2_folder, html_script_folder)


