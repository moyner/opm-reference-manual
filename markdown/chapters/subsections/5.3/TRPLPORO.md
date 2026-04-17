### TRPLPORO – Activate the Triple Porosity Model Option {#kw-TRPLPORO}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The TRPLPORO keyword activates the Triple Porosity Model option that models matrix, fractures and vuggy porosity for carbonate reservoirs, and specifies the number of matrix porosity systems

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | TRPLPORO | A positive integer value that specifies the number of matrix porosity systems in the model. TRPLPORO should be set to either: | 1 |
| Notes: |  |  |  |
: TRPLPORO Keyword Description {#tbl-5-49}
Note the keyword cannot be used in conjunction with the [NMATRIX](#kw-NMATRIX) keyword, which is also in the [RUNSPEC](#kw-RUNSPEC) section.


#### Example


```
--
--       TRPLPORO
--       OPTION
TRPLPORO
         3                                                        /
```


The above example activates the Triple Porosity Model option and specifies the porosity system is matrix, connected vugs, and isolated vugs.