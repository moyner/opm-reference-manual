### RPTONLY – Activate the Report Time Steps Only Option for the SUMMARY File {#kw-RPTONLY}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the writing out of the [SUMMARY](#kw-SUMMARY) file and the RSM file data, if the RSM file option has been requested by the [RUNSUM](#kw-RUNSUM) keyword in the [SUMMARY](#kw-SUMMARY) section, at report time steps only.  The default is for the data to be written out for all time steps to the [SUMMARY](#kw-SUMMARY) files.  This keyword reduces the file size at the expense of lower resolution in the time domain.

There is no data required for this keyword and there is no terminating “/” for this keyword.

The option can be deactivated by the [RPTONLYO](#kw-RPTONLYO) keyword in the [SUMMARY](#kw-SUMMARY) section.


#### Example


```
-- ==============================================================================
--
-- SUMMARY SECTION
--
-- ==============================================================================
SUMMARY
--
--       EXPORT STANDARD SUMMARY VARIABLE VECTORS TO FILE
--
ALL
--
--       ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION
--
RUNSUM
--
--       ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION
--
SEPARATE
--
--       ACTIVATE REPORT TIME STEPS ONLY SUMMARY FILE OPTION
--
RPTONLY
```


The above example activates the writing out of the [SUMMARY](#kw-SUMMARY) file at report time steps only.