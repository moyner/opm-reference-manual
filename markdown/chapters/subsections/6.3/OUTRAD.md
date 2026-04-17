### OUTRAD – Define the Outer Radius of a Radial Grid {#kw-OUTRAD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

OUTRAD defines the OUTER radius of the reservoir model for a radial or spider grid geometry. The [RADIAL](#kw-RADIAL) or [SPIDER](#kw-SPIDER) keyword in the [RUNSPEC](#kw-RUNSPEC) should be activated to indicate that radial or spider geometry is being used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | OUTRAD | A single real positive number greater than [INRAD](#kw-INRAD) defining the outer radius of a radial grid. | None |
| feet | m | cm |  |
| Notes: |  |  |  |
: OUTRAD Keyword Description {#tbl-6-99}
Note that the [SPIDER](#kw-SPIDER) keyword activates OPM Flow’s radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: [INRAD](#kw-INRAD), [DRV](#kw-DRV), [DTHETAV](#kw-DTHETAV), [DZ](#kw-DZ)/[DZV](#kw-DZV) etc. in the [GRID](#kw-GRID) the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software.  To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model’s pore volume to reflect radial coordinates; thus, overcoming the display limitation.

The keyword allows for an alternative method of entering the size of the R direction grid cells instead of entering the data using the [DR](#kw-DR) or [DRV](#kw-DRV) keywords in the [GRID](#kw-GRID) section. Given the internal radius set by the [INRAD](#kw-INRAD) keyword, the external radius set by the OUTRAD keyword and the number of grid cells in the R direction set by the NX variable on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, the R direction cells sizes are computed automatically on a geometric spacing, as defined by:


$$
\frac{{R}_{i}}{{R}_{i-1}} = (\frac{\mathit{OUTRAD}}{{R}_{{i}_{j}-1}}){ }^{\frac{1}{(\mathit{NX} - {i}_{j} + 1)}}
$$ {#eq-6-12}

or


$$
{R}_{i} = ({R}_{{i}_{j}-1})(\frac{\mathit{OUTRAD}}{{R}_{{i}_{j}-1}}){ }^{\frac{(i - {i}_{j} +1 )}{(\mathit{NX} - {i}_{j} + 1)}}
$$ {#eq-6-13}

and the [DR](#kw-DR) value for the ith cell, that is the value that can also be manually entered on the [DR](#kw-DR) keyword in the [GRID](#kw-GRID) section, is given by:


$$
{\mathit{[DR](#kw-DR)}}_{i} = {R}_{i} - {R}_{i - 1}
$$ {#eq-6-14}

Where:

DRi	=	[DR](#kw-DR) value for the ith cell

Ri	=	current total radius for the i radii.

Ri-1	=	total radius for the i – 1 radii.

NX  (NR)	=	number of radial grid cells excluding the inner radius

OUTRAD	=	the outer radius of the radial grid, the value includes the inner radius.


For example, given an inner radius set to 0.25, an outer radius of 2,050 and the number of cells in the R direction set to ten, then @tbl-6-100 shows the grid size calculations.


| OUTRAD Radial Grid Example |  |  |  |
| --- | --- | --- | --- |
| [INRAD](#kw-INRAD) | 0.25 |  |  |
| OUTRAD | 2050.0 |  |  |
| NX | 10 |  |  |
| NX | Ri | [DR](#kw-DR) | Ratio |
| 0 | 0.250 | 0.250 |  |
| 1 | 0.616 | 0.366 | 1.463 |
| 2 | 1.516 | 0.900 | 2.463 |
| 3 | 3.733 | 2.217 | 2.463 |
| 4 | 9.193 | 5.460 | 2.463 |
| 5 | 22.638 | 13.445 | 2.463 |
| 6 | 55.748 | 33.109 | 2.463 |
| 7 | 137.281 | 81.533 | 2.463 |
| 8 | 338.058 | 200.777 | 2.463 |
| 9 | 832.477 | 494.420 | 2.463 |
| 10 | 2050.000 | 1217.523 | 2.463 |
| Total |  | 2050.000 |  |
: OUTRAD Radial Grid Example {#tbl-6-100}
See also the [DR](#kw-DR), [DRV](#kw-DRV), [DTHETA](#kw-DTHETA), [DTHETAV](#kw-DTHETAV) and [TOPS](#kw-TOPS) keywords to fully define a Radial or Spider Grid.


#### Example


```
--
--       INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION
--
INRAD
         0.25                                                                  /
--
--       OUTER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION
--
OUTRAD
         2050.0                                                                /

```

The above example defines the inner radius to be 0.25 and the outer radius to be 2,050 feet. Note that the outer radius includes the inner radius.