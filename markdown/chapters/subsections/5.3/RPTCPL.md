### RPTCPL – Activate Couple Simulation Reporting {#kw-RPTCPL}


| FRUNSPEC | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the couple simulation reporting, that results in the simulator writing out various initialization data and simulation data in order for external “controlling programs” to interactively manage the simulation. There is no data required for this keyword but the keyword should be terminated by a “/”.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


#### Example


```
--
--       ACTIVATE COUPLE SIMULATION REPORTING
--
RPTCPL
/
```


The above example switches on couple simulation reporting; however, this has no effect in OPM Flow input decks.