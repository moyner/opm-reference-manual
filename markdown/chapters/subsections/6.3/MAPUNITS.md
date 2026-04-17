### MAPUNITS – Define the Map Axes Units {#kw-MAPUNITS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MAPUNITS keyword defines the units of the coordinates stated on the [MAPAXES](#kw-MAPAXES) keyword. It is usually output by pre-processing software when exporting the grid geometry. The data is not used by OPM Flow intrinsically, but is merely written to the output EGRID file, as specified by the [GRIDFILE](#kw-GRIDFILE) keyword, for the use of post-processing software like OPM ResInsight.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MAPUNITS | A character string that defines the units of the coordinates stated on the [MAPAXES](#kw-MAPAXES) keyword, and should be set to: | METRES |
| Notes: |  |  |  |
: MAPUNITS Keyword Description {#tbl-6-59}
#### Example


```
--
--       SET THE MAP UNITS FOR THE MAPAXES KEYWORD
MAPUNITS
         METRES                                                                /
```


The above example specifies the units on the [MAPAXES](#kw-MAPAXES) to be the default METRES.