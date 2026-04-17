### ROCKOPTS – Define Rock Compaction and Compressibility Options


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [ROCKOPTS](#__RefHeading___Toc111814_2939291539) keyword defines various options with respect to rock compaction and rock compressibility.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ROCKOPT1 | A defined character string that specifies how the overburden pressures supplied by the [OVERBURD](#__RefHeading___Toc162159_4194303431) keyword are applied to the tabulated pressures in the [ROCKTAB](#__RefHeading___Toc107256_3812137098) keywords: ROCKOPT1 should be set to PRESSURE if the [OVERBURD](#__RefHeading___Toc162159_4194303431) is not used in the input deck. Only the default value of PRESSURE is supported. | PRESSURE |
| 2 | ROCKOPT2 | A defined character string that sets the reference pressure option: Note that STORE option should not be used with the [OVERBURD](#__RefHeading___Toc162159_4194303431) keywords as the [OVERBURD](#__RefHeading___Toc162159_4194303431) data will be overwritten. | NOSTORE |
| 3 | ROCKOPT3 | A defined character string that specifies which region array should be used to allocate the various [ROCK](#__RefHeading___Toc45809_719036256) and [ROCKTAB](#__RefHeading___Toc107256_3812137098) property tables in the model: Only the [PVTNUM](#__RefHeading___Toc68366_2752266063) and [ROCKNUM](#__RefHeading___Toc118210_2939291539) options are currently supported. | [PVTNUM](#__RefHeading___Toc68366_2752266063) |
| 4 | ROCKOPT4 | A defined character string that sets the initial conditions for the HYSTER and BOBERG options: This parameter is ignored by OPM Flow as the [ROCKCOMP](#__RefHeading___Toc55593_1778172979)(ROCKOPT) options of HYSTER and BOBERG are not supported by the simulator. | DEFLATION |
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


The above example defines the default values for the [ROCKOPTS](#__RefHeading___Toc111814_2939291539) keyword.
