pelican content -o output -s pelicanconf.py
ghp-import output
git push -f origin gh-pages:master
git push -u pelican master
