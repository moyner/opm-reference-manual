### GNETDP – Group Network Pressure and Rate Controls {#kw-GNETDP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GNETDP keyword sets a group’s minimum and maximum network pressure and rate controls for when the either the Standard Network or the Extended Network options have been activated, and the group is part of a network. The keywords allows for the pressure of the group to vary in order to satisfy the rate conditions declared by this keyword. The Standard Network option is invoked if the [GRUPTREE](#kw-GRUPTREE), GRUPNET, [GNETINJE](#kw-GNETINJE), [GNETPUMP](#kw-GNETPUMP), etc. series of keywords have been used in the [SCHEDULE](#kw-SCHEDULE) section. Whereas, the Extended Network option is activated by the [NETWORK](#kw-NETWORK) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Several keywords, including, GNETDP, can be used by both network options.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.