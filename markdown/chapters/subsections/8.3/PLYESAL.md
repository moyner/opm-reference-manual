### PLYESAL – Define Polymer Effective Salinity Coefficient {#kw-PLYESAL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, PLYESAL, defines the polymer effective salinity coefficient as well as enabling the effective salinity calculation for polymer adsorption. The keyword should only be used if the [BRINE](#kw-BRINE) keyword has been declared to activate the brine phase, the [ECLMC](#kw-ECLMC) keyword to enable the Multi-Component Brine model, and the [POLYMER](#kw-POLYMER) keyword has been used to activate the polymer phase. All three keywords are in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.