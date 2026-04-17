### ISGU – End-Point Scaling of Grid Cell Maximum Gas Saturation  (Imbibition) {#kw-ISGU}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

ISGU defines the imbibition maximum gas saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the hysteresis model option has been activated on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The maximum gas saturation is defined as the maximum gas saturation in a two-phase gas relative permeability table.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | ISGU | ISGU is an array of real numbers assigning the maximum gas saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 30*0.70 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: ISGU Keyword Description {#tbl-8-66}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [ISWL](#kw-ISWL), [ISWCR](#kw-ISWCR), [ISWU](#kw-ISWU), [ISGL](#kw-ISGL), [ISGCR](#kw-ISGCR), ISGU, [ISOWCR](#kw-ISOWCR), and [ISOGCR](#kw-ISOGCR)  saturation grid arrays for the saturation end-points, and the [IKRG](#kw-IKRG), [IKRORG](#kw-IKRORG), [IKRORW](#kw-IKRORW) and [IKRW](#kw-IKRW) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISGUX, ISGUY and ISGUZ instead of ISGU. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISGUX, ISGUX-, ISGUY, ISGUY-, ISGUZ and ISGUZ-,  instead of the ISGU keyword.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT ISGU DATA FOR ALL CELLS (NX x NY x NZ = 300)
ISGU
         300*0.700                                                             /

```

The above example defines a constant connate gas saturation of 0.70 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.