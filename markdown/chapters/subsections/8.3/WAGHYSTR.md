### WAGHYSTR – Define Water-Alternating-Gas Hysteresis Parameters {#kw-WAGHYSTR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the parameters for the Water-Alternating-Gas (“WAG”) hysteresis option, for when the hysteresis option has been activated by the WAGHYSTR variable on the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

The WAG recovery mechanism is an Enhanced Oil Recovery (“EOR”) process to optimize oil recovery by improving volumetric sweep efficiency. It was originally proposed as a method to improve the sweep efficiency of gas by using water to control the mobility ratio and to stabilize the front (Caudle and Dyes, 1958^[Caudle, B. H., & Dyes, A. B. (1958, January 1). Improving Miscible Displacement by Gas-Water Injection. Society of Petroleum Engineers.]; Christensen et al., 1998^[Christensen, J. R., Stenby, E. H., & Skauge, A. (1998, January 1). Review of WAG Field Experience. Society of Petroleum Engineers. doi:10.2118/39883-MS.]; and Christensen et al., 2001^[Christensen, J. R., Stenby, E. H., & Skauge, A. (2001, April 1). Review of WAG Field Experience. Society of Petroleum Engineers. doi:10.2118/71203-PA.]). WAG injection can lead to improved oil recovery by combining better mobility control and contacting upswept zones, and by leading to improved microscopic displacement. Although initially the injected gas was immiscible with respect to the oil (WAG Immiscible) the more common process is WAG Miscible, with alternating different types of hydrocarbon gases and non-hydrocarbon gases, such as N2 and CO2 Gases.  WAG flooding has been successfully applied to various fields worldwide.

Only the gas phase relative permeability WAG hysteresis model has been implemented in the simulator.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | LANDS_PARAMETER | A real value greater than zero that defines Land’s parameter, $C$. The Land’s parameter controls how the trapped gas saturation depends on the maximum gas saturation attained and the critical gas saturation; and the shape of the imbibition curve. ${s}_{\mathit{gtrap}}={s}_{\mathit{gcr}}+\frac{({s}_{\mathit{gm}}-{s}_{\mathit{gcr}})}{(1+C({s}_{\mathit{gm}}-{s}_{\mathit{gcr}}))}$ where, ${s}_{\mathit{gtrap}}$ is the trapped gas saturation, ${s}_{\mathit{gm}}$ is the maximum gas saturation attained, and ${s}_{\mathit{gcr}}$ is the critical gas saturation. Values of the Land’s parameter that are too small give a trapped gas saturation close to the maximum gas saturation attained. This results in an unphysical steep relative permeability curve giving potential convergence problems. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | SECONDARY_DRAINAGE_REDUCTION | A real value greater than or equal to zero that defines the secondary drainage reduction factor, alpha. As alpha increases the reduction in gas mobility on secondary drainage increases. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| 3 | GAS_MODEL | A defined character string that defines whether the gas hysteresis model should be used, and should be set to one of the following character strings: Only the YES option is currently supported by the simulator. | YES |
| 4 | RES_OIL | A defined character string that defines whether the residual oil model should be used, and should be set to one of the following character strings: Only the NO option is currently supported by the simulator. | YES |
| 5 | WATER_MODEL | A defined character string that defines whether the water hysteresis model should be used, and should be set to one of the following character strings: Only the NO option is currently supported by the simulator. | YES |
| 6 | IMB_LINEAR_FRACTION | A real value greater than zero that defines the imbibtion curve linear fraction. This is the fraction of the curve between Sgm and Sgtrap that uses a linear transformation. A non-zero value for the linear fraction prevents the potential infinite gradient in the imbibition curve when using the Carlson analytic model. | 0.1 |
| dimensionless | dimensionless | dimensionless |  |
| 7 | THREEPHASE_SAT_LIMIT | A real value between zero and one that defines the three-phase model threshold saturation. When the water saturation exceeds this threshold above the connate water saturation the gas (non-wetting) phase hysteresis switches from the two-phase model to the three-phase model. In the two-phase model a secondary drainage process follows the imbibition curve. However, if the water saturation exceeds the connate saturation by the given threshold, at the beginning of the secondary drainage process a three-phase secondary drainage curve is followed. This value also defines the minimum percentage change in gas saturation to allow switching from drainage to imbibition curve and vice-versa. This threshold allows better control of the numerical sensitivity of the system, preventing it from being too unstable. | 0.001 |
| dimensionless | dimensionless | dimensionless |  |
| 8 | RES_OIL_MOD_FRACTION | A real value between zero and one that defines the residual oil modification fraction. This is the fraction of the trapped gas saturation subtracted from the residual oil (SOM) in the [STONE](#kw-STONE) 1 three-phase oil relative permeability model. This is not supported and will be ignored by the simulator. | 1.0 |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: WAGHYSTR Keyword Description {#tbl-8-3-364-1}
#### Example

The following example defines the WAG hysteresis model parameters using the WAGHYSTR keyword for a case with three saturation table regions


```
--
--       WAG HYSTERESIS PARAMETERS
--
-- LAND  ALPHA    GAS    RES    WATER  LINEAR
-- C     FACTOR   MODEL  OIL    MODEL  FRAC
WAGHYSTR
2.0      1.0      YES    YES    YES    0.2    /
2.0      1.0      YES    NO     /
2.0      /
```


Here, saturation table region one uses the gas WAG hysteresis, residual oil and water WAG hysteresis models, with a Land’s parameter of 2.0, an alpha factor of 1.0, and a imbibition curve linear factor of 0.2. The gas and water WAG hysteresis models are used in region two but the residual oil model is turned off, with a Land’s parameter of 2.0, an alpha factor of 1.0, and a default imbibition curve linear factor of 0.1. A Land’s parameter of 2.0 has been specified for region three with the remainder of the parameters defaulted.

Note that the above example uses some options that are not currently supported by OPM Flow.