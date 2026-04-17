### RPTSMRY – Activate or Deactivate Summary List Report {#kw-RPTSMRY}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates or deactivates a listing of all the summary variables that are going to be written to the [SUMMARY](#kw-SUMMARY) file and the RSM file, if the RSM file option has been requested by the [RUNSUM](#kw-RUNSUM) keyword in the [SUMMARY](#kw-SUMMARY) section.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | RPTSMRY | An integer value set to zero for no report, or one to produce the report. | 0 |
| Notes: |  |  |  |
: RPTSMRY Keyword Description {#tbl-11-32}
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
--       ACTIVATE OR DEACTIVATE SUMMARY LIST REPORT
--
RPTSMRY
         1                                                 /
```


The example switches on the summary list report.