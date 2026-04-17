### SKIP – Activate Skipping of All Keywords and Input Data {#kw-SKIP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SKIP keyword activates skipping of all keywords and input data until the [ENDSKIP](#kw-ENDSKIP) keyword is encountered. All keywords between the SKIP and [ENDSKIP](#kw-ENDSKIP) keywords are ignored. Each SKIP keyword should be paired with an [ENDSKIP](#kw-ENDSKIP) keyword. See also the [SKIP100](#kw-SKIP100) and [SKIP300](#kw-SKIP300) keywords.

There is no data required for this keyword.

The nesting of pairs of the SKIP, [SKIP100](#kw-SKIP100), or [SKIP300](#kw-SKIP300) keywords and the [ENDSKIP](#kw-ENDSKIP) keyword is not supported by OPM Flow.


#### Example


```
--
--       SWITCH ON SKIPPING OF ALL KEYWORDS AND DATA
--
SKIP
--
--       INCLUDE SIMULATION GRID WITH SLOPING FAULTS
--
INCLUDE
         './INCLUDE/GRID/IRAP_1005.GRDECL' /
--
--       SWITCH ON READING OF ALL KEYWORDS AND DATA
--
ENDSKIP
```


The example skips reading of the grid geometry data input using the [INCLUDE](#kw-INCLUDE) keyword, and then reverts back to reading the remainder of the input file.