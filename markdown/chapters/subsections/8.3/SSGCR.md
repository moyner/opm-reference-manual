### SSGCR – End-Point Scaling Grid Cell Surfactant Critical Gas Saturations {#kw-SSGCR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SSGCR defines the surfactant critical gas saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#kw-ENDSCALE) keyword and the surfactant phase has been activated by the [SURFACT](#kw-SURFACT) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The critical gas saturation is defined as the maximum gas saturation for which the gas relative permeability is zero in a two-phase relative permeability table.  SSGCR is used to scale the surfactant oil relative permeability to gas data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SSGCR | SSGCR is an array of real numbers assigning the surfactant critical gas saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 30*0.03 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SSGCR Keyword Description {#tbl-8-173}
End-point scaling allows the entered surfactant relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SSWL](#kw-SSWL), [SSWCR](#kw-SSWCR), [SSWU](#kw-SSWU), [SSGL](#kw-SSGL), SSGCR, SSGU, [SSOWCR](#kw-SSOWCR), and [SSOGCR](#kw-SSOGCR) saturation grid arrays for the saturation end-points, and the SKRG, SKROG, SKROW and [SKRW](#kw-SKRW) relative permeability grid cell arrays for the relative permeability end-point data.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT SSGCR DATA FOR ALL CELLS
--       (FOR NX x NY x NZ = 300)
--
SSGCR
         300*0.050                                                              /

```

The above example defines a constant surfactant critical oil saturation with respect to gas of 0.05 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.