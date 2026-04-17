### ECHO – Activate Echoing of User Input Files to the Print File {#kw-ECHO}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

Turns on echoing of all the input files to the print file; note that this keyword is activated by default and can subsequently be switched off by the [NOECHO](#kw-NOECHO) activation keyword.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


#### Example


```
--
--        SWITCH OFF ECHOING OF INPUT FILES
--
NOECHO
--
--        INCLUDE SIMULATION GRID WITH SLOPING FAULTS
--
INCLUDE
          './INCLUDE/GRID/IRAP_1005.GRDECL' /
--
--        SWITCH ON ECHOING OF INPUT FILES
--
ECHO
```


The examples deactivates the echoing of the input files, reads in the grid geometry data using the [INCLUDE](#kw-INCLUDE)  keyword, and then activates the echoing of the input files again.


::: {.callout-note}
Especially for the large voluminous data sets in the [GRID](#kw-GRID) section, it is good practice to deactivate the echoing of the input files when loading this data to avoid the print output file becoming too large to view in a text editor.
:::