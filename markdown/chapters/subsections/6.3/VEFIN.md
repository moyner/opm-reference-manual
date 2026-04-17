### VEFIN – Activate Vertical Equilibrium Model (LGR) {#kw-VEFIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

If the [VE](#kw-VE) keyword in the [RUNSPEC](#kw-RUNSPEC) section has been used to activate the Vertical Equilibrium (“[VE](#kw-VE)”) model for the global grid, then the VEFIN keyword may used to set various options for the Local Grid Refinements (“[LGR](#kw-LGR)”).  The [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to indicate the presence of LGRs and the keyword VEFIN should be placed in between the [CARFIN](#kw-CARFIN) and [ENDFIN](#kw-ENDFIN) keywords in the [GRID](#kw-GRID) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.