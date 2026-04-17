### APIVD – Equilibration Oil API Gravity versus Depth Tables {#kw-APIVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The APIVD keyword defines the oil [API](#kw-API) gravity versus depth tables for each equilibration region when [API](#kw-API) Tracking as been activated by the [API](#kw-API) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding [API](#kw-API) gravity    values,  [API](#kw-API). | None |
| feet | m | cm |  |
| 2 | [API](#kw-API) | A columnar vector of real values that defines the [API](#kw-API) gravity at the corresponding [DEPTH](#kw-DEPTH). The American Petroleum Institute (“[API](#kw-API)”) classifies oils based on an [API](#kw-API) gravity (γ[API](#kw-API)),  or degrees [API](#kw-API) (oAPI), the relationship between relative density (γo) of oil and [API](#kw-API) gravity (γ[API](#kw-API)) is given by: ${\mathrm{γ}}_{\mathit{[API](#kw-API)}} = \frac{141.5}{{\mathrm{γ}}_{o}} - 131.5$ | None |
| oAPI | oAPI | oAPI |  |
| Notes: |  |  |  |
: APIVD Keyword Description {#tbl-10-5}
#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the following example defines the bubble-point versus depth functions.


```
--
--       DEPTH    API
--                GRAVITY
--       ------   --------
APIVD
         3000.0    41.10
         8000.0    41.10                             / API VS DEPTH EQUIL REGN 01
--       ------   --------
         3000.0    41.10
         8000.0    38.50                             / API VS DEPTH EQUIL REGN 02
--       ------   --------
         3000.0    41.10
         8000.0    38.50                             / API VS DEPTH EQUIL REGN 03
```


Here three tables are entered; the first table has a constant [API](#kw-API) gravity versus depth relationship for  equilibration region number one and the other two equilibration regions have the [API](#kw-API) gravity varying with depth.