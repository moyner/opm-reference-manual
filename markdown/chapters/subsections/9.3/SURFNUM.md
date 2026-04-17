### SURFNUM – Define the Surfactant Miscible Saturation Table Region Numbers {#kw-SURFNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SURFNUM keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of oil-water relative permeability tables ([SWFN](#kw-SWFN), [SOF2](#kw-SOF2), [SOF3](#kw-SOF3), and [SWOF](#kw-SWOF)) are used to calculate the relative permeability and capillary pressure in a grid block.  In this case the SURFNUM allocated tables assume that oil and water are miscible, whereas the [SATNUM](#kw-SATNUM) allocated tables are used to allocate the immiscible saturation tables. To use this keyword the Surfactant option must have been activated by the [SURFACT](#kw-SURFACT) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | SURFNUM | SURFNUM defines an array of positive integers assigning a grid cell to a particular saturation table region. The maximum number of SURFNUM regions is set by the NTSFUN variable on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | 1 |
| Notes: |  |  |  |
: SURFNUM Keyword Description {#tbl-9-22}
#### Example

The example below sets three SURFNUM for the model.


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         SURFNUM     1            1*  1*   1*  1*   1*  1* / SET REGION 1
         SURFNUM     2            1*  1*   1*  1*   1   1  / SET REGION 2
         SURFNUM     3            1*  1*   1*  1*   2   2  / SET REGION 3
/
```