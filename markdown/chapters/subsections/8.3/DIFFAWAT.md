### DIFFAWAT – Define PVT Region Water Component Diffusion Coefficients (Mass Fraction Formulation) {#kw-DIFFAWAT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [DIFFAWAT](#REF_HEADING_KEYWORD_DIFFAWAT_8_3) keyword defines the water diffusion coefficients assuming a mass fraction formulation for each compositional component in the model and for each PVT region, for when the Molecular Diffusion option has been activated by the [DIFFUSE](#kw-DIFFUSE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is optional as OPM Flow will automatically calculate the coefficients assuming the mole fraction formulation, as described by Sandve et al.^[Tor Harald Sandve, Sarah E. Gasda, Atgeirr Rasmussen, and Alf Birger Rustad. Convective dissolution in field scale CO2 storage simulation using the OPM Flow simulator. Submitted to TCCS 11 – Trondheim Conference on CO2 Capture, Transport and Storage Trondheim, Norway – June 21-23, 2021.], if the [DIFFAWAT](#REF_HEADING_KEYWORD_DIFFAWAT_8_3) and [DIFFCWAT](#kw-DIFFCWAT) keywords are absent from the input deck.  The keyword thus allows one to overwrite the automatically calculated values.

The keyword should only be used if the [CO2STORE](#kw-CO2STORE) or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keywords and either the [GASWAT](#kw-GASWAT) or the [GAS](#kw-GAS) and [WATER](#kw-WATER) keywords in the [RUNSPEC](#kw-RUNSPEC) section, have also been activated for the gas-water two component model.

See also the [DIFFCGAS](#kw-DIFFCGAS) and [DIFFCWAT](#kw-DIFFCWAT) keywords that assume the standard mole fraction formulation for diffusion rather than the mass fraction formulation assumed by the [DIFFAGAS](#REF_HEADING_KEYWORD_DIFFAGAS_8_3) and [DIFFAWAT](#REF_HEADING_KEYWORD_DIFFAWAT_8_3) keywords. The [DIFFAGAS](#REF_HEADING_KEYWORD_DIFFAGAS_8_3) and [DIFFAWAT](#REF_HEADING_KEYWORD_DIFFAWAT_8_3) keywords cannot be used in combination with the [DIFFCGAS](#kw-DIFFCGAS) and [DIFFCWAT](#kw-DIFFCWAT) keywords.


::: {.callout-note}
This is an OPM Flow specific keyword used with OPM Flow’s [CO2STORE](#kw-CO2STORE) or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) and [GASWAT](#kw-GASWAT) keywords in the [RUNSPEC](#kw-RUNSPEC) section.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | CO2DIFF | A real positive number that declares the CO2 or H2 in water diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| 2 | WATDIFF | A real positive number that specifies the water in water diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| Notes: |  |  |  |
: DIFFAWAT Keyword Description {#tbl-8-3-32-1}
::: {.callout-note}
The option has been tested in combination with the [CO2STORE](#kw-CO2STORE) keyword, but not for the general case at this point.
:::


See also the [DIFFUSE](#kw-DIFFUSE) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the Molecular Diffusion option and the [DIFFAGAS](#REF_HEADING_KEYWORD_DIFFAGAS_8_3) keyword in the [PROPS](#kw-PROPS) section that defines the gas diffusion coefficients for each compositional component in the model and for each PVT region. Finally, for gas-oil systems the [DIFFC](#kw-DIFFC) keyword in the [PROPS](#kw-PROPS) section should be used.

Normally diffusion coefficients are measured in laboratory units, that is cm2/s, for ease of use, @tbl-8-3-32-2 outlines the conversion factors for converting the laboratory measured diffusion coefficients to those used by the simulator.


| Diffusivity Conversion Factors |  |  |
| --- | --- | --- |
| Laboratory Measured Units | Conversion Factor | Simulator Units |
| 1 cm2/s | 92.9979 ft2/day | Field |
| 8.64 m2/day | Metric |  |
| 3600 cm2/hour | Laboratory |  |
: Diffusivity Conversion Factors {#tbl-8-3-32-2}
#### Example

The example below is based on field units, with NTPVT equal to three on the [TABDIMS](#kw-TABDIMS) keyword.


```
--
--       PVT REGION WATER COMPONENT DIFFUSION COEFFICIENTS (OPM FLOW KEYWORD)
--
DIFFAWAT
--       CO2 IN   WAT IN
--       WAT DF   WAT DF
--       -------  -------
         0.160    0.150                / PVT REGION NO. 01
         0.165    0.155                / PVT REGION NO. 02
                                       / PVT REGION NO. 03
```


Here the third PVT region has no values for the two component diffusion coefficients, and therefore the simulator will use correlations to define the diffusivity coefficients for this PVT region.