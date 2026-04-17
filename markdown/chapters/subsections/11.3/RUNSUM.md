### RUNSUM – Activate RSM File Output of the SUMMARY Data {#kw-RUNSUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the writing out of the [SUMMARY](#kw-SUMMARY) file data in a columnar format to the PRT file. Normally the [SEPARATE](#kw-SEPARATE) keyword in the [SUMMARY](#kw-SUMMARY) section is invoked in the same run to direct the data stream to a separate RSM file for easy loading into other programs, for example, Microsoft's [EXCEL](#kw-EXCEL) or LibreOffice’s CALC spreadsheet programs.

There is no data required for this keyword and there is no terminating “/” for this keyword.

See also the [EXCEL](#kw-EXCEL), [RPTONLY](#kw-RPTONLY) and [SEPARATE](#kw-SEPARATE) keywords in the [SUMMARY](#kw-SUMMARY) section.


#### Example


```
-- ==============================================================================
--
-- SUMMARY SECTION
--
-- ==============================================================================
SUMMARY
--
--       ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION
--
RUNSUM
--
--       ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION
--
SEPARATE

```

Note unlike the commercial simulator, OPM Flow always writes out the data to a separate file.