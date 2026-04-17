### RSVD – Equilibration Dissolved Gas-Oil Ratio (Rs) versus Depth Tables {#kw-RSVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RSVD keyword defines the dissolved gas-oil ratio (Rs) versus depth tables for each equilibration region that should be used when there is dissolved gas in the model ([DISGAS](#kw-DISGAS) has been activated in the [RUNSPEC](#kw-RUNSPEC) section) and the EQLOPT1 variable has been set to a positive integer on the [EQUIL](#kw-EQUIL) keyword in the [SOLUTION](#kw-SOLUTION) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding dissolve gas-oil ratio values, [RS](#kw-RS). | None |
| feet | m | cm |  |
| 2 | [RS](#kw-RS) | A columnar vector of real values that defines the dissolved gas-oil ratio values at the corresponding [DEPTH](#kw-DEPTH). | None |
| Mscf/stb | sm3/sm3 | scc/scc |  |
| Notes: |  |  |  |
: RSVD Keyword Description {#tbl-10-30}
Alternatively, the oil bubble-point pressure versus depth tables may be entered using the [PBVD](#kw-PBVD) keyword in the [SOLUTION](#kw-SOLUTION) section instead of this keyword.

See also the [PBVD](#kw-PBVD) and [EQUIL](#kw-EQUIL) keywords in the [SOLUTION](#kw-SOLUTION) section.


#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the following example defines the bubble-point versus depth functions.


```
--
--       DEPTH    RS
--                MSCF/STB
--       ------   --------
RSVD
         3000.0    1.400
         8000.0    1.400                             / RS VS DEPTH EQUIL REGN 01
--       ------   --------
         3000.0    1.400
         8000.0    1.400                             / RS VS DEPTH EQUIL REGN 02
--       ------   --------
         3000.0    1.400
         8000.0    1.400                             / RS VS DEPTH EQUIL REGN 03
```


Here three tables are entered with a constant GOR versus depth relationship.