### GRUPTARG – Modify Group Targets and Constraints Values


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GRUPTARG keyword modifies the target and constraints values of both rates and pressures for previously defined groups without having to define all the variables on the group control keywords: GCONPROD or GCONPRI keywords. Variables not changed by the GRUPTARG keyword remain the same as those previously entered via the group control keywords or previously entered GRUPTARG keywords. Note that the group must still be initially be fully defined using the GCONPROD or GCONPRI keywords.  All the aforementioned keywords are described in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

Note that wells are allocated to groups when the wells are specified by the WELSPECS keyword in the SCHEDULE section.  Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field. Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| 2 | TARGET | A defined character string that sets the item to be changed for the group the value of the item is set by item (3). | None |
| 3 | VALUE Liquid Gas Res Vol Pressure | A real positive value that defines the value of the variable declared by TARGET | None |
| stb/d Mscf/d rb/d psia | sm3/day sm3/day rm3/day barsa | scc/hour scc/hour rcc/hour atma |  |
| Notes: |  |  |  |

*Table 12.43: GRUPTARG Keyword Description*


See also the WELTARG and WELCNTL keyword, in the SCHEDULE section that can be used to reset a well’s control mode, as well as a well’s target and constraints of both rates and pressures.


#### Example

The following example below shows the oil rates for the field at the start of the schedule section (January 1, 2000).


```
-- ------------------------------------------------------------------------------
-- 01 JAN 2000 START OF SCHEDULE SECTION
-- ------------------------------------------------------------------------------
--
--       GROUP PRODUCTION CONTROLS
--
-- GRUP  CNTL  OIL    WAT    GAS    LIQ    CNTL  GRUP  GUIDE  GUIDE  CNTL
-- NAME  MODE  RATE   RATE   RATE   RATE   OPT   CNTL  RATE   DEF    WAT
GCONPROD
FIELD    ORAT  40E3   60E3   30E3   65E3   1*     1*    1*     1*     1*      /
/                                                                               DATES
01 FEB 2000 /
/
--
--       GROUP PRODUCTION AND INJECTION TARGETS
--
--       GROUP    GROUP  TARGET
--       NAME     TARG   VALUE
GRUPTARG
         FIELD    ORAT   45E3                                                  /
         FIELD    LIQ    75E3                                                  /
/
```


From January 1, 2000 to February 1, 2000 the field is on oil rate control and has a target oil rate of 40,000 stb/d, a maximum water handling capacity of 60,000 stb/d, a maximum liquid capacity of 65,000 stb/d, and a maximum gas constraint of 30 MMscf/d. After February 1, 2000 the field’s target oil rate is increased to 45,000 stb/d and the maximum liquid constraint is increased to 75,000 stb/s; all the other parameters remain unchanged.
