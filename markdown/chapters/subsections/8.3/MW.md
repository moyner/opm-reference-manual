### MW – Molecular Weights


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [MW](#REF_HEADING_KEYWORD_MW) keyword defines the molecular weights for each of the compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [MW](#REF_HEADING_KEYWORD_MW) | A series of real numbers that define the molecular weights for each of the compositional components active in the model. | None |
| lb/lb-M | kg/kg-M | gm/gm-M |  |
| Notes: |  |  |  |

*Table 8.3.184.1: [MW](#REF_HEADING_KEYWORD_MW) Keyword Description*


#### Examples

The following example defines the molecular weights for each component in a single three-component equation of state model.


```
--
-- Molecular Weights
--
MW
  16.0425  44.009   18.01528 /

```

The following example defines the molecular weights for each component in two three-component equation of state models.


```
--
-- Molecular Weights
--
MW
  16.0425  44.009   18.01528 /
  16.0425  44.009   18.01528 /
```
