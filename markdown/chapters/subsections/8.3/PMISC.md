### PMISC – Define Miscibility versus Pressure Tables {#kw-PMISC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PMISC defines the transition between immiscible and miscible displacement as a function of oil pressure tables, for when the [MISCIBLE](#kw-MISCIBLE) keyword in the [RUNSPEC](#kw-RUNSPEC) section has be activated. If this keyword is absent from the input deck and [MISCIBLE](#kw-MISCIBLE) keyword in the [RUNSPEC](#kw-RUNSPEC) keyword has been activated, then miscibility is independent of the oil phase pressure.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | A columnar vector of real monotonically increasing down the column   values that defines the oil phase pressure. | None |
| psia | barsa | atma |  |
| 2 | [MISC](#kw-MISC) | A columnar vector of real equal or increasing down the column values that defines the corresponding miscibility factor. [MISC](#kw-MISC) is a scaling that should lie be zero and one, where zero means no miscibility and one means full miscibility. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: PMISC Keyword Description {#tbl-8-110}
#### Example


```
--
--       MISCIBILITY VERSUS PRESSURE TABLES
--
PMISC
--       OIL        MISCIBILE
--       PRESS      FACTOR
--       -------    ---------
          1000.0       0.000
          2000.0       0.250
          3000.0       1.000
          4000.0       1.000                               / TABLE NO. 01
--       OIL        MISCIBILE
--       PRESS      FACTOR
--       -------    ---------
          1500.0       0.000
          2000.0       0.000
          2500.0       0.250
          3000.0       0.350
          3500.0       1.000
          4000.0       1.000                               / TABLE NO. 02
```


The above example defines two miscibility versus pressure tables assuming NTMISC equals two and NSMISC is greater than or equal to six on the [MISCIBLE](#kw-MISCIBLE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.