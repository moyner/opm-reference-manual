### ENDFIN – End the Definition of a Local Grid Refinement {#kw-ENDFIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ENDFIN keyword defines the end of a Cartesian or radial local grid refinement (“[LGR](#kw-LGR)”) definition and a [LGR](#kw-LGR) property definition data set. In the [GRID](#kw-GRID) section the [CARFIN](#kw-CARFIN), [RADFIN](#kw-RADFIN), and [RADFIN4](#kw-RADFIN4) keywords defines the start of an [LGR](#kw-LGR) description section, whereas the [REFINE](#kw-REFINE) keyword in the [EDIT](#kw-EDIT), [PROPS](#kw-PROPS), [REGIONS](#kw-REGIONS), [SOLUTION](#kw-SOLUTION) and [SCHEDULE](#kw-SCHEDULE) section defines the start. The [REFINE](#kw-REFINE) keyword can also be used in the [GRID](#kw-GRID) section provided the [LGR](#kw-LGR) has been previously specified by the [CARFIN](#kw-CARFIN), [RADFIN](#kw-RADFIN), or [RADFIN4](#kw-RADFIN4) keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example

The example below is based on using the [CARFIN](#kw-CARFIN) keyword in the [GRID](#kw-GRID) section to define an [LGR](#kw-LGR) in the global grid, named [LGR](#kw-LGR)-OP01 with a maximum of one well allowed in the [LGR](#kw-LGR).


```
--
--       CARFIN LGR GRID COMMANDS
--
--       LGR        ----- FINE GRID ------   -- CARFIN GRID --  MAX     HOST
--       NAME       I1  I2  J1  J2  K1  K2     NX    NY    NZ   WELLS   NAME
CARFIN
         LGR-OP01   24  24  87  87   1  50      3     3    50     1     GLOBAL /


ENDFIN

```

Here the one global cell in the areal plane (24, 87) is divided into three [LGR](#kw-LGR) cells in the x-direction and three cells in the y-direction.   Since no other property data is given, then the [LGR](#kw-LGR) cells take their properties from the host grid, that is the global grid.