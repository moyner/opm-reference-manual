### PORO – Define the Porosity Values for All the Cells {#kw-PORO}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PORO defines the porosity for all the cells in the model via an array. The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PORO | PORO is an array of real positive numbers that are greater than or equal to zero and less than or equal to one that are the porosity values for each cell in the model. Repeat counts may be used, for example 3000*0.15 | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: PORO Keyword Description {#tbl-6-112}
See also the [NTG](#kw-NTG), [PERMX](#kw-PERMX), [PERMY](#kw-PERMY) and [PERMX](#kw-PERMX) keywords to fully define a grid’s properties


#### Example


```
--
--    DEFINE GRID BLOCK POROSITY DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
PORO
      300*0.300                                                                 /

```

The above example defines a constant porosity of 0.300 to all 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.