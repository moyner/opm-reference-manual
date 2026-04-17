### LGRFREE – Activate Local Grid Refinement Independent Time Steps {#kw-LGRFREE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LGRFREE keyword activates the Local Grid Refinement (“[LGR](#kw-LGR)”) Independent Time Step option that allows the [LGR](#kw-LGR) to have solution time steps independent of the host grid for the stated [LGR](#kw-LGR), and for when LGRs have been declared by the [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and defined by the [CARFIN](#kw-CARFIN) (Cartesian [LGR](#kw-LGR) grid) or RADIN/RADIN4 (radial [LGR](#kw-LGR) grid) keywords in the [GRID](#kw-GRID) section. [LGR](#kw-LGR) independent solution time stepping can be deactivated by the [LGRLOCK](#kw-LGRLOCK) keyword in the [SCHEDULE](#kw-SCHEDULE) section.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | LGRNAME | A character string of up to eight characters in length that defines the [LGR](#kw-LGR) name for which independent solution time stepping is to be activated. The [LGR](#kw-LGR) must have been previously defined by the [CARFIN](#kw-CARFIN) (Cartesian [LGR](#kw-LGR) grid) or RADIN/RADIN4 (radial [LGR](#kw-LGR) grid) keywords in the [GRID](#kw-GRID) section. | None |
| Notes: |  |  |  |
: LGRFREE Keyword Description {#tbl-12-48}
#### Example

The example below defines three oil LGRs([LGR](#kw-LGR)-OP01,-OP02, and -OP03) and all the gas well LGRs ([LGR](#kw-LGR)-GP*) that should use independent solution time steps.


```
--
--       ACTIVATE LOCAL GRID REFINEMENT INDEPENDENT TIME STEPS
--
--       LGRNAME
LGRFREE
         LGR-OP01                                                              /
         LGR-OP02                                                              /
         LGR-OP03                                                              /
         LGR-GP*                                                               /
/

```