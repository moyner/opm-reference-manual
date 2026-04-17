### GECONT – Group Tracer Economic Criteria for Production Groups


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GECONT keyword defines tracer economic criteria for production groups, including the field level group FIELD, that have previously been defined by the GCONPROD keywords in the SCHEDULE section, for tracers define by the TRACER keyword in the PROPS section.

Note that wells are allocated to a group when they are specified by the WELSPECS keyword and wells can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the GCONPROD and CECON keywords in the SCHEDULE section and the controls specified by the WECON keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1-1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field. Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| 1-2 | ACTION | A defined character string that defines the action to be taken if the economic WCUT, GOR, or WGR limits are violated. ACTION should be set to one of the following character strings: The corrective action takes places at the end of the time step in which the constraint is violated. | None |
| 1-3 | END | A defined character string that defines if the simulation should terminate if  all the producing wells in the group, including the FIELD group, are shut or stopped. END should be set to one of the following character strings: | NO |
| 1-4 | MXWELS | A positive integer defining the maximum number of producing and injecting wells for this group and any subordinate groups. The default value of zero implies that there is no limit to the number of wells. | 0 |
| 1-5 | / | Record one terminated by a “/” | Not Applicable |
| 2-1 | NAME | A three letter character string defining the tracer’s name. Note it is best to void names beginning with the letters F, S, and T as these names may create naming issues in post-processing software. | None |
| 2-2 | MXTOTAL | A real positive value that defines the maximum total (free plus solution) tracer rate. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-3 | MXFREET | A real positive value that defines the maximum total (free plus solution) tracer concentration. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-4 | MXFREEQ | A real positive value that defines the maximum free tracer rate. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-5 | MXCONC | A real positive value that defines the maximum free tracer concentration. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-6 | MXSOLNQ | A real positive value that defines the maximum solution rate. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-7 | MXSOLNC | A real positive value that defines the maximum solution concentration. Tracer units are per those defined by the carrying fluid, oil, gas, water, etc. | None |
| 2-8 | / | Record two terminated by a “/” | Not Applicable |
| 3-1 | / | Group terminated by a “/” | Not Applicable |
| Notes: |  |  |  |

*Table 12.37: GECONT Keyword Description*


See also the WELSPECS keyword to define a wells shut-in or stop options, GCONPROD for group controls, and WECON for setting a well’s economic criteria. All the aforementioned keywords are described in the SCHEDULE section.


#### Example

The following example defines the tracer economic criteria for the field and two groups, FLTBLK1 and FLTBLK,.


```
--
--       GROUP TRACER ECONOMIC CRITERIA FOR PRODUCTION GROUPS
--
-- GRUP  WORK    END    MAX
-- NAME  OVER    RUN    WELLS
GECONT
FIELD    +CON   'YES'   1*                                     / START OF GROUP
--
--       TRACER  TRACER  TRACER  TRACER  TRACER  TRACER  TRACER
--       NAME    TOTAL   TOTAL   FREE    FREE    SOLN    SOLN
--               RATE    CONCEN  RATE    CONCEN  RATE    CONCEN
         PLY     1000.0                                        /
         BRI     1000.0                                        /
         TR1     1*      0.7500                                /
                                                               /
FLTBLK1  +CON   'YES'   1*                                     / START OF GROUP
--
--       TRACER  TRACER  TRACER  TRACER  TRACER  TRACER  TRACER
--       NAME    TOTAL   TOTAL   FREE    FREE    SOLN    SOLN
--               RATE    CONCEN  RATE    CONCEN  RATE    CONCEN
         PLY     800.0                                         /
         BRI     800.0                                         /
                                                                      /
FLTBLK2  +CON   'YES'   1*                                     / START OF GROUP
--
--       TRACER  TRACER  TRACER  TRACER  TRACER  TRACER  TRACER
--       NAME    TOTAL   TOTAL   FREE    FREE    SOLN    SOLN
--               RATE    CONCEN  RATE    CONCEN  RATE    CONCEN
         PLY     800.0                                         /
         BRI     800.0                                         / END OF GROUP
                                                               / END OF KEYWORD
```

If the economic limits are violated then the worst offending connection and all below it in the worst offending well will be closed, If connections have been grouped as completions then the worst offending completion and all below it in the worst offending well will be closed.
