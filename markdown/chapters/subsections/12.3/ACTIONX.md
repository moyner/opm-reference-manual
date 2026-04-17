### ACTIONX – Define Action Conditions and Command Processing


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword defines a series of conditions that invoke run time processing of [ACTION](#__RefHeading___Toc148342_63720426) functions and is similar to executing a run time script. This is the general purpose version of the [ACTION](#__RefHeading___Toc148342_63720426) series of keywords that can apply Boolean conditional tests to variables at the field, group, region, well segment and well levels. The [ACTION](#__RefHeading___Toc148342_63720426), [ACTIONG](#__RefHeading___Toc152219_2992482751), [ACTIONR](#__RefHeading___Toc152221_2992482751), [ACTIONS](#__RefHeading___Toc152223_2992482751) and [ACTIONW](#__RefHeading___Toc152225_2992482751) keywords are not implemented in OPM Flow and are unlikely to be so, as the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword implements their functionality with greater flexibility.

This keyword starts the definition of an [ACTIONX](#__RefHeading___Toc152227_2992482751) section that stipulates the Boolean conditions to test and the resulting [SCHEDULE](#__RefHeading___Toc43945_784232322) keywords to be executed if the Boolean condition evaluates to true.  An [ACTIONX](#__RefHeading___Toc152227_2992482751) Definition Section is terminated by an [ENDACTIO](#__RefHeading___Toc109407_332691817) keyword on a separate single line.

Although this keyword is read by OPM Flow and the [ACTION](#__RefHeading___Toc148342_63720426) and [UDQ](#__RefHeading___Toc161095_2932703077) computational logic and calculations have been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword enables the user to implement complex functionality and therefore it is advisable to start with simple expressions before adding the desired complexity.

See also the [PYACTION](#__RefHeading___Toc393199_4211536922) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that implements OPM Flow’s Python scripting facility using the standard Python scripting language.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| ACTIONX | Define the start of [ACTIONX](#__RefHeading___Toc152227_2992482751) Definition Section.  This is then followed on a new line by any number of [ACTIONX](#__RefHeading___Toc152227_2992482751) records that define the conditions for which the defined action will be executed and the various operations to be performed if the conditions are satisfied. |  |  |
| 1-1 | ACTNAME | ACTNAME is a character sting of up to eight characters in length, that defines the name of this action definition. If ACTNAME has previously been used by any [ACTION](#__RefHeading___Toc148342_63720426) series keyword, then the previous [ACTION](#__RefHeading___Toc148342_63720426) series definition will be replaced by the definition declared by this [ACTIONX](#__RefHeading___Toc152227_2992482751) Definition Section. |  |
| 1-2 | ACTNSTEP | ACTNSTEP is a positive integer that defines the number times that the ACTNAME definition is executed.  [ACTIONX](#__RefHeading___Toc152227_2992482751) definitions are activated at the end of a time step and this parameter is used to set how many time steps the ACTNAME definition will be invoked. The default value of one means that the definition will be executed only once. Use a large value, for example 10,000 for the definition to be executed at every time step. Note that the counter only affects successful evaluations; i.e. if ACTNSTEP is set equal to one (the default), then the simulator will test the action at the end of every time step until it evaluates to true. | 1 |
| 1-3 | ACTDELTA | ACTDELTA is a real positive value that defines the minimum duration of time after the conditions defined on the second record have been satisfied before the [ACTIONX](#__RefHeading___Toc152227_2992482751) actions are executed.  For example, if ACTDELTA is defaulted the actions will be executed at the end of the time step for which the conditions are met.  If set to say 30, then a minimum of 30 days will pass before the actions are executed (assuming field or metric units). | 0.0 |
| days | days | hours |  |
| 1-4 | / | Record terminated by a “/” | Not Applicable |
| 2-1 | ACTLHS | ACTLHS is a series of character strings, each up to eight characters in length, that defines a constant, [UDQ](#__RefHeading___Toc161095_2932703077) defined value, or a [SUMMARY](#__RefHeading___Toc43949_784232322) variable on the left hand side of a Boolean conditional test. The format for ACTLHS is dependent on the [SUMMARY](#__RefHeading___Toc43949_784232322) variable type: Aquifer, Block, Field, Group, Region, Time, Well, Well Connection, Well Local Grid Refinement Connection, or a Well Segment. In addition to [SUMMARY](#__RefHeading___Toc43949_784232322) variables, an [UDQ](#__RefHeading___Toc161095_2932703077) defined value or a Constant variable can be used.  The format for the various data types is given in Table 12.7. | Not Applicable |
| 2-2 | ACTTEST | ACTTEST is a defined character string that states the Boolean operator and must be set to one of the following Boolean conditionals: For example to test if the field’s gas production rate is less than 600 MMscf/d then one would use: ACTIONX PHASE2       1               / GGPR  'FIELD' < 600E3        / / ... ENDACTIO | Not Applicable |
| 2-3 | ACTRHS | ACTRHS is a numeric value or a series of character strings, each up to eight characters in length, that defines a constant, an [UDQ](#__RefHeading___Toc161095_2932703077) defined value, or a [SUMMARY](#__RefHeading___Toc43949_784232322) variable on the right hand side of a Boolean conditional test, as outlined in Table 12.7 (see also ACTLHS). In the case of well quantities the set of matching wells is captured and can be used as a general "well list" with the symbol '?' in subsequent well keywords. For example, to shut-in all oil producing wells (‘OP*’) with a water cut greater than 90% for every time the field water production rate exceeds 60,000 stb/d one would use: ACTIONX MXWATER      10000           / GWPR  'FIELD' > 60E3  AND    / WWCT  'OP*'   > 0.90         / / -- WELL PRODUCTION STATUS -- --  WELL    WELL   --LOCATION--  COMPLETION --  NAME    STAT     I   J    K  FIRST LAST WELOPEN '?'         SHUT                           / / ENDACTIO | Not Applicable |
| 2-4 | ANDOR | An optional defined character string that specifies a Boolean operator that must be set to either AND or OR if included on this record, that links this record with additional records of this type. For example, to test if the field’s gas production rate is less than 600 MMscf/d after 2020 then one would use: ACTIONX PHASE2       1               / GGPR  'FIELD' < 600E3 AND    / YEAR > 2020                  / / ... ENDACTIO This item should be left blank if not required. | Not Applicable |
| 2.5 | / | Termination of an [ACTIONX](#__RefHeading___Toc152227_2992482751) Boolean condition record. Note that multiple numbers of records of this type can be entered with each record terminated by a “/”, as illustrated above. | Not Applicable |
| 3-1 | / | The Boolean condition section of the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword is terminated by an empty line with a single “/”. | Not Applicable |
|  |  | The next section contains any number of standard [SCHEDULE](#__RefHeading___Toc43945_784232322) keywords that will be executed if the Boolean expression evaluates to true.  For example, to test if the field’s gas production rate is less than 600 MMscf/d after 2020 and to open up additional wells if this occurs, then one would use: ACTIONX PHASE2       1               / GGPR  'FIELD' < 600E3 AND    / YEAR > 2020                  / / -- WELL PRODUCTION STATUS -- --  WELL    WELL   --LOCATION--  COMPLETION --  NAME    STAT     I   J    K  FIRST LAST WELOPEN GP10        OPEN                           / GP11        OPEN                           / / ENDACTIO In theory, most [SCHEDULE](#__RefHeading___Toc43945_784232322) keywords can be used in an [ACTIONX](#__RefHeading___Toc152227_2992482751) Definition Section here, except for the time stepping keywords, i.e, [TSTEP](#__RefHeading___Toc118323_1596574740) and [DATES](#__RefHeading___Toc117621_2179381650). See Table 12.8 for a list of the [SCHEDULE](#__RefHeading___Toc43945_784232322) keywords that are known to work with the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword. | Not Applicable |
| [ENDACTIO](#__RefHeading___Toc109407_332691817) | Define the end of [ACTIONX](#__RefHeading___Toc152227_2992482751) Definition Section. | Not Applicable |  |
| Notes: |  |  |  |

*Table 12.6: ACTIONX Keyword Description*


The variable types and the associated definitions that are available for use with Boolean conditionals are outlined in Table 12.7.


| Variable Type | Description |
| --- | --- |
| AQUIFER | AQUIFER variable consists of two parameters: |
| BLOCK | BLOCK variable consists of four parameters: The NX, NY, and NZ parameters are defined on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. |
| CONSTANTS | CONSTANTS can consist of one or optionally two parameters: |
| FIELD | The FIELD variable consists of any field [SUMMARY](#__RefHeading___Toc43949_784232322) variable; for example the Field average Pressure, as shown below: ACTIONX WIPHASE       1               / FPR < 2500                    / / ... ENDACTIO The above would action a set of [SCHEDULE](#__RefHeading___Toc43945_784232322) keywords if the field average pressure fell below 2,500 psia for a run using [FIELD](#__RefHeading___Toc71850_2267116897) units. |
| GROUP | GROUP variable definition consists of: To enable an action for when the field’s oil production rate drops below 20,000 stb/d then one could use. ACTIONX OILMIN        1               / GOPR  'FIELD' < 20.0E3        / / ... ENDACTIO |
| REGION | REGION variable definition consists of: For example, ACTIONX WIPHASE       1               / RPR 0 < 2500                  / / ... ENDACTIO Would action a set of [SCHEDULE](#__RefHeading___Toc43945_784232322) keywords if the field average pressure fell below 2,500 psia for a run using [FIELD](#__RefHeading___Toc71850_2267116897) units. |
| TIME | TIME variable definition consists of one parameter that can have three values: DAY for the current simulation day of the month, MNTH for the current simulation month, and YEAR for the current simulation year. Thus, to set an action for April 1, 2025 one would use: ACTIONX ACT01    1                     / DAY  = 1              AND    / MNTH ='APR'           AND    / YEAR = 2025                  / / ... ENDACTIO Note that the value for the MNTH variable,  ‘APR’, in the example, can also be entered without the quotes, that is: MNTH = APR            AND    / In addition, numerical values for MNTH, similar to DAY and YEAR, are also permitted and are converted to the nearest integer for comparison, so for example: ACTIONX ACT01    1                     / DAY  = 0.95           AND    / MNTH = 4.40           AND    / YEAR = 2024.9                / / ... ENDACTIO Would again result in the action taking place on April 1, 2025. |
| WELL | WELL variable definition consists of: Note that the use of well lists is an OPM Flow specific feature. To reduce the tubing head pressure constraint for when any of the oil producers’ oil rate drop below 100 stb/d then one could use. ACTIONX WOILMIN       1               / WOPR  'OP*'   < 100.0         / / -- -- FLOW WELLS THROUGH LOW PRESSURE SEPARATOR -- --  WELL    WELL   TARGET --  NAME    TARG   VALUE WELTARG 'OP*'       THP     150             / / ENDACTIO |
| WELL CONNECTION | WELL CONNECTION variable definition is comprised of: The NX, NY, and NZ parameters are defined on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. |
| WELL COMPLETION | WELL COMPLETION variable definition is comprised of: |
| WELL LOCAL GRID REFINEMENT CONNECTION | WELL LOCAL GRID REFINEMENT CONNECTION variable definition is comprised of: The NX, NY, and NZ parameters are defined on either the [CARFIN](#__RefHeading___Toc150726_63720426) or [RADFIN](#__RefHeading___Toc76871_718313858) keywords in the [GRID](#__RefHeading___Toc38674_784232322) section depending upon whether a Cartesian or radial local grid refinement is being utilized. Note Local Grid Refinements are currently not implemented in OPM Flow. |
| WELL SEGMENT | WELL SEGMENT variable definition consists of: Note that the total number of wells should be defined via the WELLSDIMS keyword and the number of multi-segment wells should be declared on the [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword, both keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. |

*Table 12.7: ACTIONX Variable Definitions*


See also the [ACTDIMS](#__RefHeading___Toc4408_421927891) and [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to define the dimensions for the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword and associated variables. In addition, the [EXIT](#__RefHeading___Toc627737_1466963378) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that allows for terminating the simulation for when a condition within an [ACTIONX](#__RefHeading___Toc152227_2992482751) definition is satisfied.

Although most [SCHEDULE](#__RefHeading___Toc43945_784232322) keywords should work with the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword, Table 12.8 shows the status of keywords that have been tested and known to work, together with keywords that are currently planned to be implemented.


| ACTIONX Schedule Section Keywords Status |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Action Keywords | Group Keywords | Well Keywords | Connection Keywords | Miscellaneous Keywords |  |
| [ACTIONX](#__RefHeading___Toc152227_2992482751) | [GCONINJE](#__RefHeading___Toc134874_2055188184) | [WCONHIST](#__RefHeading___Toc134880_2055188184) | [WPIMULT](#__RefHeading___Toc121645_2412586160) | [COMPDAT](#__RefHeading___Toc97651_3261743917) | [BOX](#__RefHeading___Toc42110_3671211675) |
| [UDQ](#__RefHeading___Toc161095_2932703077) | [GCONPROD](#__RefHeading___Toc146746_4203985108) | [WCONINJE](#__RefHeading___Toc146750_4203985108) | [WSEGVALV](#__RefHeading___Toc1091865_4263943340) | [COMPLUMP](#__RefHeading___Toc97655_3261743917) | [BRANPROP](#__RefHeading___Toc162078_289573908) |
|  | [GCONSUMP](#__RefHeading___Toc188037_2026549522) | [WCONINJH](#__RefHeading___Toc146752_4203985108) | [WTEST](#__RefHeading___Toc121925_2556401936) | [COMPSEGS](#__RefHeading___Toc316604_3519154785) | [ECHO](#__RefHeading___Toc52483_2479612490) |
|  | [GEFAC](#__RefHeading___Toc268455_1366622701) | [WCONPROD](#__RefHeading___Toc146754_4203985108) | [WTMULT](#__RefHeading___Toc1141674_4263943340) |  | [ENDBOX](#__RefHeading___Toc88719_1778172979) |
|  | [GLIFTOPT](#__RefHeading___Toc111805_332691817) | [WDFAC](#__RefHeading___Toc442057_2026549522) |  |  | [EXIT](#__RefHeading___Toc627737_1466963378)5 |
|  | [GRUPNET](#__RefHeading___Toc118319_1596574740) | [WECON](#__RefHeading___Toc134884_2055188184) |  |  | [INCLUDE](#__RefHeading___Toc55749_2479612490)7 |
|  | [GRUPTARG](#__RefHeading___Toc196552_870710203) | [WEFAC](#__RefHeading___Toc48856_327352552) |  |  | [MULTX](#__RefHeading___Toc80283_1778172979) |
|  | [GRUPTREE](#__RefHeading___Toc118321_1596574740) | [WELOPEN](#__RefHeading___Toc268461_1366622701) |  |  | [MULTX-](#__RefHeading___Toc80285_1778172979) |
|  | [GSATINJE](#__RefHeading___Toc116596_332691817) | [WELPI](#__RefHeading___Toc121389_332691817) |  |  | [MULTY](#__RefHeading___Toc80287_1778172979) |
|  | [GSATPROD](#__RefHeading___Toc202038_870710203) | [WELSEGS](#__RefHeading___Toc97661_3261743917) |  |  | [MULTY-](#__RefHeading___Toc80289_1778172979) |
|  |  | [WELSPECS](#__RefHeading___Toc268463_1366622701)6 |  |  | [MULTZ](#__RefHeading___Toc80291_1778172979) |
|  |  | [WELTARG](#__RefHeading___Toc134888_2055188184) |  |  | [MULTZ-](#__RefHeading___Toc80293_1778172979) |
|  |  | [WGRUPCON](#__RefHeading___Toc121641_2412586160) |  |  | [NEXT](#__RefHeading___Toc117629_2179381650) |
|  |  | [WINJMULT](#__RefHeading___Toc121402_332691817) |  |  | [NEXTSTEP](#__RefHeading___Toc323446_1841740821) |
|  |  | [WLIST](#__RefHeading___Toc179534_3325167686) |  |  | [NOECHO](#__RefHeading___Toc52487_2479612490) |
| Notes: |  |  |  |  |  |

*Table 12.8: ACTIONX Schedule Section Keywords Status*


As mentioned previously, the [UDQ](#__RefHeading___Toc161095_2932703077) keyword stipulates the variables and operations used to access the User Defined Quantities features in OPM Flow. [UDQ](#__RefHeading___Toc161095_2932703077) variables can be constants, [SUMMARY](#__RefHeading___Toc43949_784232322) variables, as defined in the [SUMMARY](#__RefHeading___Toc43949_784232322) section, or a formula using various mathematical functions together with constants and [SUMMARY](#__RefHeading___Toc43949_784232322) variables.


| Note Within an [ACTIONX](#__RefHeading___Toc152227_2992482751) Definition Section any [UDQ](#__RefHeading___Toc161095_2932703077) variables utilizing group and well variables, must have their associated groups and wells previously fully defined in the commercial simulator, otherwise an error will occur. For example, if a well’s GOR is being used as part of a [UDQ](#__RefHeading___Toc161095_2932703077) definition, then the well must be fully characterized prior to declaring the [UDQ](#__RefHeading___Toc161095_2932703077) definition. This restriction does not apply to OPM Flow; however, it should be considered if the same deck is to be run with both simulators. |
| --- |


User Defined Quantities can also be used as User Defined Arguments (“UDA”) in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section with various group, well, and connection keywords. In this case, the UDA variables are used to replace numerical values on these keywords by UDA variables that have been defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword.  For example, if we wish to make the oil rate for certain wells to be a function of their water cut, then one can define the function using the [UDQ](#__RefHeading___Toc161095_2932703077) keyword that results in a [UDQ](#__RefHeading___Toc161095_2932703077) variable, WU_OPR say, and then use WU_OPR as a UDA variable on the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword for the ORAT parameter.  See Table 12.76 for a list of keywords that can be used with UDA variables in the [UDQ - Declare User Define Quantities (“UDQ”)](#12.3.59.UDQ - Declare User Define Quantities (“UDQ”)|outline) keyword section.


#### Examples

The first example uses the [UDQ](#__RefHeading___Toc161095_2932703077) keyword to sort the oil wells from high water cut to low, via the WU_WLIST variable, and then use the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword to shut-in the worst offending well when the field’s water production is greater than 30,000 stb/d.


```
--
--      DEFINE START OF USER DEFINED QUANTITY SECTION
--
UDQ
--
--      OPERATOR VARIABLE  EXPRESSION
--
DEFINE  WU_WCUT   WWCT 'OP*'                        / WELL WWCT LIST
DEFINE  WU_LIST   SORTD(WU_WCUT)                    / WELL WWCT LIST SORTED
/                                                     END OF UDQ SECTION
--
--      DEFINE START OF ACTIONX SECTION
--
ACTIONX
        WSHUTIN        10                                                        /
        GWPR  'FIELD' > 30E3  AND                                              /
        WU_LIST 'OP*' = 1                                                      /
/

--
--      DEFINE WELL AND WELL CONNECTIONS FLOWING STATUS
--
--  WELL WELL   --LOCATION--  COMPLETION
--  NAME STAT     I   J    K  FIRST LAST
WELOPEN
'?'      SHUT                                                                  /
'?'      SHUT     0   0    0     0     0                                       /
/

ENDACTIO

```

Apart from checking that the field’s water production rate is greater than 30,000 stb/d the Boolean conditional also checks that there is at least one well in the sorted well list. Notice also the use of ‘?’ symbol as a substitution of the well name and that the [ACTIONX](#__RefHeading___Toc152227_2992482751) WSHUTIN series of commands will be executed a total of ten times.

The second example checks to see if the field’s gas rate is below 600 MMscf/d and if the simulation time is greater that July 1, 2030. If it is, then compression is installed by re-setting all the gas producing well’s THP and BHP pressures to 450 psia and 300 psia respectively. In addition all gas wells currently shut-in are tested to see if they can be opened up under the new THP and BHP constraints.


```
--
--      START ACTIONX FIELD PHASE-3 AUTOMATIC COMPRESSION
--
ACTIONX
        PHASE-3      1                                                         /
        GGPR  'FIELD' < 600E3 AND                                              /
        DAY           >= 1     AND                                             /
        MNTH          >= JUL   AND                                             /
        YEAR          >= 2030                                                  /
/

--
--      INSTALL COMPRESSION AND RESET WELL THP AND BHPS
--
--  WELL    WELL   TARGET
--  NAME    TARG   VALUE
WELTARG
'GP*'       THP     450                                                        /
'GP*'       BHP     300                                                        /
/

--
--      TEST AND OPEN ALL WELLS UNDER COMPRESSION CONSTRAINTS
--
--  WELL    TEST   CLOSE   NO.     START
--  NAME    INTV   CHECK   CHECK   TIME
WTEST
'GP*'       1.0    PE      1       3                                           /
/

--
--      END OF ACTIONX FIELD PHASE-3 AUTOMATIC COMPRESSION DEFINITION
--
ENDACTIO


```
