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

There are 3 directives, they accept a single string as argument, 
which is the path to the eagle .sch or .brd file. 
3D is available only for board::  

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd

      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.brd

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd

      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.brd

The same for schematic without 3D:: 

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
            :scale: 30%

      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.sch


The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
            :scale: 30%

      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.sch





Common options
---------------------

--------------
timeout
--------------

Using the option ``timeout`` you can set the timeout (default 20) in seconds for processing. 
Eagle can block the export by displaying a messagebox. If this happens
the export is aborted after timeout::  

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :timeout: 60

Image options
---------------------

--------------
resolution
--------------

Using the option ``resolution`` you can set the resolution in dpi, 
valid range: 50..2400, default is 150::
 
      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :resolution: 50
         
      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :resolution: 100

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :resolution: 200

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :resolution: 50
         
      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :resolution: 100

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
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

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
         :palette:   white
         :scale: 30 %

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
         :palette:   black
         :scale: 30 %

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
         :palette:   colored
         :scale: 30 %

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
         :palette:   white
         :scale: 30 %

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
         :palette:   black
         :scale: 30 %

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
         :palette:   colored
         :scale: 30 %

--------------
layers
--------------

Using the option ``layers`` you can display or hide layers. 
Check eagle documentation for valid settings. 
 

Example::

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :layers:   via,pads

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :layers:   via,pads

--------------
mirror
--------------

Using the option ``mirror`` you can mirror the image. 
 

Example::

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :mirror:   

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :mirror:   

--------------
command
--------------

Using the option ``command`` you can apply eagle commands. 
 

Example::

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :command:   display none dimension

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :command:   display none dimension

------------------------
scale, alt
------------------------

Example::

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
         :scale: 20 %
         :alt: alternate text

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :scale: 20 %
         :alt: alternate text

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.sch
         :scale: 20 %
         :alt: alternate text

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :scale: 20 %
         :alt: alternate text

---------------
height, width
---------------

Example::

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
           :height: 100px
           :width:  100 px

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
           :height: 100px
           :width:  100 px



---------------
align
---------------

Example::

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
           :height: 100px
           :width:  100 px
           :align: right

The above snippet would render like this:

      .. eagle-image:: ~/.eagle/projects/examples/tutorial/demo2.brd
           :height: 100px
           :width:  100 px
           :align: right

Image3D options
---------------------


--------------
size
--------------

Size of image, width x height::
 
      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 80x60

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 400x300

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 400x100
         
      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 100x400

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 1600x1200
         :scale: 30%

The above snippet would render like this:

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 80x60

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 400x300

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 400x100
         
      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 100x400

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :size: 1600x1200
         :scale: 30%


--------------
pcbrotate
--------------

Rotate PCB around x,y,z::
 
      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 90,0,0

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 0,90,0

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 0,0,90
         
      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 180,0,0

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 0,180,0

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 0,0,180


The above snippet would render like this:

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 90,0,0

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 0,90,0

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 0,0,90
         
      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 180,0,0

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 0,180,0

      .. eagle-image3d:: ~/.eagle/projects/examples/tutorial/demo2.brd
         :pcbrotate: 0,0,180


Partlist options
-------------------------

---------------
raw
---------------

Eagle_ partlist export is included as literal text::

      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.sch
           :raw: 

The above snippet would render like this:


      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.sch
           :raw: 



---------------
header
---------------

A comma-separated list of selected column names::

      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.sch
           :header: part, value

The above snippet would render like this:

      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.sch
           :header: part, value
          

---------------
widths
---------------

A comma- or space-separated list of relative column widths. 
The default is equal-width columns::   

      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.sch
           :header: part, value
           :widths:  2,8

The above snippet would render like this:

      .. eagle-partlist:: ~/.eagle/projects/examples/tutorial/demo2.sch
           :header: part, value
           :widths:  2,8
      
      
.. _eagle: http://www.cadsoftusa.com/
