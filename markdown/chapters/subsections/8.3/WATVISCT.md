### WATVISCT – Define Water Viscosity versus Temperature Functions


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WATVISCT defines the water viscosity as a function of temperature for when thermal option has been activated by the THERMAL keywords in the RUNSPEC. The reference pressure for this table is given by the VISCREF keyword in the PROPS section.

This keyword can only be used if OPM Flow’s thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | TEMP | A columnar vector of real monotonically increasing down the column   values that defines the temperature values. | None |
| oF | oC | oC |  |
| 2 | VIS | A columnar vector of real decreasing down the column values that defines the water viscosity for the corresponding temperature values (TEMP). VIS should be given at the reference pressure defined by the PRESS variable on the VISCREF keyword. | None |
| cP | cP | cP |  |
| Notes: |  |  |  |

*Table 8.199: WATVISCT Keyword Description*


#### Example

The following example shows the WATVISCT keyword for when the thermal option has been activated by the THERMAL keyword in the RUNSPEC section and for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set equal to one.


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
