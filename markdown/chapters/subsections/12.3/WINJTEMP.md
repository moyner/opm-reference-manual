### WINJTEMP – Define Injection Fluid Thermal Properties {#kw-WINJTEMP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WINJTEMP defines the injection fluid thermal properties for when the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section.  Only water and gas injection is supported.

This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well injection fluid thermal properties are being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | STEAMQAL | STEAMQAL is a real positive value greater than or equal to zero and less than or equal to one that defines the steam quality of the injected fluid for the defined well. This parameter should be defaulted using 1* as STEAMQAL is not used by OPM FLOW, as only water and gas injection is supported. This data is used by the commercial simulator’s [THERMAL](#kw-THERMAL) option and is not supported by OPM Flow’s [THERMAL](#kw-THERMAL) option. | 1* |
| dimensionless | dimensionless | dimensionless |  |
| 3 | [TEMP](#kw-TEMP) | [TEMP](#kw-TEMP) is a real positive value that defines the temperature of the injected fluid for the defined well. | None |
| oF | oC | oC |  |
| 4 | PRES | PRES is a real positive value that defines the pressure of the injected fluid for the defined well. | None |
| psia | barsa | atma |  |
| 5 | ENTHALPY | ENTHALPY is a real positive value that defines the specific enthalpy of the injected fluid for the defined well. This is data is used by the commercial simulator’s [THERMAL](#kw-THERMAL) option and is not supported by OPM Flow’s [THERMAL](#kw-THERMAL) option. | None |
| Btu/lbs-M | kJ/kg-M | J/gm-M |  |
| Notes: |  |  |  |
: WINJTEMP Keyword Description {#tbl-12-102}
#### Example

The following example shows the WINJTEMP keyword for when OPM Flow’s temperature option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


```
--
--       INJECTION FLUID THERMAL PROPERTIES
--
-- WELL  STEAM  INJ    INJ    SPEC
-- NAME  QUAL   TEMP   PRES   ENTH
WINJTEMP
WI01     1*     68.0   220.0    1*                         /
WI02     1*     70.0   230.0    1*                         /
/
```


Here the water injection fluid’s temperature and pressure, in field units, for two water injections well are defined. Notice that both the steam quality and the specific enthalpy of the injected fluid for the defined wells are defaulted (or skipped), as OPM Flow’s [THERMAL](#kw-THERMAL) option does not support this data.