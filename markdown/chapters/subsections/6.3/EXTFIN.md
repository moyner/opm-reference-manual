### EXTFIN – Define an External Unstructured Local Grid Refinement {#kw-EXTFIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The EXTFIN keyword defines an external Unstructured Local Grid Refinement (“[LGR](#kw-LGR)”) in a cell or a group of cells in the global grid, and for when LGRs have been activated for the model using the [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note the global grid can be either structured, see the [EXTREPGL](#kw-EXTREPGL) keyword in the [GRID](#kw-GRID) section for global structure grids, or unstructured, see the [EXTHOST](#kw-EXTHOST) keyword in the [GRID](#kw-GRID) section for unstructured global grids.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.