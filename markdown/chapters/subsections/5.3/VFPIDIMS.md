### VFPIDIMS – Injection Vertical Flow Performance Table Dimensions {#kw-VFPIDIMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

VFPIDIMS keyword defines the maximum dimensions of the injection well Vertical Lift Performance (“VFP”) tables defined by [VFPINJ](#kw-VFPINJ) keyword. The VFP tables for the producing wells are defined by the [VFPPDIMS](#kw-VFPPDIMS) keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MXMFLO | A positive integer that defines the maximum number of injection rate entries for the  [VFPINJ](#kw-VFPINJ) keyword. | 0 |
| 2 | MXMTHP | A positive integer that defines the maximum number of THP entries for the  [VFPINJ](#kw-VFPINJ) keyword. | 0 |
| 3 | MXVFPTAB | A positive integer that defines the maximum number of [VFPINJ](#kw-VFPINJ) tables entered through the [VFPINJ](#kw-VFPINJ) keyword. | 0 |
| Notes: |  |  |  |
: VFPIDIMS Keyword Description {#tbl-5-56}
#### Example


```
--       INJECTING VFP TABLES
--       VFP     VFP     VFP
--       MXMFLO  MXMTHP  NMMVFT
VFPIDIMS
         10      10      12                                                    /
```


The above example defines that the maximum number of injection rates and THP entries on the [VFPINJ](#kw-VFPINJ) keyword is 10, and the number of [VFPINJ](#kw-VFPINJ) tables is 12.