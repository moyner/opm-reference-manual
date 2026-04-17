### SUREA – Define The Initial Equilibration Urea Concentration For All Grid Blocks {#kw-SUREA}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SUREA keyword defines the initial equilibration urea concentration values for all grid cells in the model. The keyword should only be used if the [MICP](#kw-MICP) model has been activated in the [RUNSPEC](#kw-RUNSPEC) section.


::: {.callout-note}
This is an OPM Flow specific keyword.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SUREA | SUREA is an array of real numbers that are greater than or equal to zero assigning the initial equilibration urea concentration values to each cell in the model. Repeat counts may be used, for example 20*30.0. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |
: SUREA Keyword Description {#tbl-10-54}
See also the [SBIOF](#kw-SBIOF), [SCALC](#kw-SCALC), [SMICR](#kw-SMICR), and [SOXYG](#kw-SOXYG) keywords to define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION UREA CONCENTRATION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SUREA
         1000*0.0000 1000*0.0000 1000*20.0                                     /

```

The above example defines the initial equilibration urea concentration values to be 0.0000 for all the cells in the first and second layers and finally 20.0 for all the cells in the third layer.