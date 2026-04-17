### TRANGL – Define Non-Neighbor Connections Between Global and LGR Cells Manually {#kw-TRANGL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

TRANGL enables Non-Neighbor Connections (“[NNC](#kw-NNC)”) between the global cells and the Local Grid Refinement (“[LGR](#kw-LGR)”) cells to be manually specified, as oppose to the simulator calculating the transmissibilities.  The [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be utilized to define the presence of LGRs in the model and to define various [LGR](#kw-LGR) dimension parameters.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | I1 | A positive integer that defines the [LGR](#kw-LGR) grid block in the I-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NX on the [CARFIN](#kw-CARFIN) keyword in the [GRID](#kw-GRID) section. | None |
| 2 | J1 | A positive integer that defines the [LGR](#kw-LGR) grid block in the J-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NY on the [CARFIN](#kw-CARFIN) keyword in the [GRID](#kw-GRID) section. | None |
| 3 | K1 | A positive integer that defines the [LGR](#kw-LGR) grid block in the K-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NZ on the [CARFIN](#kw-CARFIN) keyword in the [GRID](#kw-GRID) section. | None |
| 4 | I2 | A positive integer that defines the GLOBAL grid block in the I-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NX on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 5 | J2 | A positive integer that defines the GLOBAL grid block in the J-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NY on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 6 | K2 | A positive integer that defines the GLOBAL grid block in the K-direction in a non-neighbor connection, must be greater than or equal to one and less than or equal to NZ on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 7 | TRANSNNC | TRANSNNC is a positive real number greater than or equal to zero that defines the transmissibility between the GLOBAL grid block (I1, J1, K1) and the [LGR](#kw-LGR) grid block (I2, J2, K2). The default value of zero sets the transmissibility between the two cells to zero. | 0.0 |
| cP.rb/day/psia | cP.rm3/day/bars | cP.rcc/hr/atm |  |
| Notes: |  |  |  |
: TRANGL Keyword Description {#tbl-6-130}
#### Example


```
--
--       MANUALLY DEFINE LGR-GLOBAL GRID NON-NEIGHBOR CONNECTIONS
--
--       ----LGR-----   ---GLOBAL----   -- TRANSNCC --
--       I1   J1   K1    I2   J2   K2
TRANGL
         1    1    1     1    1    2        0.2500     /
         1    1    2     1    1    3        0.2500     /
         1    1    3     1    1    4        0.2500     /
/

```

The above example defines the transmissibility between [LGR](#kw-LGR) cell (1, 1, 1) and global cell (1, 1, 2), [LGR](#kw-LGR) cell  (1, 1, 2) and global cell (1, 1, 3) and finally between [LGR](#kw-LGR) cell (1, 1, 3) and global cell (1, 1, 4) to be 0.2500.