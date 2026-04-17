### SGAS – Define the Initial Equilibration Gas Saturation for All Grid Blocks {#kw-SGAS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SGAS keyword defines the initial equilibration gas saturation values for all grid cells in the model and should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model. The keyword should only be used if the gas phase has been activated in the model via the [GAS](#kw-GAS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SGAS | SGAS is an array of real positive numbers that are greater than or equal to zero and less than or equal to one assigning the initial equilibration gas saturation values to each cell in the model. Repeat counts may be used, for example 20*0.600. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SGAS Keyword Description {#tbl-10-45}
Note for two phase runs it is only necessary to enter one saturation array of one of the phases present in the run (SGAS, [SOIL](#kw-SOIL), or [SWAT](#kw-SWAT)), as the simulator will calculate the other phases by difference. Similarly for three phase runs it is only necessary to enter the array data for two of the phases, as the third saturation will again be calculated by the simulator.


See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION GAS SAT VALUES FOR ALL CELLS IN THE MODEL
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SGAS
         1000*0.7000    1000*0.6500    1000*0.6000                             /

```

The above example defines the initial equilibration gas saturation values to be 0.7000 for all the cells in the first layer, 0.6500 for all the cells in the second layer, and finally 0.6000 for all the cells in the third layer.