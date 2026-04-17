### THCONSF – Define Gas Saturation Dependent Thermal Conductivity Scaling Factor for All Cells {#kw-THCONSF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The THCONSF keyword defines a gas saturation dependent scaling factor to the fluid and reservoir rock thermal conductivities entered via the [THCONR](#kw-THCONR) keyword in the [GRID](#kw-GRID) section, for when the thermal calculation is activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC).

This keyword can only be used if the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | THCONSF | THCONSF is an array of real positive numbers, greater than zero and less than or equal to one, that define the gas saturation dependent scaling factor that is applied to the [THCONR](#kw-THCONR) data, entered via the [THCONR](#kw-THCONR) keyword, to adjust the thermal conductivity of the reservoir cells in each grid block. Repeat counts may be used, for example 3000*0.15 | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: THCROCK Keyword Description {#tbl-6-125}
Note that there two ways to define the rock and in situ fluids thermal conductivity:

- Either by using the [THCONR](#kw-THCONR) keyword to define the combined rock and fluid conductivity, and optionally the THCONSF keyword in the [GRID](#kw-GRID) section, or
- by specifying the rock and fluid conductivities individually using the [THCROCK](#kw-THCROCK), [THCOIL](#kw-THCOIL), [THCGAS](#kw-THCGAS), and [THCWATER](#kw-THCWATER) keywords in the [GRID](#kw-GRID) section.

Hence,  the [THCROCK](#kw-THCROCK) and [THCONR](#kw-THCONR) keywords are mutually exclusive.

Here, the THCONSF keyword defines a scaling factor which is a function of the gas saturation that scales a cells total thermal conductivity (reservoir fluids plus reservoir rock) entered via the [THCONR](#kw-THCONR) keyword in the [GRID](#kw-GRID) section. This combination of keywords, THCONSF and [THCONR](#kw-THCONR) implies that the oil and water phase thermal conductivities are saturation independent with respect to the liquid phase, and that only the gas saturation influences a cell’s thermal conductivity as entered via the [THCONR](#kw-THCONR) keyword.

Thus, THCONSF scales the [THCONR](#kw-THCONR) values via a multiplier Ω, by:


$$
{\mathrm{Ω}}_{i,j,k} = {(1-\text{THCONSF x Gas Saturation})}_{i,j,k}
$$ {#eq-6-21}


See also the [THCGAS](#kw-THCGAS), [THCOIL](#kw-THCOIL), [THCWATER](#kw-THCWATER) and THROCK keywords in the [GRID](#kw-GRID) section, for an alternative way to enter the thermal conductivity properties. However,  the THCONSF keyword cannot be used with the [THCGAS](#kw-THCGAS), [THCOIL](#kw-THCOIL), [THCWATER](#kw-THCWATER) and [THCROCK](#kw-THCROCK) keywords. Secondly, the commercial compositional simulator's THCSOLID keyword is not supported or required by OPM Flow.


#### Example


```
--
--       DEFINE GRID SGAS DEPENDENT SCALING FACTOR FOR THE THCONR ARRAY                            --       FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--       (OPM FLOW THERMAL OPTION ONLY)
--
THCONSF
         300*0.12                                                              /

```

The above example defines the gas saturation thermal conductivity scaling factor to be applied to the [THCONR](#kw-THCONR) to be 0.12 for all 300 cells in the model, as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.