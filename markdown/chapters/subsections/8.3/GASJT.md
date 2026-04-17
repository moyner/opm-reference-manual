### GASJT – Define Gas Joule-Thomson Coefficient


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

GASJT activates the gas Joule-Thomson [Natural Gas Engineering (McGraw-Hill chemical engineering series), Donald L. Katz, Robert l Lee, McGraw-Hill Education, 1990 (ISBN 0071007776, 9780071007771).] effect in temperature calculations, and defines the gas Joule-Thomson Coefficient (“JTC”) at a given reference pressure, for when OPM Flow’s thermal option has been activated by the THERMAL keyword in the RUNSPEC.


::: {.callout-note}
This is an OPM Flow keyword used with OPM Flow’s black-oil thermal model, that is not available in the commercial simulator’s black-oil thermal formulation.
:::


This keyword can only be used if OPM Flow’s thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model, and does not include the Joule-Thomson effect in temperature calculations.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | A real positive value that defines the reference pressure for the corresponding Joule-Thomson Coefficient, GASJTC. | None |
| psia | barsa | atma |  |
| 2 | GASJTC | GASJTC is a real positive or negative value that defines the gas phase Joule-Thomson Coefficient. If the value is defaulted (1*) or set to 0, then GASJTC is internally calculated using the thermal gas density data on the GASDENT keyword in the PROPS section. If a non-zero value is specified, then the GASJTC is assumed to be constant and equal to that value. | 0 |
| oF/psia | oC/barsa | oC/atma |  |
| Notes: |  |  |  |

*Table 8.40: GASJT Keyword Description*


The Joule–Thomson effect is when a real gas, as oppose to an ideal gas, expands, resulting in the temperature of the gas dropping. During passage of a gas through a choke, the internal energy is transferred to kinetic energy with a corresponding reduction in temperature as the velocity increases. The effect for natural gas is approximately 7 oF for every 100 psi pressure reduction, or 0.5 oC per barsa [https://petrowiki.spe.org/Glossary:Joule-thompson_effect.], is valid for "normal" pressures and temperatures at the surface.

Thermodynamically, the Joule–Thomson coefficient is defined as the isenthalpic [An isenthalpic process or isoenthalpic process, is a process that proceeds without any change in enthalpy, H; or specific enthalpy, h.] change in temperature in a fluid caused by a unitary pressure drop, as shown in the following equation:


$$
\mathrm{η} = \left(\frac{\partial T}{\partial P}\right)
$$ {#eq-8-53}


One can also express enthalpy changes in terms of pressure, temperature and volume changes:


$$
\mathrm{η} = \frac{{\mathit{RT}}^{2}}{{\mathit{Pc}}_{p}}{\left(\frac{\partial Z}{\partial T}\right)}_{P}
$$ {#eq-8-54}

Where:

$η$	=	Joule–Thomson coefficient,

${C}_{g}$	= 	specific heat at constant pressure,

$P$	= 	pressure,

$R$	=	gas constant,

$T$	= 	temperature, and

$Z$	= 	gas compressibility factor.


#### Example

The following example shows the GASJT keyword for when the thermal option has been activated by the THERMAL keyword in the RUNSPEC section, and for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set equal to two.


```
--
--       GAS JOULE-THOMSON COEFFICIENT (OPM FLOW EXTENSION KEYWORD)
--
--       REF        GAS
--       PRESS      JTC
--       --------   -------
GASJT
         20.0       1*                  / TABLE NO. 01
         20.0       0.50                / TABLE NO. 02

```

Here the first entry is defaulted, and the simulator will therefore calculate the gas JTC internally using the data on the GASDENT keyword in the PROPS section.

There is no terminating “/” for this keyword.
