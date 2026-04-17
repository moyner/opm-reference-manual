### DYNRDIMS – Define Dynamic Region Dimensions {#kw-DYNRDIMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The DYNRDIMS keyword defines the dimensions for the parameters used by the Dynamic Regions facility, including the maximum number of dynamic regions.  The Dynamic Regions facility allows for property and reporting regions to vary as the run progresses, based on the parameters and logic defined by the [DYNAMICR](#kw-DYNAMICR) keyword in the [SOLUTION](#kw-SOLUTION) and [PROPS](#kw-PROPS) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.