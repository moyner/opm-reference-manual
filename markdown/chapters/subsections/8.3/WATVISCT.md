### WATVISCT – Define Water Viscosity versus Temperature Functions {#kw-WATVISCT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WATVISCT defines the water viscosity as a function of temperature for when thermal option has been activated by the [THERMAL](#kw-THERMAL) keywords in the [RUNSPEC](#kw-RUNSPEC). The reference pressure for this table is given by the [VISCREF](#kw-VISCREF) keyword in the [PROPS](#kw-PROPS) section.

This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#kw-TEMP) | A columnar vector of real monotonically increasing down the column   values that defines the temperature values. | None |
| oF | oC | oC |  |
| 2 | VIS | A columnar vector of real decreasing down the column values that defines the water viscosity for the corresponding temperature values ([TEMP](#kw-TEMP)). VIS should be given at the reference pressure defined by the PRESS variable on the [VISCREF](#kw-VISCREF) keyword. | None |
| cP | cP | cP |  |
| Notes: |  |  |  |
: WATVISCT Keyword Description {#tbl-8-199}
#### Example

The following example shows the WATVISCT keyword for when the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section and for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set equal to one.


```

--
--       WATER VISCOSITY VERSUS TEMPERATURE TABLES
--
--       WATER      WATER
--       TEMP       VISC
--       --------   -------
WATVISCT
           100.0    0.625
           110.0    0.620
           120.0    0.580
           150.0    0.550
           165.0    0.500                                  / TABLE NO. 01
```


There is no terminating “/” for this keyword.