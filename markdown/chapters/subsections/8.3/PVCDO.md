### PVCDO – Oil PVT Properties for Dead Oil (Constant Compressibility) {#kw-PVCDO}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PVCDO defines the oil PVT properties for dead oil^[“Dead” oil is oil that it contains no dissolved gas or a relatively thick oil or residue that has lost its volatile components.] with constant compressibility. If the oil has a constant and uniform dissolved gas concentration, Gas-Oil Ratio (“GOR”), and if the reservoir pressure never drops below the saturation pressure (bubble point pressure), then the model can be run more efficiently by omitting the [GAS](#kw-GAS) and [DISGAS](#kw-DISGAS) keywords from the [RUNSPEC](#kw-RUNSPEC) section, treating the oil as a dead oil, and defining a constant Rs (GOR) value with keyword [RSCONST](#kw-RSCONST) or [RSCONSTT](#kw-RSCONSTT) in the [PROPS](#kw-PROPS) section. This results in the model being run as a dead oil problem with no active gas phase. However, OPM Flow takes into account the constant Rs in the calculations and reporting.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | PRESS is a real positive value defining the oil reference pressure for the other parameters for this data set. | None |
| psia | barsa | atma |  |
| 2 | OFVF | OFVF is a real positive value defining the oil formation volume factor (Bo) at the reference pressure. | None |
| rb/stb | rm3/sm3 | rcc/scc |  |
| 3 | OCOMP | OCOMP is a real positive value defining the oil compressibility (Co) at the oil reference pressure and is defined as: ${C}_{o} = -\frac{1}{{B}_{o}}(\frac{{\mathit{dB}}_{o}}{\mathit{dP}})$ | None |
| 1/psia | 1/barsa | 1/atma |  |
| 4 | OVISC | OVISC is a real positive value defining the oil viscosity (µo) at the oil reference pressure. | None |
| cP | cP | cP |  |
| 5 | OVISCOMP | OVISCOMP is a real positive value defining the oil viscosibility (µoc) at the oil reference pressure and is defined as: ${μ}_{\mathit{oc}} = \frac{1}{{μ}_{o}}(\frac{d{μ}_{o}}{\mathit{dP}})$ | None |
| 1/psia | 1/barsa | 1/atma |  |
| Notes: |  |  |  |
: PVCDO Keyword Description {#tbl-8-3-225-1}
See also the [RSCONST](#kw-RSCONST) and [RSCONSTT](#kw-RSCONSTT) keywords to define the constant Rs for dead oil and [PVDO](#kw-PVDO) as an alternative keyword to enter the dead oil properties.


#### Example


```
--
--       OIL PVT TABLE FOR DEAD WITH CONSTANT COMPRESSIBILITY
--
PVCDO
--       REF PRES  BO         CO        VISC     VISC
--       PSIA      RB/STB     1/PSIA    CPOISE   GRAD
--       --------  --------   -------   ------   ------
          3840.0    1.080     1.5E-6     1.750    0.0       / TABLE NO. 01
          3840.0    1.100     1.5E-6     1.050    0.0       / TABLE NO. 02
          3840.0    1.120     1.6E-6     0.950    0.0       / TABLE NO. 03
          3840.0    1.140     1.7E-6     0.850    0.0       / TABLE NO. 04
          3840.0    1.160     1.7E-6     0.800    0.0       / TABLE NO. 05

```

The above example defines five dead oil PVT tables with constant compressibility and viscosity, and assumes that NTPVT equals five on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

There is no terminating “/” for this keyword.