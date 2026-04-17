### DXV – Define the Size of Grid Blocks in the X Direction via a Vector {#kw-DXV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

DXV defines the size of grid blocks in the X direction via a vector as opposed to defining the X direction cell size for each cell for a Cartesian Regular Grid.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | DXV | DXV is a vector of real numbers describing the cell size for the grid blocks in the X direction. Repeat counts may be used, for example 10*100.0. | None |
| feet | m | cm |  |
| Notes: |  |  |  |
: DXV Keyword Description {#tbl-6-27}
See also the [DYV](#kw-DYV), [DZV](#kw-DZV) and [TOPS](#kw-TOPS) keywords to fully define a Cartesian Regular Grid.


#### Example


```
--
--       DEFINE GRID BLOCK X DIRECTION CELL SIZE (BASED ON NX = 5)
--
DXV
         5*100                                                                 /
```


The above example defines the size of the cells in the X direction based on NX equals 5 on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.