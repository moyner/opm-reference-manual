### GCALECON – Group Economic Criteria for Production Calorific Groups {#kw-GCALECON}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GCALECON keyword defines economic criteria for production groups, including the field level group [FIELD](#kw-FIELD), that have previously been defined by the [GCONPROD](#kw-GCONPROD) keyword in the [SCHEDULE](#kw-SCHEDULE) section and have had their rate targets and constraints set by calorific value via the GCONVAL keyword in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

Note that wells are allocated to a group when they are specified by the [WELSPECS](#kw-WELSPECS) keyword and wells can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the [GCONPROD](#kw-GCONPROD) and [CECON](#kw-CECON) keywords in the [SCHEDULE](#kw-SCHEDULE) section and the controls specified by the [WECON](#kw-WECON) keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named [FIELD](#kw-FIELD) is the top most group and should be used to set targets and constraints for the field. Note that the group hierarchy should be defined by the [GRUPTREE](#kw-GRUPTREE) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the [FIELD](#kw-FIELD) group in the group tree hierarchy. | None |
| 2 | ENEVAL | A real positive value that defines the minimum economic surface energy production rate, below which an economic action of shutting in or stopping all the wells in the group, as requested by item (9) of the [WELSPECS](#kw-WELSPECS) keyword. A value less than or equal to zero switches of this criteria. | 0.0 |
| BTU/day | kJ/day | J/hour |  |
| 3 | CALVAL | A real positive value that defines the minimum economic surface calorific value, below which an economic action of shutting in or stopping all the wells in the group, as requested by item (9) of the [WELSPECS](#kw-WELSPECS) keyword. A value less than or equal to zero switches of this criteria, | 0.0 |
| Btu/Mscf | kJ/sm3 | J/scc |  |
| 8 | [END](#kw-END) | A defined character string that defines if the simulation should terminate if  all the producing wells in the group, including the [FIELD](#kw-FIELD) group, are shut or stopped. [END](#kw-END) should be set to one of the following character strings: | NO |
| Notes: |  |  |  |
: GCALECON Keyword Description {#tbl-12-26}
See also the [WELSPECS](#kw-WELSPECS) keyword to define a wells shut-in or stop options, [GCONPROD](#kw-GCONPROD), [GCONCAL](#kw-GCONCAL), [GCONENG](#kw-GCONENG) for group controls, and [WECON](#kw-WECON) for setting a well’s economic criteria. All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

The following example defines the economic criteria for the field with a minimum economic surface energy production rate of 5 x 109 BTU/day and a minimum economic surface calorific value of900 Btu/Mscf


```
--
--       GROUP ECONOMIC CRITERIA FOR PRODUCTION GROUPS UNDER CALORIFIC CONTROL
--
-- GRUP  ENERGY  CALORIFIC  END
-- NAME  RATE    VALUE      RUN
GCALECON
FIELD    5E9     900.0     'YES'                                               /
/
```


If the economic limits are violated then the run will stop at the next report time step.