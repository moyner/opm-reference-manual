### COPYREG – Copy an Array to Another Array based on a Region Number {#kw-COPYREG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The COPYREG keyword copies a specified array or part of an array based on cells with a specific region number to another array. The region number array can be [FLUXNUM](#kw-FLUXNUM), [MULTNUM](#kw-MULTNUM) or [OPERNUM](#kw-OPERNUM) and these arrays must be defined and be available before the COPYREG keyword is read by the simulator. The property arrays can be real or integer valued depending on the property array type; however, the property arrays that can be operated on are dependent on which section the COPYREG keyword is being applied in.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | ARRAY-1 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied from. | None |
| 2 | ARRAY-2 | A character string of up to eight characters in length that defines the keyword identifying the array to be copied to. | None |
| 3 | REGION NUMBER | Integer REGION NUMBER is the region for which the array data in (1) should be copied to array data in (2). | None |
| 4 | REGION ARRAY | The REGION ARRAY to use for selecting the REGION NUMBER in (3) for selecting the data to be copied.  REGION ARRAY can have the following values: | M |
| Notes: |  |  |  |
: COPYREG Keyword Description {#tbl-6-20}
Examples of the arrays most commonly operated on in each section are given in @tbl-6-21. Cells colored red indicate arrays that are not supported by OPM Flow operations.


| COPYREG Keyword and Variable Options by Section |  |  |  |  |  |  |
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
: COPYREG Keyword Applicable Arrays by Section {#tbl-6-21}
#### Example


```
--
--       COPY AN ARRAY TO ANOTHER ARRAY BASED ON A REGION NUMBER
--
--       ARRAY     ARRAY     REGION   REGION ARRAY
--       FROM      TO        NUMBER    M / F / O
COPYREG
         PERMX     PERMY     1         M                   / COPY PERMX TO PERMY
         PERMX     PERMZ     1         M                   / COPY PERMX TO PERMZ
/
--
--       NOW RESET PERMZ BASED ON THE MULTNUM REGION NUMBER
--
--
--       MULTIPLY AN ARRAY BY A CONSTANT BASED ON A REGION NUMBER
--
--       ARRAY     CONSTANT  REGION   REGION ARRAY
--                 VALUE     NUMBER    M / F / O
MULTIREG
         PERMX     0.95      1         M                   /
/

```

The above example first copies the [PERMX](#kw-PERMX) property array for region number one to the [PERMY](#kw-PERMY) and [PERMZ](#kw-PERMZ) property arrays for region one using the [MULTNUM](#kw-MULTNUM) array to define the region numbers. After which [PERMZ](#kw-PERMZ) property array for region one is multiplied by 0.5 using the [MULTIREG](#kw-MULTIREG) keyword.