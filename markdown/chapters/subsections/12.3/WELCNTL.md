### WELCNTL – Modify Well Control and Targets


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WELCNTL keyword modifies a well’s target control and value, both rates and pressures, for previously defined wells without having to define all the variables on the well control keywords: WCONPROD, WCONHIST, WCONINJE, or WCONINJH keywords. Variables not changed by the WELCNTL keyword remain the same as those previously entered via the well control keywords or previously entered WELCNTL keywords. Note that the well must still be initially be fully defined using the WCONPROD or WCONINJE keywords. All the aforementioned keywords are described in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well production rates and pressures data are being redefined. Note that the well name (WELNAME) must have been declared previously using the WELSPECS and WCONPROD (or WCONINJE) keywords in the SCHEDULE section, otherwise an error may occur. | None |
| 2 | TARGET | A defined character string that sets the item to be changed for the well the value of the item is set by item (3). | None |
| 3 | VALUE Liquid Gas Res Vol Pressure VFP LIFT | A real positive value that defines the value of the variable declared by TARGET | None |
| stb/d Mscf/d rb/d psia dimensionless same as VFPPROD or VFPINJ | sm3/day sm3/day rm3/day barsa dimensionless same as VFPPROD or VFPINJ | scc/hour scc/hour rcc/hour atma dimensionless same as VFPPROD or VFPINJ |  |
| Notes: |  |  |  |

*Table 12.85: WELCNTL Keyword Description*


If a well is currently a history matching well, then WELCNTL can be used to change the well to a standard well. See also the WELTARG keyword, in the SCHEDULE section that can be used to reset a well’s target and constraints of both rates and pressures.


#### Example

The following example below shows the oil rates for the OP01 oil producer at the start of the schedule section (January 1, 2000).


```
-- ------------------------------------------------------------------------------
-- 01 JAN 2000 START OF SCHEDULE SECTION
-- ------------------------------------------------------------------------------
--
--       WELL PRODUCTION WELL CONTROLS
--
-- WELL  OPEN/  CNTL   OIL    WAT    GAS   LIQ    RES    BHP    THP   VFP    VFP
-- NAME  SHUT   MODE   RATE   RATE   RATE  RATE   RATE   PRES   PRES  TABLE  ALFQ
WCONPROD
OP01     OPEN   ORAT   3000   1*     1*    1*     1*     750.0  500.  9      1* /
/                                                                               DATES
01 FEB 2000 /
/
--
--       WELL CONTROL MODE AND OPERATING TARGET
--
--  WELL WELL   TARGET
--  NAME CNTL   VALUE                                                        WELCNTL
OP01     LRAT   5000                                        /
/
```

From January 1, 2000 to February 1, 2000 well OP01 is open and is on oil rate control and has a target oil rate of 3,000 stb/d and uses VFPPROD vertical lift table number 9 with a minimum tubing head pressure constraint of 500 psia. After February 1, 2000 the well is changed to liquid control with a target rate of 5,000 stb/d of liquid and all the other parameters remain unchanged.
