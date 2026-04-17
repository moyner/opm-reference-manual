### SIMULATE – Activate the Simulation Mode {#kw-SIMULATE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SIMULATE switches the mode of the simulation to run simulation mode from the data input checking mode activated by the [NOSIM](#kw-NOSIM) keyword in the [SCHEDULE](#kw-SCHEDULE) section. Note that if [NOSIM](#kw-NOSIM) has been used in the [RUNSPEC](#kw-RUNSPEC) section then SIMULATE will have no effect.

There is no data required for this keyword and there is no terminating “/” for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


#### Example

The example below switches OPM Flow to no simulation mode for data checking of the input deck.


```
--
--       ACTIVATE SIMULATION MODE TO RUN THE MODEL
--
SIMULATE
```