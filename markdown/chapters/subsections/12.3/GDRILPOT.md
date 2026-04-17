### GDRILPOT – Define Group Potential Rates for Automatic Drilling {#kw-GDRILPOT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, GDRILPOT, defines the minimum group potential rate that will result in a well from the one of the automatic drilling queues, as defined by either the [QDRILL](#kw-QDRILL) or [WDRILPRI](#kw-WDRILPRI) keywords in the [SCHEDULE](#kw-SCHEDULE) section, to be drilled and placed on production. The advantage of using a group’s potential, as oppose to a minimum rate limit, is that setting the potential greater than the group’s minimum flow rate, will result in well being drilled in time to support the desired production rate.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.