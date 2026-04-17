### THCWATER – Define Water Phase Thermal Conductivity for All Cells {#kw-THCWATER}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The THCWATER keyword defines the water phase thermal conductivity for when the thermal calculation is activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and should be used in conjunction with [THCROCK](#kw-THCROCK) keyword in the [GRID](#kw-GRID) section.

This keyword can only be used if the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | THCWATER | THCWATER is an array of real positive numbers that define the thermal conductivity of the water phase in each grid block. Repeat counts may be used, for example 3000*20.0 | None |
| Btu/ft/day/°R | kJ/m/day/K | J/cm/hr/K |  |
| Notes: |  |  |  |
: THCWATER Keyword Description {#tbl-6-127}
Note that there two ways to define the rock and in situ fluids thermal conductivity:

- Either by using the [THCONR](#kw-THCONR) keyword to define the combined rock and fluid conductivity, and optionally the [THCONSF](#kw-THCONSF) keyword in the [GRID](#kw-GRID) section, or
- by specifying the rock and fluid conductivities individually using the [THCROCK](#kw-THCROCK), [THCOIL](#kw-THCOIL), [THCGAS](#kw-THCGAS), and THCWATER keywords in the [GRID](#kw-GRID) section.

Hence,  the [THCROCK](#kw-THCROCK) and [THCONR](#kw-THCONR) keywords are mutually exclusive.

Here, the THCWATER keyword is used in conjunction with the other thermal conductivity arrays to calculate the porosity weighted thermal conductivity of a grid block using:


$$
\text{Average Thermal Conductivity}=\frac{\mathit{[PORO](#kw-PORO)}\times (\mathit{[THCOIL](#kw-THCOIL)}+\mathit{[THCGAS](#kw-THCGAS)}+\mathit{THCWATER}+\mathit{THCSOLID})}{\text{        NUMBER OF PHASES IN THE MODEL}}\times (1-\mathit{[PORO](#kw-PORO)})\times \mathit{[THCROCK](#kw-THCROCK)}
$$ {#eq-6-23}


See also the [THCGAS](#kw-THCGAS), and [THCOIL](#kw-THCOIL), and [THCROCK](#kw-THCROCK) keywords in the [GRID](#kw-GRID) section. The commercial compositional simulator's THCSOLID keyword is not supported or required by OPM Flow


#### Example


```
--
--       DEFINE GRID BLOCK WATER PHASE THERMAL CONDUCTIVITY
–        FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
THCWATER
         300*2O.0                                                              /
```


The above example defines the water phase thermal conductivity of 20.0 for each cell in the 300 grid block model, as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.