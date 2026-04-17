### PLYMAX – Define Polymer-Salt Viscosity Mixing Concentrations


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [PLYMAX](#__RefHeading___Toc110214_2939291539) keyword defines maximum polymer and salt concentrations that are to be used in the mixing parameter calculation of the fluid component viscosities, for when the Polymer option has been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

Note that If the [BRINE](#__RefHeading___Toc162083_289573908) option has not be activated by the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then the salt concentrations in the second column are ignored.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | POLCON | A real value that defines the polymer concentration in the solution which is used to calculate maximum polymer fluid component viscosity. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| 2 | SALTCON | A real value that defines the salt concentration in the solution which is used to calculate maximum polymer fluid component viscosity. Note that If the [BRINE](#__RefHeading___Toc162083_289573908) option has not been activated by the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then this variable is ignored; however, there should still be dummy entries in this case. This variable is ignored as the [BRINE](#__RefHeading___Toc162083_289573908) and [POLYMER](#__RefHeading___Toc38609_2267116897) combination is not implemented in OPM Flow. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |

*Table 8.103: PLYMAX Keyword Description*


| Note Currently, combining the [BRINE](#__RefHeading___Toc162083_289573908) and [POLYMER](#__RefHeading___Toc38609_2267116897) models is not implemented in OPM Flow, and therefore SALTCON parameter on the [PLYMAX](#__RefHeading___Toc110214_2939291539) keyword is ignored. |
| --- |


#### Example


```
--
--       POLYMER-SALT VISCOSITY MIXING CONCENTRATIONS
--
PLYMAX
--       POLYMER    SALT
--       POLCON     SALTCON
--       -------    --------
         0.0100      0.0500                                / TABLE NO. 01
         0.0075      0.0400                                / TABLE NO. 02
         0.0050      0.0300                                / TABLE NO. 03
```


The above example defines three polymer-salt viscosity mixing concentrations, based on the NPLMIX variable on the [REGDIMS](#__RefHeading___Toc70161_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section being equal to three.
