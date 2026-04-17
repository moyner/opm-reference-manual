### SSOL – Define the Initial Equilibration Solvent Saturation for All Grid Blocks {#kw-SSOL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SSOL keyword defines the initial equilibration solvent saturation values for all grid cells in the model and should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model. The keyword should only be used if the solvent phase has been activated in the model via the [SOLVENT](#kw-SOLVENT) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SSOL | SSOL is an array of real positive numbers that are greater than or equal to zero and less than or equal to one assigning the initial equilibration solvent saturation values to each cell in the model. Repeat counts may be used, for example 20*0.000. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SSOL Keyword Description {#tbl-10-53}
See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL), and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION GAS SAT VALUES FOR ALL CELLS IN THE MODEL
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SSOL
         1000*0.0000    1000*0.0000    1000*0.0000                             /

```

The above example defines the initial equilibration solvent saturation values to be 0.0 for all the cells in the in the model.