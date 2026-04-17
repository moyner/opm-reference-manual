### GRIDUNIT – Define the Grid Units {#kw-GRIDUNIT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GRIDUNIT keyword defines the units of the grid data. It is usually output by pre-processing software when exporting the grid geometry. The data is not used by OPM Flow intrinsically, but is merely written to the output EGRID file, as specified by the [GRIDFILE](#kw-GRIDFILE) keyword, for the use of post-processing software like OPM ResInsight.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | GRIDUNIT | A character string that defines the units of the coordinates stated on the [MAPAXES](#kw-MAPAXES) keyword, and should be set to: | METRES |
| 2 | MAPOPT | A character string that defines if the grid data are measured relative to the map, or relative to the origin as stated on the [MAPAXES](#kw-MAPAXES) keyword. MAPOPT should either be left blank (the default) indicating the origin is relative to the origin on the [MAPAXES](#kw-MAPAXES) keyword, or set equal to MAP measured relative to the map. | 1* |
| Notes: |  |  |  |
: GRIDUNIT Keyword Description {#tbl-6-42}
#### Example


```
--
--       SET THE GRID UNITS FOR THE GRID
--
GRIDUNIT
         METRES                                                                /
```


The above example defines that the [GRID](#kw-GRID) units to be metric.