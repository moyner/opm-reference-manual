### SUREA – Define The Initial Equilibration Urea Concentration For All Grid Blocks


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SUREA keyword defines the initial equilibration urea concentration values for all grid cells in the model. The keyword should only be used if the MICP model has been activated in the RUNSPEC section.


| Note This is an OPM Flow specific keyword. |
| --- |


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SUREA | SUREA is an array of real numbers that are greater than or equal to zero assigning the initial equilibration urea concentration values to each cell in the model. Repeat counts may be used, for example 20*30.0. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |

*Table 10.54: SUREA Keyword Description*


See also the SBIOF, SCALC, SMICR, and SOXYG keywords to define the initial state of the model.


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
