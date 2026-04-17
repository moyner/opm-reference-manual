### SOGCR – End-Point Scaling Grid Cell Critical Oil Saturation with Respect to Gas {#kw-SOGCR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SOGCR defines the critical oil saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The critical oil saturation with respect to gas is defined as the maximum oil saturation for which the oil relative permeability is zero in a two-phase gas-oil relative permeability table.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SOGCR | SOGCR is an array of real numbers assigning the critical oil saturation with respect to gas values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 30*0.30 dimensionless | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SOGCR Keyword Description {#tbl-8-167}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SWL](#kw-SWL), [SWCR](#kw-SWCR), [SWU](#kw-SWU), [SGL](#kw-SGL), [SGCR](#kw-SGCR), [SGU](#kw-SGU), [SOWCR](#kw-SOWCR), and SOGCR  saturation grid arrays for the saturation end-points, and the [KRG](#kw-KRG), [KRGR](#kw-KRGR), [KRO](#kw-KRO), [KRORG](#kw-KRORG), [KRORW](#kw-KRORW), [KRW](#kw-KRW) and [KRWR](#kw-KRWR) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SOGCRX, SOGCRY and SOGCRZ instead of SOGCR. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the  non-reversible versions of the aforementioned arrays should be used, that is SOGCRX, SOGCRX-, SOGCRY, SOGCRY-,  SOGCRZ and SOGCRZ-,  instead of the SOGCR keyword.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT SOGCR DATA FOR ALL CELLS
--       (FOR NX x NY x NZ = 300)
--
SOGCR
         300*0.200                                                              /

```

The above example defines a constant critical gas saturation of 0.20 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.