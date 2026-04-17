### PORV – Define the Pore Volumes for All the Cells


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

[PORV](#__RefHeading___Toc96547_718313858) defines the pore volumes for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry. The keyword effectively overwrites previously entered and calculated data. The area to be modified can be defined via the various grid selection keywords, [ADD](#__RefHeading___Toc4412_421927891), [BOX](#__RefHeading___Toc42110_3671211675), [EQUALS](#__RefHeading___Toc296597_1576177388), etc., and areas that are not selected remain unchanged.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [PORV](#__RefHeading___Toc96547_718313858) | [PORV](#__RefHeading___Toc96547_718313858) is an array of real positive numbers assigning a pore volume to each cell in the model. Only the values in the currently defined input [BOX](#__RefHeading___Toc42110_3671211675) needed be entered. Repeat counts may be used, for example 20*100.0. | None |
| rb | rm3 | rcc |  |
| Notes: |  |  |  |

*Table 7.6: PORV Keyword Description*


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


Here the [BOX](#__RefHeading___Toc42110_3671211675) statement is used to define the input grid for the [PORV](#__RefHeading___Toc96547_718313858) keyword, which overwrites the pore volume previously calculated with pore volume values of zero, resulting in a no-flow boundary in that part of the field between layers 19 and 21, since layer 20 is deactivated. The [ENDBOX](#__RefHeading___Toc88719_1778172979) keyword resets the input box to the full grid.
