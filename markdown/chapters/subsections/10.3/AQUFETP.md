### AQUFETP – Define Fetkovich Analytical Aquifers


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [AQUFETP](#__RefHeading___Toc4428_421927891) keyword defines Fetkovich [Fetkovich, M. J. “A Simplified Approach to Water Influx Calculations - Finite Aquifer Systems,” Journal of Petroleum Technology, (1971) 23, No. 7, 814-828.] analytical aquifers and the aquifer properties. Each row entry in the [AQUFETP](#__RefHeading___Toc4428_421927891) keyword defines one Fetkovich analytical aquifer. In order to fully define this type of aquifer, the aquifer must be connected to the reservoir using the [AQUANCON](#__RefHeading___Toc177536_3429068809) keyword in the [GRID](#__RefHeading___Toc38674_784232322) or [SOLUTION](#__RefHeading___Toc43947_784232322) sections.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | AQUID | A positive integer greater than or equal to one and less than or equal to NANAQ on the [AQUDIMS](#__RefHeading___Toc10103_3701168388) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the Fetkovich aquifer number. | 1 |
| 2 | [DATUM](#__RefHeading___Toc135613_1317547213) | [DATUM](#__RefHeading___Toc135613_1317547213) is a single positive value that defines the Fetkovich reference datum depth for PRESS. | None |
| feet | m | cm |  |
| 3 | PRESS | PRESS is a single positive value that defines the aquifer pressure at [DATUM](#__RefHeading___Toc135613_1317547213). If PRESS is defaulted then the simulator will set the aquifer’s initial reservoir pressure to be in equilibrium with the cells the aquifer is contacted to. Defaulting this parameter will avoid inconsistent equilibration pressures between the reservoir cells and the aquifer. | 1* |
| psia | barsa | atma |  |
| 4 | [PORV](#__RefHeading___Toc96547_718313858) | A real positive value that defines the initial water volume of the aquifer. | None |
| stb | sm3 | scc |  |
| 5 | COMP | COMP is a real number defining the total compressibility (Ct) of the aquifer, that is the rock compressibility (Cf) plus the water compressibility (Cw) at the aquifer datum pressure ([DATUM](#__RefHeading___Toc135613_1317547213)) and is defined as: | None |
| 1/psia | 1/barsa | 1/atma |  |
| 6 | PI | A real positive number that defines the aquifer productivity index based on the aquifer influx rate per unit pressure drop. | None |
| stb/d/psia | sm3/d/barsa | scc/hr/atma |  |
| 7 | [PVTW](#__RefHeading___Toc2086106_3315222525) | A positive integer that defines the aquifer’s [PVTW](#__RefHeading___Toc2086106_3315222525) water property table. | 1 |
| 8 | SALTCON | SALTCON is a real positive number that defines the initial salt concentration in the aquifer, for when the simulator's Brine Model has been activated via the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. This variable is ignored by OPM Flow. | 0.0 |
| lb/stb | kg/sm3 | gm/scc |  |
| 9 | [TEMP](#__RefHeading___Toc146397_3544483072) | [TEMP](#__RefHeading___Toc146397_3544483072) is a real positive number that defines the initial temperature of the aquifer at [DATUM](#__RefHeading___Toc135613_1317547213) for use with OPM Flow's thermal option. The [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section must be activated to use this option. | 1* |
| oF | oC | oC |  |
| Notes: |  |  |  |

*Table 10.8: AQUFETP Keyword Description*


Note this keyword should only be used in equilibration and enumerated initialize runs, that is it should be omitted from [RESTART](#__RefHeading___Toc135629_1317547213) runs.


| Note If the model is unstable then this may be due to an aquifer not being in equilibrium with the connecting reservoir blocks, for example if the aquifer is connected to some hydrocarbon reservoir cells. Try commenting out the aquifer and see if this resolves the instabilities, and if so amend the aquifer connections accordingly. |
| --- |


#### Example

Given the following grid and aquifer dimensions in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section:


```
-- ==============================================================================
--
-- RUNSPEC SECTION
--
-- ==============================================================================
RUNSPEC
--
--       MAX     MAX     MAX
--       NDIVIX  NDIVIY  NDIVIZ
DIMENS
         20      1       5                                                    /

--       AQF     AQF     AQF     AQF     AQF     AQF    AQF    AQF
--       MXAQN   MXNAQC  NIFTBL  NRIFTB  NANAQU  NCAMAX MXNALI MXAAQL
AQUDIMS
         1*      1*      5       100     1       1*     1*     1*              /
```

The  Fetkovich analytical aquifer is defined in the [SOLUTION](#__RefHeading___Toc43947_784232322) sections as:


```
-- ==============================================================================
--
-- SOLUTION SECTION
--
-- ==============================================================================
SOLUTION --
--                      FETKOVICH AQUIFER DESCRIPTION
--
--      ID   DATUM   AQF    AQF    AQF     AQF    AQF   SALT
--      NUM  DEPTH   PRESS  VOLM   COMP    PI     PVT   CONC
--
AQUFETP
         1   1130.   1*    1.0E+12 3.0E-5  500E3  1     0.0                    /
/
```

And the connection of the aquifer is set in the [GRID](#__RefHeading___Toc38674_784232322) or the [SOLUTION](#__RefHeading___Toc43947_784232322) sections as:


```
--
--                      ANALYTIC AQUIFER CONNECTION
--
--       ID     ---------- BOX ---------   CONNECT  AQF    AQF      ADJOIN
--       NUMBER I1  I2   J1  J2   K1  K2   FACE     INFLX  MULTI    CELLS
AQUANCON
         1      1   1    1   1    1   1     J-      1.0    1.0      'NO'        /
/
```


Here one Fetkovich analytical aquifer is connected to a single cell (1, 1, 1) at the J- face (or Y- face) of the cell.
