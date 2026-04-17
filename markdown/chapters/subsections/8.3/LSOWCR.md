### LSOWCR – End-Point Scaling Grid Cell SOWCR (Low Salinity and Oil Wet) {#kw-LSOWCR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

LSOWCR defines the critical oil saturation with respect to water (“[SOWCR](#kw-SOWCR)”), for all the cells in the model via an array, for when the Low Salt option has been selected.  The data is used to scale the oil saturation in the low salinity oil wet water-oil relative permeability saturation tables. The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. In addition, the Low Salt option should be activated by the [LOWSALT](#kw-LOWSALT) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.