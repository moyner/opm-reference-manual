### ROCKCOMP – Activate Rock Compaction


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ROCKCOMP keyword activates rock compaction and defines various rock compaction options for the run.  By default OPM Flow models rock compaction via pore volume compressibility as entered on the ROCK keyword in the PROPS section. This keyword enables pressure dependent pore volume and transmissibility multipliers for rock compaction that are entered in the PROPS section using the ROCKTAB keyword. Currently OPM Flow only supports the default options for rock compaction.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ROCKOPT | A character string that defines the rock compaction option based on one of the following character strings: Only the REVERS and IRREVERS options are supported by OPM Flow. | REVERS |
| 2 | NTROCC | A positive integer that defines the number of rock compaction tables, that is the number of ROCKTAB tables to be used by OPM Flow. | 1 |
| 3 | WATINOPT | A character string that states if the water induced rock compaction option should be used (YES) or not (NO).  If set to YES then either the ROCKTABW or the ROCK2D and ROCKWNOD keywords should be entered in the PROPS section. | NO |
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


The above example defines the default values for the ROCKCOMP keyword with five rock compaction tables.
