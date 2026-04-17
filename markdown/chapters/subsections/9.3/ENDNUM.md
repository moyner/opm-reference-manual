### ENDNUM – Define the End-Point Scaling Depth Region Numbers


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ENDNUM keyword defines the end-point scaling depth table region numbers for each grid block. The end-point scaling depth tables for various regions are defined by the ENPVTD [This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.] and the ENKRVD [This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.] keywords in the PROPS section.  In the RUNSPEC section the NTENDP variable on the ENDSCALE keyword defines the maximum number of depth tables.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ENDNUM | ENDNUM defines an array of positive integers assigning a grid cell to a particular end-point scaling depth table region. The maximum number of ENDNUM regions is set by the NTENDP variable on the ENDSCALE keyword in the RUNSPEC section. | 1 |
| Notes: |  |  |  |

*Table 9.2: ENDNUM Keyword Description*


This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


#### Examples

The example below sets three ENDNUM regions for a 4 x 5 x 2 model.


```
--
--       DEFINE ENDNUM REGIONS FOR ALL CELLS
--
ENDNUM
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
         ENDNUM      1            1*  1*   1*  1*   1*  1* / SET REGION 1
         ENDNUM      2            1   2    1   2    1   1  / SET REGION 2
         ENDNUM      3            1   2    1   2    2   2  / SET REGION 3
/
```
