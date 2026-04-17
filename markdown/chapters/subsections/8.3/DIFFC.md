### DIFFC – Define PVT Region Molecular Diffusion Tables {#kw-DIFFC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The DIFFC keyword defines the molecular weight of the fluids and diffusion coefficients between phases for each PVT region, for when the Molecular Diffusion option has been activated by the [DIFFUSE](#kw-DIFFUSE) keyword in the [RUNSPEC](#kw-RUNSPEC) section. This keyword is optional as OPM Flow will automatically calculate the coefficients, as described by Sandve et al.^[Tor Harald Sandve1, Sarah E. Gasda, Atgeirr Rasmussen, and Alf Birger Rustad. Convective dissolution in field scale CO2 storage simulation using the OPM Flow simulator. Submitted to TCCS 11 – Trondheim Conference on CO2 Capture, Transport and Storage Trondheim, Norway – June 21-23, 2021.], if the DIFFC keyword is absent from the input deck.  The keyword thus allows one to overwrite the automatically calculated values.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | OILMW | OILMW is a real positive number that specifies the molecular weight of the oil in the given PVT region. | None |
| lb/lb-M | kg/kg-M | gm/gm-M |  |
| 2 | GASMW | GASMW is a real positive number that defines the molecular weight of the gas in the given PVT region. | None |
| lb/lb-M | kg/kg-M | gm/gm-M |  |
| 3 | GASGASDF | A real positive number that defines the gas in gas diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| 4 | OILGASDF | A real positive number that declares the oil in gas diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| 5 | GASOILDF | A real positive number that specifies the gas in oil diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| 6 | OILOILDF | A real positive number that defines the oil in oil diffusion coefficient in the given PVT region. | None |
| ft2/day | m2/day | cm2/hour |  |
| 7 | GASOILCD | A real positive number that defines the gas in oil cross phase diffusion coefficient in the given PVT region. This parameter is ignored by OPM Flow and should be defaulted or set equal to zero. | 0.0 |
| ft2/day | m2/day | cm2/hour |  |
| 8 | OILOILCD | A real positive number that defines the oil in oil cross phase diffusion coefficient in the given PVT region. This parameter is ignored by OPM Flow and should be defaulted or set equal to zero. | 0.0 |
| ft2/day | m2/day | cm2/hour |  |
| Notes: |  |  |  |
: DIFFC Keyword Description {#tbl-8-27}
::: {.callout-note}
The option has been tested in combination with the [CO2STORE](#kw-CO2STORE) keyword, but not for the general case at this point.
:::


See also the [DIFFUSE](#kw-DIFFUSE) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the Molecular Diffusion option.


#### Example

The example below is based on field units, with NTPVT equal to three on the [TABDIMS](#kw-TABDIMS) keyword.


```
--
--       PVT REGION MOLECULAR DIFFUSION TABLES
--
DIFFC
--       OIL     GAS    GAS IN   OIL IN   GAS IN   OIL IN   GAS IN   OIL IN
--       MW      MW     GAS DF   GAS DF   OIL DF   OIL DF   OIL CD   OIL CD
--       ------  -----  -------  -------  -------  -------  -------  ------
         103.20  1.120  1.35E-6  1.05E-7  4.50E-7  1.05E-8                 /TAB-1
         102.00  1.130  1.25E-6  1.25E-7  4.80E-7  1.05E-8                 /TAB-2
         100.00  1.250  1.22E-6                                            /TAB-3
```


Here the third PVT region has no values for the various oil related diffusion coefficients.