### DPGRID – Activate The Matrix Cell to Fracture Cell Option {#kw-DPGRID}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The DPGRID keyword activates the matrix cell to fracture cell option for dual porosity runs for when a Dual Porosity model has been activated by either the [DUALPORO](#kw-DUALPORO) or [DUALPERM](#kw-DUALPERM) keywords in the [RUNSPEC](#kw-RUNSPEC) section. The keyword allows for only the matrix grid data to be entered and the missing fracture cells are set to the inputted matrix cells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.