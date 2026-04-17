### WFRICSGL – Convert Friction Well to Multi-Segment Well (LGR) {#kw-WFRICSGL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WFRICSGL converts a previously defined Local Grid Refinement (“[LGR](#kw-LGR)”) friction well, as per the [WFRICTNL](#kw-WFRICTNL) keyword in the [SCHEDULE](#kw-SCHEDULE) section, to a multi-segment [LGR](#kw-LGR) well. The keyword thus acts as a replacement for the [WELSEGS](#kw-WELSEGS) and [COMPSEGL](#kw-COMPSEGL) keywords for [LGR](#kw-LGR) multi-segment wells. See also the [WFRICSEG](#kw-WFRICSEG) keyword in the [SCHEDULE](#kw-SCHEDULE) section that performs similar functionality for wells in the global grid.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.