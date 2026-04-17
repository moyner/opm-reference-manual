### LTOSIGMA – Dual Porosity Viscous Displacement Sigma Parameters {#kw-LTOSIGMA}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LTOSIGMA keyword defines parameters to calculate the sigma factor in conjunction with the data entered via the [LX](#kw-LX), [LY](#kw-LY) and [LZ](#kw-LZ) keywords in the [GRID](#kw-GRID) section, for when the [VISCD](#kw-VISCD) keyword has been used in the [RUNSPEC](#kw-RUNSPEC) section to activate the Dual Porosity Viscous Displacement option. In addition, either the [DUALPORO](#kw-DUALPORO) or [DUALPERM](#kw-DUALPERM) keyword should be entered in the [RUNSPEC](#kw-RUNSPEC) section to activate the dual porosity or dual permeability models.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.