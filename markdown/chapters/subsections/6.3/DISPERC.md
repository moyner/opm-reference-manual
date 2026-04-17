### DISPERC – Define the Mechanical Dispersivity for All Cells


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [DISPERC](#REF_HEADING_KEYWORD_DISPERC_6_3) keyword defines the mechanical dispersivity for all cells in the model via an array.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
|  | Metric | Laboratory |  |
| 1 | [DISPERC](#REF_HEADING_KEYWORD_DISPERC_6_3) | [DISPERC](#REF_HEADING_KEYWORD_DISPERC_6_3) is an array of real positive values that defines the mechanical dispersivity for each cell in the model. Repeat counts may be used, for example 20*1.0. | None |
| feet | m | cm |  |
| Notes: |  |  |  |

*Table 6.3.39.1: [DISPERC](#REF_HEADING_KEYWORD_DISPERC_6_3) Keyword Description*


::: {.callout-note}
The option has been tested in combination with the CO2STORE, [H2STORE](#REF_HEADING_KEYWORD_H2STORE), [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM), or MICP keywords, but not for the general case at this point.
:::


See also the CO2STORE and [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keywords in the RUNSPEC section that active OPM Flow’s CO2 and H2 storage models respectively.


#### Example

The example sets the mechanical dispersivity for all cells in the model to 1.0.


```
--
--       SET MECHANICAL DISPERSIVITY FOR ALL CELLS (OPM FLOW KEYWORD)
--
DISPERC
         1000*1.0                                           /
```
