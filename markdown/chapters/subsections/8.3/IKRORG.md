### IKRORG – End-Point Scaling of Grid Cell Kro(Sgcr) (Imbibition) {#kw-IKRORG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

IKRORG defines the scaling parameter for the imbibition relative permeability of oil at the critical gas saturation   ([ISGCR](#kw-ISGCR)), for all the cells in the model via an array.  The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword.  In addition, the HYSTER option on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section has to be activated to invoke the Hysteresis option. The SCALCERS keyword in the [PROPS](#kw-PROPS) section defines the options used in the re-scaling process, the options are two point scaling and three point scaling.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | IKRORG | IKRORG is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned imbibition scaling IKRORG values for each cell in the model. Repeat counts may be used, for example 50*0.850. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: IKRORG Keyword Description {#tbl-8-53}
When the IKRORG keyword is present in the input deck then the scaling matches the imbibition relative permeability at the critical saturation of the displacing phase.

If three point scaling option has been selected via the [SCALECRS](#kw-SCALECRS) keyword in the [PROPS](#kw-PROPS) section the critical displacing phase is defined as:


| No | Keywords Present | Critical Saturation |
| --- | --- | --- |
| 1 | [IKRORW](#kw-IKRORW) | S critical = 1.0 – [ISWCR](#kw-ISWCR) - [ISGL](#kw-ISGL) |
| 2 | IKRORG | S critical = 1.0 – [ISGCR](#kw-ISGCR) - [SWL](#kw-SWL) |
: Critical Displacement Relationships {#tbl-8-54}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [ISWL](#kw-ISWL), [ISWCR](#kw-ISWCR), [ISWU](#kw-ISWU), [ISGL](#kw-ISGL), [ISGCR](#kw-ISGCR), [ISGU](#kw-ISGU), [ISOWCR](#kw-ISOWCR), and [ISOGCR](#kw-ISOGCR)  saturation grid arrays for the saturation end-points, In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISWUX, ISWUY and ISWUZ instead of [ISWU](#kw-ISWU), There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISWUX, ISWUX-, ISWUY, ISWUY-, ISWUZ and ISWUZ-,  instead of the [ISWU](#kw-ISWU) keyword.

End-point scaling also allows the entered relative permeability functions to be scale on the relative permeability values using the [IKRG](#kw-IKRG), [IKRGR](#kw-IKRGR), [IKRO](#kw-IKRO), IKRORG, [IKRORW](#kw-IKRORW), [IKRW](#kw-IKRW) and [IKRWR](#kw-IKRWR) relative permeability grid cell arrays for the relative permeability end-point data.  In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is IKRGX, IKRGY and IKRGZ instead of [IKRG](#kw-IKRG), There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is IKRGX, IKRGX-, IKRGY, IKRGY-,I KRGZ and IKRGZ-,  instead of the [IKRG](#kw-IKRG) keyword.


#### Examples

The first example defines an input box for the whole grid and for layers one to three, for layer one IKRORG is set equal to 0.755, for layer two IKRORG equals 0.775, and for layer three IKRORG equals 0.800.


```
--
--       DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)
--
--       ---------- BOX ---------
--       I1  I2   J1  J2   K1  K2
BOX
         1*  1*   1*  1*   1   3                           / DEFINE BOX AREA
--
--       SET IKRORG VALUES FOR THREE LAYERS IN THE MODEL
--
IKRORG
         10000*0.755  10000*0.775  10000*0.800                /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX
```


The next example does exactly the same thing using the [EQUALS](#kw-EQUALS) keyword instead.


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         IKRORG      0.7550       1*  1*   1*  1*    1   1  / IKRORG FOR LAYER 1
         IKRORG      0.7750       1*  1*   1*  1*    2   2  / IKRORG FOR LAYER 2
         IKRORG      0.8000       1*  1*   1*  1*    3   3  / IKRORG FOR LAYER 3
/
```