### GNETINJE – Define Group Injection Network Configuration {#kw-GNETINJE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GNETINJE keyword defines the configuration of a group injection network for when the either the Standard Network or the Extended Network options have been activated. The Standard Network option is invoked if the [GRUPTREE](#kw-GRUPTREE), GRUPNET, GNETINJE, [GNETPUMP](#kw-GNETPUMP), etc. series of keywords have been used in the [SCHEDULE](#kw-SCHEDULE) section. Whereas, the Extended Network option is activated by the [NETWORK](#kw-NETWORK) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Several keywords, including, GNETINJE, can be used by both network options.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.