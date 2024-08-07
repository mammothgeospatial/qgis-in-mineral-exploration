===========================================
Working with ESRI shp and geodatabase files
===========================================

The “shp” or shapefile has been the default standard for GIS data for a number of decades, but this format has many limitations, such as field names are limited to 10 characters. The newer ESRI geodatabase file (\*.gdb) is a more modern and much more comprehensive file type.

QGIS can read shp and gdb files but the styling data is not included within the shp file or the gdb file. ESRI styling information is contained within the \*.lyr, \*.lyrx, or \*.style sidecar files.

To open an ESRI geodatabase file, we “select” the folder containing all the files.

.. image:: img/ESRI_Geodatabase.jpg
  :align: center

Use the Data Source Manager, select vector and “Directory”. Set the type to “OpenFileGDB” and select the geodatabase file.

.. image:: img/ESRI_Geodatabase-1.jpg
  :align: center

.. img/ESRI_Geodatabase-2.jpg
  :align: center

This will then import all the geodatabase layers into QGIS.

The QGIS plug-in “SLYR” has been written by Nyall Dawson (https://north-road.com/) to convert ESRI styles for QGIS users. There are two versions, a community version available from the QGIS plug-in repository and a more comprehensive commercial version available under licence.

.. img/SLYR-1.jpg
  :align: center

To apply styling to the shp or gdb file, we need to convert the lyr or style file to a QGIS style file (\*.qml). Install the SLYR plug-in and this will create a new entry in the Processing ToolBox. In this example, we will convert an lyr file to a QGIS qml file and a QGIS xml file.

.. img/SLYR-2.jpg
  :align: center

In the LYR datasets section, open the “Convert LYR to QML” algorithm and select the lyr file for conversion.

.. img/SLYR-3.jpg
  :align: center

.. img/SLYR-4.jpg
  :align: center

.. img/SLYR-ToQML.jpg
  :align: center

.. img/SLYR-ToQML-1.jpg
  :align: center

Hint: if you use the same file name as the one you wish to apply the styles to, save it into the same folder as the file and this will then automatically style this layer by default when it is opened

Press run and the following window will display on completion.

.. img/SLYR-ToQML-2.jpg
  :align: center

This process is now complete and you can apply the style file to the layer or close and re-open it to apply the styles. Note if you have not used the layer name for the qml file, you will have to use the style “Save as Default” option to save the style file with the same name as the layer.

Note that if you apply styles to a geodatabase file, remember to use the “Save as default” to save the styles into the geodatabase file.

Using a similar process to the one above, create a QGIS xml file. These files can be imported into QGIS using the style manager and allows the user to apply pre-defined styles to polygons. As an example, we will create the xml file and import it into QGIS.

.. img/SLYR-5.jpg
  :align: center

.. img/SLYR-ToXML.jpg
  :align: center

.. img/XML-to-StyleManager.jpg
  :align: center

.. img/XML-to-StyleManager-1.jpg
  :align: center

Note that these styles will be imported with a “QLD_GEO_DETAILED_SURFACE” tag. Use the select all and import into QGIS.
Once loaded into the style manager, you can then “search” for an item, e.g. geological unit using the search bar.
