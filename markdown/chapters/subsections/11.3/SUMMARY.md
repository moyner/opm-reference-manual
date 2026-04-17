### SUMMARY – Define the Start of the SUMMARY Section of Keywords {#kw-SUMMARY}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | SUMMARY | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SUMMARY activation keyword marks the end of the [SOLUTION](#kw-SOLUTION) section and the start of the SUMMARY section that defines the variables to be written out to the SUMMARY file for reporting and plotting of grid block data, production data, etc.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
-- ==============================================================================
--
-- SUMMARY SECTION
--
-- ==============================================================================
SUMMARY
```


The above example marks the end of the [SOLUTION](#kw-SOLUTION) section and the start of the SUMMARY section in the OPM Flow data input file.