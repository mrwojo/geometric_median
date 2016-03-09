geometric_median
================

Geometric median of points computed by 2 methods in Python. Although this is quite simple, I'd like to have a package that I can reuse instead of writing the minimize function every time.

https://en.wikipedia.org/wiki/Geometric_median

This point or closely related points are known by many names:

* 1-median
* spatial median
* Euclidean minisum point
* Torricelli point
* L1 estimator
* point of minimum aggregate travel, minimum aggregate distance

Requirements
------------

* NumPy
* SciPy

TODO
----

* setup.py
* Median of 3 non-collinear points can be calculated. (Wikipedia)
* Median of 4 points can be calculated. (Wikipedia)
* Performance characteristics
** Timing
** Result quality
* A nearly linear time algorithm is expected in 2016. (Wikipedia)
* Test in Python 3.
* Remove TODOs in code.
