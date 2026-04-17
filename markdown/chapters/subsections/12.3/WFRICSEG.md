### WFRICSEG – Convert Friction Well to Multi-Segment Well {#kw-WFRICSEG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WFRICSEG converts a previously defined friction well, as per the [WFRICTN](#kw-WFRICTN) keyword in the [SCHEDULE](#kw-SCHEDULE) section, to a multi-segment well. The keyword thus acts as a replacement for the [WELSEGS](#kw-WELSEGS) and [COMPSEGS](#kw-COMPSEGS) keywords for multi-segment wells. See also the [WFRICSGL](#kw-WFRICSGL) keyword in the [SCHEDULE](#kw-SCHEDULE) section that performs similar functionality for wells in Local Grid Refinements.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.