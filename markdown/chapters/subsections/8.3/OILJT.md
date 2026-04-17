### OILJT – Define Oil Joule-Thomson Coefficient


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

OILJT activates the oil Joule-Thomson effect [The Joule–Thomson coefficient is defined as the change in temperature with respect to an increase in pressure at constant enthalpy.] in temperature calculations, and defines the oil Joule-Thomson Coefficient (“JTC”) at a given reference pressure, for when OPM Flow’s thermal option has been activated by the THERMAL keyword in the RUNSPEC.


| Note This is an OPM Flow keyword used with OPM Flow’s black-oil thermal model, that is not available in the commercial simulator’s black-oil thermal formulation. |
| --- |


This keyword can only be used if OPM Flow’s thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model, and does not include the Joule-Thomson effect in temperature calculations.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | A real positive value that defines the reference pressure for the corresponding Joule-Thomson Coefficient, OILJTC. | None |
| psia | barsa | atma |  |
| 2 | OILJTC | OILJTC is a real positive or negative value that defines the oil phase Joule-Thomson Coefficient. If the value is defaulted (1*) or set to 0, then OILJTC is internally calculated using the thermal oil density data on the OILDENT keyword in the PROPS section. If a non-zero value is specified, then the OILJTC is assumed to be constant and equal to that value. | 0 |
| oF/psia | oC/barsa | oC/atma |  |
| Notes: |  |  |  |

*Table 8.92: OILJT Keyword Description*


The Joule–Thomson effect is when a real gas, as oppose to an ideal gas, expands, resulting in the temperature of the gas dropping [Natural Gas Engineering (McGraw-Hill chemical engineering series), Donald L. Katz, Robert l Lee, McGraw-Hill Education, 1990 (ISBN 0071007776, 9780071007771).]. For liquids the effect is the opposite, that is the internal energy is transferred to kinetic energy with a corresponding increase in temperature as velocity increases.

Thermodynamically, the Joule–Thomson coefficient is defined as the isenthalpic [An isenthalpic process or isoenthalpic process, is a process that proceeds without any change in enthalpy, H; or specific enthalpy, h.] change in temperature in a fluid caused by a unitary pressure drop, as shown in the following equation:


| $$ \mathrm{η} = \left(\frac{\partial T}{\partial P}\right) $$ | (8.66) |
| --- | --- |


Which can also express as [Pippard, A.B.: Elements of Classical Thermodynamics: For Advanced Students of Physics. Cambridge University Press, Cambridge, UK (1957)]:


| $$ \mathrm{η} = \left(T\mathrm{α} - 1\right)\frac{1}{(\mathrm{ρ}{C}_{p})} - {\left(\frac{g}{{C}_{p}}\frac{\mathit{dp}}{\mathit{dz}}\right)}^{-1} $$ | (8.67) |
| --- | --- |

$$
g
$$


| $$ \mathrm{η} = \left(T\mathrm{α} - 1\right)\frac{1}{(\mathrm{ρ}{C}_{b})} $$ | (8.68) |
| --- | --- |

Where:

$$
η
$$

$$
α
$$

$$
{C}_{p}
$$

$$
g
$$

$$
P
$$

$$
T
$$

$$
z
$$


#### Example

The following example shows the OILJT keyword for when the thermal option has been activated by the THERMAL keyword in the RUNSPEC section, and for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set equal to two.


```
--
--       OIL JOULE-THOMSON COEFFICIENT (OPM FLOW EXTENSION KEYWORD)
--
--       REF        OIL
--       PRESS      JTC
--       --------   -------
OILJT
         20.0       1*                  / TABLE NO. 01
         20.0       -0.20               / TABLE NO. 02

```

Here the first entry is defaulted, and the simulator will therefore calculate the oil JTC internally using the data on the OILDENT keyword in the PROPS section.

There is no terminating “/” for this keyword.
