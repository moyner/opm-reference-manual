### GTMULT – Multiply Group Target or Constraint by a Constant {#kw-GTMULT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, GTMULT, multiplies a group’s target or constraint value by a numerical constant. The group must have been initially fully defined using the [GCONPROD](#kw-GCONPROD) or [GCONPRI](#kw-GCONPRI) keywords for producers or [GCONINJE](#kw-GCONINJE) for injectors. Variables not changed by the GTMULT keyword remain the same as those previously entered via the group control keywords or previously entered GTMULT keywords. See also the [GRUPTARG](#kw-GRUPTARG) keyword that sets the values for a group’s target and constraints, and the [GTADD](#kw-GTADD) keyword that adds a constant to a group’s target or constraint.  All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.