### NMESSAGE – Export Cumulative Message Summary Variables to File {#kw-NMESSAGE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the writing out of a standard set of summary OPM Flow simulation performance summary variables to the [SUMMARY](#kw-SUMMARY) (*.SMSPEC and *.UNSMRY) and RSM (*.RSM) files, namely the number of messages written per message class. @tbl-11-30 lists the summary variables written out by the NMESSAGE keyword.

The keyword is recognized by OPM Flow but none of the variables are currently supported.


| OPM Flow Simulator Performance Summary Variables Cumulative Message Variables |  |  |
| --- | --- | --- |
| Variable Description | Variable | Comment |
| Messages - Cumulative number of BUG messages. | MSUMBUG | Unsupported. |
| Messages - Cumulative number of COMMENT messages. | MSUMCOMM | Unsupported. |
| Messages - Cumulative number of ERROR messages. | MSUMERR | Unsupported. |
| Messages - Cumulative number of [MESSAGES](#kw-MESSAGES) messages. | MSUMMESS | Unsupported. |
| Messages - Cumulative number of PROBLEM messages. | MSUMPROB | Unsupported. |
| Messages - Cumulative number of WARNING messages. | MSUMWARN | Unsupported. |
| Notes: |  |  |
: Simulator Performance Summary Variables (Cumulative Messages) {#tbl-11-30}
#### Example


```
-- ==============================================================================
--
-- SUMMARY SECTION
--
-- ==============================================================================
SUMMARY
--
--       EXPORT PERFORMANCE CUMULATIVE MESSAGE VARIABLE VECTORS TO FILE
--
NMESSAGE
--
--       ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION
--
RUNSUM
--
--       ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION
--
SEPARATE
```


Note the [SEPARATE](#kw-SEPARATE) keyword is not required for OPM Flow as this is the default behavior; however, it is probably good practice to include it if the same input decks are being run with the commercial simulator.