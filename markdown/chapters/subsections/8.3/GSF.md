### GSF – Gas Saturation Function Tables (Gas-Water Systems) {#kw-GSF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GSF keyword defines the gas relative permeability and gas-water capillary pressure data versus gas saturation tables for when only gas and water are present in the input deck.  This keyword should only be used if the gas and water phases are present in the run, and can therefore also be used with the [CO2STORE](#kw-CO2STORE) and [H2STORE](#REF_HEADING_KEYWORD_H2STORE) models. In addition, the keyword must be used in conjunction with the [WSF](#kw-WSF) keyword in the [PROPS](#kw-PROPS) section, that defines the water relative permeability versus water saturation for gas-water systems.


::: {.callout-note}
GSF is a compositional keyword in the commercial compositional simulator, and will therefore cause an error in the commercial black-oil simulator. Currently, both the GSF and [WSF](#kw-WSF) keywords can only be used with the [CO2STORE](#kw-CO2STORE) and [H2STORE](#REF_HEADING_KEYWORD_H2STORE) models.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [SGAS](#kw-SGAS) | A columnar vector of real values monotonically increasing down the column starting from zero and terminating at one minus the connate water saturation, that defines the gas saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | [KRG](#kw-KRG) | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the gas relative permeability. Note that the first entry in the column must be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | PCWG | A columnar vector of real values that are either equal or increasing down the column that defines the gas-water capillary pressure. | None |
| psia | bars | atm |  |
| Notes: |  |  |  |
: GSF Keyword Description {#tbl-8-44}
See also the [WSF](#kw-WSF) - Water Saturation Tables versus Water Saturation (Gas-Water and [CO2STORE](#kw-CO2STORE) Systems) keyword in the [PROPS](#kw-PROPS) section, that defines the water saturation as a function of water saturation for when only the gas and water phases are present in the model.


#### Example


```
--
--       GAS RELATIVE PERMEABILITY TABLES (OPM FLOW KEYWORD)
--
GSF
--       SGAS       KRG        PCGW
--       FRAC                  PSIA
--       --------  --------   -------
             0.00    0.0000      0.0
             0.05    0.0000      0.0
             0.10    0.0000      0.0
             0.15    0.0000      0.0
             0.20    0.0002      0.0
             0.25    0.0010      0.0
             0.30    0.0062      0.0
             0.35    0.0140      0.0
             0.40    0.0273      0.0
             0.45    0.0450      0.0
             0.50    0.0707      0.0
             0.55    0.1020      0.0
             0.60    0.1412      0.0
             0.65    0.1870      0.0
             0.70    0.2412      0.0
             0.77    0.3288      0.0
             0.82    0.4000      0.0
             0.85    0.4450      0.0                       / TABLE NO. 01
--       SGAS       KRG        PCGW
--       FRAC                  PSIA
--       --------  --------   -------
             0.00    0.0000      0.0
             0.05    0.0000      0.0
             0.10    0.0000      0.0
             0.15    0.0000      0.0
             0.20    0.0002      0.0
             0.25    0.0010      0.0
             0.30    0.0062      0.0
             0.35    0.0140      0.0
             0.40    0.0273      0.0
             0.45    0.0450      0.0
             0.50    0.0707      0.0
             0.55    0.1020      0.0
             0.60    0.1412      0.0
             0.65    0.1870      0.0
             0.70    0.2412      0.0
             0.77    0.3288      0.0
             0.82    0.4000      0.0
             0.85    0.4450      0.0                       / TABLE NO. 02
```


The example defines two GSF tables for when gas and water are present in the input deck. In the tables the gas-water capillary pressure data has been set to zero.