### LXFIN – Define Logarithmic LGR Grid Block Spacing in the X-Direction {#kw-LXFIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LXFIN keyword defines the parameters for automatically generating a Local Grid Refinement (“[LGR](#kw-LGR)”) grid in the X direction based on logarithmic block spacing, for when the [LGR](#kw-LGR) option has been activated by the [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section. LXFIN should be placed in between the [CARFIN](#kw-CARFIN) and [ENDFIN](#kw-ENDFIN) keywords in the [GRID](#kw-GRID) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.