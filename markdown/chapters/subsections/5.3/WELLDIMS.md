### WELLDIMS – Define the Wells and Group Dimensions {#kw-WELLDIMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WELLDIMS defines various well and group dimensions for the run. The commercial simulator combines both the black-oil and compositional simulator variables on this keyword; however, although all the parameters are explained below only the black-oil parameters are used by OPM Flow.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MXWELS | A positive integer defining the maximum number of wells for this model. | 0 |
| 2 | MXCONS | A positive integer defining the maximum number of grid block connections per well for this model. | 0 |
| 3 | MXGRPS | A positive integer defining the maximum number of groups for this model. | 0 |
| 4 | MXGRPW | A positive integer defining the maximum number of wells that can belong to a group in the model and the maximum number of child groups in a group. Note that MXGRPW sets both the maximum number of wells in a group and the maximum number of child groups in a group.  The former applies to groups that contain wells and the latter applies to groups that contain other groups.  See also the [GRUPTREE](#kw-GRUPTREE) keyword in the [SCHEDULE](#kw-SCHEDULE) section to define group hierarchy. | 0 |
| 5 | MXSTAGE | A positive integer defining the maximum number of stages per separator for this model. This option is ignored by OPM Flow. | 5 |
| 6 | MXSTRMS | A positive integer defining the maximum number of well streams for this model. This option is ignored by OPM Flow. | 10 |
| 7 | MXMIXS | A positive integer defining the maximum number of mixtures for this model. This option is ignored by OPM Flow. | 5 |
| 8 | MXSEPS | A positive integer defining the maximum number of separators for this model. This option is ignored by OPM Flow. | 4 |
| 9 | MXCOMPS | A positive integer defining the maximum number of mixture components in a mixture for the model. This option is ignored by OPM Flow. | 3 |
| 10 | MXDOCOMP | A positive integer defining the maximum number of well completions that can cross a parallel run domain boundary when the [PARALLEL](#kw-PARALLEL) option has been activated. This option is ignored by OPM Flow. | 0 |
| 11 | MXWSLIST | A positive integer defining the maximum number of well lists that a well may be concurrent belong to at one time for this model. This option is ignored by OPM Flow. | 1 |
| 12 | MXWLISTS | A positive integer defining the maximum number of dynamic well lists for this model. This option is ignored by OPM Flow. | 1 |
| 13 | MXWSECD | A positive integer defining the maximum number of secondary wells for this model. This option is ignored by OPM Flow. | 10 |
| 14 | MXNGPP | A positive integer defining the maximum number of row entries per completion in the generalized pseudo-pressure tables used for to calculate the blocking factor associated with condensate drop-out in gas condensate reservoirs. If the generalized pseudo-pressure option has not been activated then this is ignored. This option is ignored by OPM Flow. | 201 |
| Notes: |  |  |  |
: WELLDIMS Keyword Description {#tbl-5-58}
#### Example


```
--
--       WELL    WELL    GRUPS   GRUPS
--       MXWELS  MXCONS  MXGRPS  MXGRPW
WELLDIMS
         60      110     18      40                                            /
```


The above example defines the maximum number of wells to be 60 with 110 completions per well, and maximum number of groups to be 18 with maximum number of wells per group of 40.  All other parameters are defaulted.