### IMBNUMMF – Define the Imbibition Saturation Table Region Numbers (Matrix-Fracture) {#kw-IMBNUMMF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The IMBNUMMF keyword defines the imbibition saturation tables (relative permeability and capillary pressure tables) region numbers for flow between the matrix and fracture blocks, for when the HYSTER option on the [SATOPTS](#kw-SATOPTS) keyword has been invoked to activate the Hysteresis option, and the Dual Porosity or Dual Permeability models have been activated via the [DUALPORO](#kw-DUALPORO) or [DUALPERM](#kw-DUALPERM) keywords. All keywords are in the [RUNSPEC](#kw-RUNSPEC) section.

The region number specifies which set of relative permeability tables ([SGFN](#kw-SGFN), [SWFN](#kw-SWFN), [SOF2](#kw-SOF2), [SOF3](#kw-SOF3), [SOF32D](#kw-SOF32D), [SGOF](#kw-SGOF), [SLGOF](#kw-SLGOF) and [SWOF](#kw-SWOF)) are used to calculate the relative permeability and capillary pressure between the matrix and fracture blocks.  The keyword is optional and any cell not assigned a value will use the assignment from the [IMBNUM](#kw-IMBNUM) array.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.