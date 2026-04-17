### IONXROCK – Define Ion Exchange Constant by Saturation Table Regions {#kw-IONXROCK}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The IONXROCK keyword activates ion exchange and defines the ion exchange constant by saturation table regions, for when the brine phase has been activated by the [BRINE](#kw-BRINE) keyword and the Multi-Component Brine model, that allows for the water phase to have multiple water salinities, has been activated by the [ECLMC](#kw-ECLMC) keyword. Both keywords are in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.