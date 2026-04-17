### NRSOUT – Defined Maximum Number of RESTART Elements {#kw-NRSOUT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NRSOUT keyword specifies the maximum number of elements that can be written to the [RESTART](#kw-RESTART) file at each reporting time step.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NRSOUT | A positive integer value that specifies the maximum number of elements that can be written to the [RESTART](#kw-RESTART) file at each reporting time step. | 3600 |
| Notes: |  |  |  |
: NRSOUT Keyword Description {#tbl-5-28}
#### Example


```
--
--       MAX
--       NRSOUT
NRSOUT
         6000                                                     /
```


The above example sets the maximum number of elements that can be written to the [RESTART](#kw-RESTART) file at each reporting time step to 6000.