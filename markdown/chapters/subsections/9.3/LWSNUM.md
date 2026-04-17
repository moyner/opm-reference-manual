### LWSNUM – Define the Low Salt Water Wet Saturation Table Region Numbers {#kw-LWSNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LWSNUM keyword defines the saturation tables (relative permeability and capillary pressure tables) region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which set of relative permeability tables ([SWFN](#kw-SWFN), [SOF3](#kw-SOF3) and related keywords) are used to calculate the relative permeability and capillary pressure in a grid block. The keyword should only be used if the Low Salinity option for the Brine model and the Surfactant Wettability option have been activated by the [LOWSALT](#kw-LOWSALT) and [SURFACTW](#kw-SURFACTW) keywords, respectively, in the [RUNSPEC](#kw-RUNSPEC) section.

The water wet curves are calculated as a weighted average of the low salinity saturation tables (allocated by this keyword) and the high salinity water wet saturation tables (allocated by the [HWSNUM](#kw-HWSNUM) keyword), using the weights provided by the [LSALTFNC](#kw-LSALTFNC) keyword in the [PROPS](#kw-PROPS) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | LWSNUM | LWSNUM defines an array of positive integers assigning a grid cell to a particular saturation table region. The maximum number of LWSNUM regions is set by the NTSFUN variable on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | 1 |
| Notes: |  |  |  |
: LWSNUM Keyword Description {#tbl-9-14}
The [HWSNUM](#kw-HWSNUM) allocated tables correspond to the immiscible high salinity water wet curves.


#### Example

The example below sets three LWSNUM regions for the model.


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         LWSNUM      1            1*  1*   1*  1*   1*  1* / SET REGION 1
         LWSNUM      2            1   2    1   2    1   1  / SET REGION 2
         LWSNUM      3            1   2    1   2    2   2  / SET REGION 3
/

```