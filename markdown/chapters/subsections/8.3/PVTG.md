### PVTG – Gas PVT Properties for Wet Gas with Vaporized Oil {#kw-PVTG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PVTG defines the gas PVT properties for wet gas^[Natural gas that contains significant heavy hydrocarbons such as propane, butane and other liquid hydrocarbons is known as wet gas or rich gas. The general rule of thumb is if the gas contains less methane (typically less than 85% methane) and more ethane, and other more complex hydrocarbons, it is labeled as wet gas. Wet gas normally has GOR's less than 100,000 scf/stb or 18,000 Sm3/m3, with the condensate having a gravity greater than 50 oAPI.]. This keyword should be used when the [VAPOIL](#kw-VAPOIL) keyword has be declared in the [RUNSPEC](#kw-RUNSPEC) section indicating that that vaporized oil (more commonly referred to as condensate) is present in the wet gas phase. The keyword may be used for gas-water and oil-water-gas input decks that contain the oil and gas phases.


| No. | Name | Description | Default |  |
| --- | --- | :------ | --- | --- |
| Field | Metric | Laboratory |  |  |
| 1 | PRESS | A real monotonically increasing down the column vector that defines the gas phase pressure, associated with the saturated condensate-gas ratio (“CGR”) or Rv,  the gas formation volume factor and the gas viscosity for the corresponding pressure for the stated saturated RVS. For a given PRESS the variability of the gas formation volume factor and the gas viscosity with respect to the under-saturated Rv is optionally included as a sub table under RVU, FVFU and VISU columns, that is it is not necessary to repeat PRESS for each sub table entry. However, each sub table must be terminated by a “/”. The under saturated Rv entries are optional, except for perhaps the last  PRESS entry to define the PVT properties above the initial saturation pressure. | None |  |
| psia | barsa | atma |  |  |
| 2 | RVS | RVU | A columnar vector of real positive number for both the saturated (RVS) and under saturated (RVU) Rv sub table entries. The RVS entry on the main table is the saturated CGR at the pressure indicated by PRESS and may be increasing or decreasing in value as PRESS varies. Subsequent under-saturated Rv for a sub table at the given PRESS, as defined by RVU, are monotonically decreasing for entries in a given sub table. | None |
| stb/Mscf | sm3/sm3 | scc/scc |  |  |
| 3 | FVFS | FVFU | A columnar vector of real decreasing down the column values that defines the corresponding gas phase formation volume factor for a given pressure (PRESS) and for a given Rv (either RVS or RVU). | None |
| rb/Mscf | rm3/sm3 | rcc/scc |  |  |
| 4 | VISS | VISU | VISS a columnar vector of real increasing down the column values that defines the corresponding gas phase viscosity for a given pressure (PRESS) and for a given RVS. VISU a columnar vector of real decreasing from VISS down the column values that defines the corresponding gas phase viscosity for a given pressure (PRESS) and for a given RVU. | None |
| cP | cP | cP |  |  |
| Notes: |  |  |  |  |
: PVTG Keyword Description {#tbl-8-117}
Note that provided the first table has been entered, subsequent tables may be defaulted, in this case the prior table is copied to the current table. See the second example for an illustration on how to use this feature.


::: {.callout-note}
If the [VAPWAT](#kw-VAPWAT) keyword in the [RUNSPEC](#kw-RUNSPEC) section is also present in the input deck, then the PVTG keyword in the [PROPS](#kw-PROPS) section should be used to define the gas properties as function of pressure and [RV](#kw-RV), assuming water-saturated gas. Also, in this case, the [PVTGW](#kw-PVTGW) keyword, also in the [PROPS](#kw-PROPS) section, should also be in the input deck. In this case, [PVTGW](#kw-PVTGW) defines the gas properties as function of pressure and [RVW](#kw-RVW), assuming oil-saturated gas.
:::


#### Example

The first example defines two wet gas PVT tables assuming NTPVT equals two, NPPVT is greater than or equal to eight, and NRPVT greater than or equal to two on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


```
--
--       GAS PVT TABLE FOR WET GAS WITH VAPORIZED OIL
--
PVTG
--       PRES       RV           BG           VISC
--       BARSA    SM^3/SM^3     RM^3/SM^3       CPOISE
--      ------    ---------    -------       ------
           20     0.000132      0.042340      0.01344
                  0             0.042310      0.01389      /
           40     0.000124      0.020460      0.01420
                  0             0.020430      0.01450      /
           60     0.000126      0.013280      0.01526
                  0             0.013250      0.01532      /
           80     0.000135      0.009770      0.01660
                  0             0.009730      0.01634      /
          100     0.000149      0.007730      0.01818
                  0             0.007690      0.01752      /
          120     0.000163      0.006426      0.01994
                  0             0.006405      0.01883      /
          140     0.000191      0.005541      0.02181
                  0             0.005553      0.02021      /
          160     0.000225      0.004919      0.02370
                  0             0.004952      0.02163      /
                                                           / TABLE NO. 1
--       PRES       RV           BG           VISC
--       BARSA    SM^3/SM^3     RM^3/SM^3       CPOISE
--      ------    ---------    -------       ------
           20     0.000132      0.042340      0.01344      /
           40     0.000124      0.020460      0.01420      /
           60     0.000126      0.013280      0.01526      /
           80     0.000135      0.009770      0.01660      /
          100     0.000149      0.007730      0.01818      /
          120     0.000163      0.006426      0.01994      /
          140     0.000191      0.005541      0.02181      /
          160     0.000225      0.004919      0.02370
                  0             0.004952      0.02163      /
                                                           / TABLE NO. 2
```


The second example defines four wet gas PVT tables assuming NTPVT equals four, NPPVT is greater than or equal to eight, and NRPVT greater than or equal to two on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Here table two defaults to table one, and table four defaults to table three.


```
--
--       GAS PVT TABLE FOR WET GAS WITH VAPORIZED OIL
--
PVTG
--       PRES       RV           BG           VISC
--       BARSA    SM^3/SM^3     RM^3/SM^3       CPOISE
--      ------    ---------    -------       ------
           20     0.000132      0.042340      0.01344
                  0             0.042310      0.01389      /
           40     0.000124      0.020460      0.01420
                  0             0.020430      0.01450      /
           60     0.000126      0.013280      0.01526
                  0             0.013250      0.01532      /
           80     0.000135      0.009770      0.01660
                  0             0.009730      0.01634      /
          100     0.000149      0.007730      0.01818
                  0             0.007690      0.01752      /
          120     0.000163      0.006426      0.01994
                  0             0.006405      0.01883      /
          140     0.000191      0.005541      0.02181
                  0             0.005553      0.02021      /
          160     0.000225      0.004919      0.02370
                  0             0.004952      0.02163      /
                                                           / TABLE NO. 1
                                                           / TABLE NO. 2
--       PRES       RV           BG           VISC
--       BARSA    SM^3/SM^3     RM^3/SM^3       CPOISE
--      ------    ---------    -------       ------
           20     0.000132      0.042340      0.01344      /
           40     0.000124      0.020460      0.01420      /
           60     0.000126      0.013280      0.01526      /
           80     0.000135      0.009770      0.01660      /
          100     0.000149      0.007730      0.01818      /
          120     0.000163      0.006426      0.01994      /
          140     0.000191      0.005541      0.02181      /
          160     0.000225      0.004919      0.02370
                  0             0.004952      0.02163      /
                                                           / TABLE NO. 3
                                                           / TABLE NO. 4

```

Notice that in both examples there is no terminating “/” for this keyword only for a table and a sub table.