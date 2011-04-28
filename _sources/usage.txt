======
Usage
======


Configuration
---------------

Add ``sphinxcontrib.eagle`` to ``extensions`` list in ``conf.py``::

		extensions = [
		              'sphinxcontrib.eagle',
		              ]

Directives
------------

There are 2 directives, they accept a single string as argument, 
which is the path to the eagle .sch or .brd file::  

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
            :scale: 30%

      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.sch


The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
            :scale: 30%

      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.sch


The same for a board:: 

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd

      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.brd

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd

      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.brd


Image options
---------------------

--------------
timeout
--------------

Using the option ``timeout`` you can set the timeout (default 20) in seconds for processing. 
Eagle can block the export by displaying a messagebox. If this happens
the export is aborted after timeout::  

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :timeout: 60

--------------
resolution
--------------

Using the option ``resolution`` you can set the resolution in dpi, 
valid range: 50..2400, default is 150::
 
      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :resolution: 50
         
      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :resolution: 100

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :resolution: 200

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :resolution: 50
         
      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :resolution: 100

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :resolution: 200

--------------
palette
--------------

Using the option ``palette`` you can set the background color. 

Valid settings:
 - white
 - black
 - colored 
 
Default:white

Example::

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
         :palette:   white
         :scale: 30 %

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
         :palette:   black
         :scale: 30 %

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
         :palette:   colored
         :scale: 30 %

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
         :palette:   white
         :scale: 30 %

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
         :palette:   black
         :scale: 30 %

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
         :palette:   colored
         :scale: 30 %

--------------
layers
--------------

Using the option ``layers`` you can diaplay or hide layers. 
Check eagle documentation for valid settings. 
 

Example::

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :layers:   via,pads

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :layers:   via,pads

--------------
mirror
--------------

Using the option ``mirror`` you can mirror the image. 
 

Example::

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :mirror:   

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :mirror:   

--------------
command
--------------

Using the option ``command`` you can apply eagle commands. 
 

Example::

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :command:   display none dimension

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :command:   display none dimension

------------------------
scale, alt
------------------------

Example::

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
         :scale: 20 %
         :alt: alternate text

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :scale: 20 %
         :alt: alternate text

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.sch
         :scale: 20 %
         :alt: alternate text

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
         :scale: 20 %
         :alt: alternate text

---------------
height, width
---------------

Example::

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
           :height: 100px
           :width:  100 px

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
           :height: 100px
           :width:  100 px



---------------
align
---------------

Example::

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
           :height: 100px
           :width:  100 px
           :align: right

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/singlesided/singlesided.brd
           :height: 100px
           :width:  100 px
           :align: right


Partlist options
-------------------------

---------------
raw
---------------

Eagle_ partlist export is included as literal text::

      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.sch
           :raw: 

The above snippet would render like this:


      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.sch
           :raw: 



---------------
header
---------------

A comma-separated list of selected column names::

      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.sch
           :header: part, value

The above snippet would render like this:

      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.sch
           :header: part, value
          

---------------
widths
---------------

A comma- or space-separated list of relative column widths. 
The default is equal-width columns::   

      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.sch
           :header: part, value
           :widths:  2,8

The above snippet would render like this:

      .. eagle-partlist:: ~/.eagle/projects/examples/singlesided/singlesided.sch
           :header: part, value
           :widths:  2,8
      
      
.. _eagle: http://www.cadsoftusa.com/
