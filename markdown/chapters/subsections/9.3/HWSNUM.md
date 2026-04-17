### HWSNUM – Define the Saturation Table Region Numbers (High Salinity and Water Wet) {#kw-HWSNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HWSNUM keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the mode, for when the Surfactant Wettability option has been selected. The keyword may also be used with the Low Salt Brine option, in this case the water wet curves are calculated as a function of the low and high water wet salinity curves. The region number specifies which set of relative permeability tables are used to calculate the relative permeability and capillary pressure in a grid block.  Note that the keyword is obligatory if the [SURFACTW](#kw-SURFACTW) keyword in the [RUNSPEC](#kw-RUNSPEC) section has been used to invoke the Surfactant Wettability option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | HWSNUM | HWSNUM defines an array of positive integers assigning a grid cell to a particular saturation table region. The maximum number of HWSNUM regions is set by the NTSFUN variable on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | 1 |
| Notes: |  |  |  |
: HWSNUM Keyword Description {#tbl-9-8}
#### Examples

The example below sets three HWSNUM regions for a 4 x 5 x 2 model.


```
--
--       DEFINE HWSNUM REGIONS FOR ALL CELLS
--
HWSNUM
         2  2  1  1  2  2  1  1  1  1  1  1  1  1  1  1  1  1  1  1
         3  3  1  1  3  3  1  1  1  1  1  1  1  1  1  1  1  1  1  1
/
```

Alternatively the [EQUALS](#kw-EQUALS) keyword could be employed to accomplish the same task, that is:


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         HWSNUM      1            1*  1*   1*  1*   1*  1* / SET REGION 1
         HWSNUM      2            1   2    1   2    1   1  / SET REGION 2
         HWSNUM      3            1   2    1   2    2   2  / SET REGION 3
/
```