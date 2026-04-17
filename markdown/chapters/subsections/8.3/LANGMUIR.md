### LANGMUIR – Langmuir Adsorption Isotherm Tables {#kw-LANGMUIR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LANGMUIR keyword defines the coal bed methane Langmuir Adsorption Isotherms^[Langmuir, Irving (June 1918). "The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum". The Research Laboratory of the General Electric Company. 40 (9): 1361–1402. doi:10.1021/ja02242a004] tables, for when the Coal Bed Methane option has been activated via the [COAL](#kw-COAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. See the [COALNUM](#kw-COALNUM) keyword in the [GRID](#kw-GRID) section for allocating the Langmuir tables to the grid blocks and also the [LANGMPL](#kw-LANGMPL) keyword in the [PROPS](#kw-PROPS) section for re-scaling the pressure values in the tables that are allocated to a cell.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.