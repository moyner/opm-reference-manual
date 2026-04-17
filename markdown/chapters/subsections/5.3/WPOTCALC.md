### WPOTCALC – Well Potential Calculation Options {#kw-WPOTCALC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WPOTCALC defines how shut-in and stopped wells should have their well potentials calculated. Well potentials for wells under these conditions need to have their potentials calculated if they are in a Priority Drilling Queue via the [WDRILPRI](#kw-WDRILPRI) keyword in the [SCHEDULE](#kw-SCHEDULE) section, or the Prioritization option has been enabled by the [PRIORITY](#kw-PRIORITY) keyword in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.