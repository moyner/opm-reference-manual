### THCO2MIX – Specify Thermal Mixing Models


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [THCO2MIX](#REF_HEADING_KEYWORD_THCO2MIX_8_3) keyword specifies the thermal mixing models for salt in the water phase, CO2 in the liquid phase and vaporized water in gas phase.

This is an OPM Flow specific keyword that should only be used if the [CO2STORE](#__RefHeading___Toc387968_1616145207) keyword has been specified in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | SALTMOD | A defined character string that specifies the thermal mixing model for salt in the liquid phase, and should be set to one of the following: | MICHAELIDES |
| 2 | LIQMOD | A defined character string that specifies the thermal mixing model for CO2 in the liquid phase, and should be set to one of the following: | DUANSUN |
| 3 | GASMOD | A defined character string that specifies the thermal mixing model for vaporized water in the gas phase, and should be set to one of the following: | NONE |
| Notes: |  |  |  |

*Table 8.3.343.1: [THCO2MIX](#REF_HEADING_KEYWORD_THCO2MIX_8_3) Keyword Description*


#### Example

The following example specifies the default thermal mixing models for salt in the liquid phase, CO2 in the liquid phase, and vaporized water in the gas phase.


```
--
--       SPECIFY THERMAL MIXING MODELS
--
--       SALT      LIQUID    GAS
--       --------  --------  --------
THCO2MIX
      MICHAELIDES  DUANSUN   NONE    /
```
