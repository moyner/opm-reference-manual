### ROCKCOMP – Activate Rock Compaction


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword activates rock compaction and defines various rock compaction options for the run.  By default OPM Flow models rock compaction via pore volume compressibility as entered on the [ROCK](#__RefHeading___Toc45809_719036256) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. This keyword enables pressure dependent pore volume and transmissibility multipliers for rock compaction that are entered in the [PROPS](#__RefHeading___Toc39329_784232322) section using the [ROCKTAB](#__RefHeading___Toc107256_3812137098) keyword. Currently OPM Flow only supports the default options for rock compaction.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ROCKOPT | A character string that defines the rock compaction option based on one of the following character strings: Only the REVERS and IRREVERS options are supported by OPM Flow. | REVERS |
| 2 | NTROCC | A positive integer that defines the number of rock compaction tables, that is the number of [ROCKTAB](#__RefHeading___Toc107256_3812137098) tables to be used by OPM Flow. | 1 |
| 3 | WATINOPT | A character string that states if the water induced rock compaction option should be used (YES) or not (NO).  If set to YES then either the [ROCKTABW](#__RefHeading___Toc266648_516898843) or the [ROCK2D](#__RefHeading___Toc174483_4194303431) and [ROCKWNOD](#__RefHeading___Toc189921_4194303431) keywords should be entered in the [PROPS](#__RefHeading___Toc39329_784232322) section. | NO |
| 4 | PORTXROP | A character string that specifies the model to be used for when transmissibility is dependent on porosity,  and should be set to either: This option is used in the commercial compositional simulator and is therefore ignored by OPM Flow. | 1* |
| 5 | CARKZEXP | The exponent constant in the Carmen-Kozeny porosity-transmissibility equation for when PORTXROP has been set to CZ. This option is used in the commercial compositional simulator and is therefore ignored by OPM Flow. | 0.0 |
| Notes: |  |  |  |

*Table 5.38: ROCKCOMP Keyword Description*


#### Example


```
--
--       ROCK   NUMBER   WAT     POR-TRAN
--       OPTN   TABLES   INDUCE  OPTION
ROCKCOMP
         REVERS 5        NO      1*                                            /
```


The above example defines the default values for the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword with five rock compaction tables.
