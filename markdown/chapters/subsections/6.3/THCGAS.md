### THCGAS – Define Gas Phase Thermal Conductivity for All Cells


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The THCGAS keyword defines the gas phase thermal conductivity for when the thermal calculation is activated by the THERMAL keyword in the RUNSPEC section, and should be used in conjunction with THCROCK keyword in the GRID section.

This keyword can only be used if the thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | THCGAS | THCGAS is an array of real positive numbers that define the thermal conductivity of the gas phase in each grid block. Repeat counts may be used, for example 3000*20.0 | None |
| Btu/ft/day/°R | kJ/m/day/K | J/cm/hr/K |  |
| Notes: |  |  |  |

*Table 6.122: THCGAS Keyword Description*


Note that there two ways to define the rock and in situ fluids thermal conductivity:

    - Either by using the THCONR keyword to define the combined rock and fluid conductivity, and optionally the THCONSF keyword in the GRID section, or
    - by specifying the rock and fluid conductivities individually using the THCROCK, THCOIL, THCGAS, and THCWATER keywords in the GRID section.

Hence,  the THCROCK and THCONR keywords are mutually exclusive.

Here, the THCGAS keyword is used in conjunction with the other thermal conductivity arrays to calculate the porosity weighted thermal conductivity of a grid block using:


$$
\text{Average Thermal Conductivity}=\frac{\mathit{PORO}\times (\mathit{THCOIL}+\mathit{THCGAS}+\mathit{THCWATER}+\mathit{THCSOLID})}{\text{        NUMBER OF PHASES IN THE MODEL}}\times (1-\mathit{PORO})\times \mathit{THCROCK}
$$ {#eq-6-19}


See also the THCOIL, and THCWATER, and THCROCK keywords in the GRID section. The commercial compositional simulator's THCSOLID keyword is not supported or required by OPM Flow.


#### Example


```
--
--       DEFINE GRID BLOCK GAS PHASE THERMAL CONDUCTIVITY
–        FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
THCGAS
         300*20.0                                                              /
```


The above example defines the gas phase thermal conductivity of 20.0 for each cell in the 300 grid block model as defined by the DIMENS keyword in the RUNSPEC section.
