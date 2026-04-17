### NZFIN – Define the Number of LGR Grid Blocks in the Z-Direction {#kw-NZFIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

NZFIN defines the number of Local Grid Refinement (“[LGR](#kw-LGR)”) cells within a global or host cell in the z-direction via a vector, as opposed to defining the size for each cell for a Cartesian [LGR](#kw-LGR) Grid. The [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to indicate an [LGR](#kw-LGR) is being used, and the keyword [NXFIN](#kw-NXFIN) should be placed in between the [CARFIN](#kw-CARFIN) and [ENDFIN](#kw-ENDFIN) keywords in the [GRID](#kw-GRID) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | NZFIN | NZFIN is a vector of integer numbers describing the number of [LGR](#kw-LGR) cells within each defined global or host grid block in the x-direction in a Cartesian [LGR](#kw-LGR) grid. Repeat counts may be used, for example 2*2.0. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: NZFIN Keyword Description {#tbl-6-93}
See also the [CARFIN](#kw-CARFIN), [ENDFIN](#kw-ENDFIN), [NXFIN](#kw-NXFIN), and [NYFIN](#kw-NYFIN) keywords in the [GRID](#kw-GRID) section to fully define a Cartesian [LGR](#kw-LGR) grid model.


#### Example


```
--
--       CARFIN LGR GRID COMMANDS
--
--       LGR        ----- HOST GRID ------   -- CARFIN GRID --  MAX     HOST
--       NAME       I1  I2  J1  J2  K1  K2     NX    NY    NZ   WELLS   NAME
CARFIN
         LGR-OP01   24  24  86  86   1  50      8     1    100    1     GLOBAL /
--
--       DEFINE LGR GRID BLOCKS IN THE Z-DIRECTION
--
NZFIN
         50*2                                                                  /

ENDFIN

```

The above example splits the global cells (24, 86, 1-50) into two [LGR](#kw-LGR) grid blocks per host cell in the z-direction, and since the [HZFIN](#kw-HZFIN) keyword has not been supplied, then the host cells will split into equal proportions.