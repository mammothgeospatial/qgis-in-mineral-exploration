==========
About QGIS
==========

QGIS is a user-friendly open-source Geographic Information System (GIS) licensed under the GNU General Public License and is an official project of the Open Source Geospatial Foundation (OSGeo). It runs on Linux, Unix, Mac OSX, Windows and Android and supports numerous vector, raster, and database formats.

The Open Geospatial Consortium (OGC) is an international consortium of more than 530 businesses, government agencies, research organizations, and universities driven to make geospatial (location) information and services FAIR - Findable, Accessible, Interoperable, and Reusable. OGC's members create free geospatial standards. OGC also actively analyses emerging tech trends, and runs an agile, collaborative Research and Development (R&D) lab that builds and tests innovative solutions to members' use cases.
For more information visit “ogc.org”.

For those users requiring a “gentle” introduction to GIS, please see |gentle_intro|.

.. |gentle_intro| raw:: html

   <a href="https://docs.qgis.org/latest/en/docs/gentle_gis_introduction/" target="_blank">A Gentle Introduction to GIS</a>

QGIS is a volunteer driven project. They welcome contributions in the form of code contributions, bug fixes, bug reports, contributed documentation, advocacy and supporting other users on their mailing lists and gis.stackexchange.com. If you are interested in actively supporting the project, you can find more information under the development menu and on the QGIS Wiki. If you find QGIS valuable in your workplace, please donate to the QGIS project - the details are on the website.

QGIS provides a continuously growing number of capabilities provided by core functions and plugins.

This document will mainly address workflows for geoscientists but there are many other tools available in QGIS and worthy of some exploration of their functions. The Geoscience plugin can be used to display drill holes in plan and in cross section but is limited in its features. Downhole depth ticks, assay bars and labels can be displayed. QGIS is now able to handle all the various geophysical processing options with the SGTool plugin for geophysical processing.

A good explanation of QGIS and where it came from can be found `here <https://www.youtube.com/watch?v=As4hfPecxoU>`_.
If you find QGIS makes a valuable contribution to your business, please consider `making a donation <https://qgis.org/funding/donate/>`_ to assist with continual code improvements.

Installation options are available on the `QGIS download page <https://qgis.org/download/>`_ with options to download either the development version (via OSGeo4W) or the standalone installers (recommended).

The original default file format for QGIS was the ESRI shape file (\*.shp) and this format has been around for many years and can be read by many software products. It is an old format and has limitations, e.g. field names are limited to 10 characters. QGIS has adopted the new “GeoPackage” file format as its default spatial file format. GeoPackage files can contain different types of vector geometry - points, lines and polygons - and can also include raster images. GeoPackage files can be up to 140 TB in size! Layers can be imported into an existing GeoPackage by dragging from the Layer panel onto the GeoPackage name in the Browser panel. Styling information can also be saved into the GeoPackage file. When digitising into a GeoPackage file, each new feature is auto numbered. Raster images imported into a GeoPackage appear to be significantly compressed when compared with a GeoTIFF without any major loss of quality. ESRI and recent MapInfo products can read GeoPackage files.

Shapefiles have a number of limitations such as field/attribute column names are limited to 10 characters, it lacks a time data type, only supports text fields to 255 characters in length and is limited to 2 GB in size.

GeoPackage files on the other hand allows point, line vector and raster files to be stored in the one file. Formats/styles can be saved into the GeoPackage file and it can be up to 140 TB in size. When adding features during digitising, for example, a GeoPackage file will automatically populate the id field with sequential numbers. See `this web link <https://carto.com/blog/fgdb-gpkg/>`_ for further information. Note that GeoPackage files are single user only and if you need multiple user access at the same time then PostgreSQL and PostGIS may be required.
