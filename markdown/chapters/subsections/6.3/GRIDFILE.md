### GRIDFILE – Set the Grid File Output Options {#kw-GRIDFILE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword controls the output of a standard [GRID](#kw-GRID) or extended [GRID](#kw-GRID) file, as well as the extensible EGRID file for post-processing applications.  The extended and extensible [GRID](#kw-GRID) formats are comparable; however, the extensible [GRID](#kw-GRID) format is more compact and is the only format supported by OPM Flow.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NGRID | A positive integer that controls the output of the [GRID](#kw-GRID) geometry file: Only the default value of zero is supported. | 0 |
| 2 | NEGRID | A positive integer that controls the output of the EGRID geometry file: Only the default value of one is supported. | 1 |
| Notes: |  |  |  |
: GRIDFILE Keyword Description {#tbl-6-41}
#### Example


```
--
--       GRID FILE OUTPUT OPTIONS
--       GRID    EGRID
--       OPTN    OPTN
GRIDFILE
         0       1                                                             /
```


The above example defines that no [GRID](#kw-GRID) file will be written out and that the extensible [GRID](#kw-GRID) (that is the EGRID geometry format) file will be produced.  This is the only configuration that OPM Flow supports