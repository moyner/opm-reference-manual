### NYFIN – Define the Number of LGR Grid Blocks in the Y-Direction {#kw-NYFIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

NYFIN defines the number of Local Grid Refinement (“[LGR](#kw-LGR)”) cells within a global or host cell in the x-direction via a vector, as opposed to defining the size for each cell for a Cartesian [LGR](#kw-LGR) Grid. The [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to indicate an [LGR](#kw-LGR) is being used, and the keyword NYFIN should be placed in between the [CARFIN](#kw-CARFIN) and [ENDFIN](#kw-ENDFIN) keywords in the [GRID](#kw-GRID) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | NYFIN | NYFIN is a vector of integer numbers describing the number of [LGR](#kw-LGR) cells within each defined global or host grid block in the y-direction in a Cartesian [LGR](#kw-LGR) grid. Repeat counts may be used, for example 2*2.0. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: NYFIN Keyword Description {#tbl-6-92}
See also the [CARFIN](#kw-CARFIN), [ENDFIN](#kw-ENDFIN), [NXFIN](#kw-NXFIN), and [NZFIN](#kw-NZFIN) keywords in the [GRID](#kw-GRID) section to fully define a Cartesian [LGR](#kw-LGR) grid model.


#### Example


```
--
--       CARFIN LGR GRID COMMANDS
--
--       LGR        ----- HOST GRID ------   -- CARFIN GRID --  MAX     HOST
--       NAME       I1  I2  J1  J2  K1  K2     NX    NY    NZ   WELLS   NAME
CARFIN
         LGR-OP01   24  24  86  87   1  50      1     8    50     1     GLOBAL /
--
--       DEFINE LGR GRID BLOCKS IN THE Y-DIRECTION
--
NYFIN
         4  4                                                                  /

ENDFIN

```

The above example splits the global cells (24, 86-87,1-50) into four and four [LGR](#kw-LGR) grid blocks in the y-direction and since the [HYFIN](#kw-HYFIN) keyword has not been supplied, then the host cells will split into equal proportions.