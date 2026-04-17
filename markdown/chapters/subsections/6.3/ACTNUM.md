### ACTNUM – Set the Status of a Grid Block To Active or Inactive {#kw-ACTNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ACTNUM keyword specifies which grid blocks are either active or inactive. A grid block is automatically set to inactive if its pore volume is less than the value entered using the [MINPV](#kw-MINPV) keyword. The ACTNUM keyword can be used to also make blocks with pore volumes greater than [MINPV](#kw-MINPV) inactive.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | ACTNUM | An array of integers equal to either 0 or 1 that define the activity of each cell in the model. A value of 0 indicates the cell is inactive. Grid blocks are ordered with the I index cycling fastest, followed by the J and K indices. Repeat counts may be used, for example 20*1. | 1 |
| Notes: |  |  |  |
: ACTNUM Keyword Description {#tbl-6-2}
#### Examples

The example below sets several cells to be inactive for a 4 x 5 x 2 model.


```
ACTNUM
-- Layer 1
0 0 1 1
0 0 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-- Layer 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
0 0 0 0
/

```

Alternatively the [EQUALS](#kw-EQUALS) keyword could be employed to accomplish the same task, that is:


```
--       -- ARRAY    CONSTANT --  ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         'ACTNUM’    1.0000       1*  1*   1*  1*   1*  1* / SET ACTIVE CELLS
         'ACTNUM’    0.0000       1   2    1   2    1   1  / SET INACTIVE CELLS
         'ACTNUM’    0.0000       1   4    5   5    2   2  / SET INACTIVE CELLS
/
```