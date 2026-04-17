### THCOIL – Define Oil Phase Thermal Conductivity for All Cells {#kw-THCOIL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The THCOIL keyword defines the oil phase thermal conductivity for when the thermal calculation is activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and should be used in conjunction with [THCROCK](#kw-THCROCK) keyword in the [GRID](#kw-GRID) section.

This keyword can only be used if the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | THCOIL | THCOIL is an array of real positive numbers that define the thermal conductivity of the oil phase in each grid block. Repeat counts may be used, for example 3000*20.0 | None |
| Btu/ft/day/°R | kJ/m/day/K | J/cm/hr/K |  |
| Notes: |  |  |  |
: THCOIL Keyword Description {#tbl-6-123}
Note that there two ways to define the rock and in situ fluids thermal conductivity:

- Either by using the [THCONR](#kw-THCONR) keyword to define the combined rock and fluid conductivity, and optionally the [THCONSF](#kw-THCONSF) keyword in the [GRID](#kw-GRID) section, or
- by specifying the rock and fluid conductivities individually using the [THCROCK](#kw-THCROCK), THCOIL, [THCGAS](#kw-THCGAS), and [THCWATER](#kw-THCWATER) keywords in the [GRID](#kw-GRID) section.

Hence,  the [THCROCK](#kw-THCROCK) and [THCONR](#kw-THCONR) keywords are mutually exclusive.

Here, the THCOIL keyword is used in conjunction with the other thermal conductivity arrays to calculate the porosity weighted thermal conductivity of a grid block using:


$$
\text{Average Thermal Conductivity}=\frac{\mathit{[PORO](#kw-PORO)}\times (\mathit{THCOIL}+\mathit{[THCGAS](#kw-THCGAS)}+\mathit{[THCWATER](#kw-THCWATER)}+\mathit{THCSOLID})}{\text{        NUMBER OF PHASES IN THE MODEL}}\times (1-\text{ [PORO](#kw-PORO)})\times \text{[THCROCK](#kw-THCROCK)}
$$ {#eq-6-20}


See also the [THCGAS](#kw-THCGAS), and [THCWATER](#kw-THCWATER), and [THCROCK](#kw-THCROCK) keywords in the [GRID](#kw-GRID) section. The commercial compositional simulator's THCSOLID keyword is not supported or required by OPM Flow.


#### Example


```
--
--       DEFINE GRID BLOCK OIL PHASE THERMAL CONDUCTIVITY
–        FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
THCOIL
         300*20.0                                                              /
```


The above example defines the oil phase thermal conductivity of 20.0 for each cell in the 300 grid block model, as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.