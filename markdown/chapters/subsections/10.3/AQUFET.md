### AQUFET – Define Fetkovich Analytical Aquifer and Connections {#kw-AQUFET}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The AQUFET keyword defines Fetkovich^[Fetkovich, M. J. “A Simplified Approach to Water Influx Calculations - Finite Aquifer Systems,” Journal of Petroleum Technology, (1971) 23, No. 7, 814-828.] analytical aquifers, the aquifer properties, together with the cell connections to the aquifer. Each row entry in the [AQUFETP](#kw-AQUFETP) keyword defines one Fetkovich analytical aquifer and one cell face to be connected to the aquifer.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped; however, see the [AQUFETP](#kw-AQUFETP) keyword in the [SOLUTION](#kw-SOLUTION) section and [AQUANCON](#kw-AQUANCON) keyword in the [GRID](#kw-GRID) section, on how to define and connect Fetkovich analytical aquifers.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DATUM](#kw-DATUM) | [DATUM](#kw-DATUM) is a single positive value that defines the Fetkovich reference datum depth for PRESS. | None |
| feet | m | cm |  |
| 2 | PRESS | PRESS is a single positive value that defines the aquifer pressure at [DATUM](#kw-DATUM). If PRESS is defaulted then the simulator will set the aquifer’s initial reservoir pressure to be in equilibrium with the cells the aquifer is contacted to. Defaulting this parameter will avoid inconsistent equilibration pressures between the reservoir cells and the aquifer. | 1* |
| psia | barsa | atma |  |
| 3 | [PORV](#kw-PORV) |  | None |
| stb | sm3 | scc |  |
| 4 | COMP | COMP is a real number defining the total compressibility (Ct) of the aquifer, that is the rock compressibility (Cf) plus the water compressibility (Cw) at the aquifer datum pressure ([DATUM](#kw-DATUM)) and is defined as: ${C}_{t} = {C}_{f} + {C}_{w}$ | None |
| 1/psia | 1/barsa | 1/atma |  |
| 5 | PI | A real positive number that defines the aquifer productivity index based on the aquifer influx rate per unit pressure drop. | None |
| stb/d/psia | sm3/barsa | scc/hr/atma |  |
| 6 | [PVTW](#kw-PVTW) | A positive integer that defines the aquifer’s [PVTW](#kw-PVTW) water property table. | 1 |
| 7 | I1 | A positive integer that defines the lower bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to I2 and NX. | 1 |
| 8 | I2 | A positive integer that defines the upper bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to I1 and less than or equal to NX | NX |
| 9 | J1 | A positive integer that defines the lower bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to J2 and NY. | 1 |
| 10 | J2 | A positive integer that defines the upper bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to JI and less than or equal to NY. | NY |
| 11 | K1 | A positive integer that defines the lower bound of the cells in the K-direction to be to be connected to the aquifer and must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 12 | K2 | A positive integer that defines the upper bound of the cells in the K-direction to be connected to the aquifer and must be greater than or equal to KI and less than or equal to NZ. | NZ |
| 13 | AQUFACE | AQUFACE is a character string that sets the connection “face” of the cells declared by this record and should be set to one of the following: | None |
| 14 | SALTCON | SALTCON is a real positive number that defines the initial salt concentration in the aquifer. This variable is ignored by OPM Flow. | 0.0 |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |
: AQUFET Keyword Description {#tbl-10-7}
Note this keyword should only be used in equilibration and enumerated initialize runs, that is it should be omitted from [RESTART](#kw-RESTART) runs.


::: {.callout-note}
If the model is unstable then this may be due to an aquifer not being in equilibrium with the connecting reservoir blocks, for example the aquifer is connected to only hydrocarbon reservoir cells. Try commenting out the aquifer and see if this resolves the instabilities.
:::


#### Example

Given the following grid and aquifer dimensions in the [RUNSPEC](#kw-RUNSPEC) section:


```
-- ==============================================================================
--
-- RUNSPEC SECTION
--
-- ==============================================================================
RUNSPEC   --
--       MAX     MAX     MAX
--       NDIVIX  NDIVIY  NDIVIZ
DIMENS
         20      1       5                                                    /

--       AQF     AQF     AQF     AQF     AQF     AQF    AQF    AQF
--       MXAQN   MXNAQC  NIFTBL  NRIFTB  NANAQU  NCAMAX MXNALI MXAAQL
AQUDIMS
         1*      1*      5       100     1       1*     1*     1*              /
```


The Fetkovich Analytical aquifer is defined in the [SOLUTION](#kw-SOLUTION) sections as:


```
-- ==============================================================================
--
-- SOLUTION SECTION
--
-- ==============================================================================
SOLUTION --
--                      FETKOVICH AQUIFER DESCRIPTION AND CONNECTIONS
--
--       DATUM  AQF    AQF    AQF     AQF  AQF -------- BOX ------- CONNECT SALT
--       DEPTH  PRESS  VOLM   COMP    PI   PVT I1  I2  J1  J2  K1  K2 FACE  CONC
--
AQUFET
         1130.  1*    1.0E+12 3.0E-5  500E3 1   1   1   1   1   1   1  'J-'  /
```


Here one Fetkovich Analytical aquifer is connected to a single cell (1, 1, 1) at the J- face (or X- face) of the grid.