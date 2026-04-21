### SURFNUM – Define the Surfactant Miscible Saturation Table Region Numbers


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SURFNUM keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of oil-water relative permeability tables (SWFN, SOF2, SOF3, and SWOF) are used to calculate the relative permeability and capillary pressure in a grid block.  In this case the SURFNUM allocated tables assume that oil and water are miscible, whereas the SATNUM allocated tables are used to allocate the immiscible saturation tables. To use this keyword the Surfactant option must have been activated by the SURFACT keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | SURFNUM | SURFNUM defines an array of positive integers assigning a grid cell to a particular saturation table region. The maximum number of SURFNUM regions is set by the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section. | 1 |
| Notes: |  |  |  |

*Table 9.22: SURFNUM Keyword Description*


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
