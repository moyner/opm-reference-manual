### THCO2MIX – Specify Thermal Mixing Models


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [THCO2MIX](#REF_HEADING_KEYWORD_THCO2MIX_8_3) keyword specifies the thermal mixing models for salt in the water phase, CO2 in the liquid phase and vaporized water in gas phase.

This is an OPM Flow specific keyword that should only be used if the CO2STORE keyword has been specified in the RUNSPEC section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
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
