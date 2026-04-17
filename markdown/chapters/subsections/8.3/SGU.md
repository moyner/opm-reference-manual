### SGU – End-Point Scaling Grid Cell Gas Saturation {#kw-SGU}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SGU defines the maximum gas saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The maximum gas saturation is defined as the maximum gas saturation in a two-phase gas relative permeability table.

The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SGU | SGU is an array of real numbers assigning the maximum gas saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 30*0.70 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SGU Keyword Description {#tbl-8-153}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SWL](#kw-SWL), [SWCR](#kw-SWCR), [SWU](#kw-SWU), [SGL](#kw-SGL), [SGCR](#kw-SGCR), SGU, [SOWCR](#kw-SOWCR), and [SOGCR](#kw-SOGCR)  saturation grid arrays for the saturation end-points, and the [KRG](#kw-KRG), [KRORG](#kw-KRORG), [KRORW](#kw-KRORW) and [KRW](#kw-KRW) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SGUX, SGUY and SGUZ instead of SGU. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SGUX, SGUX-, SGUY, SGUY-, SGUZ and SGUZ-,  instead of the SGU keyword.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT SGU DATA FOR ALL CELLS
--       (FOR NX x NY x NZ = 300)
--
SGU
         300*0.700                                                         /

```

The above example defines a constant connate gas saturation of 0.70 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.