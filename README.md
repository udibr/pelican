Following http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/

you will have to clone few things
```bash
cd ~/Downloads/github
git clone https://github.com/jakevdp/pelican-octopress-theme.git
git clone https://github.com/getpelican/pelican-plugins
```
instructions on liquid_tags can be found [here](https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags)
Notebooks are placed at `content/notebooks` and code samples at `content/code`


you will have to add following lines to your `pelican` file
```bash
PLUGIN_PATHS = ['/Users/udi/Downloads/github/pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

THEME = '/Users/udi/Downloads/github/pelican-octopress-theme'
```
create the file `_nb_header.html`
```bash
touch _nb_header.html
```



When you want to test locally do 
```bash
pelican content
(cd output ; python -m SimpleHTTPServer & open http://localhost:8000)
```

When you want to publish you will need two different repositories on github.
The first `pelican` will contain all your code as described above.
Your `pelican` repository will have two branches: `master` which will contain the code and `gh-pages` which will contain the `output` directory content.
The content of the `gh-pages` branch will be pushed into the `master` branch of a second repository which must be named: `udibr.github.io`

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
