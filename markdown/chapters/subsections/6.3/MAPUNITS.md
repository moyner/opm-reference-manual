### MAPUNITS – Define the Map Axes Units


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MAPUNITS keyword defines the units of the coordinates stated on the MAPAXES keyword. It is usually output by pre-processing software when exporting the grid geometry. The data is not used by OPM Flow intrinsically, but is merely written to the output EGRID file, as specified by the GRIDFILE keyword, for the use of post-processing software like OPM ResInsight.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MAPUNITS | A character string that defines the units of the coordinates stated on the MAPAXES keyword, and should be set to: | METRES |
| Notes: |  |  |  |

*Table 6.59: MAPUNITS Keyword Description*


#### Example


```
--
--       SET THE MAP UNITS FOR THE MAPAXES KEYWORD
MAPUNITS
         METRES                                                                /
```


The above example specifies the units on the MAPAXES to be the default METRES.
