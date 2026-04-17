### DZ – Define the Size of Grid Blocks in the Z Direction for All Cells {#kw-DZ}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

DZ defines the size of all grid blocks in the Z direction via an array for each cell in a Cartesian Regular Grid model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | DZ | DZ is an array of real numbers describing the cell size in the Z direction for each cell in the model. Repeat counts may be used, for example 10*100.0. | None |
| feet | m | cm |  |
| Notes: |  |  |  |
: DZ Keyword Description {#tbl-6-30}
See also the [DX](#kw-DX), [DY](#kw-DY) and [TOPS](#kw-TOPS) keywords to fully define a Cartesian Regular Grid.


#### Example


```
--
--        DEFINE GRID BLOCK Z DIRECTION CELL SIZE (BASED ON NX x NY x NZ = 300)
--
DZ
          100*20.0   100*30.0   100*50.0                                        /
```


The above example defines the size of the cells in the Z direction based on 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.