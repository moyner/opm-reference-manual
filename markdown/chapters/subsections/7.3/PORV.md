### PORV – Define the Pore Volumes for All the Cells {#kw-PORV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PORV defines the pore volumes for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry. The keyword effectively overwrites previously entered and calculated data. The area to be modified can be defined via the various grid selection keywords, [ADD](#kw-ADD), [BOX](#kw-BOX), [EQUALS](#kw-EQUALS), etc., and areas that are not selected remain unchanged.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PORV | PORV is an array of real positive numbers assigning a pore volume to each cell in the model. Only the values in the currently defined input [BOX](#kw-BOX) needed be entered. Repeat counts may be used, for example 20*100.0. | None |
| rb | rm3 | rcc |  |
| Notes: |  |  |  |
: PORV Keyword Description {#tbl-7-6}
#### Example


```
--
--       DEFINE INPUT BOX FOR EDITING INPUT ARRAYS
--
--       ---------- BOX ---------
--       I1  I2   J1  J2   K1  K2
BOX
         1* 100   1* 100   20  20                          / DEFINE BOX AREA
--
--       SET PORV FOR THE GRID BLOCKS
--
PORV
         1000*0.00                                         /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX
```


Here the [BOX](#kw-BOX) statement is used to define the input grid for the PORV keyword, which overwrites the pore volume previously calculated with pore volume values of zero, resulting in a no-flow boundary in that part of the field between layers 19 and 21, since layer 20 is deactivated. The [ENDBOX](#kw-ENDBOX) keyword resets the input box to the full grid.