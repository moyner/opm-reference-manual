### ISOGCR – End-Point Scaling of Grid Cell Critical Oil Saturation to Gas (Imbibition) {#kw-ISOGCR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

ISOGCR defines the imbibition critical oil saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#kw-ENDSCALE) in the [RUNSPEC](#kw-RUNSPEC) section and the hysteresis model option has been activated on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The critical oil saturation with respect to gas is defined as the maximum oil saturation for which the oil relative permeability is zero in a two-phase gas-oil relative permeability table.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | ISOGCR | ISOGCR is an array of real numbers assigning the critical oil saturation with respect to gas values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 30*0.30 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: ISOGCR Keyword Description {#tbl-8-67}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [ISWL](#kw-ISWL), [ISWCR](#kw-ISWCR), [ISWU](#kw-ISWU), [ISGL](#kw-ISGL), [ISGCR](#kw-ISGCR), [ISGU](#kw-ISGU), [ISOWCR](#kw-ISOWCR), and ISOGCR  saturation grid arrays for the saturation end-points, and the [IKRG](#kw-IKRG), [IKRORG](#kw-IKRORG), [IKRORW](#kw-IKRORW) and [IKRW](#kw-IKRW)> relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISOGCRX, ISOGCRY and ISOGCRZ instead of ISOGCR. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the  non-reversible versions of the aforementioned arrays should be used, that is ISOGCRX, ISOGCRX-, ISOGCRY, ISOGCRY-,  ISOGCRZ and ISOGCRZ-,  instead of the ISOGCR keyword.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT ISOGCR DATA FOR ALL CELLS
--       (NX x NY x NZ = 300)
--
ISOGCR
         300*0.200                                                              /

```

The above example defines a constant critical gas saturation of 0.20 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.