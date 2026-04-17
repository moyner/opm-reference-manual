### HMMROCK – History Match Rock Compressibility Gradient Cumulative Multipliers {#kw-HMMROCK}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

HMMROCK defines the rock compressibility gradient cumulative multipliers to be applied to the rock compressibility as defined by the [ROCK](#kw-ROCK) keyword in the [PROPS](#kw-PROPS) section,  for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.  The constant should be a real number.

The allocation of the [ROCK](#kw-ROCK) tables to different grid blocks in the model is done via the [PVTNUM](#kw-PVTNUM) or the [SATNUM](#kw-SATNUM) keywords in the REGION section.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.