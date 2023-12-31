===========================
QGIS in Mineral Exploration
===========================

.. hint:: Looking for the PDF version? You can find it in the Read the Docs dropdown at the bottom of the left side panel.

QGIS is an open-source GIS program for the display and analysis of GIS data. It has developed significantly in the past few years and is now a valuable tool for the mineral exploration industry, and a viable alternative to the commercially available GIS packages. Although not specifically written for geological applications, QGIS can do most of the required GIS tasks required by today's geoscientists. The terminology is different to the usual earth sciences programs, but many QGIS algorithms do the same thing but with a different name.

This manual examines QGIS and how QGIS can assist geoscientists in undertake mapping and geoscientific tasks in their day-to-day work. The manual has evolved during several years teaching QGIS to geoscientists in Australia and has been produced to offer a go-to document for earth science related GIS activities.

Accessing data from the internet via web map and web feature servers is illustrated to show how using this data can help with compiling available data for an area. Detailed aerial photography and Google Earth can be easily integrated with mapping data to allow the creation of accurate base maps for a variety of geological applications. A wide range of vector and raster (grid and image) data formats can be easily imported into QGIS, including GPS gpx files.

The presentation options for point, line and polygon data are extensive and easily customised. A variety of geological symbols and pattern fills can be applied to points, lines , and polygons. Geochemical and geophysical data can also be presented in a variety of display options. Basic 3D display of map data is also available via the QGIS2threejs plug-in and the QGIS 3D view. QGIS has many plug-ins for specialised tasks and the semi-automatic classification plug-in (SCP), is one example of where users can select, download, and process ASTER, Landsat, and Sentinel 2 satellite data. It is recommended that new users peruse the plugins list to see what plugins are available and for those that may be of use in their work.

Map production is easy in QGIS with the “Print Layout” allowing extensive options for the display and printing of maps.

This document is a working draft and in continuous development. There may be errors and omissions, and these will be rectified as time permits. This manual applies to QGIS 3.34.

.. toctree::
  :maxdepth: 2
  :titlesonly:

.. toctree::
  :caption: About
  :titlesonly:

  source/about/index

.. toctree::
   :numbered:
   :caption: Contents

   source/introduction/index
   source/about_qgis/index
   source/installing_qgis/index
   source/plugins/index
   source/accessing_data_over_web/index
   source/geological_data/index
   source/geochemical_data/index
   source/geophysical_data/index
   source/3d_image_display/index
   source/remote_sensing/index
   source/map_production/index
   source/tips_and_tricks/index
   source/drone_mapping/index
   source/how_to/index
   source/more_resources/index
   source/references/index

.. toctree::
  :caption: Appendix

  source/appendix/lithologic_patterns
