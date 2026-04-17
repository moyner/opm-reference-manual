### RIVSALT – Define River Upstream Flow Salt Concentrations {#kw-RIVSALT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RIVSALT keyword defines the injected salt concentration in individual river branches in a previously characterized river system using the [RIVERSYS](#kw-RIVERSYS) and the [REACHES](#kw-REACHES) keywords in the [SCHEDULE](#kw-SCHEDULE) section.  The River option must be activated via the [RIVRDIMS](#kw-RIVRDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section in order to use this keyword.  In addition, the Brine option must also be enabled via the [BRINE](#kw-BRINE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.