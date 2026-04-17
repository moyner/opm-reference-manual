### LANGSOLV – Langmuir Adsorption Isotherm Solvent Tables {#kw-LANGSOLV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [LANGMUIR](#kw-LANGMUIR) keyword defines the coal bed methane Langmuir Adsorption Isotherms^[Langmuir, Irving (June 1918). "The Adsorption of Gases on Plane Surface of Glass, Mica and Platinum". The Research Laboratory of the General Electric Company. 40 (9): 1361–1402. doi:10.1021/ja02242a004] Solvent tables, for when the Coal Bed Methane option has been activated via the [COAL](#kw-COAL) keyword and the Solvent phase has been declared by the [SOLVENT](#kw-SOLVENT) keyword in the [RUNSPEC](#kw-RUNSPEC) section. See the [COALNUM](#kw-COALNUM) keyword in the [GRID](#kw-GRID) section for allocating the Langmuir solvent tables to the grid blocks, and also the [LANGMUIR](#kw-LANGMUIR) keyword in the [PROPS](#kw-PROPS) section for defining the Langmuir Adsorption Isotherm tables. Keywords [COALADS](#kw-COALADS) and [COALPP](#kw-COALPP), also in the [PROPS](#kw-PROPS) section, are used to specify the relative adsorption data in runs containing the solvent phase.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.