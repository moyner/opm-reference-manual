### GRID – Define the Start of the GRID Section of Keywords {#kw-GRID}


| [RUNSPEC](#kw-RUNSPEC) | GRID | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GRID activation keyword marks the end of the [RUNSPEC](#kw-RUNSPEC) section and the start of the GRID section  that defines the key grid property data for the simulator including the grid structure, porosity, permeability and other relevant grid property data.

There is no data required for this keyword.


#### Example


```
-- ==============================================================================
--
-- GRID SECTION
--
-- ==============================================================================
GRID
```


The above example marks the end of the [RUNSPEC](#kw-RUNSPEC) section and the start of the GRID section in the OPM Flow data input file.