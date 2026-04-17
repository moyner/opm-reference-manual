### TEMPNODE – Temperature Table for Polymer Solution Viscosity {#kw-TEMPNODE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the reservoir temperature table used to calculate the polymer solution viscosity when the temperature option has been activated by the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section in the commercial simulator.  Naturally, the polymer option must also be activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section in order to use this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.