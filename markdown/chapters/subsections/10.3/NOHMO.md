### NOHMO – Deactivate History Match Gradient Derivative Calculations (Alias) {#kw-NOHMO}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NOHMO deactivates various history match gradient derivative calculations for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword consists of a series of character strings that define which derivative should be switch off based on the keyword that requested the derivatives to be calculated, for example [HMFAULTS](#kw-HMFAULTS) keyword in the [GRID](#kw-GRID) section. If an empty list is entered then all the gradient derivative calculations previously requested are switch off. The keyword is useful for changing from history matching runs to predication cases, as the prediction cases will be more computationally efficient without the burden of the gradient derivative calculations.

The keyword is an alias for the [NOHMD](#kw-NOHMD) keyword in the [SOLUTION](#kw-SOLUTION) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.