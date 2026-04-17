### BRINE – Activate Brine Tracking Option


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The BRINE keyword activates the standard Brine Tracking model and optionally defines the water phase to have various salinities if the ECLMC keyword in the RUNSPEC section has been used to activate the Multi-Component Brine model, that allows for the water phase to have multiple water salinities.  Note that the Multi-Component Brine model is not supported by OPM Flow.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | SALTS | An optional character vector string that defines the salts to be tracked for when the Multi-Component Brine model has been activated by the ECLMC keyword in the RUNSPEC section. SALTS should be set to one or more of the following salt chemical formulae: | None |
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
| Note that the ECLMC option is currently not available in OPM Flow, so only the BRINE keyword without the optional SALT variables should be declared in the input deck. |  |  |  |
| Notes: |  |  |  |

*Table 5.6: BRINE Keyword Description*


See also the PRECSALT and VAPWAT keywords in the RUNSPEC section that activates OPM Flow’s Salt Precipitation model, and the PVTWSALT keyword in the PROPS section to define the water properties with respect to salt concentration.


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
