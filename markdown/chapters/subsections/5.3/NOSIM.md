### NOSIM – Activate the No Simulation Mode for Data File Checking


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

NOSIM switches the mode of OPM Flow to data input checking mode. In this mode the input file is read and all messages and print instructions are sent to the respective output files. The SCHEDULE section is read but the simulation is not performed.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example

The example below switches OPM Flow to no simulation mode for data checking of the input deck.


```
--
--       SWITCH NO SIMULATION MODE FOR DATA CHECKING COMMENT OUT TO RUN THE MODEL
--
NOSIM
```


And the next example shows how to commented out the NOSIM activation keyword so that the simulation will proceed.


```
--
--       SWITCH NO SIMULATION MODE FOR DATA CHECKING COMMENT OUT TO RUN THE MODEL
--
-- NOSIM
```


::: {.callout-note}
Simulation input decks are complex and are therefore prone to typing errors, thus before submitting a run that will take over 15 minutes or so, it is a good idea to run the model with the NOSIM option. If no errors are found then the NOSIM keyword should be commented out by placing “--” before the keyword, and then re-running the model. Alternatively, one could use OPMRUN to run all the jobs in the queue in NOSIM mode and have the software re-run jobs in simulation mode if there are no errors.
:::
