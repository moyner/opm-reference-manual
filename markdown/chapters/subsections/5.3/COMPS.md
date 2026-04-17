### COMPS  –  Activate Compositional Modeling Formulation {#kw-COMPS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The COMPS keyword activates the Compositional Modeling Formulation, and declares the number of components active in the model.

OPM Flow does not currently support the general compositional modeling formulation.


::: {.callout-note}
This keyword is only supported by OPM Flow when the two component gas-water CO2 storage model has been activated using the [CO2STORE](#kw-CO2STORE) keyword and either the [GASWAT](#kw-GASWAT) or the [GAS](#kw-GAS) and [WATER](#kw-WATER) keywords in the [RUNSPEC](#kw-RUNSPEC) section. Secondly, although OPM Flow parses the keyword, the simulator currently ignores the data for this keyword.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | COMPS | A positive integer defining the number of compositional components active in the model. Only the default value of two is currently supported by OPM Flow. | 2 |
| Notes: |  |  |  |
: COMPS Keyword Description {#tbl-5-7}
#### Example

The following example shows how to request a two component compositional modeling formulation to be used with the [CO2STORE](#kw-CO2STORE) and [GASWAT](#kw-GASWAT) options.


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