### MISC – Define Solvent Miscibility-Immiscibility Transform Functions {#kw-MISC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

MISC defines the transformation between the miscible and immiscible relative permeability models, for when the [MISCIBLE](#kw-MISCIBLE) and [SOLVENT](#kw-SOLVENT) keywords in the [RUNSPEC](#kw-RUNSPEC) section have been activated. The keyword can only be used with the [MISCIBLE](#kw-MISCIBLE) option and for when the oil, water, gas and solvent phases are active in the model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [SSOL](#kw-SSOL) | A columnar vector of real monotonically increasing down the column values starting from zero and terminating at one, that defines the solvent fraction with respect to the solvent and gas saturation, and is defined by: $\frac{{S}_{s}}{({S}_{g} + {S}_{s})}$ Where Sg is the gas saturation and Ss is the solvent saturation. Note that the first entry in the columnar vector should be zero and the last entry should be one to fully define the solvent fraction range. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | MISC | A columnar vector of real equal or increasing down the column values that are greater than or equal to zero and less then one,  that define the corresponding miscibility for the corresponding solvent fraction [SSOL](#kw-SSOL). The first entry in the columnar vector should be zero and the last entry should be one to fully define the miscible-immiscible relationship. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: MISC Keyword Description {#tbl-8-88}
#### Example


```
--
--       SOLVENT MISCIBILITY-IMMISCIBLITY TRANSFORM TABLE
--
MISC
--       SSOL       MISC
--       FRAC       FRAC
--       -------    --------
          0.0000     0.0000
          0.2000     0.2500
          0.5000     0.7500
          1.0000     1.0000                                / TABLE NO. 01

--       SSOL       MISC
--       FRAC       FRAC
--       -------    --------
          0.0000     0.0000
          0.3000     0.2500
          0.6000     1.0000
          1.0000     1.0000                                / TABLE NO. 02
```


The above example defines two solvent miscible-immiscible transform tables assuming NTMISC equals two and NSMISC is greater than or equal to four on the [MISCIBLE](#kw-MISCIBLE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.