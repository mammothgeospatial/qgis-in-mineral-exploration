======================
Creating a Grid Layout
======================

A regular grid of points can be created via a table of coordinates or using the “Regular Points” algorithm. Other create grid options are available in the Processing Toolbox, but these two methods are the simplest.

To create a grid, from a table of coordinates, use the “Create points from Table” algorithm located in the Processing Toolbox under the Vector Creation list. Input the table that contains the coordinates, select the X and Y coordinate fields, with optional Z and M fields as well, check the CRS and run. The algorithm will create a series of points with id's only. Use the attribute table to add Easting and Northing fields if desired to attach the point coordinates.

To create a grid of points using the map window, use the “Regular Points” algorithm in the Vector Creation list. The extent of the grid can be entered manually or defined by the map window extent. Set the grid spacing and check the CRS and run. The resulting grid can be rotated (using the Vector Geometry > Rotate algorithm) or the “Rotate Feature” on the map window icons (next to the “Move Points” icon). Both methods allow the user to select the point for rotation and the amount of rotation.

.. note:: If you want to create non-square or hexagonal grids, for example, use the “Create Grid” option under the Vector Creation options.