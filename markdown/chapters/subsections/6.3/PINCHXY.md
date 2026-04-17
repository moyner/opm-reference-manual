### PINCHXY – Define Pinch-Out Areal Options {#kw-PINCHXY}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PINCHXY keyword defines the x-direction and y-direction threshold thickness used to control the generation of Non-Neighbor Connections (“NNCs”) in the x- and y- directions for missing cells in the areal plane.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PINCHTHX | A real number defining the pinch-out threshold width for any cell in the x-direction.  NNCs are generated across inactive cells having a width less than PINCHTHX in the x-direction. | Defined |
| ft. 0.001 | m 0.001 | cm 0.001 |  |
| 2 | PINCHTHY | A real number defining the pinch-out threshold width for any cell in the y-direction.  NNCs are generated across inactive cells having a width less than PINCHTHY in the y-direction. | Defined |
| ft. 0.001 | m 0.001 | cm 0.001 |  |
| Notes: |  |  |  |
: PINCHXY Keyword Description {#tbl-6-111}
#### Example

The example below will create NNCs between the cells in the areal plane having cell widths less than 0.01 in either feet or metres in both the x- and y-directions.


```
--
--       SET PINCH-OUT PARAMETERS FOR AREAL PLANE
--
PINCHXY
--       X-DIRC      Y-DIRC
--       THRESHOLD   THRESHOLD
--
         0.01        0.01                                              /
```