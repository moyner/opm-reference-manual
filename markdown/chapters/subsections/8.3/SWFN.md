### SWFN – Water Saturation Tables (Format Type 2)


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [SWFN](#__RefHeading___Toc106882_335817223) keyword defines the water relative permeability and water-oil capillary pressure data versus water saturation tables for when water is present in the input deck.  This keyword should only be used if water is present in the run.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SWAT](#__RefHeading___Toc137373_1317547213) | A columnar vector of real monotonically increasing down the column   values starting from zero and terminating at one, that defines the water  saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | [KRW](#__RefHeading___Toc97397_621662414) | A columnar vector of real values that are either equal or increasing down the column and that are greater than or equal to zero and less than or equal to one that defines the water relative permeability with respect to gas saturation. The first value in the column should be zero. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | PCWO | A columnar vector of real values that are either equal or increasing down the column that defines the water-oil relative capillary pressure. If the [SWATINIT](#__RefHeading___Toc323952_1728001293) keyword has been used to initialize the model then columnar vector has to be strictly monotonically increasing. | None |
| psia | bars | atm |  |
| Notes: |  |  |  |

*Table 8.3.332.1: SWFN Keyword Description*


#### Example


```
--
--       WATER RELATIVE PERMEABILITY TABLES (SWFN)
--
SWFN
--       SWAT       KRW        PCOW
--       FRAC       FRAC       PSIA
--       --------   --------   -------
            0.15     0.00000     0.0
            0.20     6.25e-6     0.0
            0.25     0.00010     0.0
            0.30     0.00050     0.0
            0.35     0.00160     0.0
            0.40     0.00390     0.0
            0.45     0.00810     0.0
            0.50     0.01500     0.0
            0.55     0.02560     0.0
            0.60     0.04100     0.0
            0.65     0.06250     0.0
            0.70     0.09150     0.0
            0.75     0.12960     0.0
            0.80     0.17850     0.0
            0.85     0.24010     0.0
            0.90     0.31640     0.0
            0.95     0.40960     0.0
            1.00     0.52200     0.0                       / TABLE NO. 1
--       --------   --------   -------
            0.15     0.00000     0.0
            0.20     6.25e-6     0.0
            0.25     0.00010     0.0
            0.30     0.00050     0.0
            0.35     0.00160     0.0
            0.40     0.00390     0.0
            0.45     0.00810     0.0
            0.50     0.01500     0.0
            0.55     0.02560     0.0
            0.60     0.04100     0.0
            0.65     0.06250     0.0
            0.70     0.09150     0.0
            0.75     0.12960     0.0
            0.80     0.17850     0.0
            0.85     0.24010     0.0
            0.90     0.31640     0.0
            0.95     0.40960     0.0
            1.00     0.52200     0.0                       / TABLE NO. 2
```


The example defines two [SWFN](#__RefHeading___Toc106882_335817223) tables for use when water is present in the run.
