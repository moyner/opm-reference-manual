### INTPC – Activate Dual Porosity Integrated Capillary Pressure Option {#kw-INTPC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The INTPC keyword activates the integrated capillary pressure option for the oil, gas or both phases,  for when a Dual Porosity model has been activated by either the [DUALPORO](#kw-DUALPORO) or [DUALPERM](#kw-DUALPERM) keywords in the [RUNSPEC](#kw-RUNSPEC) section. In addition, the keyword can only be used if the Gravity Drainage option has been specified by either the [GRAVDR](#kw-GRAVDR) or [GRAVDRM](#kw-GRAVDRM) in the [RUNSPEC](#kw-RUNSPEC) section. Basically, activating this feature results in the simulator adjusting the capillary pressure curves by integrating the matrix capillary pressure curves over the matrix block height to calculate the average saturation.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.