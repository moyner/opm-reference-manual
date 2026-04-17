### GTADD – Add a Constant to a Group Target or Constraint {#kw-GTADD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, GTADD, adds a numerical constant to a group’s target or constraint value. The group must have been initially fully defined using the [GCONPROD](#kw-GCONPROD) or [GCONPRI](#kw-GCONPRI) keywords for producers or [GCONINJE](#kw-GCONINJE) for injectors.   Variables not changed by the GTADD keyword remain the same as those previously entered via the group control keywords or previously entered GTADD keywords. See also the [GRUPTARG](#kw-GRUPTARG) keyword that sets the values for a group’s target and constraints and the [GTMULT](#kw-GTMULT) keyword that multiplies a group target or constraint by a constant.  All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.