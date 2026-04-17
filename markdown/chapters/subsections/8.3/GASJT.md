### GASJT – Define Gas Joule-Thomson Coefficient


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

[GASJT](#__RefHeading___Toc163486_2545341761) activates the gas Joule-Thomson [Natural Gas Engineering (McGraw-Hill chemical engineering series), Donald L. Katz, Robert l Lee, McGraw-Hill Education, 1990 (ISBN 0071007776, 9780071007771).] effect in temperature calculations, and defines the gas Joule-Thomson Coefficient (“JTC”) at a given reference pressure, for when OPM Flow’s thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979).


| Note This is an OPM Flow keyword used with OPM Flow’s black-oil thermal model, that is not available in the commercial simulator’s black-oil thermal formulation. |
| --- |


This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model, and does not include the Joule-Thomson effect in temperature calculations.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | A real positive value that defines the reference pressure for the corresponding Joule-Thomson Coefficient, GASJTC. | None |
| psia | barsa | atma |  |
| 2 | GASJTC | GASJTC is a real positive or negative value that defines the gas phase Joule-Thomson Coefficient. If the value is defaulted (1*) or set to 0, then GASJTC is internally calculated using the thermal gas density data on the [GASDENT](#__RefHeading___Toc123086_2509125675) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. If a non-zero value is specified, then the GASJTC is assumed to be constant and equal to that value. | 0 |
| oF/psia | oC/barsa | oC/atma |  |
| Notes: |  |  |  |

*Table 8.40: GASJT Keyword Description*


The Joule–Thomson effect is when a real gas, as oppose to an ideal gas, expands, resulting in the temperature of the gas dropping. During passage of a gas through a choke, the internal energy is transferred to kinetic energy with a corresponding reduction in temperature as the velocity increases. The effect for natural gas is approximately 7 oF for every 100 psi pressure reduction, or 0.5 oC per barsa [https://petrowiki.spe.org/Glossary:Joule-thompson_effect.], is valid for "normal" pressures and temperatures at the surface.

Thermodynamically, the Joule–Thomson coefficient is defined as the isenthalpic [An isenthalpic process or isoenthalpic process, is a process that proceeds without any change in enthalpy, H; or specific enthalpy, h.] change in temperature in a fluid caused by a unitary pressure drop, as shown in the following equation:


|  | (8.53) |
| --- | --- |


One can also express enthalpy changes in terms of pressure, temperature and volume changes:


|  | (8.54) |
| --- | --- |

Where:

	=	Joule–Thomson coefficient,

	= 	specific heat at constant pressure,

	= 	pressure,

	=	gas constant,

	= 	temperature, and

	= 	gas compressibility factor.


#### Example

The following example shows the [GASJT](#__RefHeading___Toc163486_2545341761) keyword for when the thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set equal to two.


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

Here the first entry is defaulted, and the simulator will therefore calculate the gas JTC internally using the data on the [GASDENT](#__RefHeading___Toc123086_2509125675) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

There is no terminating “/” for this keyword.
