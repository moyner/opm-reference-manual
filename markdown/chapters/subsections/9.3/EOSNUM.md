### EOSNUM – Define the Equation of State Region Numbers


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [EOSNUM](#REF_HEADING_KEYWORD_EOSNUM_9_3) keyword defines the Equation Of State ([EOS](#REF_HEADING_KEYWORD_EOS_5_3)) region number for all the cells in the model via an array. The region number specifies which Equation Of State is used in each grid block. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [EOSNUM](#REF_HEADING_KEYWORD_EOSNUM_9_3) | [EOSNUM](#REF_HEADING_KEYWORD_EOSNUM_9_3) is an array of positive integers less than or equal to NMEOSR that define the [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region number for each cell in the model. The NMEOSR variable on the TABDIMS keyword in the RUNSPEC section defines the number of [EOS](#REF_HEADING_KEYWORD_EOS_5_3) regions in the model. | 1 |
| Notes: |  |  |  |

*Table 9.3.17.1: [EOSNUM](#REF_HEADING_KEYWORD_EOSNUM_9_3) Keyword Description*


#### Examples

The example below sets two [EOS](#REF_HEADING_KEYWORD_EOS_5_3)NUM regions for a 4 x 5 x 2 model.


```
--
--       DEFINE EOSNUM REGIONS FOR ALL CELLS
--
EOSNUM
         20*1
         20*2
/
```
