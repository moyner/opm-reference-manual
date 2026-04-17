### LKRO – End-Point Scaling of Grid Cell Kro(Swl) (Low Salinity and Oil Wet) {#kw-LKRO}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

LKRO defines the scaling parameter for the oil relative permeability value at the connate water saturation ([SWL](#kw-SWL)), for all the cells in the model via an array, for when the Low Salt option and the End-point Scaling options has been activated by the [LOWSALT](#kw-LOWSALT) and the [ENDSCALE](#kw-ENDSCALE) keywords in the [RUNSPEC](#kw-RUNSPEC) section. The data is used to scale the oil relative permeability in the low salinity oil wet oil relative permeability saturation tables.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.