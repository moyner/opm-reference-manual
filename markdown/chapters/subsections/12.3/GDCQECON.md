### GDCQECON – Group Economic Criteria for DCQ Production Groups {#kw-GDCQECON}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GDCQECON keyword defines economic criteria for DCQ production groups, including the field level group [FIELD](#kw-FIELD), that have previously been defined by the [GCONPROD](#kw-GCONPROD) keywords in the [SCHEDULE](#kw-SCHEDULE) section.  Note that wells are allocated to a group when they are specified by the [WELSPECS](#kw-WELSPECS) keyword and wells can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the [GCONPROD](#kw-GCONPROD) and [CECON](#kw-CECON) keywords in the [SCHEDULE](#kw-SCHEDULE) section and the controls specified by the [WECON](#kw-WECON) keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named [FIELD](#kw-FIELD) is the top most group and should be used to set targets and constraints for the field. Note that the group hierarchy should be defined by the [GRUPTREE](#kw-GRUPTREE) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the [FIELD](#kw-FIELD) group in the group tree hierarchy. | None |
| 2 | DCQ | A real positive value that defines the minimum economic DCQ gas production rate, below which an economic action of shutting in or stopping all the wells in the group, as requested by item (9) of the [WELSPECS](#kw-WELSPECS) keyword. Note if GRPNAME is equal to [FIELD](#kw-FIELD) then the run will be terminated. A value less than or equal to zero switches of this criteria. | 0.0 |
| Mscf/d | sm3/day | scc/hour |  |
| Notes: |  |  |  |
: GDCQECON Keyword Description {#tbl-12-35}
See also the [WELSPECS](#kw-WELSPECS) keyword to define a wells shut-in or stop options, [GCONPROD](#kw-GCONPROD) for group controls, and [WECON](#kw-WECON) for setting a well’s economic criteria. All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

The following example defines the minimum DCQ for the field to be 10 MMscf/d.


```
--
--       GROUP ECONOMIC CRITERIA FOR DCQ PRODUCTION GROUPS
--
-- GRUP  GAS
-- NAME  DCQ
GDCQECON
FIELD    10E3                                                                 /
/
```