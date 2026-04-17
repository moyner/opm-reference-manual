### SMULTX – Multiply Cell Transmissibility in the +X Direction (Auto-Refinement) {#kw-SMULTX}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SMULTX multiples the transmissibility between two cell faces in the +X direction between cells in a host base grid and the connecting auto-refined grid cells, via an array, that is the keyword sets the transmissibility multiplier of block (Ihost, Jhost, Khost) in the host base grid, multiplies the transmissibility all the cells (Iauto, Jauto, Kauto) and (I+Iauto, Jauto, Kauto) in the auto-refinement grid. The Auto Refinement option must be enabled to use this keyword via the [AUTOREF](#kw-AUTOREF) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

An alternative to defining the complete array is to use the [BOX](#kw-BOX) keyword to define an area of the grid and then use the SMULTX keyword to set the multipliers just for the area defined by the [BOX](#kw-BOX) keyword (see the example).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | SMULTX+ | SMULTX+ is an array of real positive numbers assigning the transmissibility multipliers in the +X direction to each cell face in the model. Repeat counts may be used, for example 20*100.0. | 1.0 |
| Notes: |  |  |  |
: SMULTX Keyword Description {#tbl-6-118}
See also the [MULTX](#kw-MULTX), [MULTY](#kw-MULTY) and [MULTZ](#kw-MULTZ) keywords for scaling transmissible between grid cells.


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
--       SET SMULTX+ TRANSMISSIBILITY MULTIPLIERS
--
SMULTX
         18*0.300                                          /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX
```


The above example defines a 0.3 scaling multiplier for the 18 cells defined by the preceding [BOX](#kw-BOX) statement. The [ENDBOX](#kw-ENDBOX) keyword resets the input box to the full grid.