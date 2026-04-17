### IMPES – Activate Implicit Pressure Explicit Saturation Solution Option {#kw-IMPES}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The IMPES keyword activates the Implicit Pressure Explicit Saturation formulation and solution options, commonly know as IMPES. OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword and there is no terminating “/” for this keyword.

See section 2.2 Running OPM Flow 2023-04 From The Command Line on how to invoke various numerical schemes via the OPM Flow command line interface.


#### Example


```
--
--       ACTIVATE THE IMPES SOLUTION OPTION
--
IMPES

```

The above example switches on the IMPES solution option; however, this has no effect in OPM Flow input decks.