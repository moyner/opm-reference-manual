### MSGFILE – Activate or Deactivate Message File Output {#kw-MSGFILE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

MSGFILE keyword activates or deactivates the message file output used by pre- and post-processing software. Note that message file processing is not available in OPM Flow.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MSGOPT | A positive integer set to 0 for to deactivate message file output or 1 to activate message file output. | 1 |
| Notes: |  |  |  |
: MSGFILE Keyword Description {#tbl-5-22}
#### Example


```
--
--       OUTPUT
--       OPTN
MSGFILE
         0                                                                     /
```


The above example deactivates the message file output, but the keyword is ignored by OPM Flow.