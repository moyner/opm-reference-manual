### TRACTVD – Activate Tracer Explicit Flux Limited Transport Option {#kw-TRACTVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

TRACTVD activates the Tracer Explicit Flux Limited Transport option. Basically the option is used to control numerical dispersion for tracers.  Both the [TRACERS](#kw-TRACERS) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section must be declared to activate tracers and to define the tracers.


See also the [TRACITVD](#kw-TRACITVD) keyword in the [PROPS](#kw-PROPS) section activates the Tracer Implicit Flux Limited Transport option.


This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.