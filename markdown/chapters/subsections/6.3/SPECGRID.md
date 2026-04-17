### SPECGRID – Define the Dimensions of a Corner-Point Grid {#kw-SPECGRID}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SPECGRID defines the dimensions of corner-point and radial grids in the x, y, and z directions as well as the number of reservoirs, where each reservoir has its own set of corner-point geometry data.

The keyword can only be used with Irregular Corner-Point Grids and Radial Grids.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NDIVIX | A positive integer value that defines the number of cells in the X or R direction | 1 |
| 2 | NDIVIY | A positive integer value that defines the number of cells in the Y or THETA direction | 1 |
| 3 | NDIVZ | A positive integer value that defines the number of cells in the Z direction | 1 |
| 4 | [NUMRES](#kw-NUMRES) | A positive integer values that defines number of coordinate data sets, or independent reservoirs in the model. OPM Flow currently only accepts a single data set, that is the default value of one. | 1 |
| 5 | TYPE | A character string set to either T of F that defines the type of grid to be defined by subsequent keywords: Only the default option F is supported by OPM Flow. | F |
| Notes: |  |  |  |
: SPECGRID Keyword Description {#tbl-6-121}
See also the [COORD](#kw-COORD), [COORDSYS](#kw-COORDSYS) and [ZCORN](#kw-ZCORN) keywords to fully define an Irregular Corner-Point Grid.


#### Example


```
--
--       MAX     MAX     MAX     MAX     GRID
--       NDIVIX  NDIVIY  NDIVIZ  NUMRES  TYPE
SPECGRID
         46      112     22      1       F                                     /
```


The above example defines a 46 x 112 x 22 grid with one set of irregular corner-point data.