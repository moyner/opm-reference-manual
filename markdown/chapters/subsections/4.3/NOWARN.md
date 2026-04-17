### NOWARN – Deactivate Warning Messages {#kw-NOWARN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

Turns off warning messages to be printed to the print file; note that this keyword is deactivated by default and can subsequently be switched off by the [WARN](#kw-WARN) activation keyword. The warning messages may be turned on and off using keywords [WARN](#kw-WARN) and NOWARN.

It is recommended that [WARN](#kw-WARN) should always be used and action taken if necessary. For subsequent runs, the warning messages can be turned off.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


#### Example


```
--
--      SWITCH OFF WARNING MESSAGES
NOWARN
--
--      INCLUDE SIMULATION GRID WITH SLOPING FAULTS
--
INCLUDE
     './INCLUDE/GRID/IRAP_1005.GRDECL' /
--
--      SWITCH ON WARNING MESSAGES
--
WARN
```


The example deactivates the warning messages before reading the grid geometry data using the [INCLUDE](#kw-INCLUDE)  keyword, and then activates the warning messages after reading the [INCLUDE](#kw-INCLUDE) file.