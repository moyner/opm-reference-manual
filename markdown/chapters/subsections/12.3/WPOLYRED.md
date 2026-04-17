### WPOLYRED – Define Well Polymer-Water Viscosity Reduction Factor {#kw-WPOLYRED}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WPOLYRED keyword defines the polymer-water reduction factor for injection wells, for when the polymer phase has been activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section.  WPOLYRED should be set to a value greater than or equal to zero and less than or equal to one that determines the injection mixture’s viscosity. A value of zero indicates for pure water injection and a value of one will use the simulator’s valuated mixture viscosity.  A value between zero and one will use an interpolated mixture viscosity.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.