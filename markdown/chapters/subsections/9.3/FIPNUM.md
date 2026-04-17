### FIPNUM – Define the Fluid In-Place Region Numbers


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FIPNUM keyword defines the fluid in-place region numbers for each grid block. The simulator can print out summaries of the fluid in-place in each region, the current flow rates between regions, and the cumulative flows between regions.

Note that the total number of FIPNUM and FIP regions must be defined by the NMFIPR variable on the REGDIMS keyword, or the NTFIP variable on the TABDIMS keyword. Both keywords are in the RUNSPEC section.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FIPNUM | FIPNUM defines an array of positive integers greater than or equal to one, that assigns a grid cell to a particular fluid in-place region. The maximum number of FIPNUM and FIP regions is set by the REGDIMS(NMFIPR) or the TABDIMS(NTFIP) keywords(variables) in the RUNSPEC section. If both REGDIMS(NMFIPR) and TABDIMS(NTFIP) have been defined then the maximum of the two is used. | 1 |
| Notes: |  |  |  |

*Table 9.5: FIPNUM Keyword Description*


::: {.callout-note}
In most simulation models the FIPNUM array is used to define various regions in the model for fluid in-place reporting and to identify (or report) the flow between the different regions. When calibrating a model’s in-place volumes it would be useful to use the FIPNUM array combined with the MULTREGP keyword to accomplish this. However, the FIPNUM array cannot be used in the GRID section. A work around is to: The above work flow will ensure that both arrays and the reporting of fluid in-place regions are consistent.
:::


#### Examples

The example below sets three FIPNUM regions for a 4 x 5 x 2 model.


```
--
--       DEFINE FIPNUM REGIONS FOR ALL CELLS
--
FIPNUM
         2  2  1  1  2  2  1  1  1  1  1  1  1  1  1  1  1  1  1  1
         3  3  1  1  3  3  1  1  1  1  1  1  1  1  1  1  1  1  1  1
/
```


Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:


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
