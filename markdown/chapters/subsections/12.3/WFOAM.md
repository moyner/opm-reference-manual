### WFOAM – Define Well Foam Injection Concentrations


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [WFOAM](#__RefHeading___Toc452036_2026549522) keyword defines an injection wells foam concentration.  The foam option must be activated by the [FOAM](#__RefHeading___Toc171586_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section in order to use this keyword. Note if a well’s foam concentration is not set with this keyword then default value of zero is assigned to a well.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well injection foam concentration is being defined. | None |
| 2 | FOAMCON | A real positive value that defines the well’s injection foam concentration. This value may be specified using a User Defined Argument (UDA). Units are dependent on the transport phase specified via the FOAMOPT1 variable on the [FOAMOPTS](#__RefHeading___Toc224982_3519154785) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. FOAMOPT1 should be set to either [GAS](#__RefHeading___Toc38607_2267116897) or [WATER](#__RefHeading___Toc38611_2267116897). Currently OPM Flow only supports injecting foam via the [GAS](#__RefHeading___Toc38607_2267116897) phase. | None |
| Gas: lb/Mscf Water: lb/stb | Gas: kg/sm3 Water: kg/sm3 | Gas: gm/scc Water: gm/scc |  |
| Notes: |  |  |  |

*Table 12.95: WFOAM Keyword Description*


See also the [FOAM](#__RefHeading___Toc171586_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, the [FOAMADS](#__RefHeading___Toc224974_3519154785), [FOAMOPTS](#__RefHeading___Toc224982_3519154785) and [FOAMROCK](#__RefHeading___Toc224980_3519154785) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section.


#### Example


```
--
--       WELL INJECTION FOAM CONCENTRATION
--
-- WELL  FOAM
-- NAME  FOAMCON
WFOAM
GI01     0.020                                                                 /
GI02     0.020                                                                 /
GI03     0.020                                                                 /
/
```


Here three gas wells are given an injection foam concentration of 0.020 lb/Mscf, assuming field units.
