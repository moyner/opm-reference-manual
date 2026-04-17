### MINNPCOL – Define the Minimum Number of Newton Iterations Used to Update Well Targets {#kw-MINNPCOL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MINNPCOL keyword defines the minimum number of Newton iterations within a time step where the well production and injection targets may be updated, after which the well targets will be frozen until the time step calculations have converged and the time step is complete.


::: {.callout-note}
This is an OPM Flow specific keyword that sets the minimum number of Newton iterations, as opposed to the [NUPCOL](#kw-NUPCOL) keyword that defines the maximum number of Newton iterations within a time step, after which well targets are frozen.
:::


The MINNPCOL keyword has been deprecated and the [NUPCOL](#kw-NUPCOL) keyword should be used instead.

Wells under group control may suffer from some dependency with other wells in the same group that are also under group control. This may cause oscillations in the production and injection well rates within the group. In order to avoid this, the [NUPCOL](#kw-NUPCOL) keyword in the [RUNSPEC](#kw-RUNSPEC) section can be used to set the maximum number of Newton iterations within a time step, after which the group well rates are frozen until the time step has converged.  Reducing the potential for well rate oscillations within the time step may result in the group targets and limits not being exactly met in this case. Increasing the value of [NUPCOL](#kw-NUPCOL), will improve the accuracy of the group targets and limits at the expense of computational efficiency. Here, the MINNPCOL keyword sets the minimum number of Newton iterations within a timestep where the well production and injection targets may be updated.

See also section 2.2 Running OPM Flow 2023-04 From The Command Line on how to set various other numerical control parameters for OPM Flow.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MINNPCOL | A positive integer that defines the minimum number of Newton iterations within a timestep where well targets may be updated. | 3 |
| Notes: |  |  |  |
: MINNPCOL Keyword Description {#tbl-5-20}
#### Example


```
--
--       DEFINE THE MIN NUMBER OF ITERATIONS TO UPDATE WELL FLOW TARGETS
--
MINNPCOL
         3                                                                    /
```


The above example sets the MINNPCOL value to its default value of three.