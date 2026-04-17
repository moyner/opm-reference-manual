### VISCAQA – Specify Ezrokhi Coefficients for Aqueous Viscosity {#kw-VISCAQA}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [VISCAQA](#REF_HEADING_KEYWORD_VISCAQA_8_3) keyword specifies the three Ezrokhi coefficients for each compositional component and for each equation of state that are used to calculate the aqueous phase viscosity. The keyword should only be used if the compositional mode has been requested using the [COMPS](#kw-COMPS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is only supported by OPM Flow when the two phase gas-water CO2 storage model has been activated using the [CO2STORE](#kw-CO2STORE) keyword and either the [GASWAT](#kw-GASWAT) or the [GAS](#kw-GAS) and [WATER](#kw-WATER) keywords in the [RUNSPEC](#kw-RUNSPEC) section. The component names "H2O", "CO2" and "NACL" (water, CO2 and salt respectively) must be specified using the [CNAMES](#kw-CNAMES) keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | COEFFS | A series of real numbers that define the three Ezrokhi coeffients for each of the compositional components active in the model. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: VISCAQA Keyword Description {#tbl-8-3-376-1}
#### Examples

The following example defines the Ezrokhi coefficients for each component in a single three-component equation of state model.


```
--
-- Ezrokhi Coefficients for Aqueous Viscosity Calculation
--
VISCAQA
--COEFF0   COEFF1   COEFF2
  2.0E-7   0.0      1.0E-9
  2.0E-7   0.0      1.0E-9
  2.0E-7   0.0      1.0E-9   /

```

The following example defines the Ezrokhi coefficients for each component in two three-component equation of state models.


```
--
-- Ezrokhi Coefficients for Aqueous Viscosity Calculation
--
VISCAQA
--COEFF0   COEFF1   COEFF2
  2.0E-7   0.0      1.0E-9
  2.0E-7   0.0      1.0E-9
  2.0E-7   0.0      1.0E-9   /
--
  2.0E-7   0.0      1.0E-9
  2.0E-7   0.0      1.0E-9
  2.0E-7   0.0      1.0E-9   /
```