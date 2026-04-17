### SCALC – Define The Initial Equilibration Calcite Volume Fraction For All Grid Blocks {#kw-SCALC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SCALC keyword defines the initial equilibration calcite volume fraction for all grid cells in the model. The keyword should only be used if the [MICP](#kw-MICP) model has been activated in the [RUNSPEC](#kw-RUNSPEC) section.


::: {.callout-note}
This is an OPM Flow specific keyword.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SCALC | SCALC is an array of real numbers that are greater than or equal to zero and less than or equal to one assigning the initial equilibration  calcite volume fraction values to each cell in the model. Repeat counts may be used, for example 20*0.0010. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SCALC Keyword Description {#tbl-10-42}
See also the [SBIOF](#kw-SBIOF), [SMICR](#kw-SMICR), [SOXYG](#kw-SOXYG) and [SUREA](#kw-SUREA) keywords to define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION CALCITE VOLUME FRACTION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SCALC
         1000*0.0000 1000*0.0000 1000*0.0010                                   /

```

The above example defines the initial equilibration calcite volume fraction values to be 0.0000 for all the cells in the first and second layers and finally 0.0010 for all the cells in the third layer.