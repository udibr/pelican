Title: Tips on working with Theano
Date: 2015-07-17 18:11
Category: ML

Debugging Theano code is notoriously hard.
Perhaps the main reason is because the python code you just wrote is not executed.
Instead, your python expressions are used to build a graph of what you want to compute.
The graph is compiled into CPU or GPU code when you use something like
`theano.function` to create a "regular" python function from your graph.
Finally the compiled code is excuted only when you call the "regular" function,
at which point, all the intermediate steps in the computation are hidden
from view.
As a result you can't just code and experiment with your code to better
understand how things work.

Luckily there is a workaround that allows you to do just that.
Somewhere at the start of the code enter something like:

    import theano
    theano.config.optimizer='fast_compile'
    theano.config.exception_verbosity='high'
    theano.config.compute_test_value = 'warn'
if you want the above code to run only while debugging you can use the following
`if` statement:

    import sys
    debug = sys.gettrace() is not None
    if debug:
        ...
next, whenever you create a Theano variable, assign to it some value that
will be used for debugging. For example:

    import numpy
    x = theano.tensor.matrix('features')
    x.tag.test_value = numpy.random.rand(3, 2)
The value you just assigned for debugging can always be examined using
`x.tag.test_value` and what is nice is that any expression that uses this
variable also has its own `test_value` that is computed on the fly,
as you would have expected from an interactive python code.

    y = x*2
    print y.tag.test_value

The expression can be broken into as many lines of code as you want 
as long as all the variables it is made off have their `test_value` defined.
If a variable has a predefined value to it, set by Theano, then there is
no need to set something using `test_value`

    b = theano.tensor.ones((3,2))
    c = theano.shared(np.ones((3,2)))
    print (y*b + c).tag.test_value
In addition to exploring the intermediate results of your computation
you will also get an excpetion whenever a `test_value` can not be
computed immediately at the spot where the offending code was called.
This usually happens to me because of misunderstanding of how Theano works.

I've found that it is important to use test values that are as realistic as possible.
Use the same input values you expect to see when the final "regular" compiled
function is going to be used.

However, if you want to speed things up while debugging you should start 
as small as possible. For example, use small number of hidden units.

Another trick that may help is using CPU at first:

    export THEANO_FLAGS=device=cpu

Finally, if everything else fails, read the entire error message Theano throws
at you,
usually it is very cryptic but it can contain helpful hints.

You can even force some of the prints to appear even without an exception

    theano.printing.debugprint(my_theano_variable, print_type=True)
