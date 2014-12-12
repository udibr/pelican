Title: Command line for cleaning the cells of an ipython notebook
Date: 2014-12-12 13:57
Category: Code

Once in a while I have an ipython notebook that has so much stuff written into its output cells that it takes forever to open it in the browser. In some cases the browser crash, blocking me from reaching the menu option to clear all the cells in the notebook.

I therefore wrote [this code](https://gist.github.com/udibr/1d4c71b79dfd360b087d) to clear the output of all the cells (and the prompt numbers.) With it I can run the code as a command line before attempting to open the notebook from the ipython notebook server.

Code example:
{% include_code clean_notebook.py %}

