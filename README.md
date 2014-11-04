This is the source of my [udibr](https://udibr.github.io/) blog.
Following the the ideas set [here](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/).
Continue reading if you want to create your own blog on github.

Install [pelican](http://docs.getpelican.com/en/3.4.0/quickstart.html#installation)
and [ghp-import](https://github.com/davisp/ghp-import):
```bash
pip install pelican markdown
pip install ghp-import
```

if you are creating a new repository (and not forking this one) you will have to add some submodules:
```bash
git submodule add https://github.com/jakevdp/pelican-octopress-theme.git
git submodule add https://github.com/getpelican/pelican-plugins
git submodule update --init --recursive
```
instructions on liquid_tags can be found [here](https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags) but just go through [this markdown](https://raw.githubusercontent.com/udibr/pelican/master/content/first-post.md) to have an idea how I got to [this page](https://udibr.github.io/blogin-on-github.html), 
notebooks are placed at `content/notebooks` and code samples at `content/code`

you will have to edit [pelicanconf.py](./pelicanconf.py) and [publishconf.py](./publishconf.py) files. Visit the files in this repository and spot the changes needed (hint: at least change udibr to your github login name.)

If you want people to comment on your blog you will have to open an account at [disqus.com](http://disqus.com) see [this site](http://querbalken.net/howto-setup-comments-with-disqus-in-pelican-en.html) for details relevant for pelican.
If you dont want comments then comment out the DISQUS line in `publishconf.py`

When you want to test locally do 
```bash
rm cache/* # this is needed if you change an existing notebook or code
# generate content in output directory
pelican content
# open browser before server because I dont want to run it in background
(sleep 5 ; open http://localhost:8000) &
(cd output ; python -m SimpleHTTPServer)
```

When you want to publish you will need two different repositories on github:
one containing your code (as this repository) and a second repository that mush have a name that looks like this: `udibr.github.io`

The code repository will have two branches: `master` which will contain the code and `gh-pages` which will contain a copy of the content inside `output` directory.
The content of the `gh-pages` branch will be pushed into the `master` branch of the second repository.

```bash
pelican content -s publishconf.py
# copy content of output directory to root of gh-pages branch
ghp-import output
# copy the gh-pages branch to the master branch on udibr.github.io
git push git@github.com:udibr/udibr.github.io.git gh-pages:master
# check  your updated site
open http://udibr.github.io
```
