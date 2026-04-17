### ENDSKIP – Deactivate Skipping of Keywords and Input Data {#kw-ENDSKIP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ENDSKIP keyword deactivates the skipping of keywords that was activated by the [SKIP](#kw-SKIP), [SKIP100](#kw-SKIP100) or [SKIP300](#kw-SKIP300) keywords. Each [SKIP](#kw-SKIP), [SKIP100](#kw-SKIP100) or [SKIP300](#kw-SKIP300) keyword should be paired with an ENDSKIP keyword.

There is no data required for this keyword.

The nesting of pairs of either the [SKIP](#kw-SKIP), [SKIP100](#kw-SKIP100), or [SKIP300](#kw-SKIP300) keyword and the ENDSKIP keyword is not supported by OPM Flow.


#### Example


```
--
--       SWITCH ON SKIPPING OF KEYWORDS AND DATA
--
SKIP
--
--       INCLUDE SIMULATION GRID WITH SLOPING FAULTS
--
INCLUDE
         './INCLUDE/GRID/IRAP_1005.GRDECL' /
--
--       SWITCH ON READING OF KEYWORDS AND DATA
--
ENDSKIP
```


The example skips reading of the grid geometry data input using the [INCLUDE](#kw-INCLUDE) keyword, and then reverts back to reading the remainder of the input file.