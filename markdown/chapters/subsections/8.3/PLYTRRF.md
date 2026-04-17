### PLYTRRF – Define Polymer Rock Permeability Reduction versus Temperature {#kw-PLYTRRF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PLYTRRF keyword defines the polymer rock permeability reduction factor to the water phase as a function of temperature, for when the Polymer option has been activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section. See the PLYTRRF keyword for the options on how this data is used in the polymer model and the PERMFAC parameter on the [PLYROCK](#kw-PLYROCK) keyword for setting the property for the whole grid for a constant temperature. Both keywords are in the [PROPS](#kw-PROPS) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.