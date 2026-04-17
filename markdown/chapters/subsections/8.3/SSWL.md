### SSWL – End-Point Scaling Grid Cell Surfactant Connate Water Saturation {#kw-SSWL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SSWL defines the surfactant connate water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the [ENDSCALE](#kw-ENDSCALE) keyword and the surfactant phase has been activated by the [SURFACT](#kw-SURFACT) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The connate water saturation is defined as the minimum water saturation in a two-phase water relative permeability table.  SSWL scales the surfactant oil relative permeability to water and gas data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SSWL | SSWL is an array of real numbers assigning the connate water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 30*0.15 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SSWL Keyword Description {#tbl-8-178}
End-point scaling allows the entered surfactant relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SSWL, [SSWCR](#kw-SSWCR), [SSWU](#kw-SSWU), [SSGL](#kw-SSGL), [SSGCR](#kw-SSGCR), SSGU, [SSOWCR](#kw-SSOWCR), and [SSOGCR](#kw-SSOGCR) saturation grid arrays for the saturation end-points, and the SKRG, SKROG, SKROW and [SKRW](#kw-SKRW) relative permeability grid cell arrays for the relative permeability end-point data.


#### Example


```
--
--       DEFINE GRID BLOCK END-POINT SSWL DATA FOR ALL CELLS
--       (FOR NX x NY x NZ = 300)
--
SSWL
         300*0.150                                                              /

```

The above example defines a constant surfactant connate water saturation of 0.15 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.