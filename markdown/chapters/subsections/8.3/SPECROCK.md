### SPECROCK – Define the Specific Heat of the Reservoir Rock {#kw-SPECROCK}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SPECROCK defines the specific heat of the reservoir rock for various PVT regions in the model for when the [THERMAL](#kw-THERMAL) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. The number of SPECROCK vector data sets is defined by the NTSFUN parameter on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the allocation of the SPECROCK data sets to different grid blocks in the model is done via the [SATNUM](#kw-SATNUM) keyword in the [REGIONS](#kw-REGIONS) section.

This keyword can only be used if OPM’s Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#kw-TEMP) | A columnar vector of real monotonically increasing down the column   values that define the temperature for the corresponding rock specific heat values. | None |
| oF | oC | oC |  |
| 2 | ROCKHEAT | ROCKHEAT is a columnar vector of positive real numbers defining the specific heat of the rock at the corresponding temperature, [TEMP](#kw-TEMP). | None |
| Btu/ft3/oR | kJ/m3/K | J/cc/K |  |
| Notes: |  |  |  |
: SPECROCK Keyword Description {#tbl-8-171}
See also the [SPECHEAT](#kw-SPECHEAT) keyword to define the specific heat relationships for the oil, water and gas phases.


#### Example

The example below defines three rock specific heat versus temperature tables assuming NTSFUN equals three and NSSFUN is greater than or equal to two on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


```
--
--       SPECIFIC HEAT OF ROCK
--
SPECROCK
--       TEMP       SPECHEAT
--                  ROCK
--       -------    --------
           0.000     20.000
         250.000     20.000                                / TABLE NO. 01
--       -------    --------
           0.000     21.000
         260.000     21.000                                / TABLE NO. 02
--       -------    --------
           0.000     23.000
         270.000     23.000                                / TABLE NO. 03
```


There is no terminating “/” for this keyword.