### WCALCVAL – Define Gas Well Calorific Value {#kw-WCALCVAL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines a gas well’s calorific value for when the Gas Calorific Value option has been activated by specifying a target calorific value for a group via the [GCONCAL](#kw-GCONCAL) keyword in the [SCHEDULE](#kw-SCHEDULE) section. If this option is invoked then the gas calorific value must be set either by this keyword for a well by well allocation of the calorific value, or by using the Tracer Tracking option (activated by the [TRACER](#kw-TRACER) keyword in the [RUNSPEC](#kw-RUNSPEC) section) combined with [CALTRAC](#kw-CALTRAC) keyword in the [SCHEDULE](#kw-SCHEDULE) section that defines the tracer for the calorific value.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.