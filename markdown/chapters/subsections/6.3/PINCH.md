### PINCH – Define Pinch-Out Layer Options


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [PINCH](#__RefHeading___Toc74261_2479612490) keyword defines the parameters used to control the generation of Non-Neighbor Connections (“NNCs”) in the vertical (K) direction due to layers pinching out. This keyword is applied to all layers in the model as opposed to the [PINCHREG](#__RefHeading___Toc74567_718313858) keyword that offers more flexibility by applying the pinch-out controls to various regions in the model defined by the [PINCHNUM](#__RefHeading___Toc74565_718313858) keyword.

OPM Flow will automatically generate connections between non neighbor cells in the vertical direction based on the parameters on this keyword.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PINCHTHK | A real number defining the pinch-out threshold thickness for any cell.  NNCs are generated across inactive cells having a vertical thickness less than PINCHTHK. | Defined |
| ft. 0.001 | m 0.001 | cm 0.001 |  |
| 2 | PINCHOPT | A character string controlling the generation of pinch-outs when the [MINPV](#__RefHeading___Toc569208_3181922006) keyword has been used to deactivate cells with small pore volumes. PINCHOPT can either be set to: | GAP |
| 3 | PINCHGAP | A real number defining the maximum “empty” thickness allowed between grid blocks in adjacent grid layers for a non-zero transmissibility to exist between them. | Defined |
| ft. 1.0E20 | m 1.0E20 | cm 1.0E20 |  |
| 4 | PINCHCAL | A character string controlling the calculation of the pinch-out transmissibilities.  PINCHCAL can either be set to: | TOPBOT |
| 5 | PINCHMUL | A character string controlling the calculation of the pinch-out transmissibilities when adjustments have been made by the [MULTZ](#__RefHeading___Toc80291_1778172979) keyword.  PINCHMUL can either be set to: Note if PINCHCAL has been set equal to [ALL](#__RefHeading___Toc4420_421927891) then PINCHMUL is reset to TOP, irrespective of the entered value for PINCHMUL. | TOP |
| Notes: |  |  |  |

*Table 6.108: PINCH Keyword Description*


#### Examples

The first example below will create NNCs between the cells above and below any cell having vertical thickness less than 0.01 in either feet or metres.


```
--
--       SET PINCH-OUT PARAMETERS FOR CALCULATING PINCH-OUT PROPERTIES
--
PINCH
--       THRESHOLD   GAP      EMPTY   TRANS    MULTZ
--       THICKNESS   NO GAP   GAP     CALC     CALC
         0.01        1*       1*      1*       1*                              /
```


For the second example, the [MINPV](#__RefHeading___Toc569208_3181922006) keyword is used to set the minimum pore volume to 500 m3  (metric units) and then the [PINCH](#__RefHeading___Toc74261_2479612490) keyword is invoked with PINCHGAP set equal to GAP, as follows:


```
--
--       MINIMUM PORE VOLUME FOR ACTIVE CELLS
--
MINPV
         500.0                                                                 /
--
--       SET PINCH-OUT CRITERIA FOR THE MODEL
--
PINCH
--       THRESHOLD   GAP      EMPTY   TRANS    MULTZ
--       THICKNESS   NO GAP   GAP     CALC     CALC
         0.1         GAP       1*     1*       1*                              /
```


In the above example the [MINPV](#__RefHeading___Toc569208_3181922006) keyword will deactivate all cells with pore volumes less than 500 m3. These deactivated cells are inactive in the model and therefore are not included in the flow calculations; however, by default they will result in no-flow barriers but may not be thin enough for [PINCH](#__RefHeading___Toc74261_2479612490) to create NNCs across them.  By setting PINCHGAP equal to GAP on the [PINCH](#__RefHeading___Toc74261_2479612490) keyword (the default setting), then OPM Flow generates NNCs across the cells that have been deactivated by the [MINPV](#__RefHeading___Toc569208_3181922006) keyword. However, in this case there may be grid blocks in the model with a pore volume greater than [MINPV](#__RefHeading___Toc569208_3181922006) but a thickness less than the pinch-out threshold. These cells will not be deactivated by the [PINCH](#__RefHeading___Toc74261_2479612490) keyword.
