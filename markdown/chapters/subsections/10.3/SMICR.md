### SMICR – Define The Initial Equilibration Microbial Concentration For All Grid Blocks {#kw-SMICR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SMICR keyword defines the initial equilibration microbial concentration values for all grid cells in the model. The keyword should only be used if either the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) or [MICP](#kw-MICP) model has been activated in the [RUNSPEC](#kw-RUNSPEC) section.


::: {.callout-note}
This is an OPM Flow specific keyword.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SMICR | SMICR is an array of real numbers that are greater than or equal to zero assigning the initial equilibration microbial concentration values to each cell in the model. Repeat counts may be used, for example 20*0.1500. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |
: SMICR Keyword Description {#tbl-10-46}
For both [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) and [MICP](#kw-MICP) models, see also the [SBIOF](#kw-SBIOF) keyword, and for the [MICP](#kw-MICP) model, the [SCALC](#kw-SCALC), [SOXYG](#kw-SOXYG), and [SUREA](#kw-SUREA) keywords to define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION MICROBIAL CONCENTRATION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SMICR
         1000*0.0000 1000*0.0000 1000*0.1500                                   /

```

The above example defines the initial equilibration microbial concentration values to be 0.0000 for all the cells in the first and second layers and finally 0.1500 for all the cells in the third layer.