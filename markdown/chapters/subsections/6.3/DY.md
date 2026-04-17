### DY – Define the Size of Grid Blocks in the Y Direction for All Cells {#kw-DY}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

DY defines the size of all grid blocks in the Y direction via an array for each cell in a Cartesian Regular Grid model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | DY | DY is an array of real numbers describing the cell size in the Y direction for each cell in the model. Repeat counts may be used, for example 10*100.0. | None |
| feet | m | cm |  |
| Notes: |  |  |  |
: DY Keyword Description {#tbl-6-28}
See also the [DX](#kw-DX), [DZ](#kw-DZ) and [TOPS](#kw-TOPS) keywords to fully define a Cartesian Regular Grid.


#### Example


```
--
--        DEFINE GRID BLOCK Y DIRECTION CELL SIZE (BASED ON NX x NY x NZ = 300)
--
DY
          300*1000                                                              /
```


The above example defines the size of the cells in the Y direction based on 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.