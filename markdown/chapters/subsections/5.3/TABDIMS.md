### TABDIMS – Define the Number of Tables and the Table Dimensions {#kw-TABDIMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The TABDIMS keyword defines the maximum number of tables for a given table type dataset and the maximum number of entries for the various tables.  The commercial simulator combines both the black-oil and compositional simulator variables on this keyword; however, although all the parameters are explained below only the black-oil parameters are used by OPM Flow.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NTSFUN | A positive integer that defines the number of relative permeability table sets defined in the input deck. The tables are allocated to different parts of the grid by the [SATNUM](#kw-SATNUM) keyword. | 1 |
| 2 | NTPVT | A positive integer that defines the number of fluid property table sets  defined in the input deck. The tables are allocated to different parts of the grid by the [PVTNUM](#kw-PVTNUM) keyword. | 1 |
| 3 | NSSFUN | A positive integer that defines the maximum number of saturation entries in the relative permeability tables defined in the input deck. | 20 |
| 4 | NPPVT | A positive integer that defines the maximum number of pressure entries in the PVT tables. | 20 |
| 5 | NTFIP | A positive integer defining the maximum number of regions in the [FIPNUM](#kw-FIPNUM) region array. Note that this parameter may also be set on the [REGDIMS](#kw-REGDIMS) keyword as well. If NTFIP is set in both places then the maximum value is used. | 1 |
| 6 | NRPVT | A positive integer that defines the maximum number of Rs and Rv entries in the PVT tables. If the [DISGAS](#kw-DISGAS) and [VAPOIL](#kw-VAPOIL) options have not been activated then this parameter is ignored. | 20 |
| 7 | NRVPVT | A positive integer that defines the maximum number of Rv entries in the PVT tables for the commercial compositional simulator. | 20 |
| 8 | NTENDP | A positive integer that defines the maximum number of saturation end-point depth tables. The end-point depth tables are used to re-scale the saturation tables as a function of depth as oppose to being a grid block property. NTENDP may also be specified on the [ENDSCALE](#kw-ENDSCALE) keyword,  and if specified on both here and on the [ENDSCALE](#kw-ENDSCALE) keyword the maximum value of the two is used. | 1 |
| 9 | NMEOSR | A positive integer that defines the maximum number of reservoir equations of states for the commercial compositional simulator. | 1 |
| 10 | NMEOSS | A positive integer that defines the maximum number of separator or surface equations of states for the commercial compositional simulator. | 1 |
| 11 | MXNFLX | A positive integer defining the maximum number flux regions in the [FLUXNUM](#kw-FLUXNUM) region array. MXNFLX can also be defined on the [REGDIMS](#kw-REGDIMS) keywords as well.  If MXNFLX is defined both here and on the [REGDIMS](#kw-REGDIMS) keyword then the maximum value of the two is used. | 10 |
| 12 | MXNTHR | A positive integer that defines the maximum number of thermal regions for the commercial compositional simulator. | 1 |
| 13 | NTROCC | A positive integer that defines the number of rock compressibility entries enter by the [ROCK](#kw-ROCK) keyword defined in the input deck. The [ROCK](#kw-ROCK) data is allocated to different parts of the grid by the either the [PVTNUM](#kw-PVTNUM) or [ROCKNUM](#kw-ROCKNUM) keywords in the [REGIONS](#kw-REGIONS) section. If NTROCC is defaulted then the [PVTNUM](#kw-PVTNUM) array will be used to allocate the [ROCK](#kw-ROCK) keyword data to the grid blocks; whereas, if a value is entered then the [ROCKNUM](#kw-ROCKNUM) array will be used instead. See also the [ROCKOPTS](#kw-ROCKOPTS) keyword in the [PROPS](#kw-PROPS) section that can be used to redefine if the [PVTNUM](#kw-PVTNUM), [ROCKNUM](#kw-ROCKNUM) or [SATNUM](#kw-SATNUM) arrays should be employed to allocate the [ROCK](#kw-ROCK) keyword data. | 1* |
| 14 | MXNPMR | A positive integer that defines the maximum number of pressure maintenance regions for the commercial compositional simulator. | 0 |
| 15 | NTABKT | A positive integer that defines the maximum number of temperature dependent K-value tables for the when the thermal option is activated in the commercial compositional simulator. | 0 |
| 16 | NTALPHA | A positive integer that defines the maximum number of transport coefficient tables for the commercial compositional simulator. | 0 |
| 17 | NASPKA | A positive integer that defines the maximum number of maximum number of entries in the ASPKDAM keyword tables for the commercial compositional simulator. | 10 |
| 18 | MXRAWG | A positive integer that defines the maximum number of maximum number of entries in the ASPREWG keyword tables for the commercial compositional simulator. | 10 |
| 19 | MXRASO | A positive integer that defines the maximum number of pressure maintenance regions for the commercial compositional simulator. | 10 |
| 20 |  | Not Used | 1* |
| 21 | MCASPP | A positive integer that defines the maximum number of column entries in the ASPPW2D keyword tables for the commercial compositional simulator. | 5 |
| 22 | MRASPP | A positive integer that defines the maximum number of row entries in the ASPPW2D keyword tables for the commercial compositional simulator. | 5 |
| 23 | MXRATF | A positive integer that defines the maximum number of entries in the ASPWETF table for the commercial compositional simulator. | 5 |
| 24 | MXNKVT | A positive integer that defines the maximum number of composition dependent K-value tables for the commercial compositional simulator. | 0 |
| 25 | RESVED | Not Used | 1* |
| Notes: |  |  |  |
: TABDIMS Keyword Description {#tbl-5-44}
#### Example


```
--
--       NO.     NO.     MAX     MAX     MAX     MAX    E300
--       NTSFUN  NTPVT   NSSFUN  NPPVT   NTFIP   NRPVT  BLANK  NTEND
TABDIMS
         15      9       40      30      1*      1*     1*     1               /
```


The above example defines number of relative permeability tables to be 15 with a maximum number of rows for each table set to 40, and the number of PVT tables to be nine with a maximum number of 30 rows per table.