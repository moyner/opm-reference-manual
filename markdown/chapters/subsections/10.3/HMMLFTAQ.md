### HMMLFTAQ – History Match Fetkovich Aquifer Gradient Multipliers {#kw-HMMLFTAQ}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [HMAQUFET](#kw-HMAQUFET) keyword defines the history match analytical Fetkovich aquifer gradient multipliers for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and analytical Fetkovich aquifers have been specified in the model via the [AQUFET](#kw-AQUFET) and/or the  [AQUFETP](#kw-AQUFETP) keywords and connected to the grid using [AQUANCON](#kw-AQUANCON) or [AQANCONL](#kw-AQANCONL) keywords. All keywords are in the [SOLUTION](#kw-SOLUTION) section.

Multipliers can be declared for the Fetkovich aquifer water volume, aquifer permeability, and the aquifer depth.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.