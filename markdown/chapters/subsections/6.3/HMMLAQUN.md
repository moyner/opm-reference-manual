### HMMLAQUN – History Match Numerical Aquifer Gradient Multipliers {#kw-HMMLAQUN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HMMLAQUN keyword defines the history match numerical aquifer gradient multipliers for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and numerical aquifers have been specified in the model via the [AQUNUM](#kw-AQUNUM) keyword and connected to the grid using the [AQUCON](#kw-AQUCON) keyword.  All keywords are in the [GRID](#kw-GRID) section.

Multipliers can be declared for numerical aquifers’ pore volume, permeability, and aquifer to grid connection factors.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.