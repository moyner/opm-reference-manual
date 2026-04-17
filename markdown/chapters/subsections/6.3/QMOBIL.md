### QMOBIL – Activate or Deactivate LGR End-Point Mobility Correction {#kw-QMOBIL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The QMOBIL keyword activates or deactivates the end-point mobility correction for Local Grid Refinements (“[LGR](#kw-LGR)”), for when LGRs have been activated for the input deck using the [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section. QMOBIL should be placed in between the [LGR](#kw-LGR) definition keywords [CARFIN](#kw-CARFIN), or RADIN (or RAFDIN4) and the [ENDFIN](#kw-ENDFIN) keyword in the [GRID](#kw-GRID) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.