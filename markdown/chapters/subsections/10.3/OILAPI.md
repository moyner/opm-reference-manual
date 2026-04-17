### OILAPI – Define the Initial Equilibration Oil API for All Grid Blocks {#kw-OILAPI}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The OILAPI keyword defines the initial equilibration oil [API](#kw-API) gravity pressures for all grid cells in the model, for when the Oil [API](#kw-API) Tracking option as been invoked by the [API](#kw-API) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model.

The keyword is used by the Enumeration Initialization method to initialize the model, as opposed to the Equilibration Initialization method that utilizes the [EQUIL](#kw-EQUIL) keyword in the [SOLUTION](#kw-SOLUTION) section. This is the non-standard formulation to initialize the model and is seldom employed in the industry.  The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | OILAPI | OILAPI is an array of real positive numbers assigning the initial equilibration oil [API](#kw-API) gravity to each cell in the model. The American Petroleum Institute (“[API](#kw-API)”) classifies oils based on an [API](#kw-API) gravity (γ[API](#kw-API)),  or degrees [API](#kw-API) (oAPI), the relationship between relative density (γo) of oil and [API](#kw-API) gravity (γ[API](#kw-API)) is given by: ${\mathrm{γ}}_{\mathit{[API](#kw-API)}} = \frac{141.5}{{\mathrm{γ}}_{o}} - 131.5$ Repeat counts may be used, for example 20*38.5 | None |
| oAPI | oAPI | oAPI |  |
| Notes: |  |  |  |
: OILAPI Keyword Description {#tbl-10-18}
See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION OIL API FOR ALL CELLS IN THE MODEL
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
OILAPI
         1000*40.2     1000*39.5     1000*38.2                                 /

```

The above example defines the initial equilibration oil [API](#kw-API) gravity to be 40.2 for all the cells in the first layer, 39.5 for all the cells in the second layer, and finally 38.2 for all the cells in the third layer.