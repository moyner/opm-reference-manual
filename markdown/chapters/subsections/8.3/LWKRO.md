### LWKRO – End-Point Scaling of Grid Cell Kro(Swl) (Low Salinity and Water Wet) {#kw-LWKRO}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

LWKRO defines the scaling parameter for the oil relative permeability value at the connate water saturation ([SWL](#kw-SWL)), for all the cells in the model via an array, for when the Low Salt and Surfactant Wettability options have been selected.  The data is used to scale the oil relative permeability in the low salinity water wet oil relative permeability saturation tables. The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. In addition the Low Salt option should be activated by the [LOWSALT](#kw-LOWSALT) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the Surfactant Wettability option activated by the [SURFACT](#kw-SURFACT) or [SURFACTW](#kw-SURFACTW) keywords, which are also in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.