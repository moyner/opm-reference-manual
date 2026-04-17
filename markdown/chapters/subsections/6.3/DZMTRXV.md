### DZMTRXV – Matrix Block Height for Gravity Drainage Model For All Cells {#kw-DZMTRXV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [DZMATRIX](#kw-DZMATRIX) keyword defines the matrix block height for the gravity drainage model by grid block for when the Dual Permeability or Dual Porosity models are activated by the [DUALPERM](#kw-DUALPERM) and [DUALPORO](#kw-DUALPORO) keywords and the Gravity Drainage option is invoked via the [GRAVDR](#kw-GRAVDR) and [GRAVDRM](#kw-GRAVDRM) keywords. All keywords are in the [RUNSPEC](#kw-RUNSPEC) section.

The keyword is identical to the [DZMATRIX](#kw-DZMATRIX) keyword in the [GRID](#kw-GRID) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.