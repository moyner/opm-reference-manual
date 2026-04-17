### OILVISCT – Define Oil Viscosity versus Temperature Functions {#kw-OILVISCT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

OILVISCT defines the oil viscosity as a function of temperature for when OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The reference pressure and solution gas-oil ratio of the oil for this table is given by the [VISCREF](#kw-VISCREF) keyword in the [PROPS](#kw-PROPS) section. Note this is an OPM Flow keyword used with OPM Flow’s black-oil thermal model that is not available in the commercial simulator’s black-oil thermal formulation.

This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#kw-TEMP) | A columnar vector of real monotonically increasing down the column values that defines the temperature values. | None |
| oF | oC | oC |  |
| 2 | VIS | A columnar vector of real increasing down the column values that defines the oil viscosity for the corresponding temperature values ([TEMP](#kw-TEMP)). VIS should be given at the reference pressure and solution gas-oil ratio as defined by  PRESS and [RS](#kw-RS) variables on the [VISCREF](#kw-VISCREF) keyword. | None |
| cP | cP | cP |  |
| Notes: |  |  |  |
: OILVISCT Keyword Description {#tbl-8-93}
There is no terminating “/” for this keyword.


#### Example

The following example shows the OILVISCT keyword for when the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section and for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set equal to one.


```
--
--       OIL VISCOSITY VERSUS TEMPERATURE TABLES (OPM FLOW EXTENSION KEYWORD)
--
--       OIL        OIL
--       TEMP       VISC
--       --------   -------
OILVISCT
           100.0    0.600
           110.0    0.650
           120.0    0.680
           150.0    0.720
           165.0    0.725                                  / TABLE NO. 01
```