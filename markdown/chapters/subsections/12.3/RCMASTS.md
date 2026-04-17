### RCMASTS – Reservoir Coupling Group Minimum Time Step for Flow Restriction {#kw-RCMASTS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

RCMASTS is used when reservoir coupling is invoked by the [GRUPMAST](#kw-GRUPMAST) and [SLAVES](#kw-SLAVES) keywords in the [SCHEDULE](#kw-SCHEDULE) section. The keyword should be placed within the master file and it sets the minimum time step size for groups for when a group is being restricted by a group’s limiting flow rate fractional change (see the [GRUPMAST](#kw-GRUPMAST) keyword in the [SCHEDULE](#kw-SCHEDULE) section).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.