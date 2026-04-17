### RIVTRACE – Define River Upstream Flow Tracer Concentrations {#kw-RIVTRACE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RIVTRACE keyword defines the injected tracer concentration in individual river branches in a previously characterized river system using the [RIVERSYS](#kw-RIVERSYS) and the [REACHES](#kw-REACHES) keywords in the [SCHEDULE](#kw-SCHEDULE) section.  The River option must be activated via the [RIVRDIMS](#kw-RIVRDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section in order to use this keyword.  In addition, the Tracer option must also be enabled by the [TRACER](#kw-TRACER) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.