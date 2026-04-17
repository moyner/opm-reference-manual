### HZFIN – Define the Ratio of LGR Grid Blocks in the Z-Direction {#kw-HZFIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

HZFIN defines the split ratio of grid blocks for the [DZV](#kw-DZV) keyword in the z-direction via a vector within a Local Grid Refinement (“[LGR](#kw-LGR)”) as opposed to defining the size for each cell for a Cartesian [LGR](#kw-LGR) Grid. The [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to indicate an [LGR](#kw-LGR) is being used, and the keyword [HYFIN](#kw-HYFIN) should be placed in between the [CARFIN](#kw-CARFIN) and [ENDFIN](#kw-ENDFIN) keywords in the [GRID](#kw-GRID) section. The [DZV](#kw-DZV) keyword in the [GRID](#kw-GRID) section defines the grid size in terms of the length, that is feet for field units, this keyword defines the length as the ratio of the coarse cells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | HYZIN | HZFIN is a vector of real numbers describing the ratio of cell size for the grid blocks in the z-direction in a Cartesian [LGR](#kw-LGR) grid. Repeat counts may be used, for example 2*2.0. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: HZFIN Keyword Description {#tbl-6-49}
See also the [CARFIN](#kw-CARFIN), [ENDFIN](#kw-ENDFIN), [HXFIN](#kw-HXFIN), and [HYFIN](#kw-HYFIN) keywords in the [GRID](#kw-GRID) section to fully define a Cartesian [LGR](#kw-LGR) grid model.


#### Example


```
--
--       CARFIN LGR GRID COMMANDS
--
--       LGR        ----- HOST GRID ------   -- CARFIN GRID --  MAX     HOST
--       NAME       I1  I2  J1  J2  K1  K2     NX    NY    NZ   WELLS   NAME
CARFIN
         LGR-OP01   24  25  86  87   1  50      5     3    100    1     GLOBAL /
--
--       DEFINE LGR GRID BLOCK IN THE Z-DIRECTION
NZFIN
         50*2                                                                  /
--
--       DEFINE GRID BLOCK LGR RATIOS IN THE Z-DIRECTION
--
HZFIN
         50*2.0                                                                /
ENDFIN

```

The above example defines the size of the cells in the z-direction based on NZ equals 100 on the [CARFIN](#kw-CARFIN) keyword in the [GRID](#kw-GRID) section.