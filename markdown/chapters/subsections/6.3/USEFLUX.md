### USEFLUX – Activate Flux Boundary Model and Define Flux File {#kw-USEFLUX}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The USEFLUX keyword activates the Flux Boundary model and defines the name of the FLUX file.  Only grid blocks that have been declared by the [FLUXREG](#kw-FLUXREG) keyword in the [GRID](#kw-GRID) section to be in an active flux region, are active for the run.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.