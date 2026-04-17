### WSEGTABL – Assign Multi-Segment Well VLP Tables to Segments {#kw-WSEGTABL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WSEGTABL assigns previously defined Vertical Lift Performance (“VLP”) tables as specified by the [VFPPROD](#kw-VFPPROD)  keyword in the [SCHEDULE](#kw-SCHEDULE) section, to multi-segment well segments, as well as stipulating how the tables are to be applied.

The FLOWOPT parameter on the [WELSEGS](#kw-WELSEGS) keyword in the [SCHEDULE](#kw-SCHEDULE) section sets the default multi-segment well model. FLOWOPT either activates the homogeneous model, that is all phases flow at the same velocity, or the Drift Flux Slip model. However, the [WSEGFMOD](#kw-WSEGFMOD) keyword in the [SCHEDULE](#kw-SCHEDULE) section, can be used to set the flow model for a segment to either the homogeneous model or the Drift Flux Slip model, and addition a: VLP table allocated via the WSEGTABL keyword, or a specific model as defined by the [WSEGVALV](#kw-WSEGVALV), [WSEGFLIM](#kw-WSEGFLIM) and [WSEGLABY](#kw-WSEGLABY) keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.