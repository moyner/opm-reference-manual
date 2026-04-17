### RTEMPVD – Define the Initial Reservoir Temperature versus Depth Tables


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the initial reservoir temperature versus depth tables for each equilibration region. Note that the RTEMPVD keyword is an alias for TEMPVD, and that both keywords are supported by OPM Flow, in both the PROPS and SOLUTION sections, but are treated as being mutually exclusive.

The initial reservoir temperature must be defined when OPM Flow’s thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil temperature model, and the THERMAL keyword to activate the compositional thermal model.

The initial reservoir temperature should be defined when OPM Flow’s CO2 or H2 storage option has been activated by the CO2STORE or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keyword in the RUNSPEC section.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column   values that defines the depth for corresponding reservoir temperature parameter TEMP. | None |
| feet | m | cm |  |
| 2 | TEMP | A columnar vector of real monotonically increasing down the column   values that defines the corresponding reservoir temperature for the given depth. | None |
| oF | oC | oC |  |
| Notes: |  |  |  |

*Table 10.31: RTEMPVD Keyword Description*


See also the RTEMP keyword in the PROPS section for an alternative way to define a uniform initial reservoir temperature.


::: {.callout-note}
The keyword is documented here in the SOLUTION section, the same as the commercial simulator, but it can also be used in the PROPS section by OPM Flow.
:::


#### Example


```
--
--       INITIAL RESERVOIR TEMPERATURE VERSUS DEPTH TABLE
--
RTEMPVD
--       DEPTH    TEMPERATURE
--       FEET     DEG F
--       ------   ----------
         1000.0     90.000
         2000.0    100.000
         3000.0    130.000
         4000.0    160.000                                 / TABLE N0. 01
--       ------   ----------
         1000.0     90.000
         2000.0    100.000
         3000.0    130.000
         4000.0    160.000                                 / TABLE N0. 02
--       ------   ----------
         1000.0     90.000
         2000.0    100.000
         3000.0    130.000
         4000.0    160.000                                 / TABLE N0. 03
```


The above example defines three identical reservoir depth versus temperature tables for the three NTEQUIL regions defined on the EQLDIMS keyword in the RUNSPEC section.
