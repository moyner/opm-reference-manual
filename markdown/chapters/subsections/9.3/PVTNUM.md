### PVTNUM – Define the PVT Regions


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PVTNUM keyword defines the PVT region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of PVT tables (DENSITY, PVDG, PVDO, PVTG, PVTO, PVCO, PVTW and ROCK) are used to calculate the PVT properties in a grid block.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | PVTNUM | PVTNUM defines an array of positive integers assigning a grid cell to a particular PVT region. The maximum number of PVTNUM regions is set by the NTPVT variable on the TABDIMS keyword in the RUNSPEC section. | 1 |
| Notes: |  |  |  |

*Table 9.17: PVTNUM Keyword Description*


::: {.callout-note}
Care should be taken that cells in different PVTNUM regions are not in communication, since the fluid properties are associated with a cell. If for example, a rbbl or a rm3 of oil flows from PVTNUM region 1 to PVTNUM region 2,  then the oil properties of that oil will change from the PVT 1 data set to the PVT data set 2.  This will result in material balance errors, that may or may not cause numerical issues. To avoid this one should use the MULTNUM (or FLUXNUM, or OPERNUM) array with the MULTREGT array to ensure that the various PVTNUM regions are not in communication.
:::


#### Examples

The example below sets three PVTNUM regions for a 4 x 5 x 2 model.


```
--
--       DEFINE PVTNUM REGION FOR ALL CELLS
--
PVTNUM
         2  2  1  1  2  2  1  1  1  1  1  1  1  1  1  1  1  1  1  1
         3  3  1  1  3  3  1  1  1  1  1  1  1  1  1  1  1  1  1  1
/
```


Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         PVTNUM      1            1*  1*   1*  1*   1*  1* / SET REGION 1
         PVTNUM      2            1   2    1   2    1   1  / SET REGION 2
         PVTNUM      3            1   2    1   2    2   2  / SET REGION 3
/
```


There third example shows how to ensure the various PVT regions are isolated. First of all define the MULTNUM array in the GRID section and ensure all the regions are isolated.


```
-- ==============================================================================
--
-- GRID SECTION
--
-- ==============================================================================
GRID
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         MULTNUM     1            1*  1*   1*  1*   1*  1* / SET REGION 1
         MULTNUM     2            1   2    1   2    1   1  / SET REGION 2
         MULTNUM     3            1   2    1   2    2   2  / SET REGION 3
/
--
--       SET TRANSMISSIBILITES ACROSS DIFFERENT RESERVOIRS TO ZERO TO ISOLATE
--       RESERVOIRS
--
--       REGION   REGION   TRANS   DIREC   NNC    REGION ARRAY
--       FROM     TO       MULT    OPT     OPTS   M / F / O
MULTREGT
         1*       1*       0.0     1*     'ALL'   M        / ALL REGIONS SEALED
/
```


Then in the REGIONS section copy the MULTNUM array to the PVTNUM array.


```
-- ==============================================================================
--
-- REGIONS SECTION
--
-- ==============================================================================
REGIONS

--
--       COPY AN ARRAY TO ANOTHER ARRAY BASED ON A REGION NUMBER
--
--       ARRAY     ARRAY     REGION   REGION ARRAY
--       FROM      TO        NUMBER    M / F / O
COPYREG
         MULTNUM   PVTNUM    1         M                   / COPY MULT TO PVT 1
         MULTNUM   PVTNUM    2         M                   / COPY MULT TO PVT 2
         MULTNUM   PVTNUM    3         M                   / COPY MULT TO PVT 3
/
```


All the separate PVT regions are now isolated.
