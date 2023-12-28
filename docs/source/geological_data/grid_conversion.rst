=========================================================================
Creating and converting Local (Non-Earth) Grids to Real World Coordinates
=========================================================================

The Geoscience plug-in allow you to create a custom CRS. For this you will need at least three points in both coordinate systems, better to have four and enter 0 for any Z values. This plug -in will create a WKT (“Well Known Text”) file that can be used to create a custom CRS in QGIS under the Settings > Custom Projections tab.

There is no easy way to convert non-earth coordinates but there is a way by using the v.transform algorithm. The algorithm requires an x, y coordinate for the grid origin and an optional rotation amount. This data should be available from the mine surveyor or can be calculated. The author uses a small python program that uses 2 common sets of points to calculate a grid origin and rotation amount. The workflow below is for point data and within one UTM zone in metre coordinates only. If you would like a copy of this python code, please contact me.

Using a new project workspace, change **project projection** to “no projection” then open the local grid file using the local coordinates (e.g. drill holes in local coordinates). Check that the local coordinates in the map window look correct.

Run the v.transform algorithm with the points in local grid coordinates. To find this algorithm display the Processing Toolbox in the RHS of the map window, type v.tr in the search box and the v.transform algorithm should now be displayed. Double click on it to open the v.transform dialog box. Use the parameters for x, y and rotation.

Allocate the new projection to the points by **firstly**, setting the projection of the transformed layer to your desired UTM projection (**very important to do this first**) via the Layer Properties > Source tab, then change the project projection to your UTM projection. Close the original local coordinates file and zoom to the extent of the new transformed layer to check the transformation was successful.

This will produce a transformed (virtual) layer which will need to be “Exported As” to save the file permanently.