### WNETDP – Define Well THP to Network Pressure Drop {#kw-WNETDP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WNETDP keyword allows for a constant pressure drop between a well’s Tubing Head Pressure (“THP”)  and the well’s connecting network node, for when the either the Standard Network or the Extended Network options have been activated, and the well is part of a network. For production wells in a production network, WNETDP is added to the well’s connecting network node pressure to arrive at the well’s THP value. Whereas for injection wells in an injection network, WNETDP is subtracted from the well’s connecting network node pressure to arrive at the well’s THP value. The Standard Network option is invoked if the [GRUPTREE](#kw-GRUPTREE), GRUPNET, [GNETINJE](#kw-GNETINJE), [GNETPUMP](#kw-GNETPUMP), etc. series of keywords have been used in the [SCHEDULE](#kw-SCHEDULE) section. The Extended Network option is activated by the [NETWORK](#kw-NETWORK) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.