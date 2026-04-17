### MLANG – Define Langmuir Maximum Gas Concentration for All Grid Cells {#kw-MLANG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, MLANG, defines the coal bed methane Langmuir Adsorption^[Langmuir, Irving (June 1918). "The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum". The Research Laboratory of the General Electric Company. 40 (9): 1361–1402. doi:10.1021/ja02242a004] maximum gas concentration for each grid cell used to scale the Langmuir isotherm table allocated to the cell, for when the Coal Bed Methane option has been activated via the [COAL](#kw-COAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. See the [LANGMUIR](#kw-LANGMUIR) keyword in the [PROPS](#kw-PROPS) section for specifying the Langmuir tables for the model.

Note that if he Dual Porosity model has been activated by either the [DUALPORO](#kw-DUALPORO) or the [DUALPERM](#kw-DUALPERM) keywords in the [RUNSPEC](#kw-RUNSPEC) section, then MLANG applies to only the matrix grid block.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.