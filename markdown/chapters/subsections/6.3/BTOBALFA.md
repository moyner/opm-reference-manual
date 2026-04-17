### BTOBALFA – Dual Porosity Matrix to Fracture Multiplier (All Cells) {#kw-BTOBALFA}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The BTOBALFA keyword defines a dual porosity matrix to fracture multiplier that is applied to all cells, for when the Dual Porosity model has been activated by either the [DUALPORO](#kw-DUALPORO) or the [DUALPERM](#kw-DUALPERM) keywords in the [RUNSPEC](#kw-RUNSPEC) section.

See also the [BTOBALFV](#kw-BTOBALFV) keyword in the [GRID](#kw-GRID) section that applies a multipliers to individual cells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.