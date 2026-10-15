quarto create
 ? Create › project
 ? Type › website
 ? Directory › .
 ? Title (website) › Ocular Microbiome Consortium
 Creating project at /home/dpuiu/projects/www.ocular-microbiome.org:
  - Created _quarto.yml
  - Created .gitignore
  - Created index.qmd
  - Created about.qmd
  - Created styles.css
 ? Open With › vscode


convert header_01_header-bg.jpg     -format %c histogram:info:- |     sort -nr |     more
         22637: (19,93,80) #135D50 srgb(19,93,80)
          2453: (20,94,81) #145E51 srgb(20,94,81)
          2036: (18,94,81) #125E51 srgb(18,94,81)
         ...
####        

# 2026-10-15

/usr/bin/python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install jupyter pandas itables
python3 -m pip freeze > requirements.txt

quarto render

###

python -c "import pandas as pd; df=pd.read_csv('Samples.csv'); print(df.nunique().to_string())" | sort -k2,2nr

http://localhost:3602/Consortium_Data/VUMC_Data/Individuals.html#V24_24 # err
