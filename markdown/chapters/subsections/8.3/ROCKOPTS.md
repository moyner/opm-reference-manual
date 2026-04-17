### ROCKOPTS – Define Rock Compaction and Compressibility Options {#kw-ROCKOPTS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ROCKOPTS keyword defines various options with respect to rock compaction and rock compressibility.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | ROCKOPT1 | A defined character string that specifies how the overburden pressures supplied by the [OVERBURD](#kw-OVERBURD) keyword are applied to the tabulated pressures in the [ROCKTAB](#kw-ROCKTAB) keywords: ROCKOPT1 should be set to [PRESSURE](#kw-PRESSURE) if the [OVERBURD](#kw-OVERBURD) is not used in the input deck. Only the default value of [PRESSURE](#kw-PRESSURE) is supported. | [PRESSURE](#kw-PRESSURE) |
| 2 | ROCKOPT2 | A defined character string that sets the reference pressure option: Note that STORE option should not be used with the [OVERBURD](#kw-OVERBURD) keywords as the [OVERBURD](#kw-OVERBURD) data will be overwritten. | NOSTORE |
| 3 | ROCKOPT3 | A defined character string that specifies which region array should be used to allocate the various [ROCK](#kw-ROCK) and [ROCKTAB](#kw-ROCKTAB) property tables in the model: Only the [PVTNUM](#kw-PVTNUM) and [ROCKNUM](#kw-ROCKNUM) options are currently supported. | [PVTNUM](#kw-PVTNUM) |
| 4 | ROCKOPT4 | A defined character string that sets the initial conditions for the HYSTER and BOBERG options: This parameter is ignored by OPM Flow as the [ROCKCOMP](#kw-ROCKCOMP)(ROCKOPT) options of HYSTER and BOBERG are not supported by the simulator. | DEFLATION |
| Notes: |  |  |  |
: ROCKOPTS Keyword Description {#tbl-8-128}
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