### EQUIL – Define the Equilibration Initialization Data


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the parameters used to initialize the model for when equilibration is calculated by OPM Flow. This is the standard methodology to initialize a model, the non-standard formulation of entering the pressures and saturations for each grid cell is seldom employed in the industry.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DATUM | DATUM is a single positive value that defines the reference datum depth for PRESS. | 0.0 |
| feet | m | cm |  |
| 2 | PRESS | PRESS is a single positive value that defines the pressure at [DATUM](#__RefHeading___Toc135613_1317547213). If the DATUM depth lies above the GOC then PRESS is the pressure with respect to the gas phase. If the DATUM depth is below OWC then PRESS refers to the water phase pressure. Otherwise, PRESS refers to the oil phase pressure. | 0.0 |
| psia | barsa | atma |  |
| 3 | WATCONT |  | 0.0 |
| feet | m | cm |  |
| 4 | WATCAP |  | 0.0 |
| psia | barsa | atma |  |
| 5 | GASCONT |  | 0.0 |
| feet | m | cm |  |
| 6 | GASCAP |  | 0.0 |
| psia | barsa | atma |  |
| 7 | EQLOPT1 | EQLOPT1 is an integer value that sets the initialization option for when dissolved gas is present in the run, as activated by the [DISGAS](#__RefHeading___Toc39767_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. EQLOPT1 is ignored if there is no dissolved gas in the run. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| 8 | EQLOPT2 | EQLOPT2 is an integer value that sets the initialization option for when vaporized oil (condensate) is present in the run, as activated by the [VAPOIL](#__RefHeading___Toc56610_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. EQLOPT2 is ignored if there is no vaporized oil in the run. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| 9 | EQLOPT3 | EQLOPT3 is an integer value that sets the initialization accuracy options for the equilibration calculation. Increasing the value of N increases the accuracy of the calculation, with the maximum value of N being set to 20 by OPM Flow. Note this option should be used with Irregular Corner-Point Grids. EQLOPT3 is ignored for Radial Grids. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| 10 | EQLOPT4 | A positive integer value greater than or equal one and less than or equal to three, that sets the initialization option in the commercial compositional simulator. EQLOPT4 should be defaulted with 1*,  as it is not used by OPM Flow. | None |
| dimensionless | dimensionless | dimensionless |  |
| 11 | EQLOPT5 | A positive integer value that if set to one forces PRESS to be used for the datum pressure in the commercial compositional simulator. EQLOPT5 should be defaulted with either 1*, as it is not used by OPM Flow. | None |
| dimensionless | dimensionless | dimensionless |  |
| 12 | EQLOPT6 | EQLOPT6 is an integer value that sets the initialization option for when vaporized water is present in the run, as activated by the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is an OPM Flow specific parameter for use with simulator's Vaporized Water Model. Note that the allocation of multiple [RVWVD](#__RefHeading___Toc137367_13175472131) tables to each grid cell is through the [EQLNUM](#__RefHeading___Toc73734_2752266063) keyword and not the [PVTNUM](#__RefHeading___Toc68366_2752266063) keyword. EQLOPT6 is ignored if there is no vaporized water in the run. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 10.14: EQUIL Keyword Description*


| Note A common method to initialize a model is by using the [SWATINIT](#__RefHeading___Toc323952_1728001293) property array to set the initial water saturation for each cell in the model. This property is normally exported from a static model, where Saturation Height Functions (“SHF”) have been used to describe the water saturation profile with depth.  In the dynamic model capillary pressure functions are used to described the water profile versus depth. Note that if the [SWATINIT](#__RefHeading___Toc323952_1728001293) array has been used to initialize the model then the fine grid block initialization via the EQLOPT3 variable, should not normally be used, and should be defaulted or set equal to zero; otherwise, the resulting water saturation will not strictly honor the [SWATINIT](#__RefHeading___Toc323952_1728001293) array. |
| --- |


See also the [PRESSURE](#__RefHeading___Toc135627_1317547213), [SGAS](#__RefHeading___Toc137369_1317547213), [SOIL](#__RefHeading___Toc137371_1317547213) and [SWAT](#__RefHeading___Toc137373_1317547213) keywords in the [SOLUTION](#__RefHeading___Toc43947_784232322) section to initialize the model using the non-standard formulation of entering the pressures and saturations for each grid cell.


#### Example


```
--
--       DATUM   DATUM   OWC     PCOW   GOC    PCGO   RS   RV   N    E300  RVW
--       DEPTH   PRESS   DEPTH   ----   DEPTH  ----   OPT  OPT  OPT  OPTS  OPT
EQUIL
         3650.0  1560.0  3712.0  0.00  1000.0  0.00   1    0    -5   2*    1*   /
         3650.0  1560.0  3741.0  0.00  1000.0  0.00   1    0    -5   2*    1*   /
         3650.0  1560.0  3741.0  0.00  1000.0  0.00   1    0    -5   2*    1*   /

```

The above example defines three equilibration records for when NTEQUL equals three on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Here there is no gas cap and the GOC has been set to a value above the reservoirs (1000.0),  and the value of EQLOPT3 (-5) has been explicitly stated.
