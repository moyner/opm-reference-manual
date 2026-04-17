### WSEGSOLV – Define Multi-Segment Well Iterative Linear Solver Parameters {#kw-WSEGSOLV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WSEGSOLV keyword defines the numerical control parameters for the iterative linear solver for multi-segment well looped flow paths, as defined by the [WSEGLINK](#kw-WSEGLINK) keyword in the [SCHEDULE](#kw-SCHEDULE) section. A looped segment results in the nodes of the two individual segments that are looped (or connected) having the same solution pressures and oil, water and gas flowing rates.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.