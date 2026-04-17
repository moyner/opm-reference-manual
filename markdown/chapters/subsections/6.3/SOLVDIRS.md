### SOLVDIRS – Define Linear Solver Principal Directions {#kw-SOLVDIRS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SOLVDIRS keyword defines the linear solver principal directions, which should be set to XY, XZ, YX, YZ, ZX, or ZY.  The default direction is based on the direction of the highest transmissibility and SOLVDIRS allows for over writing the default direction for when linear convergence of the equations are problematic.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

See section 2.2 Running OPM Flow 2023-04 From The Command Line on how to invoke various numerical schemes via the OPM Flow command line interface.