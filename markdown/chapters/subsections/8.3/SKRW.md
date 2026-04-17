### SKRW – End-Point Scaling of Grid Cell Krw(Sw =1.0) (Surfactant) {#kw-SKRW}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SKRW defines the scaling parameter at the maximum surfactant water relative permeability value ([SWU](#kw-SWU)), that is for Sw = 1.0, for all the cells in the model via an array.  The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. In addition, the Surfactant option must be enabled by either the [SURFST](#kw-SURFST) or [SURFSTES](#kw-SURFSTES) keywords in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SKRW | SKRW is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling SKRW values for each cell in the model. Repeat counts may be used, for example 50*1.000. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SKRW Keyword Description {#tbl-8-161}
```

```

End-point scaling allows the entered surfactant relative permeability functions to be scale on the relative permeability values using the [SKRO](#kw-SKRO), [SKRORG](#kw-SKRORG), [SKRORW](#kw-SKRORW), SKRW and [SKRWR](#kw-SKRWR) surfactant relative permeability grid cell arrays for the relative permeability end-point data.


#### Example

The example uses the [EQUALS](#kw-EQUALS) keyword to set SKRW for layer one equal to 0.850, layer two SKRW to 0.875, and layer three [KRW](#kw-KRW) to 0.900.


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         SKRW        0.8550       1*  1*   1*  1*    1   1  / SKRW FOR LAYER 1
         SKRW        0.8750       1*  1*   1*  1*    2   2  / SKRW FOR LAYER 2
         SKRW        0.9000       1*  1*   1*  1*    3   3  / SKRW FOR LAYER 3
/
```