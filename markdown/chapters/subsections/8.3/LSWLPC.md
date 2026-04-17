### LSWLPC – End-Point Scaling Grid Cell SWLPC (Low Salinity and Oil Wet) {#kw-LSWLPC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

LSWLPC defines the capillary pressure connate water saturation (“[SWLPC](#kw-SWLPC)”), for all the cells in the model via an array, for when the Low Salt option has been selected.  The data is used to scale the water saturation in the low salinity oil wet water-oil capillary pressure tables.  The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. In addition, the Low Salt option should be activated by the [LOWSALT](#kw-LOWSALT) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

Note the keyword only applies the scaling to the capillary pressures tables, unlike the [LSWL](#kw-LSWL) keyword that applies the scaling to both the capillary pressure and relative permeability tables.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.