### METRIC – Activate the Metric System of Units for the Model {#kw-METRIC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword switches on the METRIC system of units for the model.

OPM Flow has three sets of units, namely: METRIC, [FIELD](#kw-FIELD) and [LAB](#kw-LAB) and one of these keyword should be invoked in the [RUNSPEC](#kw-RUNSPEC) section to avoid any ambiguity. Both the simulator input and output units are controlled by including one of the METRIC, [FIELD](#kw-FIELD) or [LAB](#kw-LAB) keywords in the [RUNSPEC](#kw-RUNSPEC) section of the input file.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       SWITCH ON THE METRIC SYSTEM OF UNITS FOR BOTH INPUT AND OUTPUT
--
METRIC

```

The above example switches on the METRIC system of units for the model.