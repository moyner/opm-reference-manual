### WFRICTN – Define Well as a Friction Well {#kw-WFRICTN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WFRICTN keyword is used to declare a previously defined well as a friction well and to set the characteristics for this type of well including: tubing size, pipe roughness, and the connections to the grid. Wellbore friction is important in horizontal and multi-lateral wells where the pressure loss along the pipe can effect a well’s performance. Note that unlike other [SCHEDULE](#kw-SCHEDULE) section well keywords, multiple wells cannot be entered with one WFRICTN keyword, that is, the keyword must be repeated for each well.

See also the [WFRICTNL](#kw-WFRICTNL) keyword in the [SCHEDULE](#kw-SCHEDULE) section that performs similar functionality for wells in Local Grid Refinements.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.