### DIMPES – Define IMPES Dynamic Solution Parameters


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, DIMPES, defines the Implicit in Pressure Explicit Saturation (“IMPES”) dynamic solution parameters and results in the simulator switching from the current solution formulation to the IMPES formulation. OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword.

See section 2.2 Running OPM Flow 2023-04 From The Command Line on how to invoke various numerical schemes via the OPM Flow command line interface.


#### Example


```
--
--       ACTIVATE THE IMPES SOLUTION OPTION
--
DIMPES

```

The above example switches on the IMPES solution option; however, this has no effect in OPM Flow input decks.
