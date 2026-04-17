### SOF3 – Oil Saturation Tables with Respect to Gas and Water (Format Type 2) {#kw-SOF3}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SOF3 keyword defines the oil relative permeability versus oil saturation tables for when oil, gas and water are present in the input deck.  The keyword should only be used if oil, gas and water are present in the input deck.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [SOIL](#kw-SOIL) | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the oil or the hydrocarbon solvent saturation. The final entry should be at the connate water saturation, that is 1- Swc. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | KROW | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the oil relative permeability with respect to oil and water saturation. The first value in the column should be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | KROG | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the oil relative permeability with respect to oil, gas and connate water saturation. The first value in the column should be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SOF3 Keyword Description {#tbl-8-166}
#### Example


```
--
--       OIL RELATIVE PERMEABILITY TABLES (SOF3)
--
SOF3
--       SOIL         KRO          KROG
--       FRAC         FRAC         FRAC
--       --------     --------    --------
            0.00      0.000000    0.00000
            0.05      1.197e-5    0.00000
            0.10      0.000191    0.00000
            0.15      0.000969    0.00000
            0.20      0.003065    0.00000
            0.25      0.007483    0.00000
            0.30      0.015517    0.05932
            0.35      0.028747    0.13158
            0.40      0.049041    0.21082
            0.45      0.078555    0.29960
            0.50      0.119730    0.40095
            0.55      0.175297    0.51818
            0.60      0.248272    0.65476
            0.65      0.341961    0.81420
            0.70      0.459956    1.00000
            0.75      0.606134    1.00000
            0.80      0.784664    1.00000
            0.85      1.000000    1.00000                  / TABLE NO. 1
--       --------     --------    --------
            0.00      0.000000    0.00000
            0.05      1.197e-5    0.00000
            0.10      0.000191    0.00000
            0.15      0.000969    0.00000
            0.20      0.003065    0.00000
            0.25      0.007483    0.00000
            0.30      0.015517    0.05932
            0.35      0.028747    0.13158
            0.40      0.049041    0.21082
            0.45      0.078555    0.29960
            0.50      0.119730    0.40095
            0.55      0.175297    0.51818
            0.60      0.248272    0.65476
            0.65      0.341961    0.81420
            0.70      0.459956    1.00000
            0.75      0.606134    1.00000
            0.80      0.784664    1.00000
            0.85      1.000000    1.00000                  / TABLE NO. 2
```


The example defines two SOF3 tables for when oil, gas and water are present in the input deck.