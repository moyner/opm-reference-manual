### FIPNUM – Define the Fluid In-Place Region Numbers


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [FIPNUM](#__RefHeading___Toc77229_2752266063) keyword defines the fluid in-place region numbers for each grid block. The simulator can print out summaries of the fluid in-place in each region, the current flow rates between regions, and the cumulative flows between regions.

Note that the total number of [FIPNUM](#__RefHeading___Toc77229_2752266063) and [FIP](#__RefHeading___Toc250560_252421755) regions must be defined by the NMFIPR variable on the [REGDIMS](#__RefHeading___Toc70161_327352552) keyword, or the NTFIP variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword. Both keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [FIPNUM](#__RefHeading___Toc77229_2752266063) | [FIPNUM](#__RefHeading___Toc77229_2752266063) defines an array of positive integers greater than or equal to one, that assigns a grid cell to a particular fluid in-place region. The maximum number of [FIPNUM](#__RefHeading___Toc77229_2752266063) and [FIP](#__RefHeading___Toc250560_252421755) regions is set by the [REGDIMS](#__RefHeading___Toc70161_327352552)(NMFIPR) or the [TABDIMS](#__RefHeading___Toc89327_327352552)(NTFIP) keywords(variables) in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. If both [REGDIMS](#__RefHeading___Toc70161_327352552)(NMFIPR) and [TABDIMS](#__RefHeading___Toc89327_327352552)(NTFIP) have been defined then the maximum of the two is used. | 1 |
| Notes: |  |  |  |

*Table 9.5: FIPNUM Keyword Description*


| Note In most simulation models the [FIPNUM](#__RefHeading___Toc77229_2752266063) array is used to define various regions in the model for fluid in-place reporting and to identify (or report) the flow between the different regions. When calibrating a model’s in-place volumes it would be useful to use the [FIPNUM](#__RefHeading___Toc77229_2752266063) array combined with the [MULTREGP](#__RefHeading___Toc296617_1576177388) keyword to accomplish this. However, the [FIPNUM](#__RefHeading___Toc77229_2752266063) array cannot be used in the [GRID](#__RefHeading___Toc38674_784232322) section. A work around is to: The above work flow will ensure that both arrays and the reporting of fluid in-place regions are consistent. |
| --- |


#### Examples

The example below sets three [FIPNUM](#__RefHeading___Toc77229_2752266063) regions for a 4 x 5 x 2 model.


```
--
--       DEFINE FIPNUM REGIONS FOR ALL CELLS
--
FIPNUM
         2  2  1  1  2  2  1  1  1  1  1  1  1  1  1  1  1  1  1  1
         3  3  1  1  3  3  1  1  1  1  1  1  1  1  1  1  1  1  1  1
/
```


Alternatively the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword could be employed to accomplish the same task, that is:


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         FIPNUM     1            1*  1*   1*  1*    1*  1* / SET REGION 1
         FIPNUM     2            1   2    1   2     1   1  / SET REGION 2
         FIPNUM     3            1   2    1   2     2   2  / SET REGION 3
/


```
