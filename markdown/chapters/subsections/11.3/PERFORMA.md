### PERFORMA – Export Standard Simulator Performance Summary Variables to File


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PERFORMA keyword activates the writing out of a standard set of OPM Flow simulation numerical performance summary variables to the SUMMARY (*.SMSPEC and .*UNSMRY) and RSM (*.RSM) files. Table 11.31 lists the summary variables written out by the keyword.

Note that not all these variables are available in OPM Flow; however, the simulator will issue a warning message if this is indeed the case. It is anticipated that the number of recognized summary variables will increase in future releases of OPM Flow.


| OPM Flow Simulator Performance Summary Variables Numerical Performance Variables |  |  |
| --- | --- | --- |
| Variable Description | Variable | Comment |
| Elapsed - Elapsed time in seconds. | ELAPSED | No data written to file. |
| Iterations - Number linear iterations for each time step. | MLINEARS |  |
| Iterations - Cumulative number of linear iterations. | MSUMLINS |  |
| Iterations - Cumulative number of Newton iterations. | MSUMNEWT |  |
| Iterations - Number of Newton iterations used for each time step. | NEWTON |  |
| Iterations - Average number of linear iterations per Newton iteration for each time step. | NLINEARS | For runs with LGRs, LLINEARS will automatically be exported for each LGR. |
| Iterations - Maximum number of linear iterations in the Newton iterations per time step. | NLINSMAX |  |
| Iterations - Minimum number of linear iterations in the Newton iterations per time step. | NLINSMIN |  |
| Time Step – Criteria used to select the length of the time step. See section 11.2.24 Option Specific Variables – OPM Flow Simulation Performance for the definition of of the STEPTYPE mnemonics. | STEPTYPE | No data written to file. |
| CPU - Current CPU usage in seconds. | TCPU | Does not consider the time taken by inter-process communications in parallel runs, whereas ELAPSED does. Thus, for parallel jobs, ELAPSED is the most relevant time measurement. |
| CPU - CPU time per day (or hour in lab units depending on run units system). | TCPUDAY | No data written to file. |
| CPU - CPU time per time step in seconds. | TCPUTS | No data written to file. |
| Elapsed - Elapsed time per linear iteration in seconds. | TELAPLIN | No data written to file. |
| Time Step - Length of time step. | TIMESTEP |  |
| Notes: |  |  |

*Table 11.31: Simulator Performance Summary Variables (Numerical Performance)*


::: {.callout-note}
If the summary vector data is unavailable then zeros are written at each time step to the SUMMARY and RSM file.
:::


#### Example


```
-- ==============================================================================
--
-- SUMMARY SECTION
--
-- ==============================================================================
SUMMARY
--
--       EXPORT NUMERICAL PERFORMANCE SUMMARY VARIABLES TO FILE
--
PERFORMA
--
--       ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION
--
RUNSUM
--
--       ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION
--
SEPARATE
```


Note the SEPARATE keyword is not required for OPM Flow as this is the default behavior; however, it is probably good practice to include it if the same input decks are being run with commercial simulator.
