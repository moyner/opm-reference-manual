### SCHEDULE – Define the Start of the SCHEDULE Section of Keywords {#kw-SCHEDULE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SCHEDULE activation keyword marks the end of the [SUMMARY](#kw-SUMMARY) section and the start of the SCHEDULE section that defines the group and well definitions, operating and economic constraints, as well as how OPM Flow should advance through time. Numerical controls are also defined in this section and all parameters can be varied through time.

There is no data required for this keyword.


#### Example


```
-- ==============================================================================
--
-- SCHEDULE SECTION
--
-- ==============================================================================
SCHEDULE
```


The above example marks the end of the [SUMMARY](#kw-SUMMARY) section and the start of the SCHEDULE section in the OPM Flow data input file.