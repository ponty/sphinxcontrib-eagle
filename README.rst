This Sphinx_ 1.0 extension exports 
eagle_ partlist or image of schematic or board
during the build step and
includes them into the documentation.


Links:
 * home: https://github.com/ponty/sphinxcontrib-eagle
 * documentation: http://ponty.github.com/sphinxcontrib-eagle
 * pdf documentation: https://github.com/ponty/sphinxcontrib-eagle/raw/master/docs/_build/latex/sphinxcontrib-eagle.pdf

Basic usage
============
::

    .. eagle-image:: singlesided.sch
         :resolution: 100
         :scale: 30 %

    .. eagle-partlist:: singlesided.sch
           :header: part, value

How it works
========================

#. export image or text by eagexp_
#. include image or text into documentation


Installation
============

General
--------

 * install setuptools_
 * install PyVirtualDisplay_ , xvfb_ , xephyr_ (optional for background processing)
 * install eagexp_:

    # as root
    easy_install https://github.com/ponty/eagexp/zipball/master

 * install the program:

    # as root
    easy_install https://github.com/ponty/sphinxcontrib-eagle/zipball/master


Ubuntu
----------
::

    sudo apt-get install python-setuptools

    # optional for background processing
    sudo apt-get install xvfb xserver-xephyr

    sudo easy_install https://github.com/ponty/eagexp/zipball/master
    sudo easy_install https://github.com/ponty/sphinxcontrib-eagle/zipball/master


Uninstall
----------
::

    # as root
    pip uninstall sphinxcontrib-eagle


.. _Sphinx: http://sphinx.pocoo.org/latest
.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _Xvfb: http://en.wikipedia.org/wiki/Xvfb
.. _Xephyr: http://en.wikipedia.org/wiki/Xephyr
.. _PyVirtualDisplay: https://github.com/ponty/PyVirtualDisplay
.. _eagle: http://www.cadsoftusa.com/
.. _eagexp: https://github.com/ponty/eagexp

