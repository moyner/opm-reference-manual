### KRWR – End-Point Scaling of Grid Cell KRWR(Sowcr) (Drainage) {#kw-KRWR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

KRWR defines the scaling parameter at the drainage critical oil to water saturation value ([SOWCR](#kw-SOWCR)), for the drainage water relative permeability curve, for all the cells in the model via an array.  The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. The SCALCERS keyword in the [PROPS](#kw-PROPS) section defines the options used in the re-scaling process, the options are two point scaling and three point scaling.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | KRWR | KRWR is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling KRWR values for each cell in the model. Repeat counts may be used, for example 50*1.000. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: KRWR Keyword Description {#tbl-8-85}
```

```

When the KRWR keyword is present in the input deck then the scaling matches the relative permeability at the critical saturation of the displacing phase.

If three point scaling option has been selected via the [SCALECRS](#kw-SCALECRS) keyword in the [PROPS](#kw-PROPS) section the critical displacing phase is defined as:


| No | Phases Present | Critical Saturation |
| --- | --- | --- |
| 1 | Gas-Oil | S critical = 1.0 –  [SOWCR](#kw-SOWCR) - [SGL](#kw-SGL) |
| 2 | Gas-Oil-Water | S critical = 1.0 –  [SOWCR](#kw-SOWCR) - [SGL](#kw-SGL) |
| 3 | Gas-Water | S critical = 1.0 – [SGCR](#kw-SGCR) |
: Critical Displacement Relationships {#tbl-8-86}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SWL](#kw-SWL), [SWCR](#kw-SWCR), [SWU](#kw-SWU), [SGL](#kw-SGL), [SGCR](#kw-SGCR), [SGU](#kw-SGU), [SOWCR](#kw-SOWCR), and [SOGCR](#kw-SOGCR)  saturation grid arrays for the saturation end-points, In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SWUX, SWUY and SWUZ instead of [SWU](#kw-SWU), There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SWUX, SWUX-, SWUY, SWUY-, SWUZ and SWUZ-,  instead of the [SWU](#kw-SWU) keyword.

End-point scaling also allows the entered relative permeability functions to be scale on the relative permeability values using the [KRG](#kw-KRG), [KRGR](#kw-KRGR), KRWR, [KRORG](#kw-KRORG), [KRORW](#kw-KRORW), KRWR and KRWRR relative permeability grid cell arrays for the relative permeability end-point data.  In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is KRWRX, KRWRY and KRWRZ instead of KRWR, There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is KRWRX, KRWRX-, KRWRY, KRWRY-, KRWRZ and KRWRZ-,  instead of the KRWR keyword.

If the hysteresis model option has been activated on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the equivalent imbibition arrays suffixed with the letter I, for example [IKRWR](#kw-IKRWR), can be used to define the KRWR for the relative permeability imbibition tables.


#### Examples

The first example defines an input box for the whole grid and for layers one to three, for layer one KRWR is set equal to 0.755, for layer two KRWR equals 0.775, and for layer three KRWR equals 0.800.


```
--
--       DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)
--
--       ---------- BOX ---------
--       I1  I2   J1  J2   K1  K2
BOX
         1*  1*   1*  1*   1   3                           / DEFINE BOX AREA
--
--       SET KRWR VALUES FOR THREE LAYERS IN THE MODEL
--
KRWR
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
         KRWR        0.7550       1*  1*   1*  1*    1   1  / KRWR FOR LAYER 1
         KRWR        0.7750       1*  1*   1*  1*    2   2  / KRWR FOR LAYER 2
         KRWR        0.8000       1*  1*   1*  1*    3   3  / KRWR FOR LAYER 3
/
```