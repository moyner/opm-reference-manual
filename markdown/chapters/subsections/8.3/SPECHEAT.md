### SPECHEAT – Define the Specific Heat of Oil, Water and Gas {#kw-SPECHEAT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SPECHEAT defines the specific heat of the oil, water and gas phases for various PVT regions in the model  for when the [THERMAL](#kw-THERMAL) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. The number of SPECHEAT vector data sets is defined by the NTPVT parameter on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the allocation of the SPECHEAT data sets to different grid blocks in the model is done via the [PVTNUM](#kw-PVTNUM) keyword in the [REGIONS](#kw-REGIONS) section.

This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [TEMP](#kw-TEMP) | A columnar vector of real monotonically increasing down the column   values that define the temperature for the corresponding oil, water and gas specific heat values. | None |
| oF | oC | oC |  |
| 2 | OILSHEAT | OILSHEAT is a columnar vector of positive real numbers defining the specific heat of oil at the corresponding temperature, [TEMP](#kw-TEMP). | None |
| Btu/lb/oR | kJ/kg/K | J/gm/K |  |
| 3 | WATSHEAT | WATSHEAT is a columnar vector of positive real numbers defining the specific heat of water at the corresponding temperature, [TEMP](#kw-TEMP). | None |
| Btu/lb/oR | kJ/kg/K | J/gm/K |  |
| 4 | GASSHEAT | GASHEAT is a columnar vector of positive real numbers defining the specific heat of gas at the corresponding temperature, [TEMP](#kw-TEMP). | None |
| Btu/lb/oR | kJ/kg/K | J/gm/K |  |
| Notes: |  |  |  |
: SPECHEAT Keyword Description {#tbl-8-170}
See also the [SPECROCK](#kw-SPECROCK) keyword to define the reservoir rock specific heat.


#### Example

The example below defines three fluid phases specific heat versus temperature tables assuming NTPVT equals three and NPPVT is greater than or equal to two on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


```
--
--       SPECIFIC HEAT OF OIL, WATER AND GAS TABLE
--
SPECHEAT
--       TEMP       SPECHEAT   SPECHEAT   SPECHEAT
--                  OIL        WATER      GAS
--       -------    --------   --------   --------
           0.000     0.5000     1.5000     0.5000
         250.000     0.5000     1.5000     0.5000          / TABLE NO. 01
--       TEMP       SPECHEAT   SPECHEAT   SPECHEAT
--                  OIL        WATER      GAS
--       -------    --------   --------   --------
           0.000     0.5500     1.5000     0.5000
         260.000     0.5500     1.5000     0.5000          / TABLE NO. 02
--       TEMP       SPECHEAT   SPECHEAT   SPECHEAT
--                  OIL        WATER      GAS
--       -------    --------   --------   --------
           0.000     0.5500     1.5500     0.5000
         270.000     0.6000     1.5500     0.5000          / TABLE NO. 03
```


There is no terminating “/” for this keyword.