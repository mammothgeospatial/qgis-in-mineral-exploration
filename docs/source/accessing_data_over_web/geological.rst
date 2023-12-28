======================================
Geological Survey of Western Australia
======================================

The Department of Mines, Industry Regulation and Safety (`DMIRS <http://www.dmirs.wa.gov.au/>`_) is home to the Geological Survey of Western Australia (GSWA). This site contains many data sets, most of which can be downloaded from the `Data and Software Centre <https://dasc.dmirs.wa.gov.au>`_.

Registered raster files of the 100k and 250k geological map sheets have been mosaiced into 1:1 million map sheet areas and are in jp2 (jpeg2000) format registered in GDA94 MGA grid coordinates. The “jp2” format contains the projection and registration data embedded in the file. Raster files of individual map sheets in either GDA94 lat/long or MGA can also be downloaded from the data centre.

Always check that QGIS is using the current coordinate reference system when it loads these files - GDA94 lat/log has EPSG 4283, GDA94 UTM zone xx is EPSG 283xx.

The digital vector files for the 250k and 100k geology sheets vary in their data content depending upon the age of the map sheet edition. The GSWA use ArcView for their GIS system and many of their datasets contain "lyr" style and GeoMap "gmp" files. It has been requested that the data supplied by the GSWA also contain the colour and pattern information to allow users of other GIS systems (like QGIS) to style their maps like the GSWA style. `North Road Consulting <https://north-road.com/slyr/>`_ have developed a plugin to convert “lyr” style files to QGIS style files and assists QGIS users to style their maps in a similar fashion to the Arc GSWA maps. Some of the recent regional geology releases by the GSWA do have \=.qlr files which are QGIS layer definition files.
