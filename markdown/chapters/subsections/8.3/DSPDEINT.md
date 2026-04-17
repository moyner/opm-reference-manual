### DSPDEINT – Activate Brine Tracer Dispersion Interpolation by Water Density {#kw-DSPDEINT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, DSPDEINT, activates the brine tracer dispersion interpolation by water density option for when the Brine phase is activated in the model by the [BRINE](#kw-BRINE) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the [DISPERSE](#kw-DISPERSE) keyword in the [PROPS](#kw-PROPS) section is in the input file.  They keyword cause the lookup and interpolation of the [DISPERSE](#kw-DISPERSE) tracer concentration to water density, that is the tracer concentration data on the [DISPERSE](#kw-DISPERSE) keyword has been replaced by the water density data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.