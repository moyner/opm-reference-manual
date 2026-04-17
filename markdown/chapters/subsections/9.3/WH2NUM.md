### WH2NUM – Define WAG Hysteresis Saturation Table Region Numbers (Two Phase) {#kw-WH2NUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WH2NUM keyword defines the two phase Water-Alternating-Gas (“WAG”) hysteresis tables (relative permeability and capillary pressure tables) region numbers for each grid block, for when the hysteresis option has been activated by the [WAGHYSTR](#kw-WAGHYSTR) variable on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The region number specifies which set of relative permeability tables ([SGFN](#kw-SGFN), [SWFN](#kw-SWFN), [SOF2](#kw-SOF2), [SOF3](#kw-SOF3), [SOF32D](#kw-SOF32D), [SGOF](#kw-SGOF), [SLGOF](#kw-SLGOF) and [SWOF](#kw-SWOF)) are used to calculate the relative permeability and capillary pressure in a grid block. Note that this keyword if the two phase water relative permeabilities WAG option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | WH2NUM | WH2NUM defines an array of positive integers assigning a grid cell to a particular saturation table region. The maximum number of WH2NUM regions is set by the NTSFUN variable on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | Taken from cell allocated [SATNUM](#kw-SATNUM) |
| Notes: |  |  |  |
: WH2NUM Keyword Description {#tbl-9-28}
#### Example

The example below sets three WH2NUM regions for a model.


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         WH2NUM      1            1*  1*   1*  1*   1*  1* / SET REGION 1
         WH2NUM      2            1   2    1   2    1   1  / SET REGION 2
         WH2NUM      3            1   2    1   2    2   2  / SET REGION 3
/

```