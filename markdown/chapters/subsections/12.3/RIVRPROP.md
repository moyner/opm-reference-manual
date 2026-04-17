### RIVRPROP – Modify River Reaches Properties {#kw-RIVRPROP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RIVRPROP keyword modifies the individual reaches in a river structure of a previously characterized river system using the [RIVERSYS](#kw-RIVERSYS) and the [REACHES](#kw-REACHES) keywords in the [SCHEDULE](#kw-SCHEDULE) section.  The River option must be activated via the [RIVRDIMS](#kw-RIVRDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section in order to use this keyword.  RIVRPROP is an alternative and a more concise way to changing the individual reaches in a river structure than the [REACHES](#kw-REACHES) keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.