### WTADD – Add a Constant to a Well Target or Constraint {#kw-WTADD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, WTADD, adds a constant to a previously define well’s target or constraint, as stated on the  [WCONPROD](#kw-WCONPROD), [WCONINJE](#kw-WCONINJE), or [WELTARG](#kw-WELTARG) keywords, but not for the history matching wells using the  [WCONHIST](#kw-WCONHIST) or [WCONINJH](#kw-WCONINJH) keywords. All the aforementioned keywords are in the [SCHEDULE](#kw-SCHEDULE) section. The constant can be positive or negative.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.