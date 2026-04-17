### UNCODHMD – Activate History Match Gradient Unencoded Output {#kw-UNCODHMD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

UNCODHMD activates the history match gradient unencoded output for the history match gradient output file. Unencoded files allows external programs to read this file type.

There is no data required for this keyword and there is no terminating “/” for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


#### Example


```
--
--       ACTIVATE HISTORY MATCH GRADIENT UNENCODED OUTPUT
--
UNCODHMD
```


The above example switches on the unified output file option.