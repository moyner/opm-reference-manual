### VEFRACPV – Vertical Equilibrium Capillary Pressure Fraction (Cell) {#kw-VEFRACPV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the Vertical Equilibrium (“[VE](#kw-VE)”) capillary pressure weighting factor (α) used to calculate the [VE](#kw-VE) capillary pressure curves to be used in the simulation, for when the [VE](#kw-VE) option has been activated by the [VE](#kw-VE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.  If α = 1.0, then the [VE](#kw-VE) model calculated capillary pressure curves will be used, and if α = 0.0, then the curves entered via the [SWOF](#kw-SWOF), [SGOF](#kw-SGOF), [SLGOF](#kw-SLGOF) series of keywords or the [SWFN](#kw-SWFN), [SGFN](#kw-SGFN), [SGWFN](#kw-SGWFN), [SOF2](#kw-SOF2), [SOF3](#kw-SOF3), [SOF32D](#kw-SOF32D) series of keywords, will be used. A value of α between zero and one will result in weighted average capillary pressure curves being employed, that is:


$$
{\mathit{[VE](#kw-VE)}}_{(\mathit{average})} = (1.0 - \mathrm{α}) \times  ({\mathit{[SATNUM](#kw-SATNUM)}}_{\mathit{curves}}) + \mathrm{α} \times  (\mathit{[VE](#kw-VE)}{\mathit{Model}}_{\mathit{curves}})
$$ {#eq-8-96}


Note that VEFRACPV sets α on a cell by cell basis; whereas, the [VEFRACP](#kw-VEFRACP) keyword in the [PROPS](#kw-PROPS) section assigns α for the whole grid, See also the [VEFRAC](#kw-VEFRAC) and [VEFRACV](#kw-VEFRACV) keywords that apply the weighting factors to the relative permeability data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.