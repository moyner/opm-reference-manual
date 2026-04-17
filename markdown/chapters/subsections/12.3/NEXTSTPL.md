### NEXTSTPL – Maximum Next Time Step Size (LGR) {#kw-NEXTSTPL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the maximum time step size the simulator should take for the next time step for all Local Grid Refinements (“[LGR](#kw-LGR)”). This keyword can be used to reset the time step for when known large changes to the model are taking place that may result in time step chops. For example, if the reporting time size is using monthly reporting steps via the [DATES](#kw-DATES) keyword in the [SCHEDULE](#kw-SCHEDULE) section, then if for example, a group of wells start production at a given date, then the NEXTSTPL keyword can be used to shorten the next step in all the LGRs in order to avoid a time step chop.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | NSTEP1 | NSTEP1 is a real positive value that defines the maximum length of the next time step. | None |
| days | days | hours |  |
| 2 | NSTEP2 | NSTEP2 is a character string that should be set to either NO or YES to state if the NSTEP1 should be applied to future reporting time steps. The default value of NO means that NSTEP1 will only be applied once. | NO |
| Notes: |  |  |  |
: NEXTSTPL Keyword Description {#tbl-12-56}
See also the [NEXT](#kw-NEXT) and [NEXTSTEP](#kw-NEXTSTEP) keywords in the [SCHEDULE](#kw-SCHEDULE) section that are used to control the global grid’s next time step.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. See section 2.2 Running OPM Flow 2023-04 From The Command Line on how to control time stepping for OPM Flow.


#### Example


```
--
--       NEXT   ALL
--       STEP   TIME
--       ----   ----
NEXTSTEP
         1     'NO'                                        /
```


Here the next step size for all LGRs is set to one day and should only be used once.