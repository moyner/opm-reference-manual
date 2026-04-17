### THCONR – Define Rock and Fluid Thermal Conductivity for All Cells {#kw-THCONR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The THCONR keyword defines the reservoir rock plus fluid thermal conductivity for all cells for when the thermal calculation is activated by the [THERMAL](#kw-THERMAL) keywords in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword can only be used if the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | THCONR | THCONR is an array of real positive numbers that define the combined rock and fluid conductivity of a grid block. Repeat counts may be used, for example 3000*25.0 | None |
| Btu/ft/day/°R | kJ/m/day/K | J/cm/hr/K |  |
| Notes: |  |  |  |
: THCONR Keyword Description {#tbl-6-124}
Note that there two ways to define the rock and in situ fluids thermal conductivity:

- Either by using the THCONR keyword to define the combined rock and fluid conductivity, and optionally the [THCONSF](#kw-THCONSF) keyword in the [GRID](#kw-GRID) section, or
- by specifying the rock and fluid conductivities individually using the [THCROCK](#kw-THCROCK), [THCOIL](#kw-THCOIL), [THCGAS](#kw-THCGAS), and [THCWATER](#kw-THCWATER) keywords in the [GRID](#kw-GRID) section.

Hence,  the [THCROCK](#kw-THCROCK) and THCONR keywords are mutually exclusive.


#### Example


```
--
--       DEFINE GRID BLOCK ROCK-FLUID THERMAL CONDUCTIVITY
–        FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
THCONR
         300*25.0                                                              /
```


The above example defines the combined rock and fluid thermal conductivity of 25.0 for each cell in the 300 grid block model, as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.