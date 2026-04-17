### PLYDHFLF – Define Polymer Thermal Degradation Half-Life Tables {#kw-PLYDHFLF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PLYDHFLF keyword defines the polymer thermal degradation half-life with respect to temperature functions for when the polymer option has been activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#kw-TEMP) | A columnar vector of real monotonically increasing down the column values that defines the polymer thermal degradation temperature. | None |
| oF | oC | oC |  |
| 2 | POLHFLF | A columnar vector of real values that defines the corresponding polymer half-life. | None |
| days | days | hours |  |
| Notes: |  |  |  |
: PLYDHFLF Keyword Description {#tbl-8-102}
#### Example


```
--
--       POLYMER THERMAL DEGRADATION HALF-LIFE TABLE
--
PLYDHFLF
--       POLYMER    POLYMER
--       TEMP       HALF-LIFE
--       -------    ---------
             0.0     365.000
            40.0     200.000
            80.0     150.000
           120.0     100.000                               / TABLE NO. 01
--       POLYMER    POLYMER
--       TEMP       HALF-LIFE
--       -------    --------
             0.0     365.000
            50.0     175.000
            75.0     140.000
           100.0     120.000
           125.0      90.000
           150.0      85.000                               / TABLE NO. 02
```


The example defines two polymer thermal degradation half-life tables, based on the NTPVT variable on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section being equal to two and NPPVT variable on the same keyword being greater than or equal to six.