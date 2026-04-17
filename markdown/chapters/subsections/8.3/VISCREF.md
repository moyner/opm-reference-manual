### VISCREF –  Define Viscosity-Temperature Reference Conditions {#kw-VISCREF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

VISCREF defines the reference conditions for the viscosity-temperature tables, [GASVISCT](#kw-GASVISCT), [OILVISCT](#kw-OILVISCT) and [WATVISCT](#kw-WATVISCT), for when the thermal option has been activated by [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. This keyword can only be used if the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PRES | PRES is a real positive number defining the reference pressure for the viscosity and temperature tables | None |
| psia | barsa | atma |  |
| 2 | [RS](#kw-RS) | [RS](#kw-RS) is a real positive number defining the reference gas-oil ratio for when the model contains gas dissolved as activated by the [DISGAS](#kw-DISGAS) keyword in the [RUNSPEC](#kw-RUNSPEC) section | None |
| Mscf/stb | sm3/sm3 | scc/scc |  |
| 3 | [API](#kw-API) | [API](#kw-API) is a real number defining the oil [API](#kw-API) for when the [API](#kw-API) tracking option has been invoked by the [API](#kw-API) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note that OPM Flow does not support [API](#kw-API) tracking, and therefore this variable is ignored. | None |
| oAPI | oAPI | oAPI |  |
| Notes: |  |  |  |
: VISCREF Keyword Description {#tbl-8-196}
OPM Flow currently does not support [API](#kw-API) tracking and therefore item (3) of this keyword is ignored.  See also the [OILVISCT](#kw-OILVISCT), [GASVISCT](#kw-GASVISCT) and [WATVISCT](#kw-WATVISCT) keywords in the [PROPS](#kw-PROPS) section.


#### Example

The following example shows the VISCREF keyword for when the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section and for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set to five.


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