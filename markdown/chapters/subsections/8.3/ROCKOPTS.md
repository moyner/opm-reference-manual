### ROCKOPTS – Define Rock Compaction and Compressibility Options


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ROCKOPTS keyword defines various options with respect to rock compaction and rock compressibility.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ROCKOPT1 | A defined character string that specifies how the overburden pressures supplied by the OVERBURD keyword are applied to the tabulated pressures in the ROCKTAB keywords: ROCKOPT1 should be set to PRESSURE if the OVERBURD is not used in the input deck. Only the default value of PRESSURE is supported. | PRESSURE |
| 2 | ROCKOPT2 | A defined character string that sets the reference pressure option: Note that STORE option should not be used with the OVERBURD keywords as the OVERBURD data will be overwritten. | NOSTORE |
| 3 | ROCKOPT3 | A defined character string that specifies which region array should be used to allocate the various ROCK and ROCKTAB property tables in the model: Only the PVTNUM and ROCKNUM options are currently supported. | PVTNUM |
| 4 | ROCKOPT4 | A defined character string that sets the initial conditions for the HYSTER and BOBERG options: This parameter is ignored by OPM Flow as the ROCKCOMP(ROCKOPT) options of HYSTER and BOBERG are not supported by the simulator. | DEFLATION |
| Notes: |  |  |  |

*Table 8.128: ROCKOPTS Keyword Description*


#### Example


```
--
--       ROCKOPT1  ROCKOPT2   ROCKOPT3  ROCKOPT4
--       PRS/STRE  NO/STORE   ARRAY
--       --------  --------   --------  --------
ROCKOPTS
         PRESSURE  NOSTORE    PVTNUM                       / ROCK COMP OPTIONS
```


The above example defines the default values for the ROCKOPTS keyword.
