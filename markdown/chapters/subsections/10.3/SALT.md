### SALT – Define the Initial Equilibration Salt Concentration for All Grid Blocks {#kw-SALT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SALT keyword defines the initial equilibration salt concentration values for all grid cells in the model and should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SGAS](#kw-SGAS) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model. The keyword should only be used if the salt (brine) phase has been activated in the model via the [BRINE](#kw-BRINE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SALT | SALT is an array of real positive numbers that are greater than or equal to zero assigning the initial equilibration salt concentration values to each cell in the model. Repeat counts may be used, for example 20*15.0. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |
: SALT Keyword Description {#tbl-10-36}
See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION SALT CONCENTRATION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SALT
         10000*0.0000    10000*0.0000    10000*15.000                             /

```

The above example defines the initial equilibration salt concentration values to be 0.0000 for all the cells in the first and second layers and finally 15.000 for all the cells in the third layer.