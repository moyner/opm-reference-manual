### GASMONTH – Define Start of Annual Scheduling Event {#kw-GASMONTH}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, GASMONTH, states the month for which subsequent scheduling events take place within an Annual Schedule section for when the Gas Field Operations option has been activated by the [GASFIELD](#kw-GASFIELD) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword must lie in between the [GASBEGIN](#kw-GASBEGIN), that defines the start of an Annual Scheduling section and the [GASEND](#kw-GASEND) keyword that ends the section. Optionally, the keyword can be used to write a report to the print file (*.PRT) at the requested month.

See also the [GASBEGIN](#kw-GASBEGIN) and [GASEND](#kw-GASEND) keywords in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.