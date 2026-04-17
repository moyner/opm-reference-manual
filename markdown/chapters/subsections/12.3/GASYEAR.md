### GASYEAR – Advance Simulation by Gas Contract Year {#kw-GASYEAR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword advances the simulation over one or more gas contract years for when the Gas Field Operations option has been activated by the [GASFIELD](#kw-GASFIELD) keyword in the [RUNSPEC](#kw-RUNSPEC) section.  A contract year in this case is the period over which the Daily Contract Quantity is fixed, this can a be year, this keyword or the [GASPERIO](#kw-GASPERIO) keyword in the [SCHEDULE](#kw-SCHEDULE) section, or one or more months. If the contract period is over one or more months then the [GASPERIO](#kw-GASPERIO) keyword in the [SCHEDULE](#kw-SCHEDULE) section can be used instead of GASYEAR.

GASYEAR is an alternative to the [DATES](#kw-DATES), [TIME](#kw-TIME) and [TSTEP](#kw-TSTEP) keywords in the [SCHEDULE](#kw-SCHEDULE) section that advances the simulation to a given report time after which additional keywords may be entered to instruct OPM Flow to perform additional functions via the [SCHEDULE](#kw-SCHEDULE) section keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.