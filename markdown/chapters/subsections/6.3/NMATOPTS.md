### NMATOPTS – Define the Discretized Matrix Dual Porosity Parameters {#kw-NMATOPTS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NMATOPTS keyword defines the Discretized Matrix Dual Porosity parameters for when the Discretized Matrix Dual Porosity option has been activated by [NMATRIX](#kw-NMATRIX) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The option allows the matrix grid blocks to be subdivided into smaller cells for more accurate flow calculations, in particular the modeling of transient flow within the matrix grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.