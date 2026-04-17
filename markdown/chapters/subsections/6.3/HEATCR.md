### HEATCR – Define Reservoir Rock Heat Capacity for All Cells {#kw-HEATCR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HEATCR keyword defines the reservoir rock volumetric heat capacity for all cells for when OPM Flow’s thermal calculation is activated by the [THERMAL](#kw-THERMAL) keywords in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | HEATCR | HEATCR is an array of real positive numbers that define reservoir rock volumetric heat capacity of a grid block. Repeat counts may be used, for example 3000*25.0 | None |
| Btu/ft3/°R | kJ/m3/K | J/cm3/K |  |
| Notes: |  |  |  |
: HEATCR Keyword Description {#tbl-6-43}
Note this keyword is incompatible with [SPECROCK](#kw-SPECROCK) keyword in the [PROPS](#kw-PROPS) section.


#### Example


```
--
--       DEFINE GRID BLOCK RESERVOIR ROCK HEAT CAPACITY
--       FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--       KEYWORD IS INCOMPATIBLE WITH THE SPECROCK KEYWORD
--       (OPM FLOW THERMAL OPTION ONLY)
--
HEATCR
         300*32.0                                                              /
```


The above example defines the reservoir rock volumetric heat capacity of 32.0 for each cell in the 300 grid block model.