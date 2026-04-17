### HRFIN – Define the Ratio of LGR Grid Blocks in the R-Direction {#kw-HRFIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

HRFIN^[Radial grids are not currently implemented in this version of OPM Flow,  but is expected to be incorporated in a future release.] defines the ratio of grid blocks for the [DRV](#kw-DRV) keyword in the r-direction via a vector within a Local Grid Refinement (“[LGR](#kw-LGR)”) as opposed to defining the size for each cell for a Radial [LGR](#kw-LGR) Grid. The [LGR](#kw-LGR)  keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to indicate an [LGR](#kw-LGR) is being used, and the keyword HRFIN should be placed in between the RADIN (or RAFDIN4) and [ENDFIN](#kw-ENDFIN) keywords in the [GRID](#kw-GRID) section. The [DRV](#kw-DRV) keyword in the [GRID](#kw-GRID) section defines the radial grid size in terms of the length, that is feet for field units, this keyword defines the length as the ratio of the previous cell size, staring with the inner radius ([INRAD](#kw-INRAD)).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | HRFIN | HRFIN is a vector of real numbers describing the ratio of cell size for the grid blocks in the r-direction in a radial [LGR](#kw-LGR) for the [DRV](#kw-DRV) keyword. Repeat counts may be used, for example 2*1.5. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: HRFIN Keyword Description {#tbl-6-46}
See also the [DR](#kw-DR), [DRV](#kw-DRV), [DTHETAV](#kw-DTHETAV), and [DZ](#kw-DZ) keywords in the [GRID](#kw-GRID) section to fully define a radial [LGR](#kw-LGR) model.


#### Example


```
--
--       INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION
--
INRAD    0.25                                                                 /
--
--       DEFINE GRID BLOCK DRV RATIOS IN THE R DIRECTION
--
HRFIN
         1.50  2.00  3.00  5.00  7.00  10.00                                  /
```


The above example defines the size of the cells in the R direction based on NR equals 7, resulting in NR-1 values on the [RADFIN](#kw-RADFIN) keyword in the [GRID](#kw-GRID) section. Note the [INRAD](#kw-INRAD) keyword to define the inner radius of the radial grid.