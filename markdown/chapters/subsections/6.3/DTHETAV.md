### DTHETAV – Sets the Size of Grid Blocks in THETA Direction via a Vector {#kw-DTHETAV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

DTHETAV defines the size of grid blocks in the THETA direction via a vector as opposed to defining the property for each cell for a Radial Grid. The [RADIAL](#kw-RADIAL) or [SPIDER](#kw-SPIDER) keyword in the [RUNSPEC](#kw-RUNSPEC) should be activated to indicate that radial geometry is being used.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | DTHETAV | DTHETAV is a vector of real numbers describing the cell size for the grid blocks in the THETA direction in a radial grid. Repeat counts may be used, for example 10*100.0. | None |
| degrees | degrees | degrees |  |
| Notes: |  |  |  |
: DTHETA Keyword Description {#tbl-6-25}
Note that the [SPIDER](#kw-SPIDER) keyword activates OPM Flow’s radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: [INRAD](#kw-INRAD), [DRV](#kw-DRV), DTHETAV, [DZ](#kw-DZ)/[DZV](#kw-DZV) etc. in the [GRID](#kw-GRID) the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software.  To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model’s pore volume to reflect radial coordinates; thus, overcoming the display limitation.


See also the [DRV](#kw-DRV), [DZV](#kw-DZV) and [TOPS](#kw-TOPS) keywords to fully define a radial or spider grid model.


#### Example


```
--
--       DEFINE GRID BLOCK SIZES IN THE THETA DIRECTION (BASED ON NY = 6)
--
DTHETAV
         60.0  60.0  60.0  60.0  60.0  60.0                                    /

```

The above example defines the size of the cells in the THETA direction based on NY equals six in the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.