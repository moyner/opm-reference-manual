### DZNET – Define Grid Block Net Thickness for All Cells {#kw-DZNET}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

DZNET defines the net thickness of all grid blocks in the Z direction via an array for each cell in a Cartesian Regular Grid model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | DZNET | DZNET is an array of real numbers describing the net thickness in the Z direction for each cell in the model. Repeat counts may be used, for example 10*100.0. If the value for a grid block is not defined then the grid block size ([DZ](#kw-DZ)) is assigned to the missing values. | [DZ](#kw-DZ) |
| feet | m | cm |  |
| Notes: |  |  |  |
: DZNET Keyword Description {#tbl-6-31}
See also the [DX](#kw-DX), [DY](#kw-DY), [DZ](#kw-DZ), [NTG](#kw-NTG) and [TOPS](#kw-TOPS) keywords to fully define a Cartesian Regular Grid.


#### Example


```
--
--       DEFINE GRID BLOCK Z DIRECTION NET THICKNESS(BASED ON NX x NY x NZ = 300)
--
DZNET
         100*15.0   100*25.0   00*45.0                                          /

```

The above example defines the net thickness of the cells in the Z direction based on 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.