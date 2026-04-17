### PINCHREG – Define Pinch-Out Region Options {#kw-PINCHREG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PINCHREG keyword defines the parameters used to control the generation of Non-Neighbor Connections (“NNCs”) in the vertical (K) direction due to layers pinching out in combination with the [PINCHNUM](#kw-PINCHNUM) keyword. This allows different regions in the model to use different criteria in controlling the how pinch-outs are generated.  The keyword should contain NRPINC records defining the criteria for each pinch-out region defined with the [PINCHNUM](#kw-PINCHNUM) keyword.  NRPINC is the maximum number of [PINCHNUM](#kw-PINCHNUM) regions defined via the [GRIDOPTS](#kw-GRIDOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

An alternative method to set the pinch-out criteria is to use the [PINCH](#kw-PINCH) keyword, that applies the criteria to the whole model.

OPM Flow will automatically generate connections between non neighbor cells in the vertical direction based on the parameters on this keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PINCHTHK | A real number defining the pinch-out threshold thickness for any cell.  NNCs are generated across inactive cells having a vertical thickness less than PINCHTHK. | Defined |
| ft. 0.001 | m 0.001 | cm 0.001 |  |
| 2 | PINCHOPT | A character string controlling the generation of pinch-outs when the [MINPV](#kw-MINPV) keyword has been used to deactivate cells with small pore volumes. PINCHOPT can either be set to: | GAP |
| 3 | PINCHGAP | A real number defining the maximum “empty” thickness allowed between grid blocks in adjacent grid layers for a non-zero transmissibility to exist between them. | Defined |
| ft. 1.0E20 | m 1.0E20 | cm 1.0E20 |  |
| 4 | PINCHCAL | A character string controlling the calculation of the pinch-out transmissibilities.  PINCHCAL can either be set to: | TOPBOT |
| 5 | PINCHMUL | A character string controlling the calculation of the pinch-out transmissibilities when adjustments have been made by the [MULTZ](#kw-MULTZ) keyword.  PINCHMUL can either be set to: Note if PINCHCAL has been set equal to [ALL](#kw-ALL) then PINCHMUL is reset to TOP, irrespective of the entered value for PINCHMUL. | TOP |
| Notes: |  |  |  |
: PINCHREG Keyword Description {#tbl-6-110}
#### Example


```
--
--       SET PINCH-OUT CRITERA VIA THE PINCHNUM REGION
--
PINCHREG
--       THRESHOLD   GAP      EMPTY   TRANS
--       THICKNESS   NO GAP   GAP     CALC
         0.1         1*       1*      1*                  / PINCHNUM 01
         1.0         1*       10      1*                  / PINCHNUM 02
         1.0         NOGAP    20      1*                  / PINCHNUM 03
```


The above example sets the default pinch-out criteria for grid blocks defined as region one via the [PINCHNUM](#kw-PINCHNUM) array and different values for regions two and three.