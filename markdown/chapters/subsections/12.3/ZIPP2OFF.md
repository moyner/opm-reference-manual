### ZIPP2OFF – Deactivate Automatic Time Step Control {#kw-ZIPP2OFF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ZIPP2OFF keyword deactivates the commercial simulator’s alternative automatic time step selection algorithm that assumes no prior knowledge of the problem, as opposed to the standard time step algorithm that is controlled via the [TUNING](#kw-TUNING) keyword in the [SCHEDULE](#kw-SCHEDULE) section, combined with posterior knowledge gained from previous time steps.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

See section 2.2 Running OPM Flow 2023-04 From The Command Line on how to control time stepping for OPM Flow.