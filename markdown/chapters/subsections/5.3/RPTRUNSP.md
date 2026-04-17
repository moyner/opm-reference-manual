### RPTRUNSP – Activate RUNSPEC Reporting {#kw-RPTRUNSP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates reporting of all the [RUNSPEC](#kw-RUNSPEC) options utilized in the run. There is no data required for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


#### Example


```
--
--       ACTIVATE RUNSPEC SECTION REPORTING
--
RPTRUNSP
```


The above example switches on [RUNSPEC](#kw-RUNSPEC) reporting; however, this has no effect in OPM Flow input decks.