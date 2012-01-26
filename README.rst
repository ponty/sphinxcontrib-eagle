This Sphinx_ 1.0 extension exports 
eagle_ partlist or image (2D/3D) of schematic or board
during the build step and
includes them into the documentation.


Links:
 * home: https://github.com/ponty/sphinxcontrib-eagle
 * documentation: http://ponty.github.com/sphinxcontrib-eagle

Features:
 - eagexp_ is used for processing
 
Basic usage
============
::

    .. eagle-image:: singlesided.sch
         :resolution: 100
         :scale: 30 %

    .. eagle-image3d:: singlesided.brd

    .. eagle-partlist:: singlesided.sch
           :header: part, value

How it works
========================

#. export image or text by eagle_ using eagexp_
#. include image or text into documentation


Installation
============

General
--------

 * install eagle_
 * install povray_ (optional for 3D)
 * install pip_
 * install pyvirtualdisplay_ , xvfb_ , xephyr_ (optional for background processing)
 * install the program::

    # as root
    pip install sphinxcontrib-eagle


Ubuntu
----------
::

    sudo apt-get install eagle
    sudo apt-get install povray
    sudo apt-get install python-pip

    # optional for background processing
    sudo apt-get install xvfb xserver-xephyr

    sudo pip install sphinxcontrib-eagle


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
.. _pyvirtualdisplay: https://github.com/ponty/PyVirtualDisplay
.. _eagle: http://www.cadsoftusa.com/
.. _eagexp: https://github.com/ponty/eagexp
.. _povray: http://www.povray.org/
