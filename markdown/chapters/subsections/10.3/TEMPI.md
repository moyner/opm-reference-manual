### TEMPI – Define the Initial Temperature Values for All Cells {#kw-TEMPI}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the initial reservoir temperature for each cell in the model. The keyword is used to explicitly define the initial reservoir temperature via the Enumeration Initialization method rather than defining a uniform initial temperature or defining temperature versus depth tables.

The initial reservoir temperature must be defined when OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil temperature model, and the [THERMAL](#kw-THERMAL) keyword to activate the compositional thermal model.

The initial reservoir temperature should be defined when OPM Flow’s CO2 or H2 storage option has been activated by the [CO2STORE](#kw-CO2STORE) or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | TEMPI | TEMPI is an array of real positive numbers assigning the initial temperature to each cell in the model. Repeat counts may be used, for example 20*100.0. | None |
| oF | oC | oC |  |
| Notes: |  |  |  |
: TEMPI Keyword Description {#tbl-10-58}
See also the [RTEMP](#kw-RTEMP) keyword in the [PROPS](#kw-PROPS) section and the [RTEMPVD](#kw-RTEMPVD) keyword in the [SOLUTION](#kw-SOLUTION) section for alternative ways to initialize the model’s initial temperature.


#### Example


```
--
--       DEFINE GRID BLOCK TEMPERATURE FOR ALL CELLS
–        (BASED ON NX x NY x NZ = 300)
--
TEMPI
         100*212.0   100*215.0   100*220.0                                     /

```

The above example defines the initial temperature to be 212.0, 215.0, and 220.0 oF for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.