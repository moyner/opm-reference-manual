### SOCRS – End-Point Scaling Grid Cell Miscible Critical Oil Saturation with Respect to Water {#kw-SOCRS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SOCRS defines the miscible critical oil saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The critical oil saturation with respect to water is defined as the maximum oil saturation for which the oil relative permeability is zero in a two-phase oil-water relative permeability table.  The keyword is used with the Surfactant model to re-scale the surfactant relative permeability saturation tables allocated to a grid block by the by the [SURFNUM](#kw-SURFNUM) keyword in the [REGIONS](#kw-REGIONS) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SOCRS | SOCRS is an array of real numbers assigning the critical oil saturation with respect to water values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 30*0.30 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SOGCR Keyword Description {#tbl-8-164}
End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SWL](#kw-SWL), [SWCR](#kw-SWCR), [SWU](#kw-SWU), [SGL](#kw-SGL), [SGCR](#kw-SGCR), [SGU](#kw-SGU), SOCRS, and [SOGCR](#kw-SOGCR)  saturation grid arrays for the saturation end-points, and the [KRG](#kw-KRG), [KRORG](#kw-KRORG), [KRORW](#kw-KRORW) and [KRW](#kw-KRW) relative permeability grid cell arrays for the relative permeability end-point data.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT SOCRS DATA FOR ALL CELLS
--       (FOR NX x NY x NZ = 300)
--
SOCRS
         300*0.200                                                              /

```

The above example defines a constant critical oil saturation of 0.20 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.