### DIFFMICP – Define PVT Region MICP Diffusion Coefficients (Mass Concentration Formulation)


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [DIFFMICP](#REF_HEADING_KEYWORD_DIFFMICP_8_3) keyword defines the diffusion coefficients assuming the mass concentration formulation for each component dissolved in water and for each PVT region, for when the molecular diffusion option has been activated by the DIFFUSE keyword in the RUNSPEC section. The keyword should only be used if either the MICP or [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) model has been activated in the RUNSPEC section.


| Note This is an OPM Flow specific keyword. |
| --- |


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | MICRDIFF | A real positive number that declares the microbial concentration in water diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| 2 | OXYGDIFF | A real positive number that declares the oxygen concentration in water diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| 3 | UREADIFF | A real positive number that declares the urea concentration in water diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| Notes: |  |  |  |

*Table 8.28: DIFFMICP Keyword Description*


#### Example

The example below is based on metric units, with NTPVT equal to one on the TABDIMS keyword.


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
