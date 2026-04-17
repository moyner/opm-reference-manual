### MULTSIGV – Multiply Matrix-Fracture Coupling for Individual Cells {#kw-MULTSIGV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, MULTSIGV, defines a constant multiplier to modify the matrix-fracture coupling transmissibility for dual porosity and dual permeability models, for when the matrix-fracture coupling transmissibilities have been specified via the [SIGMAGD](#kw-SIGMAGD) or [SIGMAGDV](#kw-SIGMAGDV) keywords in the [GRID](#kw-GRID) section, and the dual porosity or dual permeability models have activated by the [DUALPORO](#kw-DUALPORO) or [DUALPERM](#kw-DUALPERM) keywords in the [RUNSPEC](#kw-RUNSPEC) section, respectively.

This keyword applies the multiplier for individual cells in model; whereas, the [MULTSIG](#kw-MULTSIG) keyword in the [SCHEDULE](#kw-SCHEDULE) section applies the multiplier to all grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.