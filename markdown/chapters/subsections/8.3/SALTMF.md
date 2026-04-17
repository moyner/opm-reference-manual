### SALTMF – Define the Salt Liquid-Phase Mole Fraction for All Cells {#kw-SALTMF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SALTMF keyword defines a uniform salt liquid-phase mole fraction for all cells in the model. The keyword should only be used with OPM Flow’s CO2-Brine model which is activated via the [CO2STORE](#kw-CO2STORE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This is an OPM Flow specific keyword.


| No. | Name | Description | Default |  |  |
| --- | --- | :------ | --- | --- | --- |
|  |  | Field | Metric | Laboratory | 0 |
| 1 | SALTMF | A real positive value that defines the salt liquid-phase mole fraction for all grid blocks in the model for when the CO2-Brine model has been activated. |  |  |  |
| mole fraction | mole fraction | mole fraction |  |  |  |
| Notes: |  |  |  |  |  |
: SALTMF Keyword Description {#tbl-8-3-277-1}
See also the [CO2STORE](#kw-CO2STORE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


#### Example

The example sets the salt liquid-phase mole fraction for all cells in the model to 0.018.


```
--
--       SET SALT LIQUID-PHASE MOLE FRACTION FOR ALL CELLS (OPM FLOW KEYWORD)
--
SALTMF
         0.018                                             /
```