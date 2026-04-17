### BIC – Binary Interaction Coefficients {#kw-BIC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [BIC](#REF_HEADING_KEYWORD_BIC) keyword defines the binary interaction coefficients for each pair of compositional components active in the model and for each equation of state. The keyword should only be used if the compositional mode has been requested using the [COMPS](#kw-COMPS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | [BIC](#REF_HEADING_KEYWORD_BIC) | A series of real numbers that define the binary interaction coefficients ${k}_{\mathit{ij}}$ for each pair (i, j) of compositional components active in the model. The matrix ${k}_{\mathit{ij}}$ is symmetrical with zeroes on the diagonal so only the portion of the matrix below the diagonal is required (i.e., i = {2, ... [COMPS](#kw-COMPS)} and j < i), where [COMPS](#kw-COMPS) is specified by the [COMPS](#kw-COMPS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The values are ordered with j cycling fastest (i.e. ${k}_{21}$, ${k}_{31}$, ${k}_{32}$, ${k}_{41}$, ${k}_{42}$, ${k}_{43}$, ...). | 0 |
| Notes: |  |  |  |
: [BIC](#REF_HEADING_KEYWORD_BIC) Keyword Description {#tbl-8-3-17-1}
#### Examples

The following example defines the binary interaction coefficients for each pair of compositional components in a single three-component equation of state model.


```
--
-- Binary Interaction Coefficients
--
BIC
  0.1209
  0.1310  0.0339 /

```

The following example defines the binary interaction coefficients for each component in two three-component equation of state models.


```
--
-- Binary Interaction Coefficients
--
BIC
  0.1209
  0.1310  0.0339 /
  0.1209
  0.1310  0.0339 /
```