### WGASPROD – Define Sale Gas Well Production Targets {#kw-WGASPROD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WGASPROD keyword declares wells to be Sales Gas producers and sets the incremental gas rate for a well and the maximum number of increments that this rate can be increased. Wells must have been previously been defined via the [WELSPECS](#kw-WELSPECS) and [WCONPROD](#kw-WCONPROD) keywords in the [SCHEDULE](#kw-SCHEDULE) section and are subject to any targets or constraints on [WCONPROD](#kw-WCONPROD) keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.