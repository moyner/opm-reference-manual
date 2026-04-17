### ISWCR – End-Point Scaling of Grid Cell Critical Water Saturation (Imbibition) {#kw-ISWCR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

ISWCR defines the imbibition critical water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#kw-ENDSCALE) in the [RUNSPEC](#kw-RUNSPEC) section and the hysteresis model option has been activated on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The critical water saturation is defined as the maximum water saturation for which the water relative permeability is zero in a two-phase relative permeability table.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | ISWCR | ISWCR is an array of real numbers assigning the critical water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 30*0.20 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: ISWCR Keyword Description {#tbl-8-69}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [ISWL](#kw-ISWL), ISWCR, [ISWU](#kw-ISWU), [ISGL](#kw-ISGL), [ISGCR](#kw-ISGCR), [ISGU](#kw-ISGU), [ISOWCR](#kw-ISOWCR), and [ISOGCR](#kw-ISOGCR)  saturation grid arrays for the saturation end-points, and the [IKRG](#kw-IKRG), [IKRORG](#kw-IKRORG), [IKRORW](#kw-IKRORW) and [IKRW](#kw-IKRW) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISWCRX, ISWCRY and ISWCRZ instead of ISWCR. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the  non-reversible versions of the aforementioned arrays should be used, that is ISWCRX, ISWCRX-, ISWCRY, ISWCRY-,  ISWCRZ and ISWCRZ-,  instead of the ISWCR keyword.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT ISWCR DATA FOR ALL CELLS
--       (NX x NY x NZ = 300)
--
ISWCR
  300*0.200                                                                     /

```

The above example defines a constant critical water saturation of 0.20 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.