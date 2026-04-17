### WNETCTRL – Define Well Control for Network Control Option {#kw-WNETCTRL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WNETCNTL keyword sets a well’s control mode that should remain fixed after each network balancing calculation, for when the either the Standard Network or the Extended Network options have been activated, and the well is part of a network. The keyword allows for a well’s Tubing Head Pressure (“THP”), oil, gas, liquid, or water rate to be selected as fixed after each network balance calculation. Normally this should be the THP, and if the keyword is absent from the input deck then THP will be used as the default value. The Standard Network option is invoked if the [GRUPTREE](#kw-GRUPTREE), GRUPNET, [GNETINJE](#kw-GNETINJE), [GNETPUMP](#kw-GNETPUMP), etc. series of keywords have been used in the [SCHEDULE](#kw-SCHEDULE) section. Whereas, the Extended Network option is activated by the [NETWORK](#kw-NETWORK) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.