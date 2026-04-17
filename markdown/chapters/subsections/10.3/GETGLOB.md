### GETGLOB – Activate Loading of Global Grid Restart Data Option {#kw-GETGLOB}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, GETGLOB, switches on the global grid read option for when the run is restarting from a [RESTART](#kw-RESTART) file. Only the global grid will be loaded in the subsequent [RESTART](#kw-RESTART) keyword and any Local Grid Refinements (“[LGR](#kw-LGR)”) on the [RESTART](#kw-RESTART) file will be ignored.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


#### Example


```
--
--       ACTIVATE LOADING OF GLOBAL GRID RESTART DATA OPTION
--
GETGLOB
```


The above example switches on the option to only load the global grid from the [RESTART](#kw-RESTART) file.