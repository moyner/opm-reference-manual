### PLYKRRF – Define Polymer Rock Permeability Reduction by Cell {#kw-PLYKRRF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PLYKRRF keyword defines the polymer rock permeability reduction factor to the water phase by individual cell, for when the Polymer option has been activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section. PLYKRRF should consist of an array of real positive values that are greater than or equal to one. See the PERMFAC parameter on the [PLYROCK](#kw-PLYROCK) keyword in the [PROPS](#kw-PROPS) section for setting the property for the whole grid.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.