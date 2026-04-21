### TCRIT – Critical Temperatures


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [TCRIT](#REF_HEADING_KEYWORD_TCRIT) keyword defines the critical temperatures for each of the compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [TCRIT](#REF_HEADING_KEYWORD_TCRIT) | A series of real numbers that define the critical temperatures for each of the compositional components active in the model. | None |
| °R | K | K |  |
| Notes: |  |  |  |

*Table 8.3.340.1: [TCRIT](#REF_HEADING_KEYWORD_TCRIT) Keyword Description*


#### Examples

The following example defines the critical temperatures for each component in a single three-component equation of state model.


```
--
-- Critical Temperatures
--
TCRIT
  547.4412 343.0152 665.802 /

```

The following example defines the critical temperatures for each component in two three-component equation of state models.


```
--
-- Critical Temperatures
--
TCRIT
  547.4412 343.0152 665.802 /
  547.4412 343.0152 665.802 /
```
