### DYNAMICR – Start of Dynamic Region Parameter Definition {#kw-DYNAMICR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The DYNAMICR keyword marks the start of a Dynamic Region section and defines the parameters used for Dynamic Regions that allows for property and reporting regions to vary as the run progresses, based on the parameters and logic defined by this keyword and section. A Dynamic Region section is terminated by the [ENDDYN](#kw-ENDDYN) keyword in the [SOLUTION](#kw-SOLUTION) or [SCHEDULE](#kw-SCHEDULE) sections.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.