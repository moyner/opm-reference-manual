### DR – Define the Size of Grid Blocks in the R Direction for All Cells {#kw-DR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

DR defines the size of all grid blocks in the R direction via an array for each cell in the model. The [RADIAL](#kw-RADIAL) or [SPIDER](#kw-SPIDER) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to indicate that radial or spider geometry is being used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | DR | DR is an array of real numbers describing the cell size in the R direction for each cell in the model in a radial grid. Repeat counts may be used, for example 10*100.0. | None |
| feet | m | cm |  |
| Notes: |  |  |  |
: DR Keyword Description {#tbl-6-22}
Note that the [SPIDER](#kw-SPIDER) keyword activates OPM Flow’s radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: [INRAD](#kw-INRAD), [DRV](#kw-DRV), [DTHETAV](#kw-DTHETAV), [DZ](#kw-DZ)/[DZV](#kw-DZV) etc. in the [GRID](#kw-GRID) the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software.  To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model’s pore volume to reflect radial coordinates; thus, overcoming the display limitation.

See also the [DRV](#kw-DRV), [DTHETAV](#kw-DTHETAV), [DZ](#kw-DZ) and [TOPS](#kw-TOPS) keywords in the [GRID](#kw-GRID) section to fully define a radial or spider grid model.


#### Example

Given the dimensions of the grid in the [RUNSPEC](#kw-RUNSPEC) section to be 10,1, 8 for NX, NY and NZ respectively, we first define the inner radius of the radial model,


```
--
--       INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION
--
INRAD
         0.25
/

```

and then DR should be defined as:


```
--
--       DEFINE GRID BLOCK R DIRECTION CELL SIZE
--
DR
	     1.75  2.32  5.01  10.84  23.39  50.55  109.21  235.92  509.68  1101.0
       1.75  2.32  5.01  10.84  23.39  50.55  109.21  235.92  509.68  1101.0
	     1.75  2.32  5.01  10.84  23.39  50.55  109.21  235.92  509.68  1101.0
	     1.75  2.32  5.01  10.84  23.39  50.55  109.21  235.92  509.68  1101.0
	     1.75  2.32  5.01  10.84  23.39  50.55  109.21  235.92  509.68  1101.0
	     1.75  2.32  5.01  10.84  23.39  50.55  109.21  235.92  509.68  1101.0
	     1.75  2.32  5.01  10.84  23.39  50.55  109.21  235.92  509.68  1101.0
	     1.75  2.32  5.01  10.84  23.39  50.55  109.21  235.92  509.68  1101.0
	/
```


The above example defines the size of the cells in the R direction based on 80 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


Note that since the first layer (K=1) must be defined and subsequent layers default to the layer above then:


```
--
--       INNER RADIUS OF FIRST GRID BLOCK IN THE RADIAL DIRECTION
--
INRAD
         0.25
/
--
--       DEFINE GRID BLOCK R DIRECTION CELL SIZE
--
DR
	     1.75  2.32  5.01  10.84  23.39  50.55  109.21  235.92  509.68  1101.0
	/
```


is equivalent to previous example.