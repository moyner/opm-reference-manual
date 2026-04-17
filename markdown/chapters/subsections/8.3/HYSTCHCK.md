### HYSTCHCK – Activate Hysteresis Imbibition and Drainage End-Point Validation {#kw-HYSTCHCK}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HYSTCHCK keyword activate the hysteresis imbibition and drainage end-point check to validate that the two sets of end-points are consistent, for when the Hysteresis option has been activated by the HYSTER variable on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and the [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section has been activated to enable end-point scaling.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.