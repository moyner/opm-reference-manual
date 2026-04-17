### SORWMIS – Miscible Residual Oil versus Water Saturation Functions {#kw-SORWMIS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SORWMIS defines the dependency between the miscible residual oil saturation and the water saturation, for when the [MISCIBLE](#kw-MISCIBLE) keyword in the [RUNSPEC](#kw-RUNSPEC) section has been activated. The keyword can only be used with the [MISCIBLE](#kw-MISCIBLE) option and for when the oil, water and gas phases are active in the model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [SWAT](#kw-SWAT) | A columnar vector of real monotonically increasing down the column   values starting from zero and terminating at one, that defines the water  saturation. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | SORMIS | A columnar vector of real equal or increasing down the column values that are greater than or equal to zero and less than one,  that define the corresponding miscible residual oil saturation for the corresponding water saturation [SWAT](#kw-SWAT). | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SORWMIS Keyword Description {#tbl-8-168}
#### Example


```
--
--       MISCIBLE RESIDUAL OIL VERSUS WATER SATURATION TABLE
--
SORWMIS
--       SWAT       SORWMIS
--       FRAC       FRAC
--       -------    --------
          0.0000     0.0000
          0.2000     0.0000
          1.0000     0.0000                                / TABLE NO. 01
--       SWAT       SORWMIS
--       FRAC       FRAC
--       -------    --------
          0.0000     0.0000
          0.3000     0.1000
          0.7500     0.1500                                / TABLE NO. 02
```


The above example defines two miscible residual oil versus water saturation tables assuming NTMISC equals two and NSMISC is greater than or equal to three on the [MISCIBLE](#kw-MISCIBLE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.