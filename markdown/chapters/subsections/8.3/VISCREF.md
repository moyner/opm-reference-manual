### VISCREF –  Define Viscosity-Temperature Reference Conditions


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

VISCREF defines the reference conditions for the viscosity-temperature tables, GASVISCT, OILVISCT and WATVISCT, for when the thermal option has been activated by THERMAL keyword in the RUNSPEC section. This keyword can only be used if the thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRES | PRES is a real positive number defining the reference pressure for the viscosity and temperature tables | None |
| psia | barsa | atma |  |
| 2 | RS | RS is a real positive number defining the reference gas-oil ratio for when the model contains gas dissolved as activated by the DISGAS keyword in the RUNSPEC section | None |
| Mscf/stb | sm3/sm3 | scc/scc |  |
| 3 | API | API is a real number defining the oil API for when the API tracking option has been invoked by the API keyword in the RUNSPEC section. Note that OPM Flow does not support API tracking, and therefore this variable is ignored. | None |
| oAPI | oAPI | oAPI |  |
| Notes: |  |  |  |

*Table 8.196: VISCREF Keyword Description*


OPM Flow currently does not support API tracking and therefore item (3) of this keyword is ignored.  See also the OILVISCT, GASVISCT and WATVISCT keywords in the PROPS section.


#### Example

The following example shows the VISCREF keyword for when the thermal option has been activated by the THERMAL keyword in the RUNSPEC section and for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to five.


```
--
--       REF        REF       REF
--       PRESSURE   GOR       API
--       --------   -------   -------
VISCREF
          3000.0    0.500                                  / TABLE NO. 01
          3200.0    0.550                                  / TABLE NO. 02
          3300.0    0.580                                  / TABLE NO. 03
          3400.0    0.620                                  / TABLE NO. 04
          3500.0    0.625                                  / TABLE NO. 05
```


There is no terminating “/” for this keyword.
