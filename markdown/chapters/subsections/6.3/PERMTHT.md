### PERMTHT – Define the Permeability for Each Cell in the THETA Direction {#kw-PERMTHT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PERMTHT sets the permeability for each cell in the THETA direction in a radial geometry grid. The [RADIAL](#kw-RADIAL) or [SPIDER](#kw-SPIDER) keyword in the [RUNSPEC](#kw-RUNSPEC) should be activated to indicate that radial or spider geometry is being used.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PERMTHT | PERMTHT is an array of real positive numbers assigning the permeability in the THETA direction to each cell in the model. This equivalent to [PERMY](#kw-PERMY) in a Cartesian grid. Repeat counts may be used, for example 20*100.0. | None |
| mD | mD | mD |  |
| Notes: |  |  |  |
: PERMTHT Keyword Description {#tbl-6-104}
Note that the [SPIDER](#kw-SPIDER) keyword activates OPM Flow’s radial grid geometry option for the model. This keyword will create a spiderweb-shaped grid based on a corner-point grid using the standard radial grid keywords: [INRAD](#kw-INRAD), [DRV](#kw-DRV), [DTHETAV](#kw-DTHETAV), [DZ](#kw-DZ)/[DZV](#kw-DZV) etc. in the [GRID](#kw-GRID) the section. A spider grid can be viewed in 3D in OPM ResInsight unlike radial grids that cannot be viewed in the software.  To overcome this, the simulator now converts radial grids to Irregular Corner-Point Grids and adjusts the model’s pore volume to reflect radial coordinates; thus, overcoming the display limitation.


See also the [PERMR](#kw-PERMR) and [PERMZ](#kw-PERMZ) keywords to fully define the permeability for a radial or spider grid model.


#### Example


```
--
--       DEFINE GRID BLOCK PERMTHT DATA FOR ALL CELLS (NX x NY x NZ = 300)
--
PERMTHT
         100*500.0   100*50.0   100*200.0                                       /

```

The above example defines the PERMTHT to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#kw-DIMENS) keyword (10, 10, 3) in the [RUNSPEC](#kw-RUNSPEC) section.