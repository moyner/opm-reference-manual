### GRADRFT – Define RFT Derivative History Match Gradient Output {#kw-GRADRFT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GRADRFT keyword defines the derivative well RFT data, the [SOLUTION](#kw-SOLUTION) pressure and saturations at a well’s connected grid block, that should be written to the History Match Gradient output file, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.