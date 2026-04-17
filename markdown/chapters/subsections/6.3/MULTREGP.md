### MULTREGP – Multiply Pore Volumes Based On Region Number


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [MULTREGP](#__RefHeading___Toc296617_1576177388) keyword multiplies the pore volume of a cell by a constant for all cells with a specific region number. The region number array can be [FLUXNUM](#__RefHeading___Toc45781_719036256), [MULTNUM](#__RefHeading___Toc61329_2752266063) or [OPERNUM](#__RefHeading___Toc67857_718313858) and these arrays must be defined and be available before the [MULTREGP](#__RefHeading___Toc296617_1576177388) keyword is read by the simulator. The constant should be a real number.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | REGION | REGION is a positive integer representing the region for which the CONSTANT in (2) should be applied. | None |
| 2 | CONSTANT | A real value to multiply the pore volume by for a given REGION. | 1 |
| 3 | REGION ARRAY | The REGION ARRAY to use for applying the CONSTANT in (2) based on the REGION in (1).  ARRAY can have the following values: | M |
| Notes: |  |  |  |

*Table 6.78: MULTREGP Keyword Description*


#### Example


```
--
-- RESET PORE VOLUME FOR DIFFERENT REGIONS
--
--    REGION    PORV          REGION ARRAY
--    NUMBER    MULT          M / F / O
MULTREGP
         1       1.0456573    M             /  Fault Block 1
         2       0            M             /  Fault Block 2
         3       0.9756715    M             /  Fault Block 3
         4       0            M             /  Inactive Blocks
/

```

The above example re-scales the pore volumes for [MULTNUM](#__RefHeading___Toc61329_2752266063) regions one and three and makes regions two and four inactive by setting their pore volumes to zero.
