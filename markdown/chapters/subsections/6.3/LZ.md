### LZ – Dual Porosity Viscous Displacement Z Direction Matrix Size for All Cells {#kw-LZ}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LZ keyword defines the size of  “representative” matrix grid blocks in the Z direction via an array in dual porosity and dual permeability runs, for when the [VISCD](#kw-VISCD) keyword has been used in the [RUNSPEC](#kw-RUNSPEC) section to activate the dual porosity viscous displacement option. In addition, either the [DUALPORO](#kw-DUALPORO) or [DUALPERM](#kw-DUALPERM) keyword should be entered in the [RUNSPEC](#kw-RUNSPEC) section to activate the dual porosity or dual permeability models.  The [VISCD](#kw-VISCD) option is used to model the viscous displacement of fluids from the matrix by the fracture pressure gradient, for when the fracture system has a more moderate permeability, and flow to and from the matrix caused by the fracture pressure gradient acts as an additional production mechanism.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | LZ | LZ is an array of real numbers describing the “representative” cell size in the Z direction for each cell in the model. Repeat counts may be used, for example 10*100.0. | 0 |
| feet | m | cm |  |
| Notes: |  |  |  |
: LZ Keyword Description {#tbl-6-57}
If the [VISCD](#kw-VISCD) keyword has been used to activate the Dual Porosity Viscous Displacement option and LZ has not been specified then LZ is set to zero in the calculation of the viscous displacement term.


See also the [LX](#kw-LX), [LY](#kw-LY) and [LTOSIGMA](#kw-LTOSIGMA) keywords in the [GRID](#kw-GRID) section.


#### Example


```
--
--       DEFINE INPUT BOX FOR EDITING INPUT ARRAYS
--
--       ---------- BOX ---------
--       I1  I2   J1  J2   K1  K2
BOX
         10  10   1   6    1   1                           / DEFINE BOX AREA
--
--       DEFINE DUAL POROSITY VISCOUS DISPLACEMENT Z DIRECTION MATRIX SIZE
--
LZ
         6*3.0                                             /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX
```


The example defines a subset of the grid and the size of the “representative” matrix cells in the Y direction to 15.0 ft.;  after which the [ENDBOX](#kw-ENDBOX) keyword resets the input to be the full grid.