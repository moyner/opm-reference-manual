### PLYTRRFA – Define Polymer Rock Permeability Reduction versus Temperature Option {#kw-PLYTRRFA}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PLYTRRFA keyword defines the how the polymer rock permeability reduction factor to the water phase as a function of temperature data, entered via the PLYTRRA keyword in the [PROPS](#kw-PROPS) section, should be used. This keyword should only be used if the Polymer option has been activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section. See the PERMFAC parameter on the [PLYROCK](#kw-PLYROCK) keyword in the [PROPS](#kw-PROPS) section for setting the property for the whole grid for a constant temperature.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.