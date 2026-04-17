### RSGI – Define Gas-Oil Ratio versus Pressure and Gi Tables {#kw-RSGI}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RSGI keyword specifies the saturated oil Gas-Oil Ratio (“GOR”) factors used to specify the variation of the maximum possible GOR of oil with respect to pressure and Gi values, for when the [GIMODEL](#kw-GIMODEL) keyword in the [RUNSPEC](#kw-RUNSPEC) section has been used to activate the [GI](#kw-GI) Pseudo Compositional option for the run. See also the [GINODE](#kw-GINODE), RSGI, [RVGI](#kw-RVGI), [BGGI](#kw-BGGI) and [BOGI](#kw-BOGI) keywords in the [PROPS](#kw-PROPS) section to describe the fluid properties for the [GI](#kw-GI) Pseudo Compositional option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.