### NTG – Define the Net-to-Gross Ratio for All the Cells {#kw-NTG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

NTG defines the Net-to-Gross Ratio (“NTG”) for all the cells in the model via an array. The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | NTG | NTG is an array of real numbers greater than or equal to zero and less than or equal to one, that are assigned the net-to-gross ratio values for each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the [DIMENS](#kw-DIMENS) keyword. Repeat counts may be used, for example 200*0.850. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: NTG Keyword Description {#tbl-6-90}
See also the [PORO](#kw-PORO), [PERMX](#kw-PERMX), [PERMY](#kw-PERMY) and [PERMZ](#kw-PERMZ) keywords to fully define a grid’s properties.


#### Example


```
--
--        DEFINE GRID BLOCK NTG DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
NTG
          100*1.000   100*0.850   100*0.500                                     /

```

The above example defines a constant NTG of 1.00 for the first 100 cells, then 0.85 for the second 100 hundred cells, and finally 0.500 for the last 100 cell, for the 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.