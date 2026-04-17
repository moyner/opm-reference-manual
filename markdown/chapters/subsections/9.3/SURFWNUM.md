### SURFWNUM – Define the Saturation Table Region Numbers (High Salinity and Water Wet) {#kw-SURFWNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SURFWNUM keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the mode, for when the Surfactant Wettability option has been selected. The keyword may also be used with the Low Salt Brine option, in this case the water wet curves are calculated as a function of the low and high water wet salinity curves. The region number specifies which set of relative permeability tables are used to calculate the relative permeability and capillary pressure in a grid block. Note that the keyword is obligatory if the [SURFACTW](#kw-SURFACTW) keyword in the [RUNSPEC](#kw-RUNSPEC) section has been used to invoke the Surfactant Wettability option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | SURFWNUM | SURFWNUM defines an array of positive integers assigning a grid cell to a particular saturation table region. The maximum number of SURFWNUM regions is set by the NTSFUN variable on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | 1 |
| Notes: |  |  |  |
: SURFWNUM Keyword Description {#tbl-9-23}
#### Example

The example below sets three SURFWNUM regions for the model.


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         SURFWNUM    1            1*  1*   1*  1*   1*  1* / SET REGION 1
         SURFWNUM    2            1   2    1   2    1   1  / SET REGION 2
         SURFWNUM    3            1   2    1   2    2   2  / SET REGION 3
/
```