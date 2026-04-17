### OILDENT – Define Oil Density Temperature Coefficients {#kw-OILDENT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

OILDENT defines the oil density as a function of temperature coefficients for when OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC). Note this is an OPM Flow keyword used with OPM Flow’s black-oil thermal model that is not available in the commercial simulator’s black-oil thermal formulation.

This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#kw-TEMP) | [TEMP](#kw-TEMP) is a real positive value greater than zero that defines the absolute reference temperature used with TEXP1 and TEXP2 to estimate the change in oil density with respect to temperature. | Defined |
| oR 527.67 | K 293.15 | K 293.15 |  |
| 2 | TEXP1 | TEXP1 is a real positive value greater than zero that defines the oil thermal expansion coefficient of the first order. | Defined |
| 1/oR 1.67 x 10-4 | 1/K 3.0 x 10-4 | 1/K 3.0 x 10-4 |  |
| 3 | TEXP2 | TEXP2 is a real positive value greater than zero that defines the oil thermal expansion coefficient of the second order. | Defined |
| 1/oR2 9.26 x 10-7 | 1/K2 3.0 x 10-6 | 1/K2 3.0 x 10-6 |  |
| Notes: |  |  |  |
: OILDENT Keyword Description {#tbl-8-3-186-1}
The oil density at a given pressure and temperature is calculated from its value at surface conditions and the oil shrinkage factor (the reciprocal of the oil formation volume factor) as shown in the following equation:


$$
{ρ}_{o}(p,T)={ρ}_{o}({p}_{s},{T}_{s}){b}_{o}(p,T)
$$ {#eq-8-3-186-1}


Where the temperature dependence of the oil shrinkage factor relative to its value at the reference temperature is calculated as shown in the following equation:


$$
{b}_{o}(p,T)=\frac{{b}_{o}(p,{T}_{\mathit{ref}})}{1+{c}_{1}(T-{T}_{\mathit{ref}})+{c}_{2}{(T-{T}_{\mathit{ref}})}^{2}}
$$ {#eq-8-3-186-2}

Where:

${ρ}_{o}$	= oil density

${b}_{o}$	= oil shrinkage factor

$p$	= pressure

$T$	= temperature

${c}_{1},{c}_{2}$	= thermal expansion coefficients to first and second order

$s$	= subscript indicating surface conditions

$\mathit{ref}$	= subscript indicating reference conditions


#### Example

The following example shows the OILDENT keyword using the default values, for when the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section and for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set to two.


```
--
--       OIL DENSITY TEMPERATURE COEFFICIENTS (OPM FLOW THERMAL KEYWORD)
--
--       OIL        DENSITY   DENSITY
--       TEMP       COEFF1    COEFF2
--       --------   -------   -------
OILDENT
         1*         1*        1*                           / TABLE NO. 01
         1*         1*        1*                           / TABLE NO. 02
```


There is no terminating “/” for this keyword.