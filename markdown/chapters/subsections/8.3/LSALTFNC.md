### LSALTFNC – Define Low Salt Weighting Factors versus Salt Concentration Functions {#kw-LSALTFNC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LSALTFNC keyword defines the low salt weighting factors versus salt concentration functions for when the Low Salt option has been activated by the [LOWSALT](#kw-LOWSALT) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The tables are used to modify the oil and water relative permeability saturation end-points, as well as the water-oil capillary pressure end-points, for different salt concentrations within a grid cell.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.