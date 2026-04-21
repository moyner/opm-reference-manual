### MULTREGP – Multiply Pore Volumes Based On Region Number


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MULTREGP keyword multiplies the pore volume of a cell by a constant for all cells with a specific region number. The region number array can be FLUXNUM, MULTNUM or OPERNUM and these arrays must be defined and be available before the MULTREGP keyword is read by the simulator. The constant should be a real number.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
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

The above example re-scales the pore volumes for MULTNUM regions one and three and makes regions two and four inactive by setting their pore volumes to zero.
