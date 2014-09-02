Following http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/

you will have to clone few things
```bash
cd ~/Downloads/github
git clone https://github.com/jakevdp/pelican-octopress-theme.git
git clone https://github.com/getpelican/pelican-plugins
```
instructions on liquid_tags can be found [here](https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags)
Notebooks are placed at `content/notebooks` and code samples at `content/code`

you will have to edit `pelicanconf.py` file. Visit the file in this repository and spot the changes needed.

When you want to test locally do 
```bash
pelican content
# open browser before server because I dont want to run it in background
(sleep 5 ; open http://localhost:8000) &
(cd output ; python -m SimpleHTTPServer)
```


When you want to publish you will need two different repositories on github:
`pelican` and `udibr.github.io`.
The `pelican` repository will have two branches: `master` which will contain the code (as described above) and `gh-pages` which will contain a copy of the `output` directory content.
The content of the `gh-pages` branch will be pushed into the `master` branch of the second repository which must be named: `udibr.github.io`

```bash
# update the output direcotry
pelican content
# copy output directory to root of gh-pages branch
ghp-import output
# copy the gh-pages branch to the master branch on udibr.github.io
git push -f origin gh-pages:master
# save a backup of your code from master branch
git push -u pelican master
# check  your updated site
open http://udibr.github.io
```
