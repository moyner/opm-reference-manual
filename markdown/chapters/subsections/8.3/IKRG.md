### IKRG – End-Point Scaling of Grid Cell Krg(Sgu) (Imbibition)


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

IKRG defines the imbibition scaling parameter at the maximum gas relative permeability value (ISGU), normally ISGU is equal to 1.0 -  Swc, for all the cells in the model via an array.  The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword.  In addition, the HYSTER option on the SATOPTS keyword in the RUNSPEC section has to be activated to invoke the Hysteresis option. The SCALCERS keyword in the PROPS section defines the options used in the re-scaling process, the options are two point scaling and three point scaling.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | IKRG | IKRG is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling IKRG imbibition values for each cell in the model. Repeat counts may be used, for example 50*0.400. dimensionless | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 8.47: IKRG Keyword Description*


```

```

For the two point scaling option and for the IKRGR gas relative permeability array NOT present in the input deck the krg value for a grid block is scaled by:


| ${k}_{\mathit{rg}} = {k}_{{\mathit{rg}}_{ \mathit{TABLE}}}\left(\frac{\mathit{IKRG}}{{k}_{{\mathit{rg}}_{ \mathit{TABLE}-\mathit{MAX}}}}\right)$ | (8.56) |
| --- | --- |

Where:

krg	=	the resulting krg value for a grid cell.

IKRG	=	the scaling gas relative permeability value from the IKRG array for a given

cell.

${k}_{{\mathit{rg}}_{ \mathit{TABLE}}}$	= 	the gas relative permeability from a grid block’s gas-oil table at the grid

blocks gas saturation.

${k}_{{\mathit{rg}}_{ \mathit{TABLE}-\mathit{MAX}}}$	= 	the maximum gas relative permeability from a grid block’s gas-oil table, that

is at the connate water saturation (Swc).


If the IKRGR keyword is present in the input deck then the scaling matches the imbibition relative permeability at the critical saturation of the displacing phase.

If three point scaling option has been selected via the SCALECRS keyword in the PROPS section the critical displacing phase is defined as:


| No | Phases Present | Critical Saturation |
| --- | --- | --- |
| 1 | Gas-Oil | S critical = 1.0 – ISOGCR - ISWL |
| 2 | Gas-Oil-Water | S critical = 1.0 – ISOGCR - ISWL |
| 3 | Gas-Water | S critical = 1.0 –  ISWCR |

*Table 8.48: Critical Displacement Relationships*


End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the ISWL, ISWCR, ISWU, ISGL, ISGCR, ISGU, ISOWCR, and ISOGCR  saturation grid arrays for the saturation end-points, In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISWUX, ISWUY and ISWUZ instead of ISWU, There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISWUX, ISWUX-, ISWUY, ISWUY-, ISWUZ and ISWUZ-,  instead of the ISWU keyword.

End-point scaling also allows the entered relative permeability functions to be scale on the relative permeability values using the IKRG, IKRGR, IKRO, IKRORG, IKRORW, IKRW and IKRWR relative permeability grid cell arrays for the relative permeability end-point data.  In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is IKRGX, IKRGY and IKRGZ instead of IKRG, There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is IKRGX, IKRGX-, IKRGY, IKRGY-,I KRGZ and IKRGZ-,  instead of the IKRG keyword.


#### Example

The example below defines an input box for the whole grid and for layers one to three, for layer one IKRG is set equal to 0.550, for layer two IKRG equals 0.575, and for layer three IKRG equals 0.600.


```
--
--       DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)
--
--       ---------- BOX ---------
--       I1  I2   J1  J2   K1  K2
BOX
         1*  1*   1*  1*   1   3                           / DEFINE BOX AREA
--
--       SET IKRG VALUES FOR THREE LAYERS IN THE MODEL
--
IKRG
         1000*0.550  1000*0.575  1000*0.600                /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX

```
