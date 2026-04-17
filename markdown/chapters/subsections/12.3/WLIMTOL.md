### WLIMTOL – Define Well Constraint Tolerance {#kw-WLIMTOL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WLIMTOL keyword defines the tolerance to be used for various constraints applied to connections, completions (if connections have been lumped via the [COMPLUMP](#kw-COMPLUMP) keyword in the [SCHEDULE](#kw-SCHEDULE) section), wells, and groups, including the field group. See also the [GCONTOL](#kw-GCONTOL) keyword in the [SCHEDULE](#kw-SCHEDULE) section that sets the tolerance parameters for groups.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.