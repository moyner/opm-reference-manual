### PRESSURE – Define the Initial Equilibration Pressures for All Grid Blocks {#kw-PRESSURE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PRESSURE keyword defines the initial equilibration pressures for all grid cells in the model and should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model.

The keyword is used by the Enumeration Initialization method to initialize the model, as opposed to the Equilibration Initialization method that utilizes the [EQUIL](#kw-EQUIL) keyword in the [SOLUTION](#kw-SOLUTION) section. This is the non-standard formulation to initialize the model and is seldom employed in the industry.  The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESSURE | PRESSURE is an array of real positive numbers assigning the initial equilibration pressures to each cell in the model. Repeat counts may be used, for example 20*4200.0. | None |
| psia | barsa | atma |  |
| Notes: |  |  |  |
: PRESSURE Keyword Description {#tbl-10-23}
See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION PRESSURES FOR ALL CELLS IN THE MODEL
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
PRESSURE
         1000*4500.0   1000*4510.0   1000*4520.0                               /

```

The above example defines the initial equilibration pressures to be 4500.0 for all the cells in the first layer, 4510.0 for all the cells in the second layer, and finally 4520.0 for all the cells in the third layer.