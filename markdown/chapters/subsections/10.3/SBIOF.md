### SBIOF – Define The Initial Equilibration Biofilm Volume Fraction For All Grid Blocks


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SBIOF keyword defines the initial equilibration biofilm volume fraction for all grid cells in the model. The keyword should only be used if either the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) or MICP model has been activated in the RUNSPEC section.


::: {.callout-note}
This is an OPM Flow specific keyword.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SBIOF | SBIOF is an array of real numbers that are greater than or equal to zero and less than or equal to one assigning the initial equilibration biofilm volume fraction values to each cell in the model. Repeat counts may be used, for example 20*0.0010. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 10.41: SBIOF Keyword Description*


For both [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) and MICP models, see also the SMICR keyword, and for the MICP model, the SCALC, SOXYG, and SUREA keywords to define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION BIOFILM VOLUME FRACTION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SBIOF
         10000*0.0000 10000*0.0000 10000*0.0010                                   /

```

The above example defines the initial equilibration biofilm volume fraction values to be 0.0000 for all the cells in the first and second layers and finally 0.0010 for all the cells in the third layer.
