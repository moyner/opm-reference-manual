### GDCQ – Define Group Multiple Daily Contract Quantities {#kw-GDCQ}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GDCQ keyword defines the Daily Contract Quantities (“DCQ”) for when multiple group contracts are required when the Gas Field Operations model has been activated by the [GASFIELD](#kw-GASFIELD) keyword in the [RUNSPEC](#kw-RUNSPEC) section, or the GWSINGF has been invoked to define multiple group contracts in the [SCHEDULE](#kw-SCHEDULE) section. The group contracts must first be defined by the [GSWINGF](#kw-GSWINGF) keyword, followed by the GCDQ keyword, and then the [GASYEAR](#kw-GASYEAR) or [GASPERIO](#kw-GASPERIO) keywords. GCDQ may be repeated in the [SCHEDULE](#kw-SCHEDULE) section to reset group DCQs.

See also the [SWINGFAC](#kw-SWINGFAC) keyword that set a single group DCQ at the field level, as opposed to having multiple DCQ group contracts using the GDCQ keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.