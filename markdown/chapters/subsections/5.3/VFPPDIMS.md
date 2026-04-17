### VFPPDIMS – Production Vertical Flow Performance Table Dimensions {#kw-VFPPDIMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

VFPPDIMS keyword defines the maximum dimensions of the production well Vertical Lift Performance (“VFP”) tables defined by [VFPPROD](#kw-VFPPROD) keyword. The VFP tables for the injection wells are defined by the [VFPIDIMS](#kw-VFPIDIMS) keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MXMFLO | A positive integer that defines the maximum number of production flow rate entries for the [VFPPROD](#kw-VFPPROD) keyword. | 0 |
| 2 | MXMTHP | A positive integer that defines the maximum number of THP entries for the [VFPPROD](#kw-VFPPROD) keyword. | 0 |
| 3 | MXMWFR | A positive integer that defines the maximum number of water fraction entries (WOR, WCUT, GWR etc.) for the [VFPPROD](#kw-VFPPROD) keyword. | 0 |
| 4 | MXMGFR | A positive integer that defines the maximum number of gas fraction entries (GOR, GLR, OGR etc.) for the [VFPPROD](#kw-VFPPROD) keyword. | 0 |
| 5 | MXMALQ | A positive integer that defines the maximum number of artificial lift quantity entries for the [VFPPROD](#kw-VFPPROD) keyword. | 0 |
| 6 | MXVFPTAB | A positive integer that defines the maximum number of [VFPPROD](#kw-VFPPROD) tables entered through the [VFPPROD](#kw-VFPPROD) keyword. | 0 |
| Notes: |  |  |  |
: VFPPDIMS Keyword Description {#tbl-5-57}
#### Example


```
--       PRODUCING VFP TABLES
--       VFP     VFP     VFP     VFP     VFP     VFP
--       MXMFLO  MXMTHP  MXMWFR  MXMGFR  MXMALQ  NMMVFT
VFPPDIMS
         20      10      10      10      6       9                             /
```


Here the example shows that there are a maximum of 20 flow rates, 10 THP entries, 10 water and gas fraction entries, and six artificial lift entries for the nine [VFPPROD](#kw-VFPPROD) VFP production tables.