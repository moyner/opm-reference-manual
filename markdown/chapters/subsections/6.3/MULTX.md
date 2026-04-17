### MULTX – Multiply Cell Transmissibility in the +X Direction {#kw-MULTX}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

MULTX multiples the transmissibility between two cell faces in the +X direction for all the cells in the model via an array, that is the keyword sets the transmissibility multiplier of block (I, J, K) between the cells (I, J, K) and (I+I, J, K).

An alternative to defining the complete array is to use the [BOX](#kw-BOX) keyword to define an area of the grid and then use the MULTX keyword to set the multipliers just for the area defined by the [BOX](#kw-BOX) keyword (see the example).

The keyword can be used for all grid types, except for the Radial Grid geometry.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MULTX+ | MULTX+ is an array of real positive numbers assigning the transmissibility multipliers in the +X direction to each cell face in the model. Repeat counts may be used, for example 20*100.0. | 1.0 |
| Notes: |  |  |  |
: MULTX Keyword Description {#tbl-6-82}
See also the [MULTX-](#kw-MULTX-), [MULTY](#kw-MULTY), [MULTY-](#kw-MULTY-), [MULTZ](#kw-MULTZ) and [MULTZ-](#kw-MULTZ-) keywords for scaling transmissible between grid cells.


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
--       SET MULTX+ TRANSMISSIBILITY MULTIPLIERS
--
MULTX
         18*0.300                                          /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX
```


The above example defines a 0.3 scaling multiplier for the 18 cells defined by the preceding [BOX](#kw-BOX) statement. The [ENDBOX](#kw-ENDBOX) keyword resets the input box to the full grid.