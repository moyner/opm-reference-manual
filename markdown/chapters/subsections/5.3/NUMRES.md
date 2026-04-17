### NUMRES – Define the Number of Reservoir Grids {#kw-NUMRES}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NUMRES keyword defines the number of reservoir grids ([COORD](#kw-COORD) data sets) that the simulator should process. OPM Flow currently only supports a single reservoir grid.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NUMRES | A positive integer that defines the number of [COORD](#kw-COORD) data sets to be processed by OPM Flow. OPM Flow currently only supports a single reservoir grid and so this item should be defaulted (1*) or set to one. | 1 |
| Notes: |  |  |  |
: NUMRES Keyword Description {#tbl-5-30}
#### Example


```
--
--       DEFINE THE NUMBER OF RESERVOIR GRIDS (COORD DATA SETS)
--
NUMRES
         1                                                                    /

```

The above example sets the maximum number of [COORD](#kw-COORD) data sets to be processed to one.