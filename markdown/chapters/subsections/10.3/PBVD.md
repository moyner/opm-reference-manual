### PBVD – Equilibration Bubble-Point versus Depth Tables {#kw-PBVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PBVD keyword defines the bubble-point pressure versus depth tables for each equilibration region that should be used when there is dissolved gas in the model ([DISGAS](#kw-DISGAS) has been activated in the [RUNSPEC](#kw-RUNSPEC) section) and the EQLOPT1 variable has been set to a positive integer on the [EQUIL](#kw-EQUIL) keyword in the [SOLUTION](#kw-SOLUTION) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding bubble-point values, PBVALS. | None |
| feet | m | cm |  |
| 2 | PBVALS | A columnar vector of real values that defines the oil bubble-point values at the corresponding [DEPTH](#kw-DEPTH). | None |
| psia | barsa | atma |  |
| Notes: |  |  |  |
: PBVD Keyword Description {#tbl-10-20}
Alternatively, the dissolved gas-oil ratio versus depth tables may be entered using the [RSVD](#kw-RSVD) keyword in the [SOLUTION](#kw-SOLUTION) section instead of this keyword. See also the [RSVD](#kw-RSVD) and [EQUIL](#kw-EQUIL) keywords in the [SOLUTION](#kw-SOLUTION) section.


#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the following example defines the bubble-point versus depth functions.


```
--
--       DEPTH    PSAT
--                PRESS
--       ------   ------
PBVD
         3000.0   3000.0
         8000.0   3025.0                            / PSAT VS DEPTH EQUIL REGN 01
--       ------   ------
         3000.0   3100.0
         8000.0   3125.0                            / PSAT VS DEPTH EQUIL REGN 02
--       ------   ------
         3000.0   3200.0
         8000.0   3225.0                            / PSAT VS DEPTH EQUIL REGN 03
```

Here three tables are entered and each table is terminated by a “/” and there is no keyword terminating “/”.