### MULTPV – Multiply Cell Pore Volumes by a Constant {#kw-MULTPV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

MULTPV multiples the pore volumes of a cell by a real positive constant for all the cells in the model via an array. An alternative to defining the complete array is to use the [BOX](#kw-BOX) keyword to define an area of the grid and then use the MULTPV keyword to set the multipliers just for the area defined by the [BOX](#kw-BOX) keyword (see the example).

The keyword can be used for all grid types, except for the Radial Grid geometry.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MULTPV | MULTPV is an array of real positive numbers assigning the pore volume multipliers for each cell in the model. Repeat counts may be used, for example 20*100.0. | 1.0 |
| Notes: |  |  |  |
: MULTPV Keyword Description {#tbl-6-73}
See also the [MULTREGP](#kw-MULTREGP) keyword for scaling the cell pore volumes by region numbers.


#### Example


```
--
--       DEFINE INPUT BOX FOR EDITING INPUT ARRAYS
--
--       ---------- BOX ---------
--       I1  I2   J1  J2   K1  K2
BOX
         10  10   1   6    1   3                           / DEFINE BOX AREA
--
--       SET PORE VOLUME MULTIPLIERS
--
MULTPV
         18*0.0500                                         /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX

```

The above example defines a 0.05 scaling multiplier for the 18 cells defined by the preceding [BOX](#kw-BOX) statement. The [ENDBOX](#kw-ENDBOX) keyword resets the input box to the full grid.