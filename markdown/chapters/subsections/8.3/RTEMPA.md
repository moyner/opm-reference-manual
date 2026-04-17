### RTEMPA – Define the Initial Reservoir Temperature for the Model


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the initial reservoir temperature for the model. Note that the RTEMPA keyword is an alias for RTEMP, and that both keywords are supported by OPM Flow, in both the PROPS and SOLUTION sections, but are treated as being mutually exclusive.

The initial reservoir temperature must be defined when OPM Flow’s thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil temperature model, and the THERMAL keyword to activate the compositional thermal model.

The initial reservoir temperature should be defined when OPM Flow’s CO2 or H2 storage option has been activated by the CO2STORE or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keyword in the RUNSPEC section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | RTEMPA | Single real positive value that define the reservoir temperature for the model. | None |
| oF | oC | oC |  |
| Notes: |  |  |  |

*Table 8.136: RTEMPA Keyword Description*

See also the RTEMPVD keyword in SOLUTION section to define the reservoir temperature as a function of depth.


#### Example


```
--
--       RESERVOIR
--       TEMPERATURE
--       -----------
RTEMPA
         190.0                                            / RESERVOIR TEMPERATURE
```


The above example defines the reservoir temperature to be 190 oF.
