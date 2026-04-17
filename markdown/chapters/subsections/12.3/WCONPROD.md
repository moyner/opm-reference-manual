### WCONPROD – Define Well Production Targets and Constraints


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WCONPROD keyword defines production targets and constraints for wells that have previously been defined by the WELSPECS keyword in the SCHEDULE section. Note that wells can be allocated to a group when they are specified by the WELSPECS keyword.  Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells using this keyword.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well production targets and constraints data are being defined. Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 2 | STATUS | A defined character string that declares the status of the well. STATUS should be set to one of the following character strings: Note a well’s STATUS should always be set either STOP or SHUT if the well’s production is to be set to zero. Just setting a well’s production rate to zero means that the well is open to flow with a zero rate, this will cause numerical issues especially for wells under THP control. | OPEN |
| 3 | TARGET | A defined character string that sets the target production phase for the well, all the other phases will therefore act as constraints. The simulator will attempt to meet the TARGET based on the phase rate stated in items (4) to (10) on this keyword. TARGET should be set to one of the following character strings: Here the default tokens of 1* or '' may be used, and both default tokens behave in the same manner; however, the actual default value used when TARGET is defaulted is dependent on the data entered on this keyword as described below: Note the default value of one atmosphere should be avoided as the BHP will result in unrealistic well potentials as well as optimistic production forecasts for the well. | 1* |
| 4 | ORAT | A real positive value that defines the maximum surface oil production rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| stb/day | sm3/day | scc/hour |  |
| 5 | WRAT | A real positive value that defines the maximum surface water production rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| stb/day | sm3/day | scc/hour |  |
| 6 | GRAT | A real positive value that defines the maximum surface gas production rate target or constraint This value may be specified using a User Defined Argument (UDA). | None |
| Mscf/day | sm3/day | scc/hour |  |
| 7 | LRAT | A real positive value that defines the maximum surface liquid (oil plus water) production rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| stb/day | sm3/day | scc/hour |  |
| 8 | RESV | A real positive value that defines the maximum reservoir volume production rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| rtb/day | rm3/day | rcc/hour |  |
| 9 | BHP | A real positive value that defines the minimum bottom-hole pressure target or constraint. This value may be specified using a User Defined Argument (UDA). Note the default value of one atmosphere should be avoided as the BHP will result in unrealistic well potentials as well as optimistic production forecasts for the well. | Defined |
| psia 14.70 | barsa 1.01325. | atma 1.0 |  |
| 10 | THP | A real positive value that defines the minimum tubing head pressure target or constraint. This value may be specified using a User Defined Argument (UDA). Note the default value of zero should be avoided if the well’s control TARGET has been set to THP, as this will result in optimistic production forecasts for a well, since a well must flow against a back pressure imposed by the surface facilities. | Defined |
| psia 0.0 | barsa 0.0 | atma 0.0 |  |
| 11 | VFPTAB | A positive integer greater than or equal to zero that defines the vertical lift performance tables to be used for calculating the tubing head pressure for the well. If a non-zero value is entered then the vertical lift performance tables must be entered via the VFPPROD keyword in the SCHEDULE section and allocated to the well via this item. The default value of zero implies no vertical lift performance tables and in this case TARGET cannot be set to THP and in addition item (10) should be defaulted or set to zero. | 0 |
| 12 | ALQ-WELL | A real positive value that defines the artificial lift quantity to be used in conjunction with the VFPPROD assigned to the well via the VFPTAB variable. This value may be specified using a User Defined Argument (UDA). VFPTAB vertical lift performance table and the artificial lift quantity ALQ-WELL are used with the well fluid rates to calculate the well’s tubing head pressures values from the bottom-hole pressure. Note that the units for ALQ-WELL are dependent on the associated variable on the VFPPROD keyword. | 0.0 |
| 13 | WGASRATE | Wet gas production rate used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 14 | MOLARATE | Total molar rate used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 15 | STEAMRAT | Thermal/Temperature steam rate (Cold Water Equivalent) for steam producers used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 16 | DELTAP | Thermal/Temperature delta pressure offset for steam producers used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 17 | DELTAT | Thermal/Temperature delta temperature offset for steam producer used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 18 | CALRATE | Calorific production rate used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 19 | COMBPROC | Linearly combined procedure for when exceeding COMBRATE, used in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| 20 | NGL | A real positive value that defines the observed Natural Gas Liquid (“NGL”) rate in the commercial compositional simulator. Not used and should be defaulted with 1*. | 1* |
| Notes: |  |  |  |

*Table 12.80: WCONPROD Keyword Description*


See also the GCONPROD and GCONINJE keywords to define a group’s production and injection targets and constraints, and the WCONINJE keyword to define an injection well’s targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.


#### Example

The following example defines the production targets and constraints for five wells as follows:


```
--
--       WELL PRODUCTION WELL CONTROLS
--
-- WELL  OPEN/  CNTL  OIL   WAT   GAS   LIQ    RES    BHP    THP   VFP    VFP
-- NAME  SHUT   MODE  RATE  RATE  RATE  RATE   RATE   PRES   PRES  TABLE  ALFQ
WCONPROD
OP01     OPEN   GRUP  5E3   1*     1*    1*    1*     500.0                    /
OP02     OPEN   GRUP 10E3   1*     1*    1*    1*     200.0  500.0  2     0.0  /
OP03     OPEN   GRUP 15E3   1*     1*    1*    1*     200.0  500.0  3    10.0  /
OP04     OPEN   ORAT 20E3   1*     1*    1*    1*     500.0                    /
OP05     SHUT   GRUP 20E3   1*     1*    1*    1*     500.0                    /
/
```

Well OP01 is open and is on group control, subject to a maximum oil rate constraint of 5,000 stb/d and a minimum bottom-hole pressure of 500 psia. OP02 is also open and on group control but it’s maximum oil rate constraint has been set 10,000 stb/d, and is subject to a minimum bottom-hole pressure limit of 200 psia and a minimum tubing head pressure limit of 500 psia using VFPPROD vertical lift table number two. Well OP03 is very similar to OP02, but with a 15,000 stb/d maximum oil constraint and using VFPPROD vertical lift table number three with an artificial lift parameter of 10. The next well is not on group control. Well OP04 is open and has an oil rate target of 20,000 stb/d, subject to a minimum bottom-hole pressure of 500 psia.  Finally, well OP05 is shut and will not be brought back on production despite being put under group control, as the well has been declared shut.


The next example defines the production targets and constraints for five wells, of which well OP01 is under group control as the well’s group target and constraints have been set with the GCONPROD keyword, and wells OP02 to OP05 belong to groups that have not had their group constraints set by GCONPROD.


```
--
--       GROUP PRODUCTION CONTROLS
--
-- GRUP  CNTL  OIL    WAT    GAS    LIQ    CNTL  GRUP  GUIDE  GUIDE  CNTL
-- NAME  MODE  RATE   RATE   RATE   RATE   OPT   CNTL  RATE   DEF    WAT
GCONPROD
GRP01    SAT   25E3   1*     1*     1*     1*     1*    1*     1*     1*       /
/
--
--       WELL SPECIFICATION DATA
--
-- WELL  GROUP     LOCATION  BHP    PHASE  DRAIN  INFLOW  OPEN  CROSS  PVT
-- NAME  NAME        I    J  DEPTH  FLUID  AREA   EQUANS  SHUT  FLOW   TABLE
WELSPECS
OP01     SAT        14   13   1*     OIL    1*     P-P    SHUT   NO     1*     /
0P02     PLATFORM   64   80   1*     OIL    1*     GPP    SHUT   NO     1*     /
OP03     PLATFORM   24  110   1*     OIL    1*     STD    SHUT   NO     1*     /
OP04     PLATFORM   24  110   1*     OIL    1*     STD    SHUT   NO     1*     /
OP05     PLATFORM   24  110   1*     OIL    1*     STD    SHUT   NO     1*     /
/
--
--       WELL PRODUCTION WELL CONTROLS
--
-- WELL  OPEN/  CNTL  OIL   WAT   GAS   LIQ    RES    BHP    THP   VFP    VFP
-- NAME  SHUT   MODE  RATE  RATE  RATE  RATE   RATE   PRES   PRES  TABLE  ALFQ
WCONPROD
OP01     OPEN   1*   15E3    1*    1*    1*    1*     500.0                    /
OP02     OPEN   1*    1*    5E3*  15E6   1*    1*     200.0  500.0  2      0.0 /
OP03     OPEN   1*    1*     1*    1*    1*    1*     1*     500.0  3     10.0 /
OP04     OPEN   ''    1*     1*    1*    1*    1*     1*     1*     1*     1*  /
OP05     SHUT   1*    1*     1*    1*    1*    1*     1*     1*     1*     1*  /
/
```

Here,  well OP01’s control mode, TARGET, will be set to group control (GRUP) and the well’s production parameters will all act as constraints.  For well OP02, the well’s control mode is set to GRAT, and the other production parameters all act as constraints.  Well OP03 control mode is set to THP and if the well’s BHP value has been previously defined then that value will be used as a constraint; otherwise the default value of one atmosphere will be used instead. Finally, wells OP04 and OP05 will have their control mode set to BHP control. Note in this case, OP04’s status has been set to OPEN; thus the well will produce at a target BHP of one atmosphere, which is unrealistic.
