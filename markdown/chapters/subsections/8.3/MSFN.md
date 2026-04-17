### MSFN – Miscible Normalized Relative Permeability Tables {#kw-MSFN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MSFN keyword defines the miscible normalized relative permeability tables for when the [MISCIBLE](#kw-MISCIBLE) and or [SOLVENT](#kw-SOLVENT) options have been activated in the [RUNSPEC](#kw-RUNSPEC) section using the respective keyword. The [MISCIBLE](#kw-MISCIBLE) keyword invokes a three component formulation (oil, water and solvent gas or an oil, water and solvent oil).  Whereas the [SOLVENT](#kw-SOLVENT) keyword results in a four component model (oil, water and gas plus a solvent). This keyword should only be used if the [MISCIBLE](#kw-MISCIBLE) and or [SOLVENT](#kw-SOLVENT) options have been activated.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | [SGAS](#kw-SGAS) | A columnar vector of real monotonically increasing down the column   values starting from zero and terminating at one, that defines the gas plus solvent saturation. | None |
| 2 | KRSG | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the gas plus solvent relative permeability multiplier. | None |
| 3 | [KRO](#kw-KRO) | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the oil relative permeability multiplier. | None |
| Notes: |  |  |  |
: MSFN Keyword Description {#tbl-8-89}
#### Example


```
--
--       MISCIBLE NORMALIZED RELATIVE PERMEABILITY TABLES
--
MSFN
--       SGAS       KRSG         KRO
--       FRAC
--       --------  --------     --------
          0.0000    0.0000       1.0000
          1.0000    1.0000       0.0000                    / TABLE NO. 01

--       SGAS       KRSG         KRO
--       FRAC
--       --------  --------     --------
          0.0000    0.0000       1.0000
          0.2000    0.2000       0.8000
          0.4000    0.3000       0.7000
          0.6000    0.4000       0.6000
          0.8000    0.5000       0.4000
          1.0000    1.0000       0.0000                    / TABLE NO. 02
```


The above example defines two MSN tables for use the [MISCIBLE](#kw-MISCIBLE) and [SOLVENT](#kw-SOLVENT) options.