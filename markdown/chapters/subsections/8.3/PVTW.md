### PVTW –  Define Water Fluid Properties for Various Regions {#kw-PVTW}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PVTW defines the water properties for various regions in the model. The number of PVTW vector data sets is defined by the NTPVT parameter on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the allocation of the PVTW tables to different grid blocks in the model is done via the [PVTNUM](#kw-PVTNUM) keyword in the [REGIONS](#kw-REGIONS) section. One data set consists of one record or line which is terminated by a “/”. If the water phase is active in the model, which is normally the case, then this keyword must be defined in the OPM Flow input deck.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PRES | PRES is a real number defining the water reference pressure (P) for the other parameters for this data set. | None |
| psia | barsa | atma |  |
| 2 | WFVF | WFVF is a real number defining the water formation volume factor (Bw) at the water reference pressure. | Defined |
| rb/stb 1.0 | rm3/sm3 1.0 | rcc/scc 1.0 |  |
| 3 | WCOMP | WCOMP is a real number defining the water compressibility (Cw) at the water reference pressure and is defined as: ${C}_{w} = -\frac{1}{{B}_{w}}(\frac{{\mathit{dB}}_{w}}{\mathit{dP}})$ | Defined |
| 1/psia 0.00004 | 1/barsa 0.00004 | 1/atma 0.00004 |  |
| 4 | WVISC | WVISC is a real number defining the water viscosity (µw) at the water reference pressure. | Defined |
| cP 0.50 | cP 0.50 | cP 0.50 |  |
| 5 | WVISCOMP | WVISCOMP is a real number defining the water viscosibility (µwc) at the water reference pressure, µwc(Pref) and is defined as: ${\mathrm{μ}}_{\mathit{wc}} = -\frac{1}{{\mathrm{μ}}_{w}}(\frac{d{\mathrm{μ}}_{w}}{\mathit{dP}})$ | Defined |
| 1/psia 0.0 | 1/barsa 0.0 | 1/atma 0.0 |  |
| Notes: |  |  |  |
: PVTW Keyword Description {#tbl-8-122}
Note that provided the first table has been entered, subsequent tables may be defaulted, in this case the prior table is copied to the current table. See the third example for an illustration on how to use this feature.


#### Examples

The following shows the PVTW keyword for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set to one.


```
--
--       WATER PVT TABLE
--
PVTW
--       REF PRES  BW         CW        VISC     VISC
--       PSIA      RB/STB     1/PSIA    CPOISE   GRAD
--       --------  --------   -------   ------   ------
         4840.0    1.019     2.7E-6     0.370    1*         / TABLE NO. 01
```


The next example shows the PVTW keyword for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set to three.


```
--
--       WATER PVT TABLE
--
PVTW
--       REF PRES  BW         CW        VISC     VISC
--       PSIA      RB/STB     1/PSIA    CPOISE   GRAD
--       --------  --------   -------   ------   ------
         4640.0    1.008     2.5E-6     0.350    1*         / TABLE NO. 01
         4840.0    1.019     2.7E-6     0.370    1*         / TABLE NO. 02
         4940.0    1.030     2.8E-6     0.390    1*         / TABLE NO. 03
```


The above example defines three water PVT tables and assumes that NTPVT equals three on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


The third, and final example, shows the PVTW keyword for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set to four. Here table two defaults to table one, and table four defaults to table three


```
--
--       WATER PVT TABLE
--
PVTW
--       REF PRES  BW         CW        VISC     VISC
--       PSIA      RB/STB     1/PSIA    CPOISE   GRAD
--       --------  --------   -------   ------   ------
         4640.0    1.008     2.5E-6     0.350    1*         / TABLE NO. 01
                                                            / TABLE NO. 02
         4940.0    1.030     2.8E-6     0.390    1*         / TABLE NO. 03
                                                            / TABLE NO. 04

```

Note that there is no terminating “/” for this keyword.