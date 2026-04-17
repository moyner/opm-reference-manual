### COPY – Copy Array Data to Another Array {#kw-COPY}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The COPY keyword copies an array (or part of an array) to another array or part of an array. The arrays can be integer or real valued; however, the arrays that can be operated on are dependent on which section the COPY keyword is being applied in.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | ARRAY-1 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied from. | None |
| 2 | ARRAY-2 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied to. | None |
| 3 | I1 | A positive integer that defines the lower bound of the array in the I-direction to be modified must be greater than or equal 1 and less than or equal to I2 and NX. | 1 |
| 4 | I2 | A positive integer that defines the upper bound of the array in the I-direction to be modified must be greater than or equal to II and less than or equal to NX | NX |
| 5 | J1 | A positive integer that defines the lower bound of the array in the J-direction to be modified must be greater than or equal 1 and less than or equal to J2 and NY. | 1 |
| 6 | J2 | A positive integer that defines the upper bound of the array in the J-direction to be modified must be greater than or equal to JI and less than or equal to NY. | NY |
| 7 | K1 | A positive integer that defines the lower bound of the array in the K-direction to be modified must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 8 | K2 | A positive integer that defines the upper bound of the array in the K-direction to be modified must be greater than or equal to KI and less than or equal to NZ. | NZ |
| Notes: |  |  |  |
: COPY Keyword Description {#tbl-6-16}
Examples of the arrays most commonly operated on in each section are given in @tbl-6-17. Cells colored red indicate arrays that are not supported by OPM Flow operations.


| COPY Keyword and Variable Options by Section |  |  |  |  |  |  |
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
: COPY Keyword Applicable Arrays by Section {#tbl-6-17}
#### Example


```
--
--       SOURCE      DESTIN.      ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
COPY
         PERMX       PERMY        1*  1*   1*  1*   1*  1* / CREATE PERMY
         PERMX       PERMZ        1*  1*   1*  1*   1*  1* / CREATE PERMZ
/

--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
MULTIPLY
         PERMZ       0.50000      1*  1*   1*  1*   1*  1* / PERMZ * 0.5
/

```

The above example copies [PERMX](#kw-PERMX) array to the [PERMY](#kw-PERMY) and [PERMZ](#kw-PERMZ) arrays in the [GRID](#kw-GRID) section for all grid blocks in the model. The [PERMZ](#kw-PERMZ) array is then multiplied by 0.5 for all grid blocks in the model.