### LAB – Activate the Laboratory System of Units for the Model {#kw-LAB}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword switches on the LABORATORY system of units for the model.

OPM Flow has three sets of units, namely: [METRIC](#kw-METRIC), [FIELD](#kw-FIELD) and LAB and one of these keyword should be invoked in the [RUNSPEC](#kw-RUNSPEC) section to avoid any ambiguity. Both the simulator input and output units are controlled by including one of the [METRIC](#kw-METRIC), [FIELD](#kw-FIELD) or LAB keywords in the [RUNSPEC](#kw-RUNSPEC) section of the input file.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       SWITCH ON THE LABORATORY SYSTEM OF UNITS FOR BOTH INPUT AND OUTPUT
--
LAB

```

The above example switches on the LABORATORY system of units for the model.