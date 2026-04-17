### HMAQUNUM – History Match Numerical Aquifer Gradient Parameters {#kw-HMAQUNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HMAQUNUM keyword defines the history match numerical aquifer gradient parameters for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and numerical aquifers have been specified in the model via the [AQUNUM](#kw-AQUNUM) keyword and connected to the grid using [AQUCON](#kw-AQUCON) keyword. All keywords are in the [GRID](#kw-GRID) section.

See also the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section that specifies the dimensions for the gradient option, including the maximum number of aquifers that can be used with the History Match Gradient option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.