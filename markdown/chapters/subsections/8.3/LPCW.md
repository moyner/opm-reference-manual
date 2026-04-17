### LPCW – End-Point Scaling of Grid Cell Water Capillary Pressure (Low Salinity and Oil Wet) {#kw-LPCW}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

LPCW defines the maximum oil-water pressure values for all the cells in the model via an array, for when the Low Salt option and the End-point Scaling options has been activated by the [LOWSALT](#kw-LOWSALT) and the [ENDSCALE](#kw-ENDSCALE) keywords in the [RUNSPEC](#kw-RUNSPEC) section. The keyword re-scales the oil-water capillary pressure in the low salinity oil wet capillary saturation tables from a cell’s assigned saturation function by the grid block’s LPCW value.

The capillary pressure for a grid block is scaled by:


$$
{P}_{c} = {P}_{{c}_{\mathit{TABLE}}}(\frac{\mathit{LPCW}}{{P}_{{c}_{\mathit{TABLE}-\mathit{MAX}}}})
$$ {#eq-8-64}

Where:

${P}_{c}$	=	the resulting low salt oil wet water capillary pressure for a grid cell.

$\mathit{LPCW}$	= 	the maximum capillary pressure from the LPCW array for a given cell.

${P}_{{c}_{\mathit{TABLE}}}$	= 	the capillary pressure in the low salt oil wet capillary pressure table

allocated to the grid block.

${P}_{{c}_{\mathit{TABLE}-\mathit{MAX}}}$	= 	the maximum capillary pressure in the low salt oil capillary pressure table

allocated to the grid block (that is at the connate water saturation).


This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.