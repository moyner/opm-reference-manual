### ACF – Define Acentric Factors


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [ACF](#REF_HEADING_KEYWORD_ACF) keyword defines the acentric factors for each of the compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | [ACF](#REF_HEADING_KEYWORD_ACF) | A series of real numbers that define the acentric factors for each of the compositional components active in the model. | None |
| Notes: |  |  |  |

*Table 8.3.1.1: ACF Keyword Description*


#### Examples

The following example defines the acentric factors for each component in a single three-component equation of state model.


```
--
-- Acentric Factors
--
ACF
  0.0108  0.2273  0.3434 /

```

The following example defines the acentric factors for each component in two three-component equation of state models.


```
--
-- Acentric Factors
--
ACF
  0.0108  0.2273  0.3434 /
  0.0110  0.2281  0.3428 /
```
