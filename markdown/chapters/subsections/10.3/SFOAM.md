### SFOAM – Define the Initial Equilibration Foam Concentration for All Grid Blocks {#kw-SFOAM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SFOAM keyword defines the initial equilibration foam concentration values for all grid cells in the model and should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SGAS](#kw-SGAS) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model. The keyword should only be used if the foam  phase has been activated in the model via the [FOAM](#kw-FOAM) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SFOAM | SFOAM is an array of real positive numbers that are greater than or equal to zero assigning the initial equilibration foam concentration values to each cell in the model. Units are dependent on the transport phase specified via the FOAMOPT1 variable on the [FOAMOPTS](#kw-FOAMOPTS) keyword in the [PROPS](#kw-PROPS) section. FOAMOPT1 should be set to either [GAS](#kw-GAS) or [WATER](#kw-WATER). Repeat counts may be used, for example 20*0.5 | None |
| Gas: lb/Mscf Water: lb/stb | Gas: kg/sm3 Water: kg/sm3 | Gas: gm/scc Water: gm/scc |  |
| Notes: |  |  |  |
: SFOAM Keyword Description {#tbl-10-44}
See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION FOAM VALUES FOR ALL CELLS IN THE MODEL
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SFOAM
         1000*0.0000    1000*0.0000    1000*0.500                             /

```

The above example defines the initial equilibration foam concentration values to be 0.0000 for all the cells in the first and second layers and finally 0.500 for all the cells in the third layer.