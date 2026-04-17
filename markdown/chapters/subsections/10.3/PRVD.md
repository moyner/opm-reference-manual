### PRVD – Define the Initial Equilibration Pressures versus Depth {#kw-PRVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PRVD keyword defines the initial reservoir pressure versus depth and should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model.  PRVD is an alternative to the [PRESSURE](#kw-PRESSURE) keyword in the [SOLUTION](#kw-SOLUTION) section, that defines the initial equilibration pressures for all grid cells in the model

The keyword is used by the Enumeration Initialization method to initialize the model, as opposed to the Equilibration Initialization method that utilizes the [EQUIL](#kw-EQUIL) keyword in the [SOLUTION](#kw-SOLUTION) section. This is the non-standard formulation to initialize the model and is seldom employed in the industry.  The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding reservoir oil pressures values, [PRESSURE](#kw-PRESSURE). | None |
| feet | m | cm |  |
| 2 | [PRESSURE](#kw-PRESSURE) | A columnar vector of real values that defines the initial equilibration oil pressure values at the corresponding [DEPTH](#kw-DEPTH). | None |
| psia | barsa | atma |  |
| Notes: |  |  |  |
: PRVD Keyword Description {#tbl-10-24}
See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to five on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the following example defines the initial oil reservoir pressure versus depth


```
--
--       DEPTH    INIT
--                PRESS
--       ------   ------
PRVD
         3000.0   3000.0
         4000.0   3345.0
         5000.0   3690.0
         7000.0   4700.0
         7200.0   4769.0                            / POIL VS DEPTH EQUIL REGN 01
--       ------   ------
         3000.0   3100.0
         4000.0   3445.0
         5000.0   3790.0
         7000.0   4700.0
         7200.0   4769.0                            / POIL VS DEPTH EQUIL REGN 02
--       ------   ------
         3000.0   3150.0
         4000.0   3495.0
         5000.0   3840.0
         7000.0   4700.0
         7200.0   4769.0                            / POIL VS DEPTH EQUIL REGN 03
```


Here three tables are entered and each table is terminated by a “/” and there is no keyword terminating “/”.