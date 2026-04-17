### ECLMC – Activate Multi-Component Brine Model {#kw-ECLMC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ECLMC keyword activates the Multi-Component Brine model that allows for the water phase to have multiple water salinities. The keyword should be used in conjunction with the [BRINE](#kw-BRINE) keyword in the [RUNSPEC](#kw-RUNSPEC). Both keywords must be specified to activate the Multi-Component Brine model, whereas the [BRINE](#kw-BRINE) keyword only is required to activate the standard brine tracking model.

There is no data required for this keyword and there is no terminating “/” for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


#### Example

The first example activates the standard Brine Tracking model.


```
--
--       ACTIVATE STANDARD BRINE MODEL
--
BRINE
```


The next example shows the ECLMC and [BRINE](#kw-BRINE) keywords for when the Multi-Component Brine model is required.


```
--
--       ACTIVATE MULTI-COMPONENT BRINE MODEL
--
ECLMC
--
--       DEFINE WATER PHASE MULTI-COMPONENT BRINE COMPONENTS
--
--       SALT1   SALT2   SALT3   SALT4   SALT5
BRINE
         NACL    CACL2   MGC03                                                 /
```


The above example activates the Multi-Component Brine model with three different water salinities.