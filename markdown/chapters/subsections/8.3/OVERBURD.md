### OVERBURD – Define Rock Overburden Pressure versus Depth Tables {#kw-OVERBURD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The OVERBURD keyword defines the overburden pressures versus depth relationship to be applied for when the rock compaction option has been invoked by the [ROCKCOMP](#kw-ROCKCOMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

The rock compaction pore volume and transmissibility multipliers, entered via the [ROCKTAB](#kw-ROCKTAB), [ROCK2D](#kw-ROCK2D) and  [ROCK2DTR](#kw-ROCK2DTR) keywords, are applied to the pore pressure, unless the OVERBURD keyword is included in the input deck.  When the OVERBURD keyword is present the multipliers are applied to the effective pore volume pressure, that is ${P}_{(\mathit{effective})} = {P}_{(\mathit{Pressure})} - {P}_{(\mathit{overburden})}$. If the keyword is not present in the input deck then the overburden pressure is set to zero.

This keyword should only be used if compaction option has been enabled.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth for corresponding overburden pressure parameter PRESS. | None |
| feet | m | cm |  |
| 2 | PRESS | A columnar vector of real monotonically increasing down the column   values that defines the corresponding overburden pressure for the given [DEPTH](#kw-DEPTH). | None |
| psia | bars | atm |  |
| Notes: |  |  |  |
: OVERBURD Keyword Description {#tbl-8-94}
See also the [ROCKTAB](#kw-ROCKTAB),  [ROCK2D](#kw-ROCK2D), [ROCK2DTR](#kw-ROCK2DTR), and [ROCKWNOD](#kw-ROCKWNOD) keywords in the [PROPS](#kw-PROPS) section.


#### Examples

The example below defines three overburden tables, assuming NTROCC is equal to three on the [ROCKCOMP](#kw-ROCKCOMP) keyword and NPPVT is greater than or equal to four on the [TABDIMS](#kw-TABDIMS) keyword.


```
--
--       OVERBURDEN PRESSURE VERSUS DEPTH TABLES
--
OVERBURD
--       DEPTH    OVERBURDEN
--       FEET     PRESSURE
--       ------   ----------
         1000.0    300.000
         2000.0    600.000
         3000.0    900.000
         4000.0   1200.000                                 / TABLE N0. 01
--       DEPTH    OVERBURDEN
--       FEET     PRESSURE
--       ------   ----------
         1000.0    200.000
         2000.0    400.000
         3000.0    800.000
         4000.0   1000.000                                 / TABLE N0. 02
--       DEPTH    OVERBURDEN
--       FEET     PRESSURE
--       ------   ----------
         1000.0    400.000
         2000.0    800.000
         3000.0   1100.000
         4000.0   1500.000                                 / TABLE N0. 03
```

Note that there must be exactly NTROCC tables entered for this keyword, otherwise an error will occur.


```
--
--       ROCK COMPACTION TABLES
--
ROCKTAB
--       PRESS    PORV     TX(YZ)
--                MULT     MULT
--       ------   ------   ------
         1000.0   0.9600   0.9650
         1500.0   0.9800   0.9850
         3000.0   0.9900   0.9950
         4500.0   1.0000   1.0000
         4750.0   1.0100   1.0100                          / TABLE NO. 01
--       PRESS    PORV     TX(YZ)
--                MULT     MULT
--       ------   ------   ------
         1000.0   0.9600   0.9650
         1500.0   0.9800   0.9850
         3000.0   0.9900   0.9950
         4500.0   1.0000   1.0000
         4750.0   1.0100   1.0100                          / TABLE NO. 02
--       PRESS    PORV     TX(YZ)
--                MULT     MULT
--       ------   ------   ------
         1000.0   0.9600   0.9650
         2000.0   0.9800   0.9850
         3000.0   0.9900   0.9950
         4000.0   1.0100   1.0100                          / TABLE NO. 03
```


Here [ROCKTAB](#kw-ROCKTAB) tables one and two are identical.