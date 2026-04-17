### ACTIONW – Define Action Conditions and Command Processing (Wells) {#kw-ACTIONW}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword starts the definition of an ACTIONW section that stipulates the Boolean conditions to test the nominated well parameters, and the resulting [SCHEDULE](#kw-SCHEDULE) keywords to be executed, if the Boolean condition evaluates to true.  An ACTIONW Definition Section is terminated by an [ENDACTIO](#kw-ENDACTIO) keyword on a separate line.  Here, the keyword defines a series of conditions applied to wells only, that invoke run time processing of [ACTION](#kw-ACTION) functions, and is similar to executing a run time script for conditions and variables at the well level.  The [ACTION](#kw-ACTION) series of keywords ([ACTION](#kw-ACTION), [ACTIONG](#kw-ACTIONG), [ACTIONR](#kw-ACTIONR), [ACTIONS](#kw-ACTIONS) and ACTIONW) can apply Boolean conditional tests to variables at the field, group, region, well segment and well levels.

Note that one should use caution when using this facility as it may result in the simulator aborting, because the ACTIONW keyword enables the user to implement complex functionality and therefore it is advisable to start with simple expressions before adding the desired complexity.

See also the [PYACTION](#kw-PYACTION) keyword in the [SCHEDULE](#kw-SCHEDULE) that implements OPM Flow’s Python scripting facility using the Python scripting language.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped; use the [ACTIONX](#kw-ACTIONX) keyword instead.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| ACTIONW | Defines the start of an ACTIONW Definition Section.  This is followed on a new line by the ACTIONW record that stipulates the conditions for which the defined action will be executed, and then this is followed by the various operations to be performed if the condition is satisfied. |  |  |
| 1-1 | ACTNAME | A character sting of up to eight characters in length that defines the name of this action definition. If ACTNAME has previously been used by any [ACTION](#kw-ACTION) series keyword, then the previous [ACTION](#kw-ACTION) definitions will be replaced by the definition declared by this ACTIONW Definition Section. | None |
| 1-2 | ACTWELL | A character string of up to eight characters in length that defines the well name for which the ACTIONW Definition Section is being defined. Note that the well name (ACTWELL) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 1-3 | ACTLHS | A character string of up to eight characters in length that stipulates a well [SUMMARY](#kw-SUMMARY) variable on the left hand side of a Boolean conditional test. For example, WOPR that stands for the Well Oil Production Rate. In addition, ACTLHS can also be a well User Defined Quantity (“[UDQ](#kw-UDQ)”) defined by the [UDQ](#kw-UDQ) - Declare User Define Quantities (“[UDQ](#kw-UDQ)”) keyword in the [SCHEDULE](#kw-SCHEDULE) section. In this case, the first two characters of ACTLHS must be set to WU and the [UDQ](#kw-UDQ) variable must have previously been declared with the [UDQ](#kw-UDQ) keyword. A complete list of well [SUMMARY](#kw-SUMMARY) vectors that can be used with ACTIONW keyword by OPM Flow and the commercial black-oil simulator is summarized in @tbl-12-5. | Not Applicable |
| 1-4 | ACTTEST | A defined character string that the defines the Boolean operator and must be set to one of the following Boolean conditionals: Note that the OPM Flow implementation of ACTTEST has been enhanced to support all of the above conditions. Whereas, the commercial simulator only supports (1) and (2). Thus, one should be mindful of this fact if the input deck is to be run by both OPM Flow and the commercial simulator. | Not Applicable |
| 1-5 | ACTRHS | A numeric value that defines the constant on the right hand side of the Boolean conditional test. The set of wells for which the Boolean condition is true, is captured and can be used as a general "well list" with the symbol '?' in subsequent well keywords.  For example, to shut wells with a gas production rate less than 5 MMscf/d, one would use: ACTIONW ACT01 'GP*'  WGPR < 5000.0 10000  / [WELOPEN](#kw-WELOPEN) '?'     SHUT                       / / ... [ENDACTIO](#kw-ENDACTIO) | Not Applicable |
| 1-6 | ACTNSTEP | A positive integer that defines the maximum number times that the ACTNAME action is to be executed. The ACTIONW action is excuted at the end of each time step if at least one well satisfies the Boolean condition until the action has been executed the specified number of times. The default value of one means that the definition will be executed only once. One can use a large value, for example 10,000 for the definition to be executed at every time step. Note that the counter only affects successful evaluations; i.e. if ACTNSTEP is set equal to one (the default), then the simulator will test the action at the end of every time step until it evaluates to true. | 1 |
| 1-3 | ACTINCR | ACTINCR is a real negative or positive value that specifies a value to increment ACTRHS every time the Boolean condition evaluates to true. For example, if ACTINCR is set to 500.0: ACTIONW ACT02 'GP*'  WGPR < 5000.0 10000  500.0 / [WELOPEN](#kw-WELOPEN) '?'     SHUT                             / / ... [ENDACTIO](#kw-ENDACTIO) Then after the third time the Boolean conditional has evaluated to true, the condition would effectively be: ACTIONW ACT02 'GP*'  WGPR < 6500.0 10000  500.0 / ... [ENDACTIO](#kw-ENDACTIO) | 0.0 |
| 1-4 | / | Record terminated by a “/” | Not Applicable |
|  |  | The next section contains any number of standard SCHEDULE keywords that will be executed if the Boolean expression evaluates to true.  For example, to reduce the tubing head pressure constraint when any of the oil producers’ oil rate drop below 100 stb/d then one could use: ACTIONW ACT03 'OP*'  WOPR < 100.0 10000   / -- -- FLOW WELLS THROUGH LOW PRESSURE SEPARATOR -- --  WELL    WELL   TARGET --  NAME    TARG   VALUE WELTARG 'OP*'       THP     150            / / ENDACTIO In theory, most SCHEDULE keywords can be used in an ACTIONW Definition Section here, except for the time stepping keywords, i.e, TSTEP and DATES. See the ACTIONX keyword for a list of the SCHEDULE keywords that are known to work with the ACTION series of keywords. | Not Applicable |
| [ENDACTIO](#kw-ENDACTIO) | Define the end of ACTIONW Definition Section. | Not Applicable |  |
| Notes: |  |  |  |
: ACTIONW Keyword Description {#tbl-12-4}
The well [SUMMARY](#kw-SUMMARY) vectors that can be used with the ACTIONW keyword by OPM Flow and the  commercial black-oil simulator are outlined in @tbl-12-5.


| No. | Well [SUMMARY](#kw-SUMMARY) Vector Description | [SUMMARY](#kw-SUMMARY) Mnemonic |
| --- | --- | --- |
| 1 | Bottom-Hole Pressure | WBHP |
| 2 | Gas Injection Rate | WGIR |
| 3 | Gas Injection Total | WGIT |
| 4 | Gas-Liquid Ratio | WGLR |
| 5 | Gas-Liquid Ratio (Bottom Hole) | WBGLR |
| 6 | Gas-Oil Ratio | WGOR |
| 7 | Gas Production Rate | WGPR |
| 8 | Gas Production Total | WGPT |
| 9 | Liquid Production Rate | WLPR |
| 10 | Liquid Production Rate | WLPT |
| 11 | Oil Injection Rate | WOIR |
| 12 | Oil Injection Total | WOIT |
| 13 | Oil Production Rate | WOPR |
| 14 | Oil Production Total | WOPT |
| 15 | Polymer Production Concentration | WCPC |
| 16 | Polymer Production Rate | WCPR |
| 17 | Salt Production Concentration | WSPC |
| 18 | Salt Production Rate | WSPR |
| 19 | Tracer Production Concentration (Tracer name should be added to WTPC) | WTPC |
| 20 | Tracer Production Rate (Tracer name should be added to WTPC) | WTPR |
| 21 | Tubing Head Pressure | WTHP |
| 22 | Voidage Injection Rate | WVIR |
| 23 | Voidage Injection Total | WVIT |
| 24 | Voidage Production Rate | WVPR |
| 25 | Voidage Production Total | WVPT |
| 26 | Water Cut | WWCT |
| 27 | Water Injection Rate | WWIR |
| 28 | Water Injection Total | WWIT |
| 29 | Water Production Rate | WWPR |
| 30 | Water Production Total | WWPT |
| 31 | Water-Gas Ratio | WWGR |
| 32 | User Defined Quantity | WUXXXXXX |
| Notes: |  |  |
: ACTIONW Supported Well SUMMARY Variables {#tbl-12-5}
See also the [ACTDIMS](#kw-ACTDIMS) and [UDADIMS](#kw-UDADIMS) keywords in the [RUNSPEC](#kw-RUNSPEC) section to define the dimensions for the [ACTION](#kw-ACTION) series of keywords and associated variables. In addition, the [EXIT](#kw-EXIT) keyword in the [SCHEDULE](#kw-SCHEDULE) section that allows for terminating the simulation for when a condition within an ACTIONW definition is satisfied

Although most [SCHEDULE](#kw-SCHEDULE) section keywords should work with the ACTIONW keyword, @tbl-12-8 under the description of [ACTIONX](#kw-ACTIONX) – Define Action Conditions and Command Processing shows the status of keywords that have been tested and known to work, together with keywords that are currently planned to be implemented.

As mentioned previously, the [UDQ](#kw-UDQ) keyword stipulates the variables and operations used to access the User Defined Quantities features in OPM Flow. [UDQ](#kw-UDQ) variables can be constants, [SUMMARY](#kw-SUMMARY) variables, as defined in the [SUMMARY](#kw-SUMMARY) section, or a formula using various mathematical functions together with constants and [SUMMARY](#kw-SUMMARY) variables.


::: {.callout-note}
Within an ACTIONW Definition Section any [UDQ](#kw-UDQ) variables utilizing well variables, must have their associated wells previously fully defined in the commercial simulator, otherwise an error will occur. For example, if a well’s GOR is being used as part of a [UDQ](#kw-UDQ) definition, then the well must be fully characterized prior to declaring the [UDQ](#kw-UDQ) definition. This restriction does not apply to OPM Flow; however, it should be considered if the same deck is to be run with both simulators.
:::


User Defined Quantities can also be used as User Defined Arguments (“UDA”) in the [SCHEDULE](#kw-SCHEDULE) section with various group, well, and connection keywords. In this case, the UDA variables are used to replace numerical values on these keywords by UDA variables that have been defined by the [UDQ](#kw-UDQ) keyword.  For example, if we wish to make the oil rate for certain wells to be a function of their water cut, then one can define the function using the [UDQ](#kw-UDQ) keyword that results in a [UDQ](#kw-UDQ) variable, WU_WOPR say, and then use WU_WOPR as a UDA variable on the [WCONPROD](#kw-WCONPROD) keyword for the ORAT parameter. See @tbl-12-76 for a list of keywords that can be used with UDA variables in the [UDQ](#kw-UDQ) - Declare User Define Quantities (“[UDQ](#kw-UDQ)”) keyword section.


#### Examples

The first example uses the ACTIONW keyword to re-complete a gas injection well, GI01, when the well’s bottom-hole pressure exceeds the fracture pressure of the formation, and to open up a structurally higher zone in the well. The keyword [NEXTSTEP](#kw-NEXTSTEP) is used to set the next step to 0.1 days to avoid convergence issues due to a well event.


```
--
--       ACTIONW WELL COMMANDS
--
ACTIONW
--       ACTION     WELL     ACTION   ACTION  ACTION  MAX      INCREMENT
--       NAME       NAME     LHS      TEST    RHS     ACTIONS  RHS
         ACTW-1     GI01     WBHP      >      6800.0                            /
--
--       ACTION COMMANDS TO BE EXECUTED
--
--       NEXT   ALL
--       STEP   TIME
NEXTSTEP
         0.1    'NO'                                                           /
--
-- WELL PRODUCTION STATUS
--
--  WELL WELL   --LOCATION--  COMPLETION
--  NAME STAT     I   J    K  FIRST LAST
WELOPEN
GI01     SHUT                                                                  /
GI01     SHUT     0   0    0     2     2                                       /
GI01     OPEN                                                                  /
GI01     OPEN     0   0    0     1     1                                       /
/
ENDACTIO
```


The second example shows how to reduce a producing well's deliverability due to water production. Here, well OP01’s productivity index is reduced by 2% when the well’s liquid production total is greater than 100,000 stb. The reduction is repeated 300 times and each time the action is executed the ACTRHS constant is increased by 10,000 stb.


```
--
--       ACTIONW WELL COMMANDS
--
ACTIONW
--       ACTION     WELL     ACTION   ACTION  ACTION  MAX      ICREMENT
--       NAME       NAME     LHS      TEST    RHS     ACTIONS  RHS
         ACTW-01    OP01     WLPT       >     100E3   300      10E3     /
--
--       DEFINE WELL CONNECTION MULTIPLIERS
--
-- WELL  PI     --LOCATION--  COMPLETION
-- NAME  MULT     I   J    K  FIRST LAST
WPIMULT
OP01     0.980    1*  1*  1*    1*    1*                                /
/

ENDACTIO

```


The final example is similar to the previous example, and shows how to nest ACTIONW blocks and how to apply ACTIONW to all the oil producers when the Boolean condition are satisfied.


```
--
--       ACTIONW WELL COMMANDS
--
ACTIONW
--       ACTION     WELL     ACTION   ACTION  ACTION  MAX      ICREMENT
--       NAME       NAME     LHS      TEST    RHS     ACTIONS  RHS
         ACTW-01A   'OP*'    WLPT       >     100E3   300      10E3     /

--
--       ACTIONW WELL COMMANDS
--
ACTIONW
--       ACTION     WELL     ACTION   ACTION  ACTION  MAX      ICREMENT
--       NAME       NAME     LHS      TEST    RHS     ACTIONS  RHS
         ACTW-01B   'OP*'    WPI       >      5.0     1        0.0      /

--
--       DEFINE WELL CONNECTION MULTIPLIERS
--
-- WELL  PI     --LOCATION--  COMPLETION
-- NAME  MULT     I   J    K  FIRST LAST
WPIMULT
'?'      0.980    1*  1*  1*    1*    1*                                /
/

ENDACTIO
ENDACTIO

```

In this case the outer ACTIONW checks if the liquid production for each OP* well is great than the calculated ACTRHS constant, if it is, then inner ACTIONW reduces all the selected wells’ productivity indices by 2%, provided the well’s productivity index is greater than five.


```

```