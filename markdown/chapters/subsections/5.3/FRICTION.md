### FRICTION – Activate Wellbore Friction Option {#kw-FRICTION}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FRICTION keyword activates the Wellbore Friction option and defines the maximum number of  wellbore friction wells together with the maximum number of well branches.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MXWELS | A positive integer defining the maximum number of wellbore friction wells for this model. | 0 |
| 3 | MXBRAN | A positive integer defining the maximum number of branches per well. The default value of one implies a standard well with no branches. | 1 |
| Notes: |  |  |  |
: FRICTION Keyword Description {#tbl-5-16}
#### Example


```
--
--       WELL    BRANCH
--       MXWELS  MXBRAN
FRICTION
         5       1                                                             /
```


The above example defines the maximum number of wellbore friction wells to be five and the maximum number of branches set to one, for standard wells.