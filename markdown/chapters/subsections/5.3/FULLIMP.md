### FULLIMP – Activate Fully Implicit Solution Option {#kw-FULLIMP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FULLIMP keyword activates the Fully Implicit Solution formulation and solution options. OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow ignores this keyword. It is documented here for completeness. The keyword as the same function as the [IMPLICIT](#kw-IMPLICIT) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

There is no data required for this keyword and there is no terminating “/” for this keyword.

See section 2.2 Running OPM Flow 2023-04 From The Command Line on how to invoke various numerical schemes via the OPM Flow command line interface.


#### Example


```
--
--       ACTIVATES THE FULLY IMPLICIT SOLUTION OPTION
--
FULLIMP

```

The above example switches on the fully implicit solution option; however, this has no effect in OPM Flow input decks.