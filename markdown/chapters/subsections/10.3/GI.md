### GI – Define the Initial Equilibration Gi Values for All Grid Blocks {#kw-GI}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GI keyword defines the initial equilibration GI values for all grid cells in the model and should be used in conjunction with the other enumeration equilibration keywords; [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model. The keyword should only be used if the GI Pseudo Compositional option has been activated in the model via the [GIMODEL](#kw-GIMODEL) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

See also the [GIALL](#kw-GIALL) keyword in the [PROPS](#kw-PROPS) section that sets the GI values as a function of pressure, as well as setting the corresponding [RVGI](#kw-RVGI), [RSGI](#kw-RSGI), [BGGI](#kw-BGGI) and [BOGI](#kw-BOGI) values at the same time.