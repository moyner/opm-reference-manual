### SURFSTES – Surfactant Water-Oil Surface Tension versus Surfactant and Salt Concentrations {#kw-SURFSTES}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SURFSTES keyword defines surfactant water-oil surface tension versus surfactant concentration in the water phase tables, used in adjusting the pressure independent capillary pressure vectors in the [SWFN](#kw-SWFN) or [SWOF](#kw-SWOF) saturation tables, entered by their respective keywords in the [PROPS](#kw-PROPS) section. SURFSTES is also used to adjust the relative permeability curves on the aforementioned tables via the capillary number.  The Surfactant option must have been activated by the SURFACTANT keyword in the [RUNSPEC](#kw-RUNSPEC) section to use this keyword and either this keyword or the [SURFST](#kw-SURFST) keyword, also in the [PROPS](#kw-PROPS) section, is obligatory in this case. In addition, the [BRINE](#kw-BRINE) keyword in the [RUNSPEC](#kw-RUNSPEC) section must be activated and the [ESSNODE](#kw-ESSNODE) keyword in the [PROPS](#kw-PROPS) section must be used to define the salt concentration or the effective salinity.


See also the SURFSTS that defines the surfactant water-oil surface tension as a function of surfactant concentration in the water phase only.


This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.