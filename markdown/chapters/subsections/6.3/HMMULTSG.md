### HMMULTSG – History Match Dual porosity Sigma Gradient Cumulative Multipliers {#kw-HMMULTSG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

HMMULTSG defines the history match dual porosity sigma parameter gradient cumulative multipliers applied to the dual porosity sigma value declared by the [SIGMAV](#kw-SIGMAV) and [SIGMAGDV](#kw-SIGMAGDV) keywords in the [PROPS](#kw-PROPS) section, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. In addition to the [HMDIMS](#kw-HMDIMS) keyword, either the [DUALPERM](#kw-DUALPERM) keyword that activates the Dual Permeability option, or the [DUALPORO](#kw-DUALPORO) keyword that activates the Dual Porosity option for the run, must be declared in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.