### ROCK2D – Pore Volume Compaction versus Pressure and Sw Tables {#kw-ROCK2D}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ROCK2D keyword defines rock compressibility pore volume multipliers as a function of pressure and water saturation (“Sw”) for when the rock compaction option has been invoked by the [ROCKCOMP](#kw-ROCKCOMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The pressure values are defined on this keyword and the water saturations are declared on the associated [ROCKWNOD](#kw-ROCKWNOD) keyword in the [PROPS](#kw-PROPS) section

The rock compaction pore volume and transmissibility multipliers, entered via the [ROCKTAB](#kw-ROCKTAB), ROCK2D and  [ROCK2DTR](#kw-ROCK2DTR) keywords, are applied to the pore pressure, unless the [OVERBURD](#kw-OVERBURD) keyword in [PROPS](#kw-PROPS) section is included in the input deck.  When the [OVERBURD](#kw-OVERBURD) keyword is present the multipliers are applied to the effective pore volume pressure, that is${P}_{(\mathit{effective})} = {P}_{(\mathit{Pressure})} - {P}_{(\mathit{overburden})}$. If the keyword is not present in the input deck then the overburden pressure is set to zero.

This keyword should only be used if compaction option has been enabled.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | A columnar vector of real monotonically increasing down the column   values that defines the corresponding overburden pressure for the subsequent MULT columnar vector. | None |
| psia | bars | atm |  |
| 2 | MULT | A columnar vector of real equal or decreasing down the column values that are less than or equal to one, that defines the rock compressibility pore volume multipliers corresponding to PRESS and for each water saturation entry in the [ROCKWNOD](#kw-ROCKWNOD) keyword. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: ROCK2D Keyword Description {#tbl-8-126}
See also the [OVERBURD](#kw-OVERBURD), [ROCKTAB](#kw-ROCKTAB),  [ROCK2DTR](#kw-ROCK2DTR), and [ROCKWNOD](#kw-ROCKWNOD) keywords in the [PROPS](#kw-PROPS) section.


#### Example

The following example defines two pore volume compaction tables, assuming NTROCC is equal to two on the [ROCKCOMP](#kw-ROCKCOMP) keyword and NSSFUN is greater than or equal to four on the [TABDIMS](#kw-TABDIMS) keyword.


```
--
--       ROCK COMPACTION VERSUS PRESSURE AND SW TABLES
--
ROCK2D
--       PRESS    PORV          FIRST ROCK2D TABLE DATA
--       PSIA     MULTIPLER
--       ------   ----------
            0.0      0.850
                     0.850
                     0.850
                     0.085                                / P-SW SET TABLE NO. 01
--       PRESS    PORV
--       PSIA     MULTIPLER
--       ------   ----------
         1000.0      0.900
                     0.900
                     0.900
                     0.900                                / P-SW SET TABLE NO. 01
--       PRESS    PORV
--       PSIA     MULTIPLER
--       ------   ----------
         2500.0      0.950
                     0.950
                     0.950
                     0.950                                / P-SW SET TABLE NO. 01
--       PRESS    PORV
--       PSIA     MULTIPLER
--       ------   ----------
         5000.0      1.000
                     1.000
                     1.000
                     1.000                                / P-SW SET TABLE NO. 01
--
--       PRESS    PORV          SECOND ROCK2D TABLE DATA
--       PSIA     MULTIPLER
--       ------   ----------
            0.0      0.800
                     0.800
                     0.800
                     0.800                                / P-SW SET TABLE NO. 02
--       PRESS    PORV
--       PSIA     MULTIPLER
--       ------   ----------
         1000.0      0.880
                     0.880
                     0.880
                     0.880                                / P-SW SET TABLE NO. 02
--       PRESS    PORV
--       PSIA     MULTIPLER
--       ------   ----------
         2500.0      0.950
                     0.950
                     0.950
                     0.950                                / P-SW SET TABLE NO. 02
--       PRESS    PORV
--       PSIA     MULTIPLER
--       ------   ----------
         5000.0      1.000
                     1.000
                     1.000
                     1.000                                / P-SW SET TABLE NO. 02
```

Note that there must be exactly NTROCC tables entered for this keyword, otherwise an error will occur.