### LGROFF – Deactivate a Local Grid Refinement {#kw-LGROFF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LGROFF keyword deactivates a stated Local Grid Refinement (“[LGR](#kw-LGR)”) and optionally sets the minimum number of wells below which the [LGR](#kw-LGR) will be automatically deactivated. LGRs must have declared by the [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and defined by the [CARFIN](#kw-CARFIN) (Cartesian [LGR](#kw-LGR) grid) or RADIN/RADIN4 (radial [LGR](#kw-LGR) grid) keywords in the [GRID](#kw-GRID) section. LGRs can subsequently be activated by the  [LGRON](#kw-LGRON) keyword in the [SCHEDULE](#kw-SCHEDULE) section.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | LGRNAME | A character string of up to eight characters in length that defines the [LGR](#kw-LGR) name for which the [LGR](#kw-LGR) is being deactivated. The [LGR](#kw-LGR) must have been previously defined by the [CARFIN](#kw-CARFIN) (Cartesian [LGR](#kw-LGR) grid) or RADIN/RADIN4 (radial [LGR](#kw-LGR) grid) keywords in the [GRID](#kw-GRID) section. | None |
| 2 | MNWELLS | A positive integer greater than or equal to zero that defines the minimum number of active wells, below which the [LGR](#kw-LGR) will be automatically deactivated. The default value of zero implies that there is no limit to the number of wells and results in the [LGR](#kw-LGR) being unconditionally being deactivated. | 0 |
| Notes: |  |  |  |
: LGROFF Keyword Description {#tbl-12-50}
#### Example

The example below unconditionally deactivates [LGR](#kw-LGR)-OP01, and sets the minimum number of active wells for deactivating [LGR](#kw-LGR)-OP02 and [LGR](#kw-LGR)-OP03 to one. For all the gas well LGRs ([LGR](#kw-LGR)-GP*) the minimum number of wells for deactivation is set to two.


```
--
--       DEACTIVATE LOCAL GRID REFINEMENTS
--
--       LGRNAME   MNWELLS
LGROFF
         LGR-OP01                                                              /
         LGR-OP02  1                                                           /
         LGR-OP03  1                                                           /
         LGR-GP*   2                                                           /
/

```