### FOAMROCK – Define Foam Rock Properties


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [FOAMROCK](#__RefHeading___Toc224980_3519154785) keyword defines the foam rock properties for when the Foam option has been activated by the [FOAM](#__RefHeading___Toc171586_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

The keyword is recognized by the input deck parser and simulator support is available in the experimental "ebos" simulator.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ADINDX | A positive integer of 1 or 2 that defines foam desorption option, as per: Only the default value of 1 is supported by OPM Flow. | Defined |
| dimensionless 1 | dimensionless 1 | dimensionless 1 |  |
| 2 | [DENSITY](#__RefHeading___Toc45799_719036256) | A real value that defines the rock in situ density, that is at reservoir conditions. | None |
| lb/rb | kg/rm3 | gm/rcc |  |
| Notes: |  |  |  |

*Table 8.38: FOAMROCK Keyword Description*


| Note In the commercial simulator if the [POLYMER](#__RefHeading___Toc38609_2267116897) and [SURFACT](#__RefHeading___Toc863854_4250154414) phases have been activated in conjunction with the [FOAM](#__RefHeading___Toc171586_289573908) phase then the mass density of rock will be set by the [PLYROCK](#__RefHeading___Toc110216_2939291539), [SURFROCK](#__RefHeading___Toc903548_4250154414), or the [FOAMROCK](#__RefHeading___Toc224980_3519154785) keywords depending on the order entered in the run deck. This is not the case for OPM Flow. OPM Flow’s [FOAM](#__RefHeading___Toc171586_289573908) phase is a standalone implementation and cannot be used in conjunction with the either the [POLYMER](#__RefHeading___Toc38609_2267116897) or [SURFACT](#__RefHeading___Toc863854_4250154414) phases. |
| --- |


#### Example


```
--
--       FOAM-ROCK PROPERTIES
--
FOAMROCK
--       DESORP   INSITU
--       OPTN     DENSITY
--       ------   -------
           1      1800.0                                   / TABLE NO. 01
           2      1980.0                                   / TABLE NO. 02
           1      2005.0                                   / TABLE NO. 03

```

The above example defines three foam-rock tables, based on the NTSFUN variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section being equal to three.

There is no terminating “/” for this keyword.
