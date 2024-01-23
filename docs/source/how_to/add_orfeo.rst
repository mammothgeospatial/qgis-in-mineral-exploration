==========================
Enabling the Orfeo Toolbox
==========================

To install the Orfeo Toolbox, we have to download the binaries from https://www.orfeo-toolbox.org/download/.

.. image:: img/OTB_1.jpg
  :align: center


.. image:: img/OTB_2.jpg
  :align: center


Extract the files to a folder on your local machine. I have put mine into the C drive root directory in a folder called “OTB-8.1.2-Win64”. Next back in QGIS, open the Processing Toolbox and select the spanner (Settings) icon and enter the location of the OTB and the SAGA Next Gen folders. You need to click in the right hand side to make the browse buttons appear.
The “OTB Applications folder” is located in the OTB xxxxx > lib > otb > applications, and the OTB folder points to the upper level OTB folder.
To enable the SAGA Next Gen algorithms enter the location of the SAGA version 9 folder.

.. image:: img/OTB_3.jpg
  :align: center

The algoritms then become available in the Processing Toolbox.

.. image:: img/OTB_4.jpg
  :align: center
