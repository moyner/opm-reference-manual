### SCVD – Define Equilibration Coal Solvent Concentration versus Depth Tables {#kw-SCVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SCVD keyword defines the initial coal solvent concentration versus depth tables for each equilibration region for when the coal phase has been activated in the run via the [COAL](#kw-COAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword may be used in conjunction with the [SOLVCONC](#kw-SOLVCONC) keyword in the [SOLUTION](#kw-SOLUTION) section, to fully describe the initial state of the model. Note both [SOLVCONC](#kw-SOLVCONC) and SCVD are optional as the simulator will calculate the coal gas concentration based on the equilibrium concentration and the block pressure.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding coal solvent concentration, SCVALS. | None |
| feet | m | cm |  |
| 2 | SCVALS | A columnar vector of real values that defines the coal solvent concentration values at the corresponding [DEPTH](#kw-DEPTH). | None |
| Mscf/ft3 | sm3/m3 | scc/cc |  |
| Notes: |  |  |  |
: SCVD Keyword Description {#tbl-10-43}
See also the [SOLVCONC](#kw-SOLVCONC), [GCVD](#kw-GCVD), [GASCONC](#kw-GASCONC) and [GASSATC](#kw-GASSATC) keywords in the [SOLUTION](#kw-SOLUTION) section.


#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the following example defines the coal solvent concentration versus depth functions.


```
--
--       DEPTH    SOLVC
--                MSCF/FT
--       ------   --------
SCVD
          100.0   75.5000
         1000.0   75.5000                            / SC VS DEPTH EQUIL REGN 01
--       ------   --------
          100.0   65.5000
         1000.0   65.5000                            / SC VS DEPTH EQUIL REGN 02
--       ------   --------
          100.0   60.0000
         1000.0   60.0000                            / SC VS DEPTH EQUIL REGN 03
```


Here three tables are entered with a constant coal solvent concentration versus depth relationship for each equilibration region