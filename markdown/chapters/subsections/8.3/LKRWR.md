### LKRWR – End-Point Scaling of Grid Cell KRWR(Sowcr) (Low Salinity and Oil Wet) {#kw-LKRWR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

LKRWR defines the scaling parameter at the maximum oil relative permeability value ([SWU](#kw-SWU)), that is for Sw = 1.0, for all the cells in the model via an array, for when the Low Salt option and the End-point Scaling options has been activated by the [LOWSALT](#kw-LOWSALT) and the [ENDSCALE](#kw-ENDSCALE) keywords in the [RUNSPEC](#kw-RUNSPEC) section.   The data is used to scale the water relative permeability in the low salinity oil wet water relative permeability saturation tables.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.