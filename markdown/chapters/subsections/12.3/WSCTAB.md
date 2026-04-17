### WSCTAB – Assign Well Scale Deposition and Scale Damage Tables {#kw-WSCTAB}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WSCTAB assigns scale deposition and scale damage tables to a well, for when the Scale Deposition option has been activated by declaring the dimensions of the scaling deposition tables using the [SCDPDIMS](#kw-SCDPDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Scale deposits reduce the productivity of well and this relationship is defined in the [SCDPTAB](#kw-SCDPTAB) and [SCDATAB](#kw-SCDATAB) keywords in the [SCHEDULE](#kw-SCHEDULE) section, and are allocated to a well by the WSCTAB keyword.

See also the [WPIMULT](#kw-WPIMULT) keyword in the [SCHEDULE](#kw-SCHEDULE) section that adjusts a well’s productivity index by a constant value.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.