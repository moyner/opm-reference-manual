### HMWPIMLT – History Match Well Productivity Index Parameters {#kw-HMWPIMLT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, HMWPIMLT, defines the history match gradient parameters for well productiviity indices, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Wells must be specified using the WELPSECS keyword in the [SCHEDULE](#kw-SCHEDULE) section and their connections defined by the [COMPDAT](#kw-COMPDAT) and/or [COMPDATL](#kw-COMPDATL) keywords, also in the [SCHEDULE](#kw-SCHEDULE) section

See also the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section that specifies the dimensions for the gradient option, including the maximum number of gradient wellss that can be used with the History Match Gradient option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.