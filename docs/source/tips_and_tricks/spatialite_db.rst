====================
Spatialite Databases
====================

A Spatialite database is a simple, single file database structure that can hold very large files but with the advantage that the data is spatially referenced. The spatial referencing allows the data to be quickly displayed when panning across a map. This is very useful for data such as the 250k vector data (from GA) for Australia or the large GSWA open file drill hole database.

The use of Spatialite database files can rapidly increase the speed of accessing large data sets. As an example, the entire 1:250 000 Geoscience Australia Australia-wide topographic vector data in zipped shapefile format is 1.01 Gb in size (GA file 64058.zip) and comprises many layers including road, rivers, etc. This file can be loaded into a Spatialite database file of about 3 Gb, but although a large file, the data is spatially indexed, and re-drawing of the data is very fast when panning from area to area.

Another spatialite option is to use the new GeoPackage file format which can store large datasets comprising vector, raster and non-spatial data.
