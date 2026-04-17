### SCDATAB – Well Connection PI Multipliers versus Scale Deposit {#kw-SCDATAB}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SCDATAB defines well connection Productivity Index (“PI”) reduction multipliers versus scale deposited per unit length of the perforated interval tables, for when the Scale Deposition option has been activated by declaring the dimensions of the scaling deposition tables using the [SCDPDIMS](#kw-SCDPDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The SCDATAB tables are allocated to individual wells using the [WSCTAB](#kw-WSCTAB) keyword and the rate of scale accumulation around the well connections is given by the [SCDPTAB](#kw-SCDPTAB) keyword; both keywords are in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.