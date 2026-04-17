### LWSWLPC – End-Point Scaling Grid Cell SWLPC (Low Salinity and Water Wet) {#kw-LWSWLPC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

LWSWLPC defines the capillary pressure connate water saturation (“[SWLPC](#kw-SWLPC)”), for all the cells in the model via an array, for when the Low Salt and Surfactant Wettability options have been selected.  The data is used to scale the water saturation in the low salinity water wet water-oil capillary pressure tables.  The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. In addition, the Low Salt option should be activated by the [LOWSALT](#kw-LOWSALT) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the Surfactant Wettability option activated by the [SURFACT](#kw-SURFACT) or [SURFACTW](#kw-SURFACTW) keywords, which are also in the [RUNSPEC](#kw-RUNSPEC) section.

Note the keyword only applies the scaling to the capillary pressures tables, unlike the [LWSWL](#kw-LWSWL) keyword that applies the scaling to both the capillary pressure and relative permeability tables.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.