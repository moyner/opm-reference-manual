### BTOBALFV – Dual Porosity Matrix to Fracture Multiplier (Individual Cells) {#kw-BTOBALFV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The BTOBALFV keyword defines a dual porosity matrix to fracture multiplier that is applied to individual cells, for when the Dual Porosity model has been invoked by either the [DUALPORO](#kw-DUALPORO) or the [DUALPERM](#kw-DUALPERM) keywords in the [RUNSPEC](#kw-RUNSPEC) section.

See also the BTOBALFAV keyword in the [GRID](#kw-GRID) section that applies a constant multiplier to all cells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.