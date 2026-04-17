### ADDREG – Add a Constant to an Array based on a Region Number


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ADDREG keyword adds a constant to a specified array or part of an array based on cells with a specific region number. The region number array can be FLUXNUM, MULTNUM or OPERNUM and these arrays must be defined and be available before the ADDREG keyword is read by the simulator. The constant can be an integer or real value depending on the array type; however, the arrays that can be operated on are dependent on which section the ADDREG keyword is being applied in.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ARRAY | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| 2 | CONSTANT | An integer or real value to be added to the ARRAY in the same units as the ARRAY property for a given REGION. | 0 |
| 3 | REGION NUMBER | REGION NUMBER is a positive integer representing the region for which the CONSTANT in (2) should be applied. | None |
| 4 | REGION ARRAY | The REGION ARRAY to use for applying the CONSTANT in (2) based on the REGION NUMBER in (3).  REGION ARRAY can have the following values: | M |
| Notes: |  |  |  |

*Table 6.5: ADDREG Keyword Description*


Examples of the arrays most commonly operated on in each section are given in Table 6.6. Cells colored red indicate arrays that are not supported by OPM Flow operations.


| ADDREG Keyword and Variable Options by Section |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| DX | DEPTH | SWL | ENDNUM | PRESSURE |  |  |
| DY | PORV | SWCR | EQLNUM | SWAT |  |  |
| DZ | TRANX | SWU | FIPNUM | SGAS |  |  |
| PERMX | TRANY | SGL | IMBNUM | RV |  |  |
| PERMY | TRANZ | SGCR | MISCNUM | RS |  |  |
| PERMZ | DIFFX | SGU | PVTNUM | TBLK |  |  |
| MULTX | DIFFY | KRW | ROCKNUM | GI |  |  |
| MULTY | DIFFZ | KRO | SATNUM | OILAPI |  |  |
| MULTZ | TRANR | KRG | WH2NUM | SALT |  |  |
| DR | TRANTHT | PCG |  | GASCONC |  |  |
| DTHETA | DIFFR | PCW |  | SOLVCONC |  |  |
| PERMR | DIFFTHT |  |  | SOLVFRAC |  |  |
| PERMTHT |  |  |  | SFOAM |  |  |
| DZNET |  |  |  | SPOLY |  |  |
| PORO |  |  |  |  |  |  |
| NTG |  |  |  |  |  |  |
| FLUXNUM |  |  |  |  |  |  |
| MULTNUM |  |  |  |  |  |  |
| MPFANUM |  |  |  |  |  |  |
| DIFFX |  |  |  |  |  |  |
| DIFFY |  |  |  |  |  |  |
| DIFFZ |  |  |  |  |  |  |
| DIFFR |  |  |  |  |  |  |
| DIFFTHT |  |  |  |  |  |  |

*Table 6.6: ADDREG Keyword Applicable Arrays by Section*


#### Example


```
--
-- FIRST DEFINE THE PROPERTY ARRAYS AND MULTNUM ARRAYS FOR 10 X 10 X 20 MODEL
--
--  ARRAY    CONSTANT --  ---------- BOX ---------
--                          I1  I2   J1  J2   K1  K2
EQUALS
    PORO      0.2000        1*  1*   1*  1*   1*  1*  / PORO  TO 0.20 IN MODEL
    PERMX     100.00        1*  1*   1*  1*   1*  1*  / PERMX TO 0.10 IN MODEL
    MULTNUM   1             1*  1*   1*  1*   1*  1*  / MULTNUM IN MODEL
    MULTNUM   2             1*  5    1   5    6   6   / MULTNUM IN MODEL
    MULTNUM   3             1*  1*   1*  1*   10  10  / MULTNUM IN MODEL
/
--
–        NOW RESET PORO AND PERMX BASED ON THE MULTNUM REGION NUMBER
--
--       ADD A CONSTANT TO AN ARRAY BASED ON A REGION NUMBER
--
--       ARRAY     CONSTANT  REGION   REGION ARRAY
--                 VALUE     NUMBER    M / F / O                                           ADDREG
      PORO         0.050     1         M                /
      PORO         0.100     2         M                /
      PORO        -0.050     3         M                /
      PERMX        25.00     1         M                /
      PERMX        100.0     2         M                /
      PERMX       -50.00     3         M                /
/
```

The example first defines the PORO and PERMX property arrays for the model and then sets the MULTNUM array to 1 for all cells in the model, after which selected areas of model are assigned various MULTNUM integer values. The ADDREG can then be invoked to add or subtract constant values from the PORO and PERMX arrays for the various MULTNUM regions.
