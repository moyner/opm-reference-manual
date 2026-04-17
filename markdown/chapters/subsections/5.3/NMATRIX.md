### NMATRIX – Activate the Discretized Matrix Dual Porosity Option {#kw-NMATRIX}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NMATRIX keyword activates the Discretized Matrix Dual Porosity option and specifies the number of sub-grid blocks in the actual matrix grid blocks. See also the NMATOPS keyword in the [GRID](#kw-GRID) section that defines various parameters for this option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NMATRIX | A positive integer value that specifies the number of sub-grid blocks in the actual matrix grid blocks. | 1 |
| Notes: |  |  |  |
: NMATRIX Keyword Description {#tbl-5-26}
Note the keyword cannot be used in conjunction with the [TRPLPORO](#kw-TRPLPORO) keyword, which is also in the [RUNSPEC](#kw-RUNSPEC) section.


#### Example


```
--
--       SUB-GRIDS
--       NMATRIX
NMATRIX
         4                                                        /
```


The above example activates the Discretized Matrix Dual Porosity option and specifies the number of sub-grid blocks in the actual matrix grid block to be four.