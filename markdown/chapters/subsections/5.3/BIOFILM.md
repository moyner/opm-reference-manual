### BIOFILM – Activate the Biofilm Model


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) keyword activates the biofilm model for the run. Biofilm-related effects in subsurface applications such as hydrogen storage include reduced injectivity and hydrogen loss. The conceptual model includes the following mechanisms: (1) Biofilm is present in the storage site prior to injection and (2) the biofilm consumes injected H2/CO2, leading to clogging effects.


::: {.callout-note}
This is an OPM Flow specific keyword used to investigate biofilm effects in underground applications. The module requires that either the CO2STORE or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keywords in the RUNSPEC to be active.
:::


There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
		--
--       ACTIVATE THE BIOFILM MODEL
--
BIOFILM
--
--       ACTIVATE THE H2STORE MODEL
--
WATER
GAS
H2STORE

```

The above example declares that the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) model is active for the run and activates the [H2STORE](#REF_HEADING_KEYWORD_H2STORE) model. For a complete example of this model, see [H2STORE_BIOFILM.DATA](https://github.com/OPM/opm-tests/blob/master/h2store/H2STORE_BIOFILM.DATA).
