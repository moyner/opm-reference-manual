### COMPS  –  Activate Compositional Modeling Formulation


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The COMPS keyword activates the Compositional Modeling Formulation, and declares the number of components active in the model.

OPM Flow does not currently support the general compositional modeling formulation.


::: {.callout-note}
This keyword is only supported by OPM Flow when the two component gas-water CO2 storage model has been activated using the CO2STORE keyword and either the GASWAT or the GAS and WATER keywords in the RUNSPEC section. Secondly, although OPM Flow parses the keyword, the simulator currently ignores the data for this keyword.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | COMPS | A positive integer defining the number of compositional components active in the model. Only the default value of two is currently supported by OPM Flow. | 2 |
| Notes: |  |  |  |

*Table 5.7: COMPS Keyword Description*


#### Example

The following example shows how to request a two component compositional modeling formulation to be used with the CO2STORE and GASWAT options.


```
-- ==============================================================================
--
-- RUNSPEC SECTION
--
-- ==============================================================================
RUNSPEC

--
--       ACTIVATE CO2 STORAGE IN THE MODEL (OPM FLOW CO2 STORAGE KEYWORD)
--
CO2STORE
--
--       ACTIVATE COMPOSITIONAL MODELING FORMULATION (OPM FLOW KEYWORD)
--
COMPS
         2                                                                     /
--
--       ACTIVATE GAS-WATER THE MODEL (OPM FLOW KEYWORD)
--
GASWAT
```
