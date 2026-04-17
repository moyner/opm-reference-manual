### RTEMP – Define the Initial Reservoir Temperature for the Model {#kw-RTEMP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the initial reservoir temperature for the model. Note that the RTEMP keyword is an alias for [RTEMPA](#kw-RTEMPA), and that both keywords are supported by OPM Flow, in both the [PROPS](#kw-PROPS) and [SOLUTION](#kw-SOLUTION) sections, but are treated as being mutually exclusive.

The initial reservoir temperature must be defined when OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil temperature model, and the [THERMAL](#kw-THERMAL) keyword to activate the compositional thermal model.

The initial reservoir temperature should be defined when OPM Flow’s CO2 or H2 storage option has been activated by the [CO2STORE](#kw-CO2STORE) or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | RTEMP | Single real positive value that defines the reservoir temperature for the model. | None |
| oF | oC | oC |  |
| Notes: |  |  |  |
: RTEMP Keyword Description {#tbl-8-3-259-1}
See also the [RTEMPVD](#kw-RTEMPVD) keyword in [SOLUTION](#kw-SOLUTION) section to define the reservoir temperature as a function of depth.


#### Example


```
--
--       RESERVOIR
--       TEMPERATURE
--       -----------
RTEMP
         190.0                                            / RESERVOIR TEMPERATURE
```


The above example defines the reservoir temperature to be 190 oF.