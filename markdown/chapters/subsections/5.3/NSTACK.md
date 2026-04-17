### NSTACK – Define the Stack Length for the Iterative Linear Solver {#kw-NSTACK}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NSTACK keyword defines the maximum number of previous search directions stored by the linear solver. Increasing the value of NSTACK may improve the efficiency of the solver on difficult problems, but will increase the memory requirements of the simulator. The default value of 10 should be sufficient for most problems; however, if OPM Flow is having issues with the convergence of the linear questions then increasing NSTACK and the value of LITMAX on the [TUNING](#kw-TUNING) keyword may improve performance.

OPM Flow uses a different numerical scheme which makes this keyword redundant; see section 2.2 Running OPM Flow 2023-04 From The Command Line on how to invoke various numerical schemes via the OPM Flow command line interface.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NSTACK | A positive integer that defines the maximum number of previous search directions stored by the linear solver. | 10 |
| Notes: |  |  |  |
: NSTACK Keyword Description {#tbl-5-29}
#### Example


```
--
--         SET STACK SIZE FOR LINEAR SOLVER
--
NSTACK
           30                                                                  /
```


The above example sets maximum number of previous search directions stored by the linear solver to 30, this has no effect in OPM Flow input decks.


::: {.callout-note}
If the run is suffering from linear convergence problems, then check the data first for any data issues before manipulating the numerical control parameters. For example, if OPM Flow has written some WARNING messages with respect to end-point scaling, etc., then resolve these messages first before adjusting the numerical controls.
:::