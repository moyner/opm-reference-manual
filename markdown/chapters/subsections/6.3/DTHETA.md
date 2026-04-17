### DTHETA – Define the Size of Grid Blocks in the THETA Direction for All Cells {#kw-DTHETA}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

DTHETA defines the size of all grid blocks in the Theta direction via an array for each cell in model. The [RADIAL](#kw-RADIAL) or [SPIDER](#kw-SPIDER) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to indicate that radial or spider geometry is being used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | DTHETA | DTHETA is an array of real numbers describing the cell size in the THETA direction in radial grids for each cell in the model. Repeat counts may be used, for example 10*25.0 | None |
| degrees | degrees | degrees |  |
| Notes: |  |  |  |
: DTHETA Keyword Description {#tbl-6-24}
Note that the [SPIDER](#kw-SPIDER) keyword activates OPM Flow’s radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: [INRAD](#kw-INRAD), [DRV](#kw-DRV), [DTHETAV](#kw-DTHETAV), [DZ](#kw-DZ)/[DZV](#kw-DZV) etc. in the [GRID](#kw-GRID) the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software.  To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model’s pore volume to reflect radial coordinates; thus, overcoming the display limitation. See also the [DRV](#kw-DRV), [DTHETAV](#kw-DTHETAV), [DZ](#kw-DZ) and [TOPS](#kw-TOPS) keywords in the [GRID](#kw-GRID) section to fully define a radial or spider grid model.


#### Example

Given the dimensions of the grid in the [RUNSPEC](#kw-RUNSPEC) section to be 10, 6, 1 for NX, NY and NZ respectively, then DTHETA should be defined as:


```
--
--       DEFINE GRID BLOCK SIZES IN THE THETA DIRECTION
--
DTHETA
         10*60.0
         10*60.0
         10*60.0
         10*60.0
         10*60.0
         10*60.0
/
```

The above example defines the size of the cells in the R direction based on 60 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.