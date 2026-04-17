### OPERATER – Define Mathematical Operations on Arrays by Region {#kw-OPERATER}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The OPERATER keyword is similar to the [OPERATE](#kw-OPERATE) keyword, except it applies the mathematical operation on specific regions, whereas, [OPERATE](#kw-OPERATE) applies the operations on a cell by cell basis. Here the OPERATER keyword performs a mathematical operation on a specified property array, optionally using another property array as input to the function. The keyword allows for various mathematical functions and their associated variables to be defined and applied to the specified region data. Input constants can be integer or real valued depending on the array type; however, the arrays that can be operated on are dependent on which section the OPERATER keyword is being applied in.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | Y | A character string of up to eight characters in length that defines the keyword identifying the array to be modified. | None |
| 2 | REGION | REGION is a positive integer representing the region for which the EQUATION should be applied. The default is to use the region number from the [OPERNUM](#kw-OPERNUM) keyword; however this can be reset to another region array via the ARRAY item on this keyword, provided the array exists at the time the keyword is declared in the input deck. Note also the [OPERNUM](#kw-OPERNUM) keyword must precede the use of the OPERATER keyword. | 0 |
| 3 | EQUATION | A defined character string of up to eight characters that defines the mathematical function to be applied, using the X array and the ALPHA and BETA constants declared on this keyword. EQUATION should be set to one of the following character strings: | None |
| ‘MULTA’  -$Y = αX + β$ ‘POLY’     -$Y =Y + α{X}^{β}$ ‘SLOG’    -$Y = {10}^{α + βX}$ ‘LOG10’  -$Y = log(X)$ ‘LOGE’    -$Y = ln(X)$ ‘INV’       -$Y = \frac{1}{X}$ ‘[MULTX](#kw-MULTX)’ -$Y = αX$ | ‘ADDX’     -$Y = α + X$ ‘[COPY](#kw-COPY)’      -$Y = X$ ‘MAXLIM’   -$Y = \mathit{min}(α,X)$ ‘MINLIM’    -$Y = \mathit{max}(α,X)$ ‘MULTP’     -$Y = α{X}^{β}$ ‘ABS’          -$Y = \|(X)\|$ ‘[MULTIPLY](#kw-MULTIPLY)’ -$Y = \mathit{XY}$ |  |  |
| 4 | X | A character string of up to eight characters in length that defines the keyword identifying the array to be used as an input parameter. | None |
| 5 | ALPHA | An integer or real value that is the α variable in the EQUATION function. | None |
| 6 | BETA | An integer or real value that is the β variable in the EQUATION function. | None |
| 7 | ARRAY | The name of the array for which the REGION variable references. This can be any standard region array as declared in the REGION section ([FIPNUM](#kw-FIPNUM), [PVTNUM](#kw-PVTNUM), etc.), provided the array exists at the time the OPERATER keyword is invoked. In addition, the [MULTNUM](#kw-MULTNUM), [FLUXNUM](#kw-FLUXNUM) and [OPERNUM](#kw-OPERNUM) may be used. Only the default value of [OPERNUM](#kw-OPERNUM) is supported by OPM Flow. | [OPERNUM](#kw-OPERNUM) |
| Notes: |  |  |  |
: OPERATER Keyword Description {#tbl-6-96}
Examples of the arrays most commonly operated on in each section are given in @tbl-6-97. Cells colored red indicate arrays that are not supported by OPM Flow operations.


| OPERATER Keyword and Variable Options by Section |  |  |  |  |  |  |
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
: OPERATER Keyword Applicable Arrays by Section {#tbl-6-97}
Double precision and integer work arrays may also be used to hold temporary values for use in more complex operations. Note that these work arrays are reset to zero at the start of each section of the data file. The names of the double precision work arrays should be of the form 'WORKn', where n is a positive integer that defines the work array index, for example 'WORK1', 'WORK2', and so on. Similarly, the names of integer work arrays should be of the form 'IWORKn', for example 'IWORK1', 'IWORK2', and so on. OPM Flow currently only supports double precision work arrays, and does not currently support using work arrays with "global" arrays ([MULTZ](#kw-MULTZ)*). Note that the permeability arrays (PERM*) are treated as "global" arrays in the [GRID](#kw-GRID) section only. In the commercial simulator the maximum number of double precision and integer work arrays are specified using the [REGDIMS](#kw-REGDIMS) keyword. Whereas, OPM Flow does not impose a limit on the maximum number of work arrays.

Note that care should be exercised when performing operations on integer array data as all transforms are performed using floating point arithmetic operations. In addition, operations on any of the transmissibility arrays ([TRANX](#kw-TRANX), [TRANX](#kw-TRANX)-, [TRANY](#kw-TRANY), [TRANY](#kw-TRANY)-, [TRANZ](#kw-TRANZ), and [TRANZ](#kw-TRANZ)-) may result in unintended consequences as these arrays have zero values on the boundary of the grid. In this use OPM ResInsight to verify and visually inspect the results.


::: {.callout-note}
The OPERATER and [OPERATE](#kw-OPERATE) keywords allow for great flexibility in generating or modifying the simulator’s input arrays. In addition, OPM Flow also has a Python facility to manipulate and calculate data that offers even greater flexibility, but note that this feature is not compatible with the commercial simulator. Finally, OPM ResInsight, the post-processing plotting software, has both Octave and Python scripting facilities that enable both data generation and visual inspection of the results. The resulting calculated arrays can then be exported from OPM ResInsight and “included”  back into OPM Flow, thus maintaining compatibility with the commercial simulator.
:::


#### Example

The first example uses the MULTP function combined with the Net-to-Gross ([NTG](#kw-NTG)) array to re-scale the [MULTX](#kw-MULTX), [MULTY](#kw-MULTY) and [MULTZ](#kw-MULTZ) arrays to reduce the transmissibility in three separate reservoirs based on the reservoir quality ([NTG](#kw-NTG)). This keyword sequence should be in the [GRID](#kw-GRID) section.


```
--
--       MATHEMATICAL OPERATIONS ON ARRAYS BY REGION
--
--       OUTPUT   REGN   OPERATION   SOURCE   ALPHA   BETA    REGN
--       ARRAY    NUM    TYPE        ARRAY    CONST   CONST   ARRAY
OPERATER
         MULTX    1     'MULTP'      NTG      1.00    0.75        / RES1
         MULTY    1     'MULTP'      NTG      1.00    0.75        / RES1
         MULTZ    1     'MULTP'      NTG      1.00    0.75        / RES1

         MULTX    2     'MULTP'      NTG      1.00    0.85        / RES2
         MULTY    2     'MULTP'      NTG      1.00    0.85        / RES2
         MULTZ    2     'MULTP'      NTG      1.00    0.85        / RES2

         MULTX    3     'MULTP'      NTG      1.00    0.50        / RES3
         MULTY    3     'MULTP'      NTG      1.00    0.50        / RES3
         MULTZ    3     'MULTP'      NTG      1.00    0.50        / RES3
/
```

Notice that the ARRAY variable has been defaulted, resulting in [OPERNUM](#kw-OPERNUM) being the regional array for the REGION variable.

The next example shows how to set the maximum gas saturation ([SGU](#kw-SGU)) based on the minimum (lowest) water saturation ([SWL](#kw-SWL)) when using the End-Point Scaling option, in the [PROPS](#kw-PROPS) section.


```
--
--       MATHEMATICAL OPERATIONS ON ARRAYS
--
--       OUTPUT   REGN   OPERATION   SOURCE   ALPHA   BETA    REGN
--       ARRAY    NUM    TYPE        ARRAY    CONST   CONST   ARRAY
OPERATER
         SGU      1     'MULTA'      SWL      -1.0    1.0          /
         SGU      2     'MULTA'      SWL      -1.0    1.0          /
         SGU      3     'MULTA'      SWL      -1.0    1.0          /
/
```


The above example sets the maximum gas saturation to be one minus the minimum water saturation for regions one to three.

The final example shows how to reset the [FIPNUM](#kw-FIPNUM) array when the exported array from the earth model does not correspond to the simulator’s desired numbering scheme.


```
--
--       MATHEMATICAL OPERATIONS ON ARRAYS BY REGION
--
--       RESET FIPNUM BASED ON MULTNUM AND OPERNUM
--
--       DESTIN   REGN   OPERATION   SOURCE   ALPHA   BETA  INPUT  SEGNUM   EQUIL
--       ARRAY    NUM    TYPE        ARRAY    CONST   CONST ARRAY  NUMBER  NUMBER
OPERATER
         FIPNUM    26    'MULTA'   'MULTNUM'  0.00     1          /  26       1
         FIPNUM    44    'MULTA'   'MULTNUM'  0.00     2          /  44       2
         FIPNUM    62    'MULTA'   'MULTNUM'  0.00     3          /  62       3
         FIPNUM    98    'MULTA'   'MULTNUM'  0.00     4          /  98       4
         FIPNUM   116    'MULTA'   'MULTNUM'  0.00     5          / 116       5
         FIPNUM   134    'MULTA'   'MULTNUM'  0.00     6          / 134       6
         FIPNUM    46    'MULTA'   'MULTNUM'  0.00     7          /  46       7
         FIPNUM    64    'MULTA'   'MULTNUM'  0.00     8          /  64       8
         FIPNUM    82    'MULTA'   'MULTNUM'  0.00     9          /  82       9
         FIPNUM   226    'MULTA'   'MULTNUM'  0.00    10          / 226      10
         FIPNUM   262    'MULTA'   'MULTNUM'  0.00    11          / 262      11
         FIPNUM   280    'MULTA'   'MULTNUM'  0.00    12          / 280      12
         FIPNUM   298    'MULTA'   'MULTNUM'  0.00    13          / 298      13
         FIPNUM    33    'MULTA'   'MULTNUM'  0.00    14          /  33      14
         FIPNUM    51    'MULTA'   'MULTNUM'  0.00    15          /  51      15
         FIPNUM   105    'MULTA'   'MULTNUM'  0.00    16          / 105      16
         FIPNUM   159    'MULTA'   'MULTNUM'  0.00    17          / 159      17
         FIPNUM   195    'MULTA'   'MULTNUM'  0.00    18          / 195      18
         FIPNUM   267    'MULTA'   'MULTNUM'  0.00    19          / 267      19
         FIPNUM   303    'MULTA'   'MULTNUM'  0.00    20          / 303      20
         FIPNUM   321    'MULTA'   'MULTNUM'  0.00    21          / 321      21
         FIPNUM   339    'MULTA'   'MULTNUM'  0.00    22          / 339      22
         FIPNUM    54    'MULTA'   'MULTNUM'  0.00    23          /  54      23
         FIPNUM    72    'MULTA'   'MULTNUM'  0.00    24          /  72      24
         FIPNUM   108    'MULTA'   'MULTNUM'  0.00    25          / 108      25
         FIPNUM   144    'MULTA'   'MULTNUM'  0.00    26          / 144      26
         FIPNUM   270    'MULTA'   'MULTNUM'  0.00    27          / 270      27
/
```

Note that operation can only be done in the REGION section as [FIPNUM](#kw-FIPNUM) is only available for use in this section and that the ARRAY variable has been defaulted, resulting in [OPERNUM](#kw-OPERNUM) being the regional array for the REGION variable.