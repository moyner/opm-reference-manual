### AQUCON – Define Numerical Aquifer Connections to the Grid {#kw-AQUCON}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

AQUCON keyword defines how numerical aquifers are connected to the simulation grid and these type of  aquifers are characterized by the [AQUNUM](#kw-AQUNUM) keyword in the [GRID](#kw-GRID) section. Analytical aquifers are connected to the simulation grid by the [AQUANCON](#kw-AQUANCON) keyword in the [GRID](#kw-GRID) section, this includes the Carter-Tracy and Fetkovich analytical aquifers, both of which are implemented in OPM Flow. Both aquifer types dimensions are declared by the [AQUDIMS](#kw-AQUDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | AQUID | AQUID is a positive integer greater than or equal to one and less than or equal to the maximum number of numerical aquifers as defined by the MXNAQN variable on the [AQUDIMS](#kw-AQUDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, that defines the aquifer to be connected to the grid. | None |
| 2 | I1 | A positive integer that defines the lower bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to I2 and NX. | 1 |
| 3 | I2 | A positive integer that defines the upper bound of the cells in the I-direction to be connected to the aquifer and must be greater than or equal to I1 and less than or equal to NX | NX |
| 4 | J1 | A positive integer that defines the lower bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to one and less than or equal to J2 and NY. | 1 |
| 5 | J2 | A positive integer that defines the upper bound of the cells in the J-direction to be connected to the aquifer and must be greater than or equal to JI and less than or equal to NY. | NY |
| 6 | K1 | A positive integer that defines the lower bound of the cells in the K-direction to be to be connected to the aquifer and must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 7 | K2 | A positive integer that defines the upper bound of the cells in the K-direction to be connected to the aquifer and must be greater than or equal to KI and less than or equal to NZ. | NZ |
| 8 | AQUFACE | AQUFACE is a character string that sets the connection “face” of the cells declared by this record and should be set to one of the following: | None |
| 9 | AQUMULT | AQUMULT is a positive real number greater than or equal to zero that scales the OPM Flow calculated transmissibility between the AQUID aquifer and the grid cell connections defined by this record. The default value of one sets the transmissibility between the aquifer and grid cells to the OPM Flow calculated value. | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| 10 | AQUOPT1 | AQUOPT1 is a defined integer value set to either zero or one, that defines the area to be used in calculating the connection transmissibility between the aquifer and the grid cells: | 0 |
| dimensionless | dimensionless | dimensionless |  |
| 11 | AQUOPT2 | AQUOPT2 is a character string that sets the cell face connection and should be set to one of the following: | NO |
| 12 | VEOPT1 | Vertical Equilibrium Option Number 1– Not Used | 1 |
| 13 | VEOPT2 | Vertical Equilibrium Option Number 2– Not Used | 1 |
| Notes: |  |  |  |
: AQUCON Keyword Description {#tbl-6-8}
::: {.callout-note}
If the AQUCON keyword has been utilized in the run deck then OPM Flow will write the AQUIFERN array to the *.[INIT](#kw-INIT) file in order to visualize the aquifer connections in OPM ResInsight. This is accomplished by setting the AQUIFERN value to 2^(AQUID-1) for cells connected to aquifer AQUID. If a cell is connected to multiple numerical aquifers then AQUIFERN is summed for all aquifers connected to a cell. Note that connecting cells to multiple aquifers is best avoided. Finally, for cells representing the numerical aquifers themselves,  AQUIFERN is set to minus AQUID.
:::


#### Example

The following example defines numerical aquifer number one connected to the I+ face of various cells in the model.


```
--
--        NUMERICAL AQUIFER CONNECTIONS
--
--       ID     ---------- BOX ---------   CONNECT  TRANS  TRANS  ADJOIN
--       NUMBER I1  I2   J1  J2   K1  K2   FACE     MULT   OPTN   CELLS
AQUCON
         1     57  57   28  36   46  58    'I+'     1*     1*     'NO'        /
         1    111 111   38  41   22  31    'I+'     1*     1*     'NO'        /
         1     96  96   44  49   22  31    'I+'     1*     1*     'NO'        /
         1     43  43   28  35   54  58    'I+'     1*     1*     'NO'        /
         1     98  98   38  42   32  40    'I+'     1*     1*     'NO'        /
         1     79  79   41  67    5  11    'I+'     1*     1*     'NO'        /
         1     61  61   48  72   12  17    'I+'     1*     1*     'NO'        /
/

```

See the [AQUNUM](#kw-AQUNUM) keyword in the [GRID](#kw-GRID) section for a complete example on defining and connecting a numerical aquifer to a simulation grid.