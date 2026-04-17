### NOHYST – Deactivate the Hysteresis Option {#kw-NOHYST}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NOHYST keyword deactivates the Hysteresis option and informs the simulator to ignore the [IMBNUM](#kw-IMBNUM) array in the [REGIONS](#kw-REGIONS) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       DEACTIVATE THE HYSTERESIS OPTION
--
NOHYST

```

The above example switches off the default behavior of multiplying the fracture porosity by the fracture permeability to calculate the effective fracture permeability.