### GLIFTLIM – Group Artificial Lift Constraints {#kw-GLIFTLIM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GLIFTLIM keyword defines the maximum number of wells on artificial lift and the maximum amount of the artificial lift that is available for a group, including the top most group in the group hierarchy known as the [FIELD](#kw-FIELD) group. Wells are allocated to groups when the wells are specified by the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section.  Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group’s artificial lift constraints are being defined. The group named [FIELD](#kw-FIELD) is the top most group and should be used to set targets and constraints for the field. Note that the group hierarchy should be defined by the [GRUPTREE](#kw-GRUPTREE) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the [FIELD](#kw-FIELD) group in the group tree hierarchy. | None |
| 2 | MXLIFT | A real positive value that defines the total amount of artificial lift available for this group and any subordinate groups. The units for MXLIFT are the same as that defined by the ALQ parameter on the [VFPPROD](#kw-VFPPROD) keyword in the [SCHEDULE](#kw-SCHEDULE) section. For example, if ALQ has been set to GRAT on the [VFPPROD](#kw-VFPPROD) keyword, then MXLIFT would be the maximum amount of gas lift gas available for this group and any subordinate groups, and the units would Mscf, assuming [FIELD](#kw-FIELD) units had been activated in the [RUNSPEC](#kw-RUNSPEC) section. The default value of zero implies that there is no limit applied to the group and its subordinate groups. | 0 |
| See [VFPPROD](#kw-VFPPROD) (ALQ) | See [VFPPROD](#kw-VFPPROD) (ALQ) | See [VFPPROD](#kw-VFPPROD) (ALQ) |  |
| 3 | MXWELS | A positive integer defining the maximum number of producing wells on artificial lift for this group and any subordinate groups. The default value of zero implies that there is no limit to the number of wells. | 0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: GLIFTLIM Keyword Description {#tbl-12-39}
See also the [GRUPTREE](#kw-GRUPTREE) keyword to define the hierarchy of the groups below the [FIELD](#kw-FIELD) level, the  [GCONPROD](#kw-GCONPROD) and [GCONINJE](#kw-GCONINJE) keywords to define a group’s production and injection rate targets and constraints, the [WCONPROD](#kw-WCONPROD) keyword to define a production well’s targets and constraints, and the [WCONINJE](#kw-WCONINJE) keyword to define an injection well’s targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

The following example defines the artificial lift constraints for the field, assuming all the wells are on gas lift.


```
---
--       GROUP ARTIFICIAL LIFT CONSTRAINTS
--
-- GRUP  MAX   MAX
-- NAME  ALQ   WELLS
GLIFTLIM
FIELD    20E3  20                                                             /
/
```


Here the maximum amount of gas lift gas for the field is set to 20.0 MMscf/f and a maximum of 20 wells can utilize gas lift at a time.