### IKRGR – End-Point Scaling of Grid Cell Krgr(1-Sogcr) (Imbibition) {#kw-IKRGR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

IKRGR defines the imbibition scaling parameter at the relative permeability of gas at residual oil saturation (1 – [ISOGCR](#kw-ISOGCR)), or critical water saturation in a gas-water run (Swc), for all the cells in the model via an array.  The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. In addition, the HYSTER option on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section has to be activated to invoke the Hysteresis option. The SCALCERS keyword in the [PROPS](#kw-PROPS) section defines the options used in the re-scaling process, the options are two point scaling and three point scaling.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | IKRGR | IKRGR is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned imbibition scaling IKRGR values for each cell in the model.  In addition, for a given grid block IKGRGT should be less than [IKRG](#kw-IKRG). Repeat counts may be used, for example 50*0.400. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: IKRGR Keyword Description {#tbl-8-49}
```

```

When the IKRGR keyword is present in the input deck then the scaling matches the imbibition relative permeability at the critical saturation of the displacing phase (oil or water).

If three point scaling option has been selected via the [SCALECRS](#kw-SCALECRS) keyword in the [PROPS](#kw-PROPS) section the critical displacing phase is defined as:


| No | Phases Present | Critical Saturation |
| --- | --- | --- |
| 1 | Gas-Oil | S critical = 1.0 – [ISOGCR](#kw-ISOGCR) - [ISWL](#kw-ISWL) |
| 2 | Gas-Oil-Water | S critical = 1.0 – [ISOGCR](#kw-ISOGCR) - [ISWL](#kw-ISWL) |
| 3 | Gas-Water | S critical = 1.0 – [ISWCR](#kw-ISWCR) |
: Critical Displacement Relationships {#tbl-8-50}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [ISWL](#kw-ISWL), [ISWCR](#kw-ISWCR), [ISWU](#kw-ISWU), [ISGL](#kw-ISGL), [ISGCR](#kw-ISGCR), [ISGU](#kw-ISGU), [ISOWCR](#kw-ISOWCR), and [ISOGCR](#kw-ISOGCR)  saturation grid arrays for the saturation end-points, In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISWUX, ISWUY and ISWUZ instead of [ISWU](#kw-ISWU), There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISWUX, ISWUX-, ISWUY, ISWUY-, ISWUZ and ISWUZ-,  instead of the [ISWU](#kw-ISWU) keyword.

End-point scaling also allows the entered relative permeability functions to be scale on the relative permeability values using the [IKRG](#kw-IKRG), IKRGR, [IKRO](#kw-IKRO), [IKRORG](#kw-IKRORG), [IKRORW](#kw-IKRORW), [IKRW](#kw-IKRW) and [IKRWR](#kw-IKRWR) relative permeability grid cell arrays for the relative permeability end-point data.  In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is IKRGX, IKRGY and IKRGZ instead of [IKRG](#kw-IKRG), There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is IKRGX, IKRGX-, IKRGY, IKRGY-,I KRGZ and IKRGZ-,  instead of the [IKRG](#kw-IKRG) keyword.


#### Examples

The first example defines an input box for the whole grid and for layers one to three, for layer one IKRRG is set equal to 0.500, for layer two IKRGR equals 0.570, and for layer three IKRGR equals 0.580.


```
--
--       DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)
--
--       ---------- BOX ---------
--       I1  I2   J1  J2   K1  K2
BOX
         1*  1*   1*  1*   1   3                           / DEFINE BOX AREA
--
--       SET IKRGR VALUES FOR THREE LAYERS IN THE MODEL
--
IKRGR
         10000*0.500  10000*0.570  10000*0.580                /
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
         IKRGR’      0.5000       1*  1*   1*  1*    1   1  / IKRGR FOR LAYER 1
         IKRGR’      0.5700       1*  1*   1*  1*    2   2  / IKRGR FOR LAYER 2
         IKRGR’      0.5800       1*  1*   1*  1*    3   3  / IKRGR FOR LAYER 3
/
```