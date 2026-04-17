### RVVD – Equilibration Vaporized Oil-Gas Ratio (Rv) versus Depth Tables {#kw-RVVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RVVD keyword defines the vaporized oil-gas ratio (Rv) versus depth tables for each equilibration region that should be used when there is vaporized oil in the model ([VAPOIL](#kw-VAPOIL) has been activated in the [RUNSPEC](#kw-RUNSPEC) section) and the EQLOPT2 variable has been set to a positive integer on the [EQUIL](#kw-EQUIL) keyword in the [SOLUTION](#kw-SOLUTION) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding vaporized oil-gas ratio values, [RV](#kw-RV). | None |
| feet | m | cm |  |
| 2 | [RV](#kw-RV) | A columnar vector of real values that defines the vaporized oil-gas ratio values at the corresponding [DEPTH](#kw-DEPTH). | None |
| stb/Mscf | sm3/sm3 | scc/scc |  |
| Notes: |  |  |  |
: RVVD Keyword Description {#tbl-10-33}
Alternatively, the gas dew-point pressure versus depth tables may be entered using the [PDVD](#kw-PDVD) keyword in the [SOLUTION](#kw-SOLUTION) section instead of this keyword.

See also the [PDVD](#kw-PDVD) and [EQUIL](#kw-EQUIL) keywords in the [SOLUTION](#kw-SOLUTION) section.


#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the following example defines the dew-point versus depth functions.


```
--
--       DEPTH    RV
--                STB/MSCF
--       ------   --------
RVVD
         3000.0   0.00725
         8000.0   0.00725                            / RV VS DEPTH EQUIL REGN 01
--       ------   --------
         3000.0   0.00730
         8000.0   0.00730                            / RV VS DEPTH EQUIL REGN 02
--       ------   --------
         3000.0   0.00750
         8000.0   0.00750                            / RV VS DEPTH EQUIL REGN 03
```


Here three tables are entered with a constant CGR versus depth relationship for each equilibration region.