### WCONINJE – Well Injection Targets and Constraints {#kw-WCONINJE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WCONINJE keyword defines injection targets and constraints for wells that have previously been defined by the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section. Note that wells can be allocated to a group  when they are specified by the [WELSPECS](#kw-WELSPECS) keyword.  Wells defined to be under group control will have their injection rates controlled by the group to which they belong, in addition to any well constraints defined for the wells using this keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well injection targets and constraints data are being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | TYPE | A defined character string that defines the type of injection well. TYPE should be set to one of the following character strings: | None |
| 3 | STATUS | A defined character string that declares the status of the well. STATUS should be set to one of the following character strings: Note a well’s STATUS should always be set either STOP or SHUT if the well’s injection is to be set to zero. Just setting a well’s injection rate to zero means that the well is open for injection with a zero rate, this will cause numerical issues especially for wells under THP control. | OPEN |
| 4 | TARGET | A defined character string that sets the target injection control mode for the well. TARGET should be set to one of the following character strings: | None |
| 5 | RATE | A real positive value that defines the maximum surface injection rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| Liquid stb/d Gas Mscf/d | Liquid sm3/day Gas sm3/day | Liquid scc/hour Gas scc/hour |  |
| 6 | RESV | A real positive value that defines the maximum reservoir volume injection rate target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| rb/d | rm3/day | rcc/hour |  |
| 7 | BHP | A real positive value that defines the maximum bottom-hole pressure target or constraint. This value may be specified using a User Defined Argument (UDA). Note the default value basically means unlimited injection or no constraint and should therefore be avoided as the BHP will result in unrealistic well potentials as well as optimistic injection forecasts for the well. | Defined |
| psia 10,0000 | barsa 6,895 | atma 6,803 |  |
| 8 | THP | A real positive value that defines the maximum tubing head pressure target or constraint. This value may be specified using a User Defined Argument (UDA). | None |
| psia | barsa | atma |  |
| 9 | VFPTAB | A positive integer greater than or equal to zero that defines the vertical lift performance tables to be used for calculating the tubing head pressure for the well. If a non-zero value is entered then the vertical lift performance tables must be entered via the [VFPINJ](#kw-VFPINJ) keyword in the [SCHEDULE](#kw-SCHEDULE) section and allocated to the well via this item. The default value of zero implies no vertical lift performance tables and in this case TARGET cannot be set to THP and in addition item (10) should be defaulted or set to zero. | 0 |
| 10 | RSRVINJ | The dissolved gas-oil ratio in the injected oil, or the vaporized oil-gas ratio in the injected gas. | 0.0 |
| Gas Injection: stb/Mscf Oil Injection: Mscf/stb | Gas Injection: sm3/sm3 Oil Injection: sm3/sm3 | Gas Injection: scc/scc Oil Injection: scc/scc |  |
| 11 | RSSTEAM | Thermal/Temperature gas-steam ratio for steam-gas injectors. The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 12 | OILFRAC | Surface oil fraction in a multi-phase injector. The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 13 | WATFRAC | Surface water fraction in a multi-phase injector. The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 14 | GASFRAC | Surface gas fraction in a multi-phase injector. The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| 15 | OILSTEAM | Surface oil volume to steam volume ratio in a steam-oil injector. The parameter is ignored by OPM Flow and should be defaulted or set to the default value of zero. | 0.0 |
| Notes: |  |  |  |
: WCONINJE Keyword Description {#tbl-12-78}
See also the [GCONPROD](#kw-GCONPROD) and the [GCONINJE](#kw-GCONINJE) keywords to define a group’s production and injection targets and constraints, and the [WCONPROD](#kw-WCONPROD) keyword to define a production well’s targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

The following example defines the injection targets and constraints for one gas injection well and one water injection well as follows:


```
--
--       WELL INJECTION CONTROLS
--
-- WELL  FLUID  OPEN/  CNTL  SURF   RESV   BHP   THP   VFP
-- NAME  TYPE   SHUT   MODE  RATE   RATE   PRSES PRES  TABLE
WCONINJE
GI01     GAS    OPEN   GRUP  50E3   1*     1*     1*    1*  /
WI01     WAT    OPEN   RATE  25E3   1*     5000.  1*    1*  /
/

```

Well GI01 is a gas injection well directly under group control constrained by a maximum surface gas injection rate of 50 MMscf/d and well WI01 is an open water injection well with a surface water injection rate target of 25,000 stb/d, subject to a maximum bottom-hole pressure constraint 5,000 psia.