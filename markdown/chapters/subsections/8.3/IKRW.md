### IKRW – End-Point Scaling of Grid Cell Krw(Sw =1.0) (Imbibition) {#kw-IKRW}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

IKRW defines the scaling parameter at the maximum imbibition water relative permeability value ([ISWU](#kw-ISWU)), that is for Sw = 1.0, for all the cells in the model via an array.  The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. In addition, the HYSTER option on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section has to be activated to invoke the Hysteresis option. The SCALCERS keyword in the [PROPS](#kw-PROPS) section defines the options used in the re-scaling process, the options are two point scaling and three point scaling.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | IKRW | IKRW is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned imbibition scaling IKRW values for each cell in the model. Repeat counts may be used, for example 50*1.000. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: IKRW Keyword Description {#tbl-8-57}
```

```

For the two point scaling option and for the [IKRWR](#kw-IKRWR) water relative permeability array NOT present in the input deck the krw value for a grid block is scaled by:


$$
{k}_{\mathit{rw}} = {k}_{{\mathit{rw}}_{ \mathit{TABLE}}}(\frac{\mathit{IKRW}}{{k}_{{\mathit{rw}}_{ \mathit{TABLE}-\mathit{MAX}}}})
$$ {#eq-8-58}

Where:

$\mathit{krw}$	=	the resulting IKRW value for a grid cell.

$\mathit{IKRW}$	= 	the scaling water relative permeability value from the IKRW array for a

given cell.

${k}_{{\mathit{rw}}_{ \mathit{TABLE}}}$	=	the water relative permeability from a grid block’s oil relative permeability

table at the grid blocks water saturation.

${k}_{{\mathit{rw}}_{ \mathit{TABLE}-\mathit{MAX}}}$	=	the maximum water relative permeability from a grid block’s water

relative table, that is at the maximum water saturation.


If the [IKRWR](#kw-IKRWR) keyword is present in the input deck then the scaling matches the imbibition relative permeability at the critical saturation of the displacing phase.

If three point scaling option has been selected via the [SCALECRS](#kw-SCALECRS) keyword in the [PROPS](#kw-PROPS) section the critical displacing phase is defined as:


| No | Phases Present | Critical Saturation |
| --- | --- | --- |
| 1 | Gas-Oil | S critical = 1.0 –  [ISOWCR](#kw-ISOWCR) - [ISGL](#kw-ISGL) |
| 2 | Gas-Oil-Water | S critical = 1.0 –  [ISOWCR](#kw-ISOWCR) - [ISGL](#kw-ISGL) |
| 3 | Gas-Water | S critical = 1.0 – [ISGCR](#kw-ISGCR) |
: Critical Displacement Relationships {#tbl-8-58}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [ISWL](#kw-ISWL), [ISWCR](#kw-ISWCR), [ISWU](#kw-ISWU), [ISGL](#kw-ISGL), [ISGCR](#kw-ISGCR), [ISGU](#kw-ISGU), [ISOWCR](#kw-ISOWCR), and [ISOGCR](#kw-ISOGCR)  saturation grid arrays for the saturation end-points, In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISWUX, ISWUY and ISWUZ instead of [ISWU](#kw-ISWU), There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISWUX, ISWUX-, ISWUY, ISWUY-, ISWUZ and ISWUZ-,  instead of the [ISWU](#kw-ISWU) keyword.

End-point scaling also allows the entered relative permeability functions to be scale on the relative permeability values using the [IKRG](#kw-IKRG), [IKRGR](#kw-IKRGR), [IKRO](#kw-IKRO), [IKRORG](#kw-IKRORG), [IKRORW](#kw-IKRORW), IKRW and [IKRWR](#kw-IKRWR) relative permeability grid cell arrays for the relative permeability end-point data.  In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is IKRGX, IKRGY and IKRGZ instead of [IKRG](#kw-IKRG), There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is IKRGX, IKRGX-, IKRGY, IKRGY-,I KRGZ and IKRGZ-,  instead of the [IKRG](#kw-IKRG) keyword.


#### Example

The example below defines an input box for the whole grid and for layers one to three, for layer one IKRW is set equal to 0.850, for layer two IKRW equals 0.875, and for layer three IKRW equals 0.900.


```
--
--       DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)
--
--       ---------- BOX ---------
--       I1  I2   J1  J2   K1  K2
BOX
         1*  1*   1*  1*   1   3                           / DEFINE BOX AREA
--
--       SET IKRW VALUES FOR THREE LAYERS IN THE MODEL
--
IKRW
         10000*0.850  10000*0.875  10000*0.900                /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX

```