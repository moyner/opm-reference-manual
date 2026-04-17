### PLYVSCST – Define Polymer-Salt-Temperature Viscosity Scaling Factors {#kw-PLYVSCST}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PLYVSCST defines the polymer-salt-temperature viscosity scaling factor tables applied to pure water that are used to determine the viscosity of the polymer at a given salt concentration and for a given temperature, with respect to increasing polymer concentration within a grid block. Both the polymer option must be activated by the [POLYMER](#kw-POLYMER) keyword and the temperature option invoked by the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section in order to use this keyword.  In addition, the [BRINE](#kw-BRINE) keyword in the [RUNSPEC](#kw-RUNSPEC) must also be invoked.  The keyword is used in conjunction with the [SALTNODE](#kw-SALTNODE) keyword to define the various salt concentrations and the [TEMPNODE](#kw-TEMPNODE) keyword to define the various reservoir temperatures. Both keywords are in the [PROPS](#kw-PROPS) section.

See also the [PLYVISCS](#kw-PLYVISCS) keyword in the [PROPS](#kw-PROPS) section to enter polymer viscosity scaling factor data that is dependent just salt concentration and the [PLYVISCT](#kw-PLYVISCT) keyword in the [PROPS](#kw-PROPS) section to enter polymer viscosity scaling factor data that is dependent just on reservoir temperature.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.