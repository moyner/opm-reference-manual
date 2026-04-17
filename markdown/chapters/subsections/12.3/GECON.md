### GECON – Group Economic Criteria for Production Groups


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GECON keyword defines economic criteria for production groups, including the top level FIELD group, that have been created by having wells assigned to them via the WELSPECS keyword in the SCHEDULE section.

Note that wells are allocated to a group when they are specified by the WELSPECS keyword and wells can also have well level economic controls. Wells under group control are therefore subject to the economic criteria set via the GECON and WECON keywords and the controls specified by the GCONPROD keyword in the SCHEDULE section.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field. Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| 2 | ORAT | A real positive value that defines the minimum economic surface oil production rate, below which an economic action of shutting in or stopping all the wells in the group, as requested by the AUTO variable item (9) of the WELSPECS keyword. This value may be specified using a User Defined Argument (UDA). A value less than or equal to zero switches off this criteria. | 0.0 |
| stb/d | sm3/day | scc/hour |  |
| 3 | GRAT | A real positive value that defines the minimum economic surface gas production rate, below which an economic action of shutting in or stopping all the wells in the group, as requested by the AUTO variable item (9) of the WELSPECS keyword. This value may be specified using a User Defined Argument (UDA). A value less than or equal to zero switches off this criteria, | 0.0 |
| Mscf/d | sm3/day | scc/hour |  |
| 4 | WCUT | A real positive value that defines the maximum economic surface water cut, above which an economic action will take place. This value may be specified using a User Defined Argument (UDA). Water cut is defined as:${f}_{w} = \frac{{q}_{w}}{{q}_{w} + {q}_{o}}$, and the various actions that are available if the water cut limit is exceeded are described in item (7). A value less than or equal to zero switches off this criteria. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | GOR | A real positive value that defines the maximum economic surface gas-oil ratio, above which an economic action will take place, as defined by item (7). This value may be specified using a User Defined Argument (UDA). A value less than or equal to zero switches off this criteria. | 0.0 |
| Mscf/stb | sm3/sm3 | scc/scc |  |
| 6 | WGR | A real positive value that defines the maximum economic surface water-gas ratio, above which an economic action will take place, as defined by item (7). This value may be specified using a User Defined Argument (UDA). A value less than or equal to zero switches off this criteria. | 0.0 |
| stb/Mscf | sm3/sm3 | scc/scc |  |
| 7 | ACTION | A defined character string that defines the action to be taken if the economic WCUT, GOR, or WGR limits are violated. ACTION should be set to one of the following character strings: The corrective action takes places at the end of the time step in which the constraint is violated. Only the NONE option is currently supported by the simulator. | None |
| 8 | END | A defined character string that defines if the simulation should terminate if  all the producing wells in the group, including the FIELD group, are shut or stopped. END should be set to one of the following character strings: Only the NO option is currently supported by the simulator. | NO |
| 9 | MXWELS | A positive integer defining the maximum number of producing and injecting wells for this this group and any subordinate groups. The default value of zero implies that there is no limit to the number of wells. This is not currently supported by the simulator and must be defaulted. | 0 |
| Notes: |  |  |  |

*Table 12.3.98.1: GECON Keyword Description*


See also the WELSPECS keyword to define a well’s shut-in or stop options, GCONPROD for group controls, and WECON for setting a well’s economic criteria. All the aforementioned keywords are described in the SCHEDULE section.


#### Example

The following example defines the economic criteria for the field with a minimum oil rate of 2,000 m3/day and a maximum water cut of 95%.


```
--
--       GROUP ECONOMIC CRITERIA FOR PRODUCTION GROUPS
--
-- GRUP  OIL   GAS    WCT    GOR    WGR    WORK   END   MAX
-- NAME  MIN   MIN    MAX    MAX    MAX    OVER   RUN   WELLS
GECON
FIELD    2E3   1*     0.95     1*    1*     CON   'YES'  1*                     /
/

```

If the economic limits are violated then the run will stop at the next report time step.
