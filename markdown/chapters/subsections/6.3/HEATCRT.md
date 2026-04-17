### HEATCRT – Define Reservoir Rock Heat Capacity Temperature Dependence for All Cells {#kw-HEATCRT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HEATCRT keyword defines the reservoir rock volumetric heat capacity temperature dependence for all cells for when OPM Flow’s thermal calculation is activated by the [THERMAL](#kw-THERMAL) keywords in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | HEATCRT | HEATCRT is an array of real positive numbers that define reservoir rock volumetric heat capacity temperature dependence of a grid block. Repeat counts may be used, for example 3000*0.05 | None |
| Btu/ft3/°R2 | kJ/m3/K2 | J/cm3/K2 |  |
| Notes: |  |  |  |
: HEATCRT Keyword Description {#tbl-6-44}
Note this keyword is incompatible with [SPECROCK](#kw-SPECROCK) keyword in the [PROPS](#kw-PROPS) section.

The data for this keyword and the [HEATCR](#kw-HEATCR) keyword are used to calculate the reservoir rock volumetric heat capacity temperature dependence using the following relationship:


$$
\text{Heat Capacity of Rock }=\text{[HEATCR](#kw-HEATCR)}(\mathit{Temp} - {\mathit{Temp}}_{\mathit{ref}}) + \frac{\text{HEATCRT}{(\mathit{Temp} - {\mathit{Temp}}_{\mathit{ref}})}^{2}}{2}
$$ {#eq-6-3}


#### Example


```
--
--       DEFINE RESERVOIR ROCK HEAT CAPACITY TEMPERATURE DEPENDENCE
--       FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--       KEYWORD IS INCOMPATIBLE WITH THE SPECROCK KEYWORD
--       (OPM FLOW THERMAL OPTION ONLY)
--
HEATCRT
         300*0.05                                                              /
```


The above example defines the reservoir rock volumetric heat capacity temperature dependence of 0.05 for each cell in the 300 grid block model.