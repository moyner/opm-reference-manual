### SEPARATE – Activate the Separate RSM File Output Option {#kw-SEPARATE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the writing out of the [SUMMARY](#kw-SUMMARY) file date in a columnar format to the RSM file, if the [RUNSUM](#kw-RUNSUM) keyword has also been activated in the [SUMMARY](#kw-SUMMARY) section. Both the SEPARATE and the [RUNSUM](#kw-RUNSUM) keywords need to be invoked. If the SEPARATE option is not activated then the RSM output is directed to the end of the PRT file. Normally the both the SEPARATE and [RUNSUM](#kw-RUNSUM) keywords are invoked in the same run to enable easy loading of the data into Microsoft's [EXCEL](#kw-EXCEL) or LibreOffice’s CALC spreadsheet programs.

There is no data required for this keyword and there is no terminating “/” for this keyword.

See also the [EXCEL](#kw-EXCEL), [RPTONLY](#kw-RPTONLY) and [RUNSUM](#kw-RUNSUM) keywords in the [SUMMARY](#kw-SUMMARY) section.


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


Note unlike the commercial simulator, OPM Flow always writes out the data to a separate file; however, it is probably good practice to include it if the same input decks are being run with commercial simulator.