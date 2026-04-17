### EQUALREG – Sets an Array to a Constant by Region Number {#kw-EQUALREG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The EQUALREG keyword sets a specified array to a constant for cells with a specific region number. The region number array can be [FLUXNUM](#kw-FLUXNUM), [MULTNUM](#kw-MULTNUM) or [OPERNUM](#kw-OPERNUM) and these arrays must be defined and be available before the EQUALREG keyword is read by the simulator. The constant can be an integer or real value depending on the array type; however, the arrays that can be operated on are dependent on which section the EQUALREG keyword is being applied in.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | ARRAY | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| 2 | CONSTANT | An integer or real value to be assigned to the ARRAY in the same units as the ARRAY property for a given REGION | 0 |
| 3 | REGION NUMBER | REGION NUMBER is a positive integer representing the region for which the CONSTANT in (2) should be applied | None |
| 4 | REGION ARRAY | The REGION ARRAY to use for applying the CONSTANT in (2) based on the REGION NUMBER in (3).  REGION ARRAY can have the following values: | M |
| Notes: |  |  |  |
: EQUALREG Keyword Description {#tbl-6-33}
Examples of the arrays most commonly operated on in each section are given in @tbl-6-34. Cells colored red indicate arrays that are not supported by OPM Flow operations.


| EQUALREG Keyword and Variable Options by Section |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| [DX](#kw-DX) | [DEPTH](#kw-DEPTH) | [SWL](#kw-SWL) | [ENDNUM](#kw-ENDNUM) | [PRESSURE](#kw-PRESSURE) |  |  |
| [DY](#kw-DY) | [PORV](#kw-PORV) | [SWCR](#kw-SWCR) | [EQLNUM](#kw-EQLNUM) | [SWAT](#kw-SWAT) |  |  |
| [DZ](#kw-DZ) | [TRANX](#kw-TRANX) | [SWU](#kw-SWU) | [FIPNUM](#kw-FIPNUM) | [SGAS](#kw-SGAS) |  |  |
| [PERMX](#kw-PERMX) | [TRANY](#kw-TRANY) | [SGL](#kw-SGL) | [IMBNUM](#kw-IMBNUM) | [RV](#kw-RV) |  |  |
| [PERMY](#kw-PERMY) | [TRANZ](#kw-TRANZ) | [SGCR](#kw-SGCR) | [MISCNUM](#kw-MISCNUM) | [RS](#kw-RS) |  |  |
| [PERMZ](#kw-PERMZ) | [DIFFX](#kw-DIFFX) | [SGU](#kw-SGU) | [PVTNUM](#kw-PVTNUM) | [TBLK](#kw-TBLK) |  |  |
| [MULTX](#kw-MULTX) | [DIFFY](#kw-DIFFY) | [KRW](#kw-KRW) | [ROCKNUM](#kw-ROCKNUM) | [GI](#kw-GI) |  |  |
| [MULTY](#kw-MULTY) | [DIFFZ](#kw-DIFFZ) | [KRO](#kw-KRO) | [SATNUM](#kw-SATNUM) | [OILAPI](#kw-OILAPI) |  |  |
| [MULTZ](#kw-MULTZ) | [TRANR](#kw-TRANR) | [KRG](#kw-KRG) | [WH2NUM](#kw-WH2NUM) | [SALT](#kw-SALT) |  |  |
| [DR](#kw-DR) | [TRANTHT](#kw-TRANTHT) | [PCG](#kw-PCG) |  | [GASCONC](#kw-GASCONC) |  |  |
| [DTHETA](#kw-DTHETA) | [DIFFR](#kw-DIFFR) | [PCW](#kw-PCW) |  | [SOLVCONC](#kw-SOLVCONC) |  |  |
| [PERMR](#kw-PERMR) | [DIFFTHT](#kw-DIFFTHT) |  |  | [SOLVFRAC](#kw-SOLVFRAC) |  |  |
| [PERMTHT](#kw-PERMTHT) |  |  |  | [SFOAM](#kw-SFOAM) |  |  |
| [DZNET](#kw-DZNET) |  |  |  | [SPOLY](#kw-SPOLY) |  |  |
| [PORO](#kw-PORO) |  |  |  |  |  |  |
| [NTG](#kw-NTG) |  |  |  |  |  |  |
| [FLUXNUM](#kw-FLUXNUM) |  |  |  |  |  |  |
| [MULTNUM](#kw-MULTNUM) |  |  |  |  |  |  |
| [MPFANUM](#kw-MPFANUM) |  |  |  |  |  |  |
| [DIFFX](#kw-DIFFX) |  |  |  |  |  |  |
| [DIFFY](#kw-DIFFY) |  |  |  |  |  |  |
| [DIFFZ](#kw-DIFFZ) |  |  |  |  |  |  |
| [DIFFR](#kw-DIFFR) |  |  |  |  |  |  |
| [DIFFTHT](#kw-DIFFTHT) |  |  |  |  |  |  |
: EQUALREG Keyword Applicable Arrays by Section {#tbl-6-34}
#### Example


```
-- FIRST DEFINE MULTNUM ARRAYS FOR 10 X 10 X 20 MODEL
--
--      ARRAY     CONSTANT    ---------- BOX ---------
--                            I1  I2   J1  J2   K1  K2
EQUALS
        MULTNUM    1          1*  1*   1*  1*   1*  1*     / MULTNUM IN MODEL
        MULTNUM    2          1*  1*   1*  1*   6   6      / MULTNUM IN MODEL
        MULTNUM    3          1*  1*   1*  1*   10  10     / MULTNUM IN MODEL
/
--    NOW SET PORO AND PERMX BASED ON THE MULTNUM REGION NUMBER
--
--       SETS A CONSTANT TO AN ARRAY BASED ON A REGION NUMBER
--
--       ARRAY     CONSTANT  REGION   REGION ARRAY
--                 VALUE     NUMBER    M / F / O                                           EQUALREG
         PORO      0.200     1         M                   /
         PORO      0.150     2         M                   /
         PORO      0.120     3         M                   /
         PERMX    100.00     1         M                   /
         PERMX     75.00     2         M                   /
         PERMX     50.00     3         M                   /
/
```

The example first defines the [MULTNUM](#kw-MULTNUM) array to 1 for all cells in the model, after which selected areas of model are assigned various [MULTNUM](#kw-MULTNUM) integer values. The EQUALREG can then be invoked to set constant values for the [PORO](#kw-PORO) and [PERMX](#kw-PERMX) arrays for the various [MULTNUM](#kw-MULTNUM) regions.