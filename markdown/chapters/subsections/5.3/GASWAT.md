### GASWAT – Activate the Gas-Water Model Formulation {#kw-GASWAT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the two-phase Gas-Water model, as such it is equivalent to using both the [GAS](#kw-GAS) and [WATER](#kw-WATER) keywords in the [RUNSPEC](#kw-RUNSPEC) section..


::: {.callout-note}
This is an OPM Flow keyword, and should not be confused with the more general version of the GASWAT keyword used in the commercial compositional simulator.
:::


There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


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


The above example declares that the run should use the Gas-Water model, together with the [CO2STORE](#kw-CO2STORE) option, and with two components.