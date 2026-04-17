### ACTIONX – Define Action Conditions and Command Processing


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ACTIONX keyword defines a series of conditions that invoke run time processing of ACTION functions and is similar to executing a run time script. This is the general purpose version of the ACTION series of keywords that can apply Boolean conditional tests to variables at the field, group, region, well segment and well levels. The ACTION, ACTIONG, ACTIONR, ACTIONS and ACTIONW keywords are not implemented in OPM Flow and are unlikely to be so, as the ACTIONX keyword implements their functionality with greater flexibility.

This keyword starts the definition of an ACTIONX section that stipulates the Boolean conditions to test and the resulting SCHEDULE keywords to be executed if the Boolean condition evaluates to true.  An ACTIONX Definition Section is terminated by an ENDACTIO keyword on a separate single line.

Although this keyword is read by OPM Flow and the ACTION and UDQ computational logic and calculations have been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the ACTIONX keyword enables the user to implement complex functionality and therefore it is advisable to start with simple expressions before adding the desired complexity.

See also the PYACTION keyword in the SCHEDULE section that implements OPM Flow’s Python scripting facility using the standard Python scripting language.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| ACTIONX | Define the start of ACTIONX Definition Section.  This is then followed on a new line by any number of ACTIONX records that define the conditions for which the defined action will be executed and the various operations to be performed if the conditions are satisfied. |  |  |
| 1-1 | ACTNAME | ACTNAME is a character sting of up to eight characters in length, that defines the name of this action definition. If ACTNAME has previously been used by any ACTION series keyword, then the previous ACTION series definition will be replaced by the definition declared by this ACTIONX Definition Section. |  |
| 1-2 | ACTNSTEP | ACTNSTEP is a positive integer that defines the number times that the ACTNAME definition is executed.  ACTIONX definitions are activated at the end of a time step and this parameter is used to set how many time steps the ACTNAME definition will be invoked. The default value of one means that the definition will be executed only once. Use a large value, for example 10,000 for the definition to be executed at every time step. Note that the counter only affects successful evaluations; i.e. if ACTNSTEP is set equal to one (the default), then the simulator will test the action at the end of every time step until it evaluates to true. | 1 |
| 1-3 | ACTDELTA | ACTDELTA is a real positive value that defines the minimum duration of time after the conditions defined on the second record have been satisfied before the ACTIONX actions are executed.  For example, if ACTDELTA is defaulted the actions will be executed at the end of the time step for which the conditions are met.  If set to say 30, then a minimum of 30 days will pass before the actions are executed (assuming field or metric units). | 0.0 |
| days | days | hours |  |
| 1-4 | / | Record terminated by a “/” | Not Applicable |
| 2-1 | ACTLHS | ACTLHS is a series of character strings, each up to eight characters in length, that defines a constant, UDQ defined value, or a SUMMARY variable on the left hand side of a Boolean conditional test. The format for ACTLHS is dependent on the SUMMARY variable type: Aquifer, Block, Field, Group, Region, Time, Well, Well Connection, Well Local Grid Refinement Connection, or a Well Segment. In addition to SUMMARY variables, an UDQ defined value or a Constant variable can be used.  The format for the various data types is given in Table 12.7. | Not Applicable |
| 2-2 | ACTTEST | ACTTEST is a defined character string that states the Boolean operator and must be set to one of the following Boolean conditionals: For example to test if the field’s gas production rate is less than 600 MMscf/d then one would use: ACTIONX PHASE2       1               / GGPR  'FIELD' < 600E3        / / ... ENDACTIO | Not Applicable |
| 2-3 | ACTRHS | ACTRHS is a numeric value or a series of character strings, each up to eight characters in length, that defines a constant, an UDQ defined value, or a SUMMARY variable on the right hand side of a Boolean conditional test, as outlined in Table 12.7 (see also ACTLHS). In the case of well quantities the set of matching wells is captured and can be used as a general "well list" with the symbol '?' in subsequent well keywords. For example, to shut-in all oil producing wells (‘OP*’) with a water cut greater than 90% for every time the field water production rate exceeds 60,000 stb/d one would use: ACTIONX MXWATER      10000           / GWPR  'FIELD' > 60E3  AND    / WWCT  'OP*'   > 0.90         / / -- WELL PRODUCTION STATUS -- --  WELL    WELL   --LOCATION--  COMPLETION --  NAME    STAT     I   J    K  FIRST LAST WELOPEN '?'         SHUT                           / / ENDACTIO | Not Applicable |
| 2-4 | ANDOR | An optional defined character string that specifies a Boolean operator that must be set to either AND or OR if included on this record, that links this record with additional records of this type. For example, to test if the field’s gas production rate is less than 600 MMscf/d after 2020 then one would use: ACTIONX PHASE2       1               / GGPR  'FIELD' < 600E3 AND    / YEAR > 2020                  / / ... ENDACTIO This item should be left blank if not required. | Not Applicable |
| 2.5 | / | Termination of an ACTIONX Boolean condition record. Note that multiple numbers of records of this type can be entered with each record terminated by a “/”, as illustrated above. | Not Applicable |
| 3-1 | / | The Boolean condition section of the ACTIONX keyword is terminated by an empty line with a single “/”. | Not Applicable |
|  |  | The next section contains any number of standard SCHEDULE keywords that will be executed if the Boolean expression evaluates to true.  For example, to test if the field’s gas production rate is less than 600 MMscf/d after 2020 and to open up additional wells if this occurs, then one would use: ACTIONX PHASE2       1               / GGPR  'FIELD' < 600E3 AND    / YEAR > 2020                  / / -- WELL PRODUCTION STATUS -- --  WELL    WELL   --LOCATION--  COMPLETION --  NAME    STAT     I   J    K  FIRST LAST WELOPEN GP10        OPEN                           / GP11        OPEN                           / / ENDACTIO In theory, most SCHEDULE keywords can be used in an ACTIONX Definition Section here, except for the time stepping keywords, i.e, TSTEP and DATES. See Table 12.8 for a list of the SCHEDULE keywords that are known to work with the ACTIONX keyword. | Not Applicable |
| ENDACTIO | Define the end of ACTIONX Definition Section. | Not Applicable |  |
| Notes: |  |  |  |

*Table 12.6: ACTIONX Keyword Description*


The variable types and the associated definitions that are available for use with Boolean conditionals are outlined in Table 12.7.


| Variable Type | Description |
| --- | --- |
| AQUIFER | AQUIFER variable consists of two parameters: |
| BLOCK | BLOCK variable consists of four parameters: The NX, NY, and NZ parameters are defined on the DIMENS keyword in the RUNSPEC section. |
| CONSTANTS | CONSTANTS can consist of one or optionally two parameters: |
| FIELD | The FIELD variable consists of any field SUMMARY variable; for example the Field average Pressure, as shown below: ACTIONX WIPHASE       1               / FPR < 2500                    / / ... ENDACTIO The above would action a set of SCHEDULE keywords if the field average pressure fell below 2,500 psia for a run using FIELD units. |
| GROUP | GROUP variable definition consists of: To enable an action for when the field’s oil production rate drops below 20,000 stb/d then one could use. ACTIONX OILMIN        1               / GOPR  'FIELD' < 20.0E3        / / ... ENDACTIO |
| REGION | REGION variable definition consists of: For example, ACTIONX WIPHASE       1               / RPR 0 < 2500                  / / ... ENDACTIO Would action a set of SCHEDULE keywords if the field average pressure fell below 2,500 psia for a run using FIELD units. |
| TIME | TIME variable definition consists of one parameter that can have three values: DAY for the current simulation day of the month, MNTH for the current simulation month, and YEAR for the current simulation year. Thus, to set an action for April 1, 2025 one would use: ACTIONX ACT01    1                     / DAY  = 1              AND    / MNTH ='APR'           AND    / YEAR = 2025                  / / ... ENDACTIO Note that the value for the MNTH variable,  ‘APR’, in the example, can also be entered without the quotes, that is: MNTH = APR            AND    / In addition, numerical values for MNTH, similar to DAY and YEAR, are also permitted and are converted to the nearest integer for comparison, so for example: ACTIONX ACT01    1                     / DAY  = 0.95           AND    / MNTH = 4.40           AND    / YEAR = 2024.9                / / ... ENDACTIO Would again result in the action taking place on April 1, 2025. |
| WELL | WELL variable definition consists of: Note that the use of well lists is an OPM Flow specific feature. To reduce the tubing head pressure constraint for when any of the oil producers’ oil rate drop below 100 stb/d then one could use. ACTIONX WOILMIN       1               / WOPR  'OP*'   < 100.0         / / -- -- FLOW WELLS THROUGH LOW PRESSURE SEPARATOR -- --  WELL    WELL   TARGET --  NAME    TARG   VALUE WELTARG 'OP*'       THP     150             / / ENDACTIO |
| WELL CONNECTION | WELL CONNECTION variable definition is comprised of: The NX, NY, and NZ parameters are defined on the DIMENS keyword in the RUNSPEC section. |
| WELL COMPLETION | WELL COMPLETION variable definition is comprised of: |
| WELL LOCAL GRID REFINEMENT CONNECTION | WELL LOCAL GRID REFINEMENT CONNECTION variable definition is comprised of: The NX, NY, and NZ parameters are defined on either the CARFIN or RADFIN keywords in the GRID section depending upon whether a Cartesian or radial local grid refinement is being utilized. Note Local Grid Refinements are currently not implemented in OPM Flow. |
| WELL SEGMENT | WELL SEGMENT variable definition consists of: Note that the total number of wells should be defined via the WELLSDIMS keyword and the number of multi-segment wells should be declared on the WSEGDIMS keyword, both keywords are in the RUNSPEC section. |

*Table 12.7: ACTIONX Variable Definitions*


See also the ACTDIMS and UDADIMS keyword in the RUNSPEC section to define the dimensions for the ACTIONX keyword and associated variables. In addition, the EXIT keyword in the SCHEDULE section that allows for terminating the simulation for when a condition within an ACTIONX definition is satisfied.

Although most SCHEDULE keywords should work with the ACTIONX keyword, Table 12.8 shows the status of keywords that have been tested and known to work, together with keywords that are currently planned to be implemented.


| ACTIONX Schedule Section Keywords Status |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Action Keywords | Group Keywords | Well Keywords | Connection Keywords | Miscellaneous Keywords |  |
| ACTIONX | GCONINJE | WCONHIST | WPIMULT | COMPDAT | BOX |
| UDQ | GCONPROD | WCONINJE | WSEGVALV | COMPLUMP | BRANPROP |
|  | GCONSUMP | WCONINJH | WTEST | COMPSEGS | ECHO |
|  | GEFAC | WCONPROD | WTMULT |  | ENDBOX |
|  | GLIFTOPT | WDFAC |  |  | EXIT5 |
|  | GRUPNET | WECON |  |  | INCLUDE7 |
|  | GRUPTARG | WEFAC |  |  | MULTX |
|  | GRUPTREE | WELOPEN |  |  | MULTX- |
|  | GSATINJE | WELPI |  |  | MULTY |
|  | GSATPROD | WELSEGS |  |  | MULTY- |
|  |  | WELSPECS6 |  |  | MULTZ |
|  |  | WELTARG |  |  | MULTZ- |
|  |  | WGRUPCON |  |  | NEXT |
|  |  | WINJMULT |  |  | NEXTSTEP |
|  |  | WLIST |  |  | NOECHO |
| Notes: |  |  |  |  |  |

*Table 12.8: ACTIONX Schedule Section Keywords Status*


As mentioned previously, the UDQ keyword stipulates the variables and operations used to access the User Defined Quantities features in OPM Flow. UDQ variables can be constants, SUMMARY variables, as defined in the SUMMARY section, or a formula using various mathematical functions together with constants and SUMMARY variables.


::: {.callout-note}
Within an ACTIONX Definition Section any UDQ variables utilizing group and well variables, must have their associated groups and wells previously fully defined in the commercial simulator, otherwise an error will occur. For example, if a well’s GOR is being used as part of a UDQ definition, then the well must be fully characterized prior to declaring the UDQ definition. This restriction does not apply to OPM Flow; however, it should be considered if the same deck is to be run with both simulators.
:::


User Defined Quantities can also be used as User Defined Arguments (“UDA”) in the SCHEDULE section with various group, well, and connection keywords. In this case, the UDA variables are used to replace numerical values on these keywords by UDA variables that have been defined by the UDQ keyword.  For example, if we wish to make the oil rate for certain wells to be a function of their water cut, then one can define the function using the UDQ keyword that results in a UDQ variable, WU_OPR say, and then use WU_OPR as a UDA variable on the WCONPROD keyword for the ORAT parameter.  See Table 12.76 for a list of keywords that can be used with UDA variables in the UDQ - Declare User Define Quantities (“UDQ”) keyword section.


#### Examples

The first example uses the UDQ keyword to sort the oil wells from high water cut to low, via the WU_WLIST variable, and then use the ACTIONX keyword to shut-in the worst offending well when the field’s water production is greater than 30,000 stb/d.


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

Apart from checking that the field’s water production rate is greater than 30,000 stb/d the Boolean conditional also checks that there is at least one well in the sorted well list. Notice also the use of ‘?’ symbol as a substitution of the well name and that the ACTIONX WSHUTIN series of commands will be executed a total of ten times.

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
