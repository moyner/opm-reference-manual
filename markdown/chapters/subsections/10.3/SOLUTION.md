### SOLUTION – Define the Start of the SOLUTION Section of Keywords {#kw-SOLUTION}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | SOLUTION | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SOLUTION activation keyword marks the end of the [REGIONS](#kw-REGIONS) section and the start of the SOLUTION section that defines the parameters used to initialize the model, by:

- defining fluid contacts and pressures, or
- defining pressures and fluid saturations for all cells in the model, or
- by restarting from a previously OPM Flow completed run.

There is no data required for this keyword.


#### Example


```
-- ==============================================================================
--
-- SOLUTION SECTION
--
-- ==============================================================================
SOLUTION
```


The above example marks the end of the [REGIONS](#kw-REGIONS) section and the start of the SOLUTION section in the OPM Flow data input file.