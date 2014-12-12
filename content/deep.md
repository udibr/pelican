Title: Getting deeper into deep learning
Date: 2014-12-03 10:34
Category: ML

What do you prefer? Coffee, Tea? or should I ask CAFFE or ThEAno?

These days there are two main tracks to doing deep learning. Either use [Pylearn2](http://deeplearning.net/software/pylearn2/)/Theano or use [Caffe](http://caffe.berkeleyvision.org/). Pyearn2 is [very confusing to use](http://fastml.com/how-to-get-predictions-from-pylearn2/) but I've found a very nice video lecture showing how to bypass Pylearn2 and do learning directly with Theano. My notebooks made from the code of the lecture can be found [here](http://nbviewer.ipython.org/github/udibr/Theano-Tutorials/blob/master/notebooks/index.ipynb).

Theano is easy to install (on OS X or Ubuntu) and
in Theano you have full control of the algorithm being used, this make it ideal for researching new ways of doing things. For example, if your data has special structure to it or if you want to use a special loss function.

I've found out that running the last network of the tutorial crashes my Mac when running on a GPU. I think it is a result of GPU overheating so it could be a local problem.

Caffe is much easier to use. The setup is a little bit complex but I found it is [easy to setup an image on Amazon's AWS EC2](https://github.com/udibr/caffe-on-aws). The price per hour of a GPU machine on AWS (g2.2xlarge) is surprisingly low but you can get even lower price using spot instances. I've used spot instances for many hours without any unexpected termination (looks like there is less peak demand for these machines.) The only downside of spot is that you can not stop/start the machine but you can always create an image of your work.

Caffe looks to me to be much faster than Theano both in development time and running time. The downside is that you have to use one of the pre-built modules for everything. Another problem is when running the python interface to Caffe from an ipython notebook. If you have an error in your configuration files (protobufs) the entire ipython engine crash and you have to re-run the entire notebook.

