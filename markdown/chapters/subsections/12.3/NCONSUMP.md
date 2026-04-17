### NCONSUMP – Node Gas Consumption (Extended Network) {#kw-NCONSUMP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NCONSUMP keyword defines an extended network node’s gas consumption rate, for when the Extended Network option has been activated by the [NETWORK](#kw-NETWORK) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword can also be used to attribute the gas consumption to a previously defined group.  See also the [GCONSUMP](#kw-GCONSUMP) keyword in the [SCHEDULE](#kw-SCHEDULE) section that overs more flexibility and can also be used with the Extended Network option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.