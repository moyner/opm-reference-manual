### WINJGAS  –  Define Gas Injection Properties for a Well


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WINJGAS keyword defines the properties of the injection gas stream, for a given well. Once a gas well stream has been defined via the WELLSTRE keyword in the RUNSPEC section, it can be used with either the WINJGAS or GINJGAS keywords, to set the injected gas composition. Similarly,  if an oil well stream has been defined by WELLSTRE, then the well stream can be used with the WINJOIL keyword in the SCHEDULE section, to specify the injected oil composition.  Note that, it is unnecessary to use WINJGAS for wells subordinate to a group having gas injection control, with the gas properties set by GINJGAS keyword in the RUNSPEC section. In this case the injection stream is defined by the GINJGAS keyword. However, if a gas injection well under group control users the WINJGAS keyword, then this fluid, and not the group's fluid will be injected instead, at a rate controlled by the group.

The keyword should only be used if the CO2STORE and GASWAT keywords in the RUNSPEC section have also be activated for the gas-water two component model.


| Note This is an OPM Flow keyword used with OPM Flow’s CO2STORE and GASWAT keywords in the RUNSPEC section, and should not be confused with the more general version of the WINJGAS keyword used in the commercial compositional simulator. Secondly, although OPM Flow parses the keyword, the simulator currently ignores the data for this keyword. |
| --- |


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | WELNAME | A character string of up to eight characters in length that defines the injection well name, for which the gas injection properties are being specified. Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 2 | STREAM | A defined character string that determines the properties of the injection gas, and as should be set to one of the following values: Only the STREAM option is supported by OPM Flow. | GRUP |
| 3 | [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) | A character string of up to eight characters in length, that defines the source of the gas injection stream, based on the value of STREAM. If STREAM equals GV, then source should be set to a group name. For STREAM equal to MIX or STREAM, then [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) should be set to the name of the gas stream, as defined by the WINJMIX, WINJORD, or WELLSTRE keywords. | None |
| 4 | MAKEUP | The name of the well stream used for the make-up gas, if make-up gas is required for WELNAME to match the injection target for the well. This option is not supported by OPM Flow. | None |
| 5 | STAGE | STAGE defines the separator stage from which the injection gas should be taken from. In this case, the vapor phase from any stage may be used, and the default value of zero users the total vapor phase from the separator. This option is not supported by OPM Flow. | 0 |
| Notes: |  |  |  |

*Table 12.100: WINJGAS Keyword Description*


#### Example

The following example defines how to specify a two component formulation, together with defining the names of the composition components, to be used with the CO2STORE and GASWAT options.


```
-- ==============================================================================
--
-- PROPS SECTION
--
-- ==============================================================================
PROPS             --
--       CONFIRM NUMBER OF COMPOSITIONAL COMPONENTS (OPM FLOW KEYWORD)
--
NCOMPS
                2                                                                      /
--
--       DEFINE COMPOSITIONAL COMPONENTS NAMES (OPM FLOW KEYWORD)
--
CNAMES
         'CO2'
         'H2O'                                                                 /
```


The second part of the example, defines the well stream for the above two component CO2 water system.


```
-- ==============================================================================
--
-- SCHEDULE SECTION
--
-- ==============================================================================
SCHEDULE
--
--       WELL STREAM INJECTION COMPOSITION (OPM FLOW Keyword)
--
-- WELL     -- WELL STREAM COMPOSITIONAL COMPONENT       --
-- STREAM   --          MOLE FRACTIONS                   --
WELLSTRE
'C02STREAM'    1.000   0.000                               /
/
--
--       WELL GAS INJECTION PROPERTIES
--
-- WELL  STREAM   SOURCE      MAKEUP   SEP
-- NAME  OPTION   DEPTH       GAS      STAGE
WINJGAS
GI01     STREAM   C02STREAM   1*       1* /
/
```


Here the well stream consists of 100% CO2 and zero water, with well GI01 using the gas injection properties as defined by the WELLSTRE keyword and allocated via the WINJGAS keyword.

Finally, the gas injection rate is set via the WCONINJE keyword as shown below.


```
--
--       WELL INJECTION CONTROLS
--
-- WELL  FLUID  OPEN/  CNTL  SURF   RESV   BHP   THP   VFP
-- NAME  TYPE   SHUT   MODE  RATE   RATE   PRES  PRES  TABLE
WCONINJE
GI01     GAS    OPEN   RATE  10E4   1*     300    1*    1*                     /
/
```


Thus, gas injector GI01 will inject 10 x 104 m3 of CO2 per day, assuming metric units.
