### SOXYG – Define The Initial Equilibration Oxygen Concentration For All Grid Blocks {#kw-SOXYG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SOXYG keyword defines the initial equilibration oxygen concentration values for all grid cells in the model. The keyword should only be used if the [MICP](#kw-MICP) model has been activated in the [RUNSPEC](#kw-RUNSPEC) section.


::: {.callout-note}
This is an OPM Flow specific keyword.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SOXYG | SOXYG is an array of real numbers that are greater than or equal to zero assigning the initial equilibration oxygen concentration values to each cell in the model. Repeat counts may be used, for example 20*0.1500 | None |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |
: SOXYG Keyword Description {#tbl-10-50}
See also the [SBIOF](#kw-SBIOF), [SCALC](#kw-SCALC), [SMICR](#kw-SMICR), and [SUREA](#kw-SUREA) keywords to define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION OXYGEN CONCENTRATION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SOXYG
         1000*0.0000 1000*0.0000 1000*0.1500                                   /

```

The above example defines the initial equilibration oxygen concentration values to be 0.0000 for all the cells in the first and second layers and finally 0.1500 for all the cells in the third layer.