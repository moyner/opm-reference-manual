### ISGCR – End-Point Scaling of Grid Cell Critical Gas Saturation  (Imbibition) {#kw-ISGCR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

ISGCR defines the imbibition critical gas saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the hysteresis model option has been activated on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The critical gas saturation is defined as the maximum gas saturation for which the gas relative permeability is zero in a two-phase relative permeability table.

The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | ISGCR | ISGCR is an array of real numbers assigning the critical gas saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 30*0.03 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: ISGCR Keyword Description {#tbl-8-63}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [ISWL](#kw-ISWL), [ISWCR](#kw-ISWCR), [ISWU](#kw-ISWU), [ISGL](#kw-ISGL), ISGCR, [ISGU](#kw-ISGU), [ISOWCR](#kw-ISOWCR), and [ISOGCR](#kw-ISOGCR)  saturation grid arrays for the saturation end-points, and the [IKRG](#kw-IKRG), [IKRORG](#kw-IKRORG), [IKRORW](#kw-IKRORW) and [IKRW](#kw-IKRW) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISGCRX, ISGCRY and ISGCRZ instead of ISGCR. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the  non-reversible versions of the aforementioned arrays should be used, that is ISGCRX, ISGCRX-, ISGCRY, ISGCRY-,  ISGCRZ and ISGCRZ-,  instead of the ISGCR keyword.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT ISGCR DATA FOR CELLS (NX x NY x NZ = 300)
ISGCR
         300*0.050                                                             /

```

The above example defines a constant critical gas saturation of 0.05 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.