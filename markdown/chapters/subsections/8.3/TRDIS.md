### TRDIS – Tracer Dispersion Table Number Allocation {#kw-TRDIS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, TRDIS, specifies the tracer diffusion tables that should be allocated to a tracer, the actual dispersion tables are specified by the [DISPERSE](#kw-DISPERSE) keyword in the [PROPS](#kw-PROPS) section. The keyword can be used with Environmental Tracers if the MXENVTR parameter has been set greater than zero on the [TRACERS](#kw-TRACERS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The option does not work with two-phase Standard Partitioned Tracers and Multi-Partitioned Tracers. Unlike other keywords, the [TRADS](#kw-TRADS) keyword must be concatenated with the three character name of the tracer declared by [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section.


This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.