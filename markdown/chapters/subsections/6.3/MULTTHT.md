### MULTTHT – Multiply Cell Transmissibility in the +Theta Direction {#kw-MULTTHT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

MULTTHT multiples the transmissibility between two cell faces in the +Theta direction for all the cells in the model via an array, that is the keyword sets the transmissibility multiplier of block (I, J, K) between the cells (I, J, K) and (I, J+1, K).  An alternative to defining the complete array is to use the [BOX](#kw-BOX) keyword to define an area of the grid and then use the MULTTHT keyword to set the multipliers just for the area defined by the [BOX](#kw-BOX) keyword (see the example).

The keyword should only be used with radial and spider grids, as declared by the [RADIAL](#kw-RADIAL) or [SPIDER](#kw-SPIDER) keywords in the [RUNSPEC](#kw-RUNSPEC) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MULTTHT+ | MULTTHT+ is an array of real positive numbers assigning the transmissibility multipliers in the +Theta direction to each cell face in the model. Repeat counts may be used, for example 20*100.0. | 1.0 |
| Notes: |  |  |  |
: MULTTHT Keyword Description {#tbl-6-80}
See also the [MULTTHT-](#kw-MULTTHT-), [MULTR](#kw-MULTR), [MULTR-](#kw-MULTR-), [MULTZ](#kw-MULTZ) and [MULTZ-](#kw-MULTZ-) keywords for scaling transmissible between l grid cells in the Theta direction.


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
--       SET MULTTHT+ TRANSMISSIBILITY MULTIPLIERS
--
MULTTHT
         18*0.300                                          /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX
```


The above example defines a 0.3 scaling multiplier for the 18 cells defined by the preceding [BOX](#kw-BOX) statement. The [ENDBOX](#kw-ENDBOX) keyword resets the input box to the full grid.