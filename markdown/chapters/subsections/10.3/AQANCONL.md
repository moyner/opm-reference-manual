### AQANCONL – Define Analytical Connections to a LGR Grid


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The AQANCON keyword defines how analytical aquifers are connected to a Local Grid Refinement ("LGR") grid, this includes the Carter-Tracy, Fetkovich and Constant Flux analytical aquifers, all of which are implemented in OPM Flow.  Carter-Tracy analytical aquifers are characterized by the AQUCT keyword in the GRID section and Fetkovich analytical aquifers are defined by either the AQUFET or AQUFETP keywords in the SOLUTION section. Finally, the Constant Flux aquifer is defined by the AQUFLUX keyword in SOLUTION section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | AQUID | AQUID is a positive integer greater than or equal to one and less than the maximum number of analytical aquifers as defined by the NANAQU variable on the AQUDIMS keyword in the RUNSPEC section, that defines the aquifer to be connected to the grid. | None |
| 2 | LGRNAME | A character string of up to eight characters in length that defines the name of the LGR that will connect to an analytical aquifer AQUID. The LGR must have been previously defined by the either the CARFIN (Cartesian LGR grid) keyword, or the RADIN/RADIN4 (radial LGR grid) keyword in the GRID section. | None |
| 3 | I1 | A positive integer that defines the LGR's lower bound of the cells in the I-direction to be connected to the aquifer, and must be greater than or equal to one and less than or equal to I2 and NX on the CARFIN keyword for Cartesian grids. | 1 |
| 4 | I2 | A positive integer that defines the LGR's upper bound of the cells in the I-direction to be connected to the aquifer, and must be greater than or equal to I1 and less than or equal to NX on the CARFIN keyword for Cartesian grids. | NX |
| 5 | J1 | A positive integer that defines the LGR's lower bound of the cells in the J-direction to be connected to the aquifer, and must be greater than or equal to one and less than or equal to J2 and NY on the CARFIN keyword for Cartesian grids. | 1 |
| 6 | J2 | A positive integer that defines the LGR's upper bound of the cells in the J-direction to be connected to the aquifer, and must be greater than or equal to JI and less than or equal to NY on the CARFIN keyword for Cartesian grids. | NY |
| 7 | K1 | A positive integer that defines the LGR's lower bound of the cells in the K-direction to be to be connected to the aquifer, and must be greater than or equal to one and less than or equal to K2 and NZ on the CARFIN keyword for Cartesian grids. | 1 |
| 8 | K2 | A positive integer that defines the LGR's upper bound of the cells in the K-direction to be connected to the aquifer, and must be greater than or equal to KI and less than or equal to NZ on the CARFIN keyword for Cartesian grids. | NZ |
| 9 | AQUFACE | AQUFACE is a character string that sets the connection “face” of the cells declared by this record and should be set to one of the following: | None |
| 10 | AQUFLUX | AQUFLUX is a positive real value that sets the fraction of the total influx between the aquifer and the defined cells declared on this keyword. If defaulted the cell face for each cell is applied and if a values is declared then this values is applied to all cells declared by this record. | 1* |
| ft2 | m2 | cm2 |  |
| 11 | AQUCOEF | AQUCOEF is a real positive values that scales the calculated connection between the aquifer and the cells declared on this record. | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| 12 | AQUOPT | AQUOPT is a character string that sets the cell face connection and should be set to one of the following: | NO |
| Notes: |  |  |  |

*Table 10.6: AQANCONL Keyword Description*


::: {.callout-note}
If the AQANCONL keyword has been utilized in the run deck then OPM Flow will write the  AQUIFERA array to the *.INIT file in order to visualize the aquifer connections in OPM ResInsight. This is accomplished by setting the AQUIFERA value to 2(AQUID-1) for cells connected to aquifer AQUID. If a cell is connected to multiple analytical aquifers then AQUIFERA is summed for all aquifers connected to a cell. Note that connecting cells to multiple aquifers is best avoided.
:::


#### Example

The following example defines aquifer number one connected to the J- face of various cells in the LGROP001 LGR, and a second basal aquifer connected to the K+ face.


```
--
--                      LGR ANALYTIC AQUIFER CONNECTION
--
--       ID   LGR       ---------- BOX ---------   CONNECT  AQF    AQF    ADJOIN
--       NUM  NAME      I1  I2   J1  J2   K1  K2   FACE     INFLX  MULTI  CELLS
AQANCONL
         1    LGROP001   1  10   1   15   1   10    J-      1*     1.0     'NO' /
         1    LGROP001   1  10   1   15   12  18    J-      1*     1.0     'NO' /
         2    LGROP001   1  10   1   15   20  20    K+      1*     1.0     'NO' /
/

```

See the AQUCT keyword in the GRID section for a complete example on defining and connecting a Carter-Tracy aquifer to a simulation grid.
