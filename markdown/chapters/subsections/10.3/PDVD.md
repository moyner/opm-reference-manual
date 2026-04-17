### PDVD – Define Equilibration Dew-Point versus Depth Tables {#kw-PDVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PDVD keyword defines the dew-point pressure versus depth tables for each equilibration region that should be used when there is vaporized oil in the model ([VAPOIL](#kw-VAPOIL) has been activated in the [RUNSPEC](#kw-RUNSPEC) section) and the EQLOPT2 variable has been set to a positive integer on the [EQUIL](#kw-EQUIL) keyword in the [SOLUTION](#kw-SOLUTION) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding dew-point values, PDVALS. | None |
| feet | m | cm |  |
| 2 | PDVALS | A columnar vector of real values that defines the gas dew-point values at the corresponding [DEPTH](#kw-DEPTH). | None |
| psia | barsa | atma |  |
| Notes: |  |  |  |
: PDVD Keyword Description {#tbl-10-22}
Alternatively, the vaporized oil-gas ratio (condensate-gas ratio) versus depth tables may be entered using the [RVVD](#kw-RVVD) keyword in the [SOLUTION](#kw-SOLUTION) section instead of this keyword.

See also the [RVVD](#kw-RVVD) and [EQUIL](#kw-EQUIL) keywords in the [SOLUTION](#kw-SOLUTION) section.


#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the following example defines the bubble-point versus depth functions.


```
--
--       DEPTH    PSAT
--                PRESS
--       ------   ------
PDVD
         3000.0   2000.0
         8000.0   2025.0                            / PSAT VS DEPTH EQUIL REGN 01
--       ------   ------
         3000.0   2100.0
         8000.0   2125.0                            / PSAT VS DEPTH EQUIL REGN 02
--       ------   ------
         3000.0   2200.0
         8000.0   2225.0                            / PSAT VS DEPTH EQUIL REGN 03
```

Here three tables are entered and each table is terminated by a “/” and there is no keyword terminating “/”.