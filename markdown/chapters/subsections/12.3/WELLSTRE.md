### WELLSTRE  –  Define Injection Stream Composition


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [WELLSTRE](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2) keyword defines a well stream together with the compositional component mole factions, associated with the well stream, as such it should have the same number of entries as that declared via the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and the [NCOMPS](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. Once a gas well stream has been defined, it can be used with either the [WINJGAS](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2 Copy 1) or GINJGAS keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, to set the injected gas composition. Similarly,  if an oil well stream has been defined by [WELLSTRE](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2), then the well stream can be used with the WINJOIL keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, to specify the injected oil composition.

The keyword should only be used if the [CO2STORE](#__RefHeading___Toc387968_1616145207) and [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section have also be activated for the gas-water two component model.


| Note This is an OPM Flow keyword used with OPM Flow’s [CO2STORE](#__RefHeading___Toc387968_1616145207) and [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and should not be confused with the more general version of the [WELLSTRE](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1 Copy 1 Copy 2) keyword used in the commercial compositional simulator. Secondly, although OPM Flow parses the keyword, the simulator currently ignores the data for this keyword. |
| --- |


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | STREAM | STREAM is a character string of up to eight characters in length, representing the well stream name. The [WELLDIMS](#__RefHeading___Toc82886_327352552)(MXSTRMS) parameter in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section determines the maximum number of well streams allowed in the model. | None |
| 2 | ZCOMP | A row vector, with each item representing a compositional component mole fraction for a given component. In addition, the sum of the compositional component mole fractions must sum to one, otherwise an error will occur. Note that the number ZCOMP values, should be the same as that entered via the [NCOMPS](#__RefHeading___Toc27871_3671211675 Copy 1 Copy 1) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, and the [COMPS](#__RefHeading___Toc27871_3671211675 Copy 1) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. However,  for a given ZCOMP component, the mole fraction may be defaulted with 1*, in which case the mole fraction is set to zero. Secondly, ZCOMP may be terminated early, in this case the undefined mole fractions will be set to zero. Finally, only the default value of two components are currently supported by OPM Flow. | None |
| mole fraction | mole fraction | mole fraction |  |
| Notes: |  |  |  |

*Table 12.86: WELLSTRE Keyword Description*


#### Example

The following example defines how to specify a two component formulation, together with defining the names of the composition components, to be used with the [CO2STORE](#__RefHeading___Toc387968_1616145207) and [GASWAT](#__RefHeading___Toc38607_2267116897 Copy 1) options.


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
```


Here the well stream consists of 100% CO2 and zero water.
