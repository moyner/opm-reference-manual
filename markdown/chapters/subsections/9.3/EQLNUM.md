### EQLNUM – Define the Equilibration Region Numbers


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The EQLNUM keyword defines the equilibration region numbers for each grid block. The equilibration data for various regions are defined in the SOLUTION section. For example, the EQUIL keyword in the SOLUTION section defines the initial pressures and fluid contacts for each equilibration region identified by the EQLNUM region array.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | EQLNUM | EQLNUM defines an array of positive integers assigning a grid cell to a particular equilibration region. The maximum number of EQLNUM regions is set by the NTEQUL variable on the EQLDIMS keyword in the RUNSPEC section. | 1 |
| Notes: |  |  |  |

*Table 9.3: EQLNUM Keyword Description*


#### Examples

The example below sets three EQLNUM regions for a 4 x 5 x 2 model.


```
--
--       DEFINE EQLNUM REGIONS FOR ALL CELLS
--
EQLNUM
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
         EQLNUM’     1            1*  1*   1*  1*   1*  1* / SET REGION 1
         EQLNUM’     2            1   2    1   2    1   1  / SET REGION 2
         EQLNUM’     3            1   2    1   2    2   2  / SET REGION 3
/

```
