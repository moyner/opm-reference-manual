### SWLPC – End-Point Scaling Grid Cell Capillary Pressure Connate Water Saturations


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SWLPC defines the connate water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword in the RUNSPEC section. The connate water saturation is defined as the minimum water saturation in a two-phase water relative permeability table.  The keyword only applies the scaling to the drainage capillary pressures tables, unlike the SWL keyword that applies the scaling to both the capillary pressure and relative permeability tables. The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SWLPC | SWLPC is an array of real numbers assigning the connate water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword. If SWLPC is omitted from the input deck the values will be defaulted to those on the SWL series of keywords. If the SWL series of keywords are missing from the input deck then the values are taken from the cell allocated capillary pressure table. Repeat counts may be used, for example 30*0.03 | Taken from SGL or from the cell allocated capillary pressure table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 8.188: SWLPC Keyword Description*


End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR, and SOGCR  saturation grid arrays for the saturation end-points, and the KRG, KROG, KROW and KRW relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SWLX, SWLY and SWLZ instead of SWL or SWLPC. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SWLX, SWLX-, SWLY, SWLY-, SWLZ and SWLZ-,  instead of the SWL or SWLPC keywords.


Missing Some Functionality - Use with Caution.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT SWLPC DATA FOR ALL CELLS
--       (FOR NX x NY x NZ = 300)
--
SWLPC
         300*0.150                                                              /

```

The above example defines a constant connate water saturation of 0.15 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
