# Introduction
* everything was written in VSCode with Python 3
* Juypter notebooks are used to merge text (as markdown) and code

# Creating and activating venv in VSCode
* `Ctrl + Shift + P`
* Select "Python: Create Environment"
* Select the directory where you want to create the venv

* `Ctrl + Shift + P`
* Select "Python: Select Interpreter"
* Select the local venv you just created

# Handle requirements/packages with pip
* use requirement file if possible `pip install -r requirements.txt`
* if you want to store your local requirements use `pip freeze > requirements.txt`
* you can see the installed packages with `pip list`
* you can upgrade packages with pip in the terminal using `pip install --upgrade <package_name>`
* in general you might need the following packages (details in requirement.txt):
    * scipy
    * nbconvert	
    * jupyter notebook
    * jupyterlab_hide_code
    * jupyter lab
    * (optional) selenium and webdriver-manager selenium for html2pdf print
    * (optional) mistune for markdown to html conversion
	
# Run notebook with VSCode and Jupyter
* in VS code the individual notebook cells can be run by pressing `Ctrl + Enter` (double click if you want to enter a rendered cell)
* to open in the browser do the following:
    * make sure your venv is active
    * open the terminal (e.g. in VSCode with `Ctrl + Shift + ö` on German keyboard layout)
    * use either Juypter Lab or Notebook with the file of your choice
    * `jupyter lab .\<filename>.ipynb`
    * `jupyter notebook .\<filename>.ipynb`


# Convert slides notebook to static page (*.ipynb -> *.html)
* *make sure slide/sub-slide types properly set*
* run `jupyter nbconvert notebook_name.ipynb --to slides --post serve --no-input --no-prompt --SlidesExporter.reveal_number='c/t' --SlidesExporter.reveal_scroll=True` 
* `--SlidesExporter.reveal_number='c/t'` enables slide numbers
* `--SlidesExporter.reveal_scroll=True` enables scrolling on slides (not through slides)
* one can add additional argument like `--mathjax` to enable math rendering via mathjax
* open html in browser

# Convert script to html or pdf (requires pandoc and latex) or webpdf (requires nbconvert[webpdf] and chromium)
## html
jupyter nbconvert 'physics2/2_01_script.ipynb' --no-input --to html

# html print
pip install selenium 
pip install webdriver-manager selenium

## pdf with intermediate tex (not working properly)
jupyter nbconvert '.\physics2\2_02_script.ipynb' --to latex --no-input --no-prompt
pdflatex .\physics2\2_02_script.tex

# pdf (not working properly)
pandoc -f html -t pdf .\html_slides\2_02_slides.slides.html -o test.pdf --resource-path .\img\ --pdf-engine xelatex
jupyter nbconvert 'physics2/2_01_script.ipynb' --no-input --to pdf  
jupyter nbconvert 'physics2/2_01_script.ipynb' --no-input --no-prompt --to webpdf --allow-chromium-download
