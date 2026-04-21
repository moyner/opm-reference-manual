### ACTCO2S – Activity Model for CO2


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The keyword [ACTCO2S](#REF_HEADING_KEYWORD_ACTCO2S) specifies the activity model for salting-out effects when calculating mutual solubility in the CO2 storage module which is activated by the CO2STORE keyword in the RUNSPEC section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | ACTMODEL | A positive integer value selecting the activity model for the salting-out effect. The choices are: | 3 |
| Notes: |  |  |  |

*Table 8.3.1.1: [ACTCO2S](#REF_HEADING_KEYWORD_ACTCO2S) Keyword Description*


#### Example

The following example activates activity model number 1.


```
--
--       ACTIVITY MODEL FOR SALTING-OUT EFFECTS IN CO2
--
ACTCO2S
         1                                                 /

```
