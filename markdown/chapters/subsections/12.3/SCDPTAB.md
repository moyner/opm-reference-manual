### SCDPTAB – Well Connection Scale Deposition Tables {#kw-SCDPTAB}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

[SCDATAB](#kw-SCDATAB) defines the well connection scale deposition rate as a function of sea water flow rate, for when the Scale Deposition option has been activated by declaring the dimensions of the scaling deposition tables using the [SCDPDIMS](#kw-SCDPDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The [SCDATAB](#kw-SCDATAB) tables are allocated to individual wells using the [WSCTAB](#kw-WSCTAB) keyword and the sea water fraction is based on a water tracer entered via the [SCDPTRAC](#kw-SCDPTRAC) keyword; both keywords are in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.