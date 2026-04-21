### SGLPC – End-Point Scaling Grid Cell Capillary Pressure Connate Gas Saturations


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SGLPC defines the connate gas saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword in the RUNSPEC section. The connate gas saturation is defined as the minimum gas saturation in a two-phase gas relative permeability table.  The keyword only applies the scaling to the drainage capillary pressure tables, unlike the SGL keyword that applies the scaling to both the capillary pressure and relative permeability tables. The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SGLPC | SGLPC is an array of real numbers assigning the connate gas saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword. If SGLPC is omitted from the input deck the values will be defaulted to those on the SGL series of keywords. If the SGL series of keywords are missing from the input deck then the values are taken from the cell allocated capillary pressure table. Repeat counts may be used, for example 30*0.03 | Taken from SGL or from the cell allocated capillary pressure table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 8.150: SGLPC Keyword Description*


End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR, and SOGCR  saturation grid arrays for the saturation end-points, and the KRG, KRGR, KRO, KRORG, KRORW, KRW and KRWR relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SGLX, SGLY and SGLZ instead of SGL or SGLPC. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SGLX, SGLX-, SGLY, SGLY-, SGLZ and SGLZ-,  instead of the SGL or SGLPC keywords.


Missing Some Functionality - Use with Caution.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT SGLPC DATA FOR ALL CELLS
–-       (FOR NX x NY x NZ = 300)
--
SGLPC
         300*0.030                                                              /

```

The above example defines a constant connate gas saturation of 0.03 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
