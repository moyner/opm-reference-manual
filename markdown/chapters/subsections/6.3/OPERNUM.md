### OPERNUM – Define Regions for Mathematical Operations on Arrays {#kw-OPERNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the [OPERATER](#kw-OPERATER) region numbers for each grid block. The OPERNUM keyword defines the region numbers for each grid block, as such there must be one entry for each cell in the model. The array can also be used with the [EQUALREG](#kw-EQUALREG), [ADDREG](#kw-ADDREG), [COPYREG](#kw-COPYREG), [MULTIREG](#kw-MULTIREG), [MULTREGP](#kw-MULTREGP) and [MULTREGT](#kw-MULTREGT) keywords, as well as the [OPERATER](#kw-OPERATER) keyword in calculating various grid properties in the [GRID](#kw-GRID) and REGION section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | OPERNUM | OPERNUM defines an array of positive integers greater than or equal to one that assigns a grid cell to a particular OPERNUM region. The maximum number of OPERNUM regions is set by the NOPREG variable on the [REGDIMS](#kw-REGDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note that the default value of zero implies that the calculations requested by the [OPERATER](#kw-OPERATER) keyword will not be performed. | 0 |
| Notes: |  |  |  |
: OPERNUM Keyword Description {#tbl-6-98}
#### Examples

The example below sets three OPERNUM regions for a 4 x 5 x 2 model.


```
--
--       DEFINE OPERNUM REGIONS FOR ALL CELLS
--
OPERNUM
         2  2  1  1  2  2  1  1  1  1  1  1  1  1  1  1  1  1  1  1
         3  3  1  1  3  3  1  1  1  1  1  1  1  1  1  1  1  1  1  1
/
```

Alternatively the [EQUALS](#kw-EQUALS) keyword could be employed to accomplish the same task, that is:


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         OPERNUM     1            1*  1*   1*  1*   1*  1* / SET REGION 1
         OPERNUM     2            1   2    1   2    1   1  / SET REGION 2
         OPERNUM     3            1   2    1   2    2   2  / SET REGION 3
/
```

One can then increase [PERMX](#kw-PERMX) by 25% in region three only.


```
--
--       MULTIPLY AN ARRAY BY A CONSTANT BASED ON A REGION NUMBER
--
--       ARRAY     CONSTANT  REGION   REGION ARRAY
--                 VALUE     NUMBER    M / F / O
MULTIREG
         PERMX     1.25      3         O                   /
/
```