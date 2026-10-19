### 

quarto create
quarto create project website

###

convert header_01_header-bg.jpg     -format %c histogram:info:- |     sort -nr |     more
         22637: (19,93,80) #135D50 srgb(19,93,80)
          2453: (20,94,81) #145E51 srgb(20,94,81)
          2036: (18,94,81) #125E51 srgb(18,94,81)
         ...
###


/usr/bin/python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install jupyter pandas itables
python3 -m pip freeze > requirements.txt

###

python -c "import pandas as pd; df=pd.read_csv('Samples.csv'); print(df.nunique().to_string())" | sort -k2,2nr

###

http://localhost:3602/Consortium_Data/VUMC_Data/Individuals.html#V24_24 # err

###

quarto render
quarto render --clean

###

cat Individuals.csv0 | perl -ane 'print "U24-" if($.>1); print;' > Individuals.csv
more Samples.csv0 | sed 's|,|\t|g'  | perl -ane '@F=split /\t/; $F[28]="U24-".$F[28] if($.>1 and $F[28]); print join ",",@F;' > Samples.csv

###

grep 'class="' _site/index.html | grep -v popover | sed 's|class=|\nclass=|g' | grep ^class=  | sed 's|">||' | sed 's|<|\t|' | awk '{print $1}'| sed 's|"$||' | sort | uniq -c   | sort -nr| egrep -v 'quarto|nav|menu|dropdown'

npm install --global prettier
prettier  _site/index.html

cat _site/index.html  | wc -l 
prettier _site/index.html  | wc -l 

prettier  _site/index.html --print-width 10000 | grep 'class="quarto' -C 1

