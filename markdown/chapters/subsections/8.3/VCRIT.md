### VCRIT – Critical Volumes


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [VCRIT](#REF_HEADING_KEYWORD_VCRIT) keyword defines the critical volumes for each of the compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [VCRIT](#REF_HEADING_KEYWORD_VCRIT) | A series of real numbers that define the critical volumes for each of the compositional components active in the model. | None |
| ft3/lb-M | m3/kg-M | m3/kg-M |  |
| Notes: |  |  |  |

*Table 8.3.359.1: VCRIT Keyword Description*


#### Examples

The following example defines the critical volumes for each component in a single three-component equation of state model.


```
--
-- Critical Volumes
--
VCRIT
  1.505  1.585  3.250 /

```

The following example defines the critical volumes for each component in two three-component equation of state models.


```
--
-- Critical Volumes
--
VCRIT
  1.505  1.585  3.250 /
  1.505  1.585  3.250 /
```
