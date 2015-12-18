Title: Fast classifier calibration for 10^8 unbalanced examples
Date: 2015-12-17 21:08
Category: ML

Sam Steingold has introduced MIMIC in
[NYC Machine Learning meetup](http://www.meetup.com/NYC-Machine-Learning/events/227412933/).
MIMIC is
a method for calibrating the score of a binary classifier into probability.
 The method is different from the usual
[Platts and Isotonic calibration](http://fastml.com/classifier-calibration-with-platts-scaling-and-isotonic-regression/)

Its advantage is that it is much faster than Isotonic calibration,
and is capable of processing 10^8 examples in few hours, in addition it
does not lose information in the way Isotonic calibration does.

Compared to Platt (Logistic Regression) calibration it gives much better results
for unbalanced data (positive rates of 1/1000) and when the distribution of the
scores is not a simple Gaussian for the positive and/or negative examples.

The method is very simple:

* sort your scores (this expensive step can be parallelized)
* collect every 5 sorted scores to a cell
* measure the true success rate of each cell
* move between the cells form low to high score and merge the next cell with the current cell whenever the true success rate falls
* re-compute the success rate of the merged cell, this can result in another merger with the cell just before the current cell and so on...
* once finished you have a monotonic step function, which you can convert into a piece linear function.
