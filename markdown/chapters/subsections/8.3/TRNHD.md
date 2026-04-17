### TRNHD – Activate Dispersion Non-Homogeneous Diffusion Option {#kw-TRNHD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The TRNHD keyword activates the Dispersion Non-Homogeneous Diffusion option for when tracer dispersion is independent of velocity or tracer concentration. Unlike other keywords, the TRNHD keyword must be concatenated with the name of the tracer declared by [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.