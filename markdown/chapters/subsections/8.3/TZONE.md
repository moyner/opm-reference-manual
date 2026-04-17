### TZONE – End-Point Scaling Transition Zone Options {#kw-TZONE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The TZONE keyword sets the transition end-point scaling options for the oil, water and gas phases, for when the End-Point Scaling option has been activated by the [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword determines if the phase critical saturation should or should not be set to the initial immobile saturation in areas where the initial saturation is below the entered critical saturation.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | OILZONE | OILZONE is a single character that sets the oil phase transition zone end-point scaling option and should be set to either T or F: | F |
| 2 | WATZONE | WATZONE is a single character that sets the water phase transition zone end-point scaling option and should be set to either T or F: | F |
| 3 | GASZONE | GASZONE is a single character that sets the gas phase transition zone end-point scaling option and should be set to either T or F: | F |
| Notes: |  |  |  |
: TZONE Keyword Description {#tbl-8-195}
See also the [SCALECRS](#kw-SCALECRS) keyword in the [PROPS](#kw-PROPS) section that sets the end-point scaling option to be either two-point or three-point scaling.


#### Example


```
--
--       END-POINT SCALING TRANSITION ZONE OPTIONS
--
--       OILZONE  WATZONE  GASZONE
--       -------  -------  -------
TZONE
         F        T        F                               / SCALING OPTION
```


The above example results in the [SWCR](#kw-SWCR) values being adjusted to the initial immobile saturations.