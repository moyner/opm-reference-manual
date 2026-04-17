### OPERATE – Define Mathematical Operations on Arrays {#kw-OPERATE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The OPERATE keyword performs a mathematical operation on a specified array or part of an array, optionally using another specified array as input to the operation.  The keyword allows for various mathematical functions and their associated variables to be defined and applied to the specified array. Input constants can be integer or real valued depending on the array type; however, the arrays that can be operated on are dependent on which section the OPERATE keyword is being applied in.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | Y | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| 2 | I1 | A positive integer that defines the lower bound of the array in the I-direction to be modified must be greater than or equal to one and less than or equal to I2 and NX. | 1 |
| 3 | I2 | A positive integer that defines the upper bound of the array in the I-direction to be modified must be greater than or equal to I1 and less than or equal to NX | NX |
| 4 | J1 | A positive integer that defines the lower bound of the array in the J-direction to be modified must be greater than or equal to one and less than or equal to J2 and NY. | 1 |
| 5 | J2 | A positive integer that defines the upper bound of the array in the J-direction to be modified must be greater than or equal to J1 and less than or equal to NY. | NY |
| 6 | K1 | A positive integer that defines the lower bound of the array in the K-direction to be modified must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 7 | K2 | A positive integer that defines the upper bound of the array in the K-direction to be modified must be greater than or equal to K1 and less than or equal to NZ. | NZ |
| 8 | EQUATION | A defined character string of up to eight characters that defines the mathematical function to be applied, using the X array and the ALPHA and BETA constants declared on this keyword. EQUATION should be set to one of the following character strings: | None |
| ‘MULTA’    -$Y = αX + β$ ‘POLY’       -$Y =Y + α{X}^{β}$ ‘SLOG’      -$Y = {10}^{α + βX}$ ‘LOG10’    -$Y = log(X)$ ‘LOGE’      -$Y = ln(X)$ ‘INV’         -$Y = \frac{1}{X}$ ‘[MULTX](#kw-MULTX)’   -$Y = αX$ | ‘ADDX’      -$Y = α + X$ ‘[COPY](#kw-COPY)’       -$Y = X$ ‘MAXLIM’   -$Y = \mathit{min}(α,X)$ ‘MINLIM’    -$Y = \mathit{max}(α,X)$ ‘MULTP’     -$Y = α{X}^{β}$ ‘ABS’          -$Y = \|(X)\|$ ‘[MULTIPLY](#kw-MULTIPLY)’ -$Y = \mathit{XY}$ |  |  |
| 9 | X | A character string of up to eight characters in length that defines the keyword identifying the array to be used as an input parameter. | None |
| 10 | ALPHA | An integer or real value that is the α variable in the EQUATION function. | None |
| 11 | BETA | An integer or real value that is the β variable in the EQUATION function. | None |
| Notes: |  |  |  |
: OPERATE Keyword Description {#tbl-6-94}
Examples of the arrays most commonly operated on in each section are given in @tbl-6-95 . Cells colored red indicate arrays that are not supported by OPM Flow operations.


| OPERATE Keyword and Variable Options by Section |  |  |  |  |  |  |
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
: OPERATE Keyword Applicable Arrays by Section {#tbl-6-95}
Double precision and integer work arrays may also be used to hold temporary values for use in more complex operations. Note that these work arrays are reset to zero at the start of each section of the data file. The names of the double precision work arrays should be of the form 'WORKn', where n is a positive integer that defines the work array index, for example 'WORK1', 'WORK2', and so on. Similarly, the names of integer work arrays should be of the form 'IWORKn', for example 'IWORK1', 'IWORK2', and so on. OPM Flow currently only supports double precision work arrays, and does not currently support using work arrays with "global" arrays ([MULTZ](#kw-MULTZ)*). Note that the permeability arrays (PERM*) are treated as "global" arrays in the [GRID](#kw-GRID) section only. In the commercial simulator the maximum number of double precision and integer work arrays are specified using the [REGDIMS](#kw-REGDIMS) keyword. Whereas, OPM Flow does not impose a limit on the maximum number of work arrays.

Note that care should be exercised when performing operations on integer array data as all transforms are performed using floating point arithmetic operations. In addition, operations on any of the transmissibility arrays ([TRANX](#kw-TRANX), [TRANX](#kw-TRANX)-, [TRANY](#kw-TRANY), [TRANY](#kw-TRANY)-, [TRANZ](#kw-TRANZ), and [TRANZ](#kw-TRANZ)-) may result in untended consequences as these arrays have zero values on the boundary of the grid. In this use OPM ResInsight to verify and visually inspect the results.


#### Example

The first example uses the MULTP function combined with the Net-to-Gross ([NTG](#kw-NTG)) array to re-scale the [MULTX](#kw-MULTX), [MULTY](#kw-MULTY) and [MULTZ](#kw-MULTZ) arrays to reduce the transmissibility in three separate reservoirs based on the reservoir quality ([NTG](#kw-NTG)).


```
--
--       MATHEMATICAL OPERATIONS ON ARRAYS BY CELL
--
--       OUTPUT  ---------- BOX ---------  OPERATION  INPUT   ALPHA   BETA
--       ARRAY   I1  I2   J1  J2   K1  K2  ---------  ARRAY   -----   ----
OPERATE
         MULTX   1*  1*   1*  1*     1 32  ‘MULTP’    NTG     1.00    0.75 / RES1
         MULTY   1*  1*   1*  1*     1 32  ‘MULTP’    NTG     1.00    0.75 / RES1
         MULTZ   1*  1*   1*  1*     1 32  ‘MULTP’    NTG     1.00    0.75 / RES1

         MULTX   1*  1*   1*  1*    34 64  ‘MULTP’    NTG     1.00    0.85 / RES2
         MULTY   1*  1*   1*  1*    34 64  ‘MULTP’    NTG     1.00    0.85 / RES2
         MULTZ   1*  1*   1*  1*    34 64  ‘MULTP’    NTG     1.00    0.85 / RES2

         MULTX   1*  1*   1*  1*    67 96  ‘MULTP’    NTG     1.00    0.50 / RES3
         MULTY   1*  1*   1*  1*    67 96  ‘MULTP’    NTG     1.00    0.50 / RES3
         MULTZ   1*  1*   1*  1*    67 96  ‘MULTP’    NTG     1.00    0.50 / RES3
/

```

The next example shows how to set the maximum gas saturation ([SGU](#kw-SGU)) based on the minimum (lowest) water saturation ([SWL](#kw-SWL)) when using the End-Point Scaling option.


```
--
--       MATHEMATICAL OPERATIONS ON ARRAYS
--
--       OUTPUT  ---------- BOX ---------  OPERATION  INPUT   ALPHA   BETA
--       ARRAY   I1  I2   J1  J2   K1  K2  ---------  ARRAY   -----   ----
OPERATE
         SGU     1*  1*   1*  1*   1*  1*  'MULTA'     SWL    -1.0    1.0      /
/
```


The above example sets the maximum gas saturation to be one minus the minimum water saturation.