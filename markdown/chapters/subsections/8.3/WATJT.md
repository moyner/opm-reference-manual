### WATJT – Define Water Joule-Thomson Coefficient {#kw-WATJT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WATJT activates the water Joule-Thomson effect^[The Joule–Thomson coefficient is defined as the change in temperature with respect to an increase in pressure at constant enthalpy.] in temperature calculations, and defines the water Joule-Thomson Coefficient (“JTC”) at a given reference pressure, for when OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC).


::: {.callout-note}
This is an OPM Flow keyword used with OPM Flow’s black-oil thermal model, that is not available in the commercial simulator’s black-oil thermal formulation.
:::


This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model, and does not include the Joule-Thomson effect in temperature calculations.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | A real positive value that defines the reference pressure for the corresponding Joule-Thomson Coefficient, WATJTC. | None |
| psia | barsa | atma |  |
| 2 | WATJTC | WATJTC is a real positive or negative value that defines the water phase Joule-Thomson Coefficient. If the value is defaulted (1*) or set to 0, then WATJTC is internally calculated using thermal water density data on the WATSDENT keyword in the [PROPS](#kw-PROPS) section. If a non-zero value is specified, then the WATJTC is assumed to be constant and equal to that value. | 0 |
| oF/psia | oC/barsa | oC/atma |  |
| Notes: |  |  |  |
: WATJT Keyword Description {#tbl-8-198}
The Joule–Thomson effect is when a real gas, as oppose to an ideal gas, expands, resulting in the temperature of the gas dropping^[Natural Gas Engineering (McGraw-Hill chemical engineering series), Donald L. Katz, Robert l Lee, McGraw-Hill Education, 1990 (ISBN 0071007776, 9780071007771).]. For liquids the effect is the opposite, that is the internal energy is transferred to kinetic energy with a corresponding increase in temperature as velocity increases.

Thermodynamically, the Joule–Thomson coefficient is defined as the isenthalpic^[An isenthalpic process or isoenthalpic process, is a process that proceeds without any change in enthalpy, H; or specific enthalpy, h.] change in temperature in a fluid caused by a unitary pressure drop, as shown in the following equation:


$$
\mathrm{η} = (\frac{\partial T}{\partial P})
$$ {#eq-8-98}


Which can also express as^[Pippard, A.B.: Elements of Classical Thermodynamics: For Advanced Students of Physics. Cambridge University Press, Cambridge, UK (1957)]:


$$
\mathrm{η} = (T\mathrm{α} - 1)\frac{1}{(\mathrm{ρ}{C}_{p})} - {(\frac{g}{{C}_{p}}\frac{\mathit{dp}}{\mathit{dz}})}^{-1}
$$ {#eq-8-99}

Setting the gravity term, $g$, to zero we have:


$$
\mathrm{η} = (T\mathrm{α} - 1)\frac{1}{(\mathrm{ρ}{C}_{b})}
$$ {#eq-8-100}

Where:

$η$	=	Joule–Thomson coefficient (oC/Pa),

$α$	=	thermal expansivity at constant pressure (1/oC),

${C}_{p}$	= 	specific heat at constant pressure (J/kg oC),

$g$	= 	gravitational acceleration (m/s2)

$P$	= 	pressure (Pa),

$T$ 	= 	temperature (oC), and

$z$ 	= 	height (m).


#### Example

The following example shows the WATJT keyword for when the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set equal to two.


```
--
--       WATER JOULE-THOMSON COEFFICIENT (OPM FLOW EXTENSION KEYWORD)
--
--       REF        OIL
--       PRESS      JTC
--       --------   -------
WATJT
         20.0       1*                  / TABLE NO. 01
         20.0       -0.20               / TABLE NO. 02
```


Here the first entry is defaulted, and the simulator will therefore calculate the water JTC internally using the data on the [WATDENT](#kw-WATDENT) keyword in the [PROPS](#kw-PROPS) section.

There is no terminating “/” for this keyword.