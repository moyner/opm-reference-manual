### RS – Define the Initial Equilibration GOR (Rs) for All Grid Blocks {#kw-RS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RS keyword defines the initial equilibration gas-oil ratio values for all grid cells in the model and should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model. The keyword should only be used if dissolved gas has been activated in the model via the [DISGAS](#kw-DISGAS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | RS | RS is an array of real positive numbers assigning the initial equilibration gas-oil ratio values to each cell in the model. Repeat counts may be used, for example 20*1.30. | None |
| Mscf/stb | sm3/sm3 | scc/scc |  |
| Notes: |  |  |  |
: RS Keyword Description {#tbl-10-29}
See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION GOR VALUES FOR ALL CELLS IN THE MODEL
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
RS
         1000*1.3500   1000*1.3010   1000*1.3000                               /

```

The above example defines the initial equilibration GOR values to be 1.3500 for all the cells in the first layer, 1.3010 for all the cells in the second layer, and finally 1.3000 for all the cells in the third layer.