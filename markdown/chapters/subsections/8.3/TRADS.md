### TRADS – Environmental Tracer Adsorption Tables {#kw-TRADS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, TRADS, specifies the environmental tracer adsorption tables that describe how a tracer is absorbed by the surrounding rock, for when the MXENVTR parameter has been set to greater than zero on the [TRACERS](#kw-TRACERS) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate environmental tracers.  The keyword can only be used with environmental tracers.

Unlike other keywords, the TRADS keyword must be concatenated with the three character name of the tracer declared by [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.