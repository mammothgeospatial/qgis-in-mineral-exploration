===========================
Digitising Toolbar (Plugin)
===========================

Every tool is activated as soon as the active layer is of an appropriate type and in edit mode. Keep in mind that some tools need that the current layer's CRS matches the project CRS.

As a general rule of thumb your editing layer's CRS and the project's CRS should match. It makes life easier. If you need results in a different CRS, transform the layer after you have finished your digitizing session.

All edits can be undone/redone using QGIS' standard undo/redo capabilities.

Split multipart to single part
-------------------------------

*applies to: MultiPoint, MultiLine and MultiPolygon layer*

    #. batch mode: The selected multi-part features in the active layer are split into single part and added to the layer as new features, keeping the attributes of the original (multi-part) feature.
    #. interactive mode: click on any multi-part feature. The feature will be split into single parts which are added to the layer as new features, keeping the attributes of the original (multi-part) feature.

Split off one part and add it as new feature
--------------------------------------------

*applies to: MultiPoint, MultiLine and MultiPolygon layer*

Click on any part of a multi-part feature. The part will be deleted from the original feature and added as a new (single-part) feature to the layer keeping the attributes of its parent (multi-part) feature.

Split features
--------------

*applies to: Line, MultiLine, Polygon and MultiPolygon layers*

Works exactly like Split Features tool in QGIS' Advanced Digitizing Toolbar when applied to non-multi features. When applied to multi features the user is asked via a dialog (see below) which of the newly created geometries (fraction of a part) should become the new feature. The other fraction stays as part within the original multi feature. Thus it replaces QGIS' Split Parts, too, which is of limited use, because its application results in an invalid geometry if the split-off part is not edited any further. The dialog shown when splitting multi-part features has four buttons:

    #. Cancel aborts the current splitting operation and leaves all features untouched.
    #. No to All aborts the splitting of the current feature and leaves it untouched.
    #. No leaves the currently highlighted fraction in the multi-part feature.
    #. Yes accepts the currently highlighted fraction for becoming the new feature.

Merge selected features
-----------------------

*applies to: any layer with a primary key field, i.e. a database layer*

This works as the Merge selected features button in QGIS Core, except that Core's Merge selected features deletes all selected features and then inserts a new feature. DigitizingTools' method offers the user to choose which feature to keep by choosing its primary key value. This feature's geometry is updated with the combined geometry of all selected features, while all other selected features are deleted. This feature will be removed once #13490 is closed and implemented.

Exchange attributes between selected features
---------------------------------------------

*applies to: any vector layer*

Exchanges the attributes between two selected features of the active layer. Reasoning: when splitting features in a layer coming from a database provider the user can thus control which feature is going to keep the primary key value (important for related tables).

Cut with polygon from another layer
-----------------------------------

*applies to: line and polygon layer (multi or single part)*

Choose another layer whose selected features are used like a cookie cutter on the active layer. Everything that falls under the cutter feature(s) is erased. If a selection exists in the active layer only selected features are cut. In case a feature would completely disappear, a message is issued to the user, asking if this feature should be deleted.

Clip with polygon from another layer
------------------------------------

*applies to: line and polygon layer (multi or single part)*

Choose another layer whose selected feature is used like a cookie cutter on the active layer. Everything that falls under this feature will survive, everything outside will be erased. If a selection exists in the active layer only selected features will be clipped.

Fill ring
---------

*applies to: polygon layer (multi or single part)*

Fill rings (islands) in polygons with new features. This tool has two modes:

    #. batch mode: all rings in the selected features are filled with new features. The attribute set for all features is identical and can be entered once if form popup after feature creation is not suppressed.
    #. interactive mode: click into any the ring. A new feature is snuggled into the ring.

Fill gap
--------

*applies to: polygon layer (multi or single part)*

Fill gaps between the selected polygons of the active layer with new features. The algorithm has to union all selected features first, thus the selection is necessary to speed up the process, especially if the layer contains many features. This tool has two modes:

    #. batch mode: all gaps between the selected features are filled with new features. The attribute set for all features is identical and can be entered once if form popup after feature creation is not suppressed.
    #. interactive mode: click into the gap to be filled. A new feature is snuggled into the gap.

Fill gap (all visible layers)
-----------------------------

*applies to: polygon layer (multi or single part)*

Fill gaps between the polygons of all visible layers with a new feature: click into the gap to be filled. A new feature is snuggled into the gap.

Split selected features with selected line from another layer
-------------------------------------------------------------

*applies to: line and polygon layer (multi or single part)*

Splits all selected features of the active layer with the selected line feature of another layer. The splitting creates new features (not multi features). Each new feature resulting from being split retains its original attributes.

Flip line
---------

*applies to: line layer (multi or single part; does not make too much sense with multi part, though)*

Flip the direction of a line, i.e. reverse the node order within the line. This tool has two modes:

    #. batch mode: all selected lines are flipped.
    #. interactive mode: click any line feature to have it flipped (successful clicking depends on layer's snap settings).
