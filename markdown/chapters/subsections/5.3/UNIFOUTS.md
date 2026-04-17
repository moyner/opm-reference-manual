### UNIFOUTS – Activate The Unified Output Summary File Option {#kw-UNIFOUTS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The UNIFOUTS keyword causes the [SUMMARY](#kw-SUMMARY) file output files to be a unified file, as opposed to non-unified multiple files. A unified file is a single file containing output for each reporting time step. Here a single [SUMMARY](#kw-SUMMARY) file will be generated, as opposed to one file per report time step. See also the [MULTOUT](#kw-MULTOUT) keyword in the [RUNSPEC](#kw-RUNSPEC) section that sets both the [SUMMARY](#kw-SUMMARY) and [RESTART](#kw-RESTART) files to be non-unified multiple files, as opposed to unified files. Note also that UNIFOUTS keyword has precedence over the [MULTOUT](#kw-MULTOUT) keyword for [SUMMARY](#kw-SUMMARY) files.


There is no data required for this keyword and there is no terminating “/” for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


#### Example


```
--
--       ACTIVATE THE UNIFIED OUTPUT SUMMARY FILE OPTION
--
UNIFOUTS
```


The above example switches on writing of unified [SUMMARY](#kw-SUMMARY) output files.