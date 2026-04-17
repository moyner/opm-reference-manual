### WEFAC – Define Well Efficiency {#kw-WEFAC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

Defines a well’s efficiency or up-time as opposed to setting the efficiency at the group level.

Note that wells are allocated to a group when they are specified by the [WELSPECS](#kw-WELSPECS) keyword and groups can also have efficiency factors.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well efficiency factor is being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | FACTOR | A real positive value greater than zero and less than or equal to one that defines the efficiency factor for the well. If a well’s down time is 5% then FACTOR should be set to 0.95 (1.0 – 0.05). Note that well pressures and rates are calculated at their full flowing conditions but subject to any operating constraints, that is without the well efficiency being applied (FACTOR), in order to represent the actual flowing conditions in the field. The effective rates and volumes are calculated by applying FACTOR when summing individual well rates to their group level and higher, including summing to the top most group [FIELD](#kw-FIELD). In terms of a well’s cumulative production, FACTOR is applied to the well rate times the time interval for the time step. This ensures that correct effective volume is withdrawn from (or injected to) the reservoir. This approach means that wells are effectively arbitrarily offline for a period during a time step, as opposed to all wells going offline concurrently. And thus the group and field rates and volumes are the effective rates and volumes for the field. | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| 3 | WELNETWK | A defined character string that determines if the WELNAME efficiency factor should be applied when calculating the flows and pressure losses in the Extended Network Model, and should be set to either: This option is only applicable for the Extended Network Model, as in the Standard Network Model groups flow rates are always used in the calculation of pressure drops (this is equivalent to the default option, YES). | YES |
| Notes: |  |  |  |
: WEFAC Keyword Description {#tbl-12-84}
See also the [GEFAC](#kw-GEFAC) keyword in the [SCHEDULE](#kw-SCHEDULE) section to set the efficiency at the group level, as opposed to applying the efficiency to individual wells.


::: {.callout-note}
One can also apply plant efficiencies through the [GEFAC](#kw-GEFAC) keyword in the [SCHEDULE](#kw-SCHEDULE) section. If all the wells in a group are flowing through a facility that has an overall efficiency factor, then it is more appropriate to apply the efficiency factor at the group level.  This of course does not preclude applying additional well efficiencies to individual wells. For example, subsea wells (wet trees) may have additional  down time compared to platform wells (dry trees) even though both sets of well are flowing through the same platform.  Another example would be gas lift wells and wells using electrical submersible pumps, as their artificial lift mechanisms.
:::


#### Example


```
--
--       WELL EFFICIENCY FACTORS
--
-- WELL  EFF    NETWK
-- NAME  FACT   OPTN
WEFAC
'GP*  '  0.950                                                                 /
'OP*  '  0.862                                                                 /
/

```

In the above example the all the gas wells are are defined as having a well efficiency factor (up time) of 0.950 and all the oil wells have a lower efficiency factor of 0.862.