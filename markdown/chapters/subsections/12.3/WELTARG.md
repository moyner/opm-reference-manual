### WELTARG – Modify Well Target and Constraint Values {#kw-WELTARG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WELTARG keyword modifies the target and constraints values of both rates and pressures for previously defined wells without having to define all the variables on the well control keywords: [WCONPROD](#kw-WCONPROD), [WCONHIST](#kw-WCONHIST), [WCONINJE](#kw-WCONINJE), or [WCONINJH](#kw-WCONINJH). Variables not changed by the  WELTARG keyword remain the same as those previously entered via the well control keywords or previously entered WELTARG keywords. Note that the well must still be initially fully defined using the [WCONPROD](#kw-WCONPROD) or [WCONINJE](#kw-WCONINJE) keywords.  All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well production rates and pressures data are being redefined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) and [WCONPROD](#kw-WCONPROD) (or [WCONINJE](#kw-WCONINJE)) keywords in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | TARGET | A defined character string that sets the item to be changed for the well the value of the item is set by item (3). The commercial compositional simulator options:  WGRA, NGL, CVAL, REIN, STRA, SATP and SATT are not applicable.  Note that TARGET only defines the variable to be changed, it does not change how a well is controlled. For example, if a well is operating on ORAT control, as defined by the previously entered [WCONPROD](#kw-WCONPROD) keyword, entering TARGET equal to LRAT with a value, changes the liquid constraint but the well still remains on ORAT control. Use the [WELCNTL](#kw-WELCNTL) keyword in the [SCHEDULE](#kw-SCHEDULE) section to change the control mode of a well. | None |
| 3 | VALUE Liquid Gas Res Vol Pressure VFP LIFT | A real positive value that defines the value of the variable declared by TARGET This value may be specified using a User Defined Argument (UDA). | None |
| stb/d Mscf/d rb/d psia dimensionless same as [VFPPROD](#kw-VFPPROD) or [VFPINJ](#kw-VFPINJ) | sm3/day sm3/day rm3/day barsa dimensionless same as [VFPPROD](#kw-VFPPROD) or [VFPINJ](#kw-VFPINJ) | scc/hour scc/hour rcc/hour atma dimensionless same as [VFPPROD](#kw-VFPPROD) or [VFPINJ](#kw-VFPINJ) |  |
| Notes: |  |  |  |
: WELTARG Keyword Description {#tbl-12-93}
If a well is currently a history matching well, then WELTARG should only be used to change a well's bottom-hole pressure limit, vertical flow performance table number or the artificial lift quantity.


See also the [WELCNTL](#kw-WELCNTL) keyword, in the [SCHEDULE](#kw-SCHEDULE) section that can be used to reset the control mode, as well as a well’s target and constraints of both rates and pressures.


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
--       WELL PRODUCTION AND INJECTION TARGETS
--
--  WELL WELL   TARGET
--  NAME TARG   VALUE
WELTARG
OP01     ORAT   2000                                        /
/
```

From January 1, 2000 to February 1, 2000 well OP01 is open and is on oil rate control and has a target oil rate of 3,000 stb/d, and uses [VFPPROD](#kw-VFPPROD) vertical lift table number 9 with a minimum tubing head pressure constraint of 500 psia. After February 1, 2000 the well’s oil rate is reduced to 2,000 stb/d and all the other parameters remain unchanged.