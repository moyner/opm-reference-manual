### BRINE – Activate Brine Tracking Option


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [BRINE](#__RefHeading___Toc162083_289573908) keyword activates the standard Brine Tracking model and optionally defines the water phase to have various salinities if the [ECLMC](#__RefHeading___Toc206960_803326780) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section has been used to activate the Multi-Component Brine model, that allows for the water phase to have multiple water salinities.  Note that the Multi-Component Brine model is not supported by OPM Flow.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | SALTS | An optional character vector string that defines the salts to be tracked for when the Multi-Component Brine model has been activated by the [ECLMC](#__RefHeading___Toc206960_803326780) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. SALTS should be set to one or more of the following salt chemical formulae: | None |
| Salt Name | Salt Chemical Formulae |  |  |
| Sodium Chloride | NaCl |  |  |
| Potassium Chloride | KCl |  |  |
| Calcium Chloride | CaCl2 |  |  |
| Magnesium Chloride | MgCl2 |  |  |
| Sodium Carbonate | Na2CO3 |  |  |
| Potassium Carbonate | K2CO3 |  |  |
| Calcium Carbonate | CaCO3 |  |  |
| Magnesium Carbonate | MgCO3 |  |  |
| Sodium Sulfate | Na2SO4 |  |  |
| Potassium Sulfate | K2SO4 |  |  |
| Calcium Sulfate | CaSO4 |  |  |
| Magnesium Sulfate | MgSO4 |  |  |
| Note that the [ECLMC](#__RefHeading___Toc206960_803326780) option is currently not available in OPM Flow, so only the [BRINE](#__RefHeading___Toc162083_289573908) keyword without the optional [SALT](#__RefHeading___Toc593214_516898843) variables should be declared in the input deck. |  |  |  |
| Notes: |  |  |  |

*Table 5.6: BRINE Keyword Description*


See also the [PRECSALT](#__RefHeading___Toc332782_3149455253) and [VAPWAT](#__RefHeading___Toc317543_3149455253) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that activates OPM Flow’s Salt Precipitation model, and the [PVTWSALT](#__RefHeading___Toc331848_501926209) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section to define the water properties with respect to salt concentration.


#### Example

The first example actives the standard Brine model and has no terminating “/”.


```
--
--       ACTIVATE STANDARD BRINE MODEL IN THE RUN
--
BRINE

```

The second example illustrates how to activate OPM Flow’s Salt Precipitation model.


```
--
--       ACTIVATE STANDARD BRINE MODEL IN THE RUN
--
BRINE
--
--       ACTIVATE THE OPM FLOW SALT PRECIPITATION MODEL (OPM FLOW KEYWORD)
--
PRECSALT
--
--       VAPORIZED WATER IN DRY/WET GAS IS PRESENT IN THE RUN (OPM FLOW KEYWORD)
--
VAPWAT

```

The third and final example activates the Multi-Component brine model with four different salts.


```
--
--       ACTIVATE MULTI-COMPONENT BRINE MODEL
--
ECLMC
--
--       DEFINE WATER PHASE MULTI-COMPONENT BRINE COMPONENTS
--
--       SALT1   SALT2   SALT3   SALT4   SALT5
BRINE
         NACL    CACL2   MGC03   K2CO3                                         /

```

This option is currently not available in OPM Flow.
