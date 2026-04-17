### DPNUM – Define Dual and Single Porosity Grid Block Array {#kw-DPNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

In dual porosity runs only, that is not dual permeability runs, the DPNUM keyword defines which wells should be treated as single porosity cells and which cells should be treated as dual porosity cells, for when the Dual Porosity model has been activated by the [DUALPORO](#kw-DUALPORO) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.