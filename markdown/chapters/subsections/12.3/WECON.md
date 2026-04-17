### WECON – Well Economic Criteria for Production Wells


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [WECON](#__RefHeading___Toc134884_2055188184) keyword defines the economic criteria for production wells that have previously been defined by the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WCONPROD](#__RefHeading___Toc146754_4203985108) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

Note that wells can be allocated to a group when they are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword and groups can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the [GCONPROD](#__RefHeading___Toc146746_4203985108) and [GECON](#__RefHeading___Toc134876_2055188184) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and the economic criteria specified by the [WECON](#__RefHeading___Toc134884_2055188184) keyword.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well economic criteria data is being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| 2 | ORAT | A real positive value that defines the minimum economic surface oil production rate, below which an economic action will take place, as outlined below: Only option (2) is supported by OPM Flow as STATUS equals AUTO on the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword is currently not supported by the simulator. Hence, the well be either shut or stopped. A value less than or equal to zero switches off this criterion. This value may be specified using a User Defined Argument (UDA). | 0.0 |
| stb/d | sm3/day | scc/hour |  |
| 3 | GRAT | A real positive value that defines the minimum economic surface gas production rate, below which an economic action will take place, as outlined below: Only option (2) is supported by OPM Flow as STATUS equals AUTO on the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword is currently not supported by the simulator. Hence, the well be either shut or stopped. A value less than or equal to zero switches off this criterion. This value may be specified using a User Defined Argument (UDA). | 0.0 |
| Mscf/d | sm3/day | scc/hour |  |
| 4 | WCUT | A real positive value that defines the maximum economic surface water cut, above which an economic action will take place. This value may be specified using a User Defined Argument (UDA). Water cut is defined as:, and the various actions that are available if the water cut limit is exceeded are described in item (7). A value less than or equal to zero switches off this criterion. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | GOR | A real positive value that defines the maximum economic surface gas-oil ratio, above which an economic action will take place, as defined by item (7). A value less than or equal to zero switches off this criterion. This value may be specified using a User Defined Argument (UDA). | 0.0 |
| Mscf/stb | sm3/sm3 | scc/scc |  |
| 6 | WGR | A real positive value that defines the maximum economic surface water-gas ratio, above which an economic action will take place, as defined by item (7). A value less than or equal to zero switches off this criterion. This value may be specified using a User Defined Argument (UDA). | 0.0 |
| stb/Mscf | sm3/sm3 | scc/scc |  |
| 7 | ACTION | A defined character string that defines the action to be taken if the economic WCUT, GOR, or WGR limits are violated. ACTION should be set to one of the following character strings: The corrective action takes places at the end of the time step in which the constraint is violated. The +CON option is not currently supported by OPM Flow. | NONE |
| 8 | END | A defined character string that defines if the simulation should terminate if the well is shut or stopped. END should be set to one of the following character strings: The YES option is not currently supported by OPM Flow. | NO |
| 9 | WELOPEN | A character string of up to eight characters in length that defines the name of the well, which will be opened when the current well (WELNAME) has been automatically closed/shut by the simulator. Wells closed manually do not invoke this opton. The well name (WELOPEN) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| 10 | ELTOPT | A defined character string that defines the type of quantity used to test the economic limit, and should be set to one of the following character strings: Wells under group control via the [GCONPROD](#__RefHeading___Toc146746_4203985108) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section will be subject to the ELT, except for when the group’s production target rate is set to zero. Wells under group control via the [GCONPRI](#__RefHeading___Toc659214_1190369742) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section will be subject to the ELT, except for when the group has curtailed a well’s production. | RATE |
| 11 | WCUT2 | A real positive value that defines the secondary maximum economic surface water cut, above which an economic action will take place. A value less than or equal to zero switches off this criterion. This item is not supported by OPM Flow and should be defaulted (1*) or set to zero. | 0.0 |
| 12 | ACTION2 | A defined character string that defines the action to be taken if the secondary economic WCUT2 limits is violated. This item is not supported by OPM Flow and should be defaulted (1*). | 1* |
| 13 | GLR | A real positive value that defines the maximum economic surface gas-liquid ratio, above which an economic action will take place, as defined by item (7). A value less than or equal to zero switches off this criterion. This item is not supported by OPM Flow and should be defaulted (1*). | None |
| 14 | LRAT | A real positive value that defines the minimum liquid rate, below which the well (WELNAME) is shut-in. This item is not supported by OPM Flow and should be defaulted (1*). | 0.0 |
| 15 | TEMP | A real positive value that defines the maximum economic temperature in the commercial compositional Thermal/Temperature model for a well. This item is not supported by OPM Flow and should be defaulted (1*). | None |
| 16 | RESV | A real positive value that defines the minimum reservoir volume rate, below which the well (WELNAME) is shut-in. This item is not supported by OPM Flow and should be defaulted (1*). | 0.0 |
| Notes: |  |  |  |

*Table 12.81: WECON Keyword Description*


See also the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword to define a wells shut-in or stop options, [GCONPROD](#__RefHeading___Toc146746_4203985108) for group controls, and [GECON](#__RefHeading___Toc134876_2055188184) for setting a group’s economic criteria. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.


#### Example

The following example defines one oil well and one gas well using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword, together with their economic criteria.


```
--
-- WELL SPECIFICATION DATA
--
-- WELL     GROUP      LOCATION  BHP    PHASE  DRAIN  INFLOW  SHUT  CROSS  PRESS
-- NAME     NAME        I    J   DEPTH  FLUID  AREA   EQUA.   IN    FLOW   TABLE
WELSPECS
GP01      PLATFORM     14   13   1*      GAS   1*     GPP     SHUT   NO    1*  /
OP01      PLATFORM     28   96   1*      OIL   1*     STD     SHUT   NO    1*  /
/
--
--       WELL ECONOMIC CRITERIA FOR PRODUCTION WELLS
-- WELL  MIN    MIN    MAX    MAX    MAX    CNTL    END
-- NAME  ORAT   GRAT   WCUT   GOR    WGR    MODE    RUN
WECON
GP01     1*     5.0E3  1*     1*     1*    'WELL'  'NO'                        /
OP01     500    1*     0.95   15     1*    'WELL'  'YES'                       /
/

```

Well GP01 has a minimum economic gas rate of 5 MMscf/d and will shut-in if the gas rate falls below this rate, but the simulation will continue even if this occurs. Well OP01 has a minimum economic oil rate of 500 stb/d, a maximum water cut limit of 95%, and a maximum GOR of 15 Mscf/stb, if any any of these limits are violated the well will be shut-in and the run should be terminated at the next reporting time step, however the option to end the run is not currently supported by OPM Flow.
