### SURFADDW – Defined Surfactant Adsorbed Concentration versus Wettability Fraction {#kw-SURFADDW}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SURFADDW defines tables of surfactant adsorbed concentration versus wettability fraction for when the [SURFACTW](#kw-SURFACTW) keyword in the [RUNSPEC](#kw-RUNSPEC) section as been declared to activate the surfactant phase with changing wettability. The tables consists of columnar vectors of adsorbed surfactant concentration versus a wettability fraction that indicates the fraction of phase wettability.  Here, a wettability fraction of zero indicates a 100% water wet rock resulting in the [SURFWNUM](#kw-SURFWNUM) allocated saturation tables being used, and a value of one meaning 100% oil wet rock, with the [SATNUM](#kw-SATNUM) allocated saturations tables being employed. Both the [SURFWNUM](#kw-SURFWNUM) and [SATNUM](#kw-SATNUM) keywords are in the [REGIONS](#kw-REGIONS) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.