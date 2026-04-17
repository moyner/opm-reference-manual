### DIFFMICP – Define PVT Region MICP Diffusion Coefficients (Mass Concentration Formulation) {#kw-DIFFMICP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [DIFFMICP](#REF_HEADING_KEYWORD_DIFFMICP_8_3) keyword defines the diffusion coefficients assuming the mass concentration formulation for each component dissolved in water and for each PVT region, for when the molecular diffusion option has been activated by the [DIFFUSE](#kw-DIFFUSE) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword should only be used if either the [MICP](#kw-MICP) or [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) model has been activated in the [RUNSPEC](#kw-RUNSPEC) section.


::: {.callout-note}
This is an OPM Flow specific keyword.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | MICRDIFF | A real positive number that declares the microbial concentration in water diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| 2 | OXYGDIFF | A real positive number that declares the oxygen concentration in water diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| 3 | UREADIFF | A real positive number that declares the urea concentration in water diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| Notes: |  |  |  |
: DIFFMICP Keyword Description {#tbl-8-28}
#### Example

The example below is based on metric units, with NTPVT equal to one on the [TABDIMS](#kw-TABDIMS) keyword.


```
--
--       PVT REGION MICP COMPONENT DIFFUSION COEFFICIENTS (OPM FLOW KEYWORD)
--
DIFFMICP
--       MICR IN   OXYG IN   UREA IN
--       WAT DF    WAT DF    WAT DF
--       -------   -------   -------
         2E-04     2E-04     1E-04                / PVT REGION NO. 01
```