
.. _geological_data:

===============
Geological Data
===============

Geological data is varied in nature but is usually either as points, lines, or polygons. Geological mapping comprises the collection of points using a GPS, with lines and polygons drawn as an overlay on aerial or satellite images. More commonly these days is that the data is collected in a portable field device and uploaded to the GIS database.

.. hint:: When editing data, remember that in QGIS, it is a click to select and then click to the location to be moved - not a click and drag!

The following discussion covers a variety of tasks commonly associated with field data collection and interpretation. Detailed editing tasks will not be discussed as there are numerous resources available on the web, in the QGIS User Manual and various books. A variety of tips and tricks can be found in section 13.

The Android tablet application “QField” and MerginMaps are available for tablets and more details on this will be added in the near future. They can both be used in the field for data collection and mapping.

QGIS can sometimes have problems when digitising into layers with differing projections in the map window. It is recommended that digitising be done on layers in one projection at a time. The new file can be reprojected at subsequently into a different projection if required.

.. note:: Turn off the *auto-save plugin* if you have this enabled, as it may cause problems during digitising.

Details on the digitising and editing functions can be found in the `QGIS User Guide <https://docs.qgis.org/latest/en/docs/user_manual/>`_. This guide gets regularly updated.

.. toctree::

   point_data
   outcrop_photographs
   line_data
   plotting_drill_hole_traces/index
   polygon_data
   symbols_patterns
   line_styles
   labelling
   data_joins
   legends
   gps_data
   gswa
   grid_conversion
   grid_layout
   geopackages
