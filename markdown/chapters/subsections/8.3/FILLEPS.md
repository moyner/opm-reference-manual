### FILLEPS – Activate Saturation End-Point Export to the INIT File {#kw-FILLEPS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword switches on the export of the saturation end-point data ([SWL](#kw-SWL), [SWCR](#kw-SWCR), [SOWCR](#kw-SOWCR) array etc.) to the *.[INIT](#kw-INIT) file so that the data can be viewed in post-processing software like OPM ResInsight.

There is no data required for this keyword.


#### Example


```
--
--       ACTIVATE SATURATION END-POINT EXPORT TO THE INIT FILE
--
FILLEPS
```


The above example switches on the export of the end-point saturation data to the *.[INIT](#kw-INIT) file.