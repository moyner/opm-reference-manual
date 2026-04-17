### GCONPROD – Group Production Targets and Constraints


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [GCONPROD](#__RefHeading___Toc146746_4203985108) keyword defines production targets and constraints for groups, including the top most group in the group hierarchy known as the FIELD group. Wells are allocated to groups when the wells are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.  Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field. Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| 2 | TARGET | A defined character string that specifies the production rate control mode for the group. The simulator will attempt to meet the TARGET rate as defined by remaining items on this keyword. TARGET should be set to one of the following character strings: Note that the commercial simulator includes additional options (not listed above) that are not currently supported by OPM Flow. | None |
| 3 | ORAT | A real positive value that defines the maximum surface oil production rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| stb/d | sm3/day | scc/hour |  |
| 4 | WRAT | A real positive value that defines the maximum surface water production rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| stb/d | sm3/day | scc/hour |  |
| 5 | GRAT | A real positive value that defines the maximum surface gas production rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| Mscf/d | sm3/day | scc/hour |  |
| 6 | LRAT | A real positive value that defines the maximum surface liquid (oil plus water) production rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| stb/d | sm3/day | scc/hour |  |
| 7 | ACTION | A defined character string that specifies the action to be taken if the constraints in (3) to (6) are violated. ACTION should be set to one of the following character strings: The corrective action takes places at the end of the time step in which the constraint is violated. Note that only the NONE, WELL and RATE options are currently supported by OPM Flow. | None |
| 8 | GRPCNTL | A defined character string that determines if this group is subject to higher level group control. GRPCNTL will be ignored for the FIELD group. | None |
| 9 | GRPGUIDE | A real positive value that defines a group's production guide rate expressed as a dimensionless number.  A group requires a value for GRPGUIDE only if it is required to produce a specified proportion of a higher level group’s rate | None |
| dimensionless | dimensionless | dimensionless |  |
| 10 | GUIPHASE | A defined character string that sets the guide phase to which the guide rate in item (9) applies.  GUIPHASE should be set to one of the following character strings: Note that only the [OIL](#__RefHeading___Toc97439_1778172979), WAT, [GAS](#__RefHeading___Toc38607_2267116897), LIQ and default options are currently supported by OPM Flow. | 1* |
| 11 | ACTWAT | A defined character string that defines the action to be taken if the WRAT constraint, item (4), is violated. ACTWAT should be set to one of the following character strings: If defaulted then procedure defined by ACTION, item (7), is applied.  The corrective action takes places at the end of the time step in which the constraint is violated. Note that only the NONE and RATE options are currently supported by OPM Flow. | 1* |
| 12 | ACTGAS | A defined character string that defines the action to be taken if the GRAT constraint, item (5), is violated. ACTGAS should be set to one of the following character strings: If defaulted then procedure defined by ACTION, item (7), is applied.  The corrective action takes places at the end of the time step in which the constraint is violated Note that only the NONE and RATE options are currently supported by OPM Flow. | 1* |
| 13 | ACTLIQ | A defined character string that defines the action to be taken if the LRAT constraint, item (6), is violated. ACLIQT should be set to one of the following character strings: If defaulted then procedure defined by ACTION, item (7), is applied.  The corrective action takes places at the end of the time step in which the constraint is violated. Note that only the NONE and RATE options are currently supported by OPM Flow. | 1* |
| 14 | RESV | A real positive value that defines the maximum reservoir volume production rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| rb/d | rm3/day | rcc/hour |  |
| 15 | RESVFRAC | A real positive value that defines the maximum reservoir volume production balancing fraction. Not used and should be defaulted with 1*. | 1* |
| 16 | WGASRATE | Wet gas production rate used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 17 | CALRATE | Calorific production rate used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 18 | GASFRAC | Surface gas production fraction used in the commercial compositional simulator Not used and should be defaulted with 1*. | 1* |
| 19 | WATFRAC | Surface water production fraction used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 20 | COMBRATE | Linearly combined production rate used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 21 | COMBPROC | Linearly combined procure for when exceeding COMBRATE, used in the commercial black-oil simulator. Not used and should be defaulted with 1*. | 1* |
| Notes: |  |  |  |

*Table 12.3.89.1: GCONPROD Keyword Description*


See also the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword to define the hierarchy of the groups below the FIELD level, the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword to define a group’s injection targets and constraints, the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword to define a production well’s targets and constraints, and the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword to define an injection well’s targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.


#### Example

The following example defines the production targets and constraints for the field and two groups that are one level below the field group, since the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword has not been entered to define the group  hierarchy.


```
--
--       GROUP PRODUCTION CONTROLS
--
-- GRUP  CNTL  OIL    WAT    GAS    LIQ    CNTL  GRUP  GUIDE  GUIDE  CNTL
-- NAME  MODE  RATE   RATE   RATE   RATE   OPT   CNTL  RATE   DEF    WAT
GCONPROD
FIELD    ORAT  40E3   60E3   300E3  60E3   1*     1*    1*     1*     1*      /
GRP01    FLD   25E3   1*     1*     1*     1*     1*    1*     1*     1*      /
GRP02    FLD   25E3   1*     1*     1*     1*     1*    1*     1*     1*      /
/
```


All groups are controlled by oil rate targets or constraints, but only the field level has water, gas and liquid constraints to reflect the actual production facility constraints. The wells under group control will be produced based on oil potential of each of the wells under group control, such that the field oil production target of 40,000 stb/d is honored and subject to the other phase fluid constraints.  In addition, GRP01 and GRP02 oil rate values of 25,000 stb/d are constraints as these two groups are subject to the FIELD level targets and constraints.
