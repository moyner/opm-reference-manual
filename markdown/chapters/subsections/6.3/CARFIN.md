### CARFIN – Define a Cartesian Local Grid Refinement {#kw-CARFIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

CARFIN defines a Cartesian Local Grid Refinement (“[LGR](#kw-LGR)”) in a cell or a group of cells in the host grid, for when LGRs have been activated for the input deck using the [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword marks the start of an [LGR](#kw-LGR) description section and all subsequent keywords between the CARFIN and [ENDFIN](#kw-ENDFIN) keywords are deemed to be associated with the current [LGR](#kw-LGR) and not the host grid.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | LGRNAME | A character string of up to eight characters in length that defines the [LGR](#kw-LGR) name for which the [LGR](#kw-LGR) is being being defined. | None |
| 2 | I1 | A positive integer that defines the lower index of the global or host grid in the I-direction to be refined; must be greater than or equal 1 and less than or equal to I2 and NX on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 3 | I2 | A positive integer that defines the upper index of the global or host grid in the I-direction to be refined; must be greater than or equal 1 and II,  and less than or equal to NX on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 4 | J1 | A positive integer that defines the lower index of the global or host grid in the J-direction to be refined; must be greater than or equal 1 and less than or equal to J2 and NY on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 5 | J2 | A positive integer that defines the upper index of the global or host grid in the J-direction to be refined; must be greater than or equal 1 and JI,  and less than or equal to NY on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 6 | K1 | A positive integer that defines the lower index of the global or host grid in the K-direction to be refined; must be greater than or equal 1 and less than or equal to K2 and NZ on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 7 | K2 | A positive integer that defines the upper index of the global or host grid in the K-direction to be refined; must be greater than or equal 1 and KI,  and less than or equal to NZ on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 8 | NX | A positive integer value that defines the number of [LGR](#kw-LGR) grid blocks in the x direction for Cartesian grids or the number of grid blocks in the r direction for radial grids | None |
| 9 | NY | A positive integer value that defines the number of [LGR](#kw-LGR) grid blocks in the y direction for Cartesian grids or the number of grid blocks in the theta direction for radial grids. | None |
| 10 | NZ | A positive integer value that defines the number of [LGR](#kw-LGR) grid blocks in the z direction for both Cartesian and radial grids. | None |
| 11 | MXWELS | A positive integer defining the maximum number of wells contained in this [LGR](#kw-LGR). | None |
| 12 | HOSTNAME | A character string of up to eight characters in length that defines the host grid name for nested refinements. The default value of “GLOBAL” sets the host name to the global grid, that is for a conventional [LGR](#kw-LGR). A nested refinement is when the HOSTNAME is a previously declared [LGR](#kw-LGR) for which the current [LGR](#kw-LGR) is specifying a further [LGR](#kw-LGR) refinement. | GLOBAL |
| Notes: |  |  |  |
: CARFIN Keyword Description {#tbl-6-12}
Note that if the Dual Porosity option has be activated by either the [DUALPORO](#kw-DUALPORO) or [DUALPERM](#kw-DUALPERM) keywords in the [RUNSPEC](#kw-RUNSPEC) section, then the host grid definition (I1-I2, J1-J2, K1-K2) applies only to the matrix cells; however, the [LGR](#kw-LGR) NZ parameter in this case must include the fracture blocks, similar to the NZ parameter on the [DIMENS](#kw-DIMENS) keyword. This means that all property data should be entered for both the matrix and fracture cells in the [LGR](#kw-LGR) description.


#### Example

The example below defines an [LGR](#kw-LGR) in the global grid, named [LGR](#kw-LGR)-OP01 with a maximum of one well allowed in the [LGR](#kw-LGR).


```
--
--       CARFIN LGR GRID COMMANDS
--
--       LGR        ----- HOST GRID ------   -- CARFIN GRID --  MAX     HOST
--       NAME       I1  I2  J1  J2  K1  K2     NX    NY    NZ   WELLS   NAME
CARFIN
         LGR-OP01   24  24  87  87   1  50      3     3    50     1     GLOBAL /


ENDFIN

```

Here the one global cell in the areal plane (24, 87) is divided into three [LGR](#kw-LGR) cells in the x-direction and three cells in the y-direction.   Since no other property data is given, then the [LGR](#kw-LGR) cells take their properties from the host grid, that is the global grid.