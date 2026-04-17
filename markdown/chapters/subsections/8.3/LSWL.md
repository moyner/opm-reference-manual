### LSWL – End-Point Scaling Grid Cell SWL (Low Salinity and Oil Wet) {#kw-LSWL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

LSWL defines the connate water saturation (“[SWL](#kw-SWL)”), for all the cells in the model via an array, for when the Low Salt option has been selected.  The data is used to scale the water saturation in the low salinity oil wet water-oil relative permeability saturation tables, as well as the associated capillary pressure tables. The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. In addition, the Low Salt option should be activated by the [LOWSALT](#kw-LOWSALT) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.