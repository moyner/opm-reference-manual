### THERMAL – Activate the Thermal Modeling Option


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the thermal modeling option.

In OPM Flow's thermal model (THERMAL keyword) enthalpy is conserved and the energy equations are solved fully implicitly with the black-oil equations. Whereas, in OPM Flow's temperature model (TEMP keyword) internal energy is conserved (the work term is neglected and internal energy is equal to enthalpy) and the energy equations are solved sequentially after the black-oil equations. Note that the thermal model can be modified so that internal energy rather than enthalpy is conserved by setting the command line option --conserve-inner-energy-thermal=true (the default is false). If properties like density or viscosity "strongly" depend on temperature, the thermal model is recommended.

There is no data required for this keyword and there is no terminating “/” for this keyword.

The temperature option (TEMP keyword) and the thermal option (THERMAL keyword) are two separate modeling facilities in the commercial simulator, although some keywords can be used by both options, for example the RTEMP keyword.  OPM Flow’s thermal model is not directly equivalent to either the commercial simulator’s black-oil TEMP or compositional THERMAL formulation.

The energy black-oil implementation in OPM Flow uses a mixture of the commercial simulators black-oil and the commercial simulators “compositional thermal” keywords, as well as some OPM Flow specific keywords. Keywords specifically associated with both OPM Flow’s THERMAL and the commercial simulators TEMP and THERMAL options are listed in Table 5.46 for ease of reference.


| Section | Keyword | Function | OPM Flow | Commercial Simulator |  |
| --- | --- | --- | --- | --- | --- |
| THERMAL MODEL | TEMP MODEL | THERMAL MODEL |  |  |  |
| RUNSPEC | ROCKDIMS | Thermal Rock Dimensions of Over and Underburden Rock Types |  |  |  |
| TEMP | Activate the Temperature Modeling Option |  |  | Black-Oil |  |
| THERMAL | Activate the Thermal Modeling Option |  |  |  |  |
| GRID | ROCKCON | Thermal Rock Over and Underburden Connection Data |  |  |  |
| ROCKPROP | Thermal Rock Over and Underburden Property Data |  |  |  |  |
| HEATCR | Rock Heat Capacity. |  |  |  |  |
| HEATCRT | Rock Heat Capacity Temperature. |  |  |  |  |
| THCGAS | Gas Phase Thermal Conductivity. |  |  |  |  |
| THCOIL | Oil Phase Thermal Conductivity. |  |  |  |  |
| THCONR | Thermal Conductivity of liquids and reservoir rock. |  |  |  |  |
| THCONSF | Thermal Conductivity of liquids and reservoir rock scaling factor applied to THCONR to account for gas saturation. |  |  |  |  |
| THCROCK | Rock Thermal Conductivity. |  |  |  |  |
| THCSOLID | Solid Phase Thermal Conductivity. |  |  |  |  |
| THCWATER | Water Thermal Conductivity. |  |  |  |  |
| PROPS | HEATVAP | Thermal Oil Component Heat of Vaporization |  |  |  |
| GASDENT | Gas Density Temperature Coefficients (OPM Flow keyword). |  |  |  |  |
| GASJT | Gas Joule-Thomson Coefficient (OPM Flow keyword). |  |  |  |  |
| GASVISCT | Gas Viscosity versus Temperature Functions  (OPM Flow black-oil keyword). |  |  |  |  |
| OILDENT | Oil Density Temperature Coefficients (OPM Flow keyword). |  |  |  |  |
| OILJT | Oil Joule-Thomson Coefficient (OPM Flow keyword). |  |  |  |  |
| OILVISCT | Oil Viscosity versus Temperature Functions  (OPM Flow black-oil keyword). |  |  |  |  |
| RTEMP | Constant Initial Reservoir Temperature. |  |  |  |  |
| RTEMPA | Constant Initial Reservoir Temperature. |  |  |  |  |
| RTEMPVD | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| SPECHA | Thermal Specific Heat of Oil Component |  |  |  |  |
| SPECHEAT | Specific Heat of Oil, Water and Gas |  |  |  |  |
| SPECROCK | Specific Heat of the Reservoir Rock |  |  |  |  |
| TEMPVD | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| THANALB | Activate Thermal Analytic Water Density Option |  |  |  |  |
| THERMEX1 | Liquid Components Thermal Expansion Coefficient |  |  |  |  |
| WATDENT | Oil Density Temperature Coefficients. |  |  |  |  |
| WATJT | Water Joule-Thomson Coefficient (OPM Flow keyword). |  |  |  |  |
| WATVISCT | Oil Viscosity versus Temperature Function. |  |  |  |  |
| REGIONS | THERMNUM | Thermal Region Numbers. |  |  |  |
| SOLUTION | RTEMP | Constant Initial Reservoir Temperature. |  |  |  |
| RTEMPA | Constant Initial Reservoir Temperature. |  |  |  |  |
| RTEMPVD | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| TEMPI | Initial Reservoir Temperature for All Cells. |  |  |  |  |
| TEMPVD | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| SCHEDULE | WTEMP | Set An Injection Well’s Fluid Temperature |  |  |  |
| WINJTEMP | Define Injection Fluid Thermal Properties |  |  |  |  |
| Notes: |  |  |  |  |  |

Table 5.46: OPM Flow’s THERMAL Option Associated Keywords


In thermal runs a producing well’s bottom-hole temperature is calculated based on a weighted average of the temperature in the grid cell connections open to flow in the producing well, that is the reported bottom-hole temperature, TBHT, is calculated as:


$$
{T}_{\mathit{BHT}} = \frac{{\sum }_{i=1}^{M}{W}_{i}{T}_{i}}{{\sum }_{i=1}^{M}{W}_{i}}
$$ {#eq-5-1}

with


$$
{W}_{i} = {\sum }_{p}^{N}({{ρ}^{r}}_{\mathit{pi}}) ({{q}^{r}}_{\mathit{pi}}) {c}_{p}
$$ {#eq-5-2}

The term $({{ρ}^{r}}_{\mathit{pi}}) ({{q}^{r}}_{\mathit{pi}}) {c}_{p}$is the energy rate density (J/(K s)) of phase p,

where:

$N$	=	number of phases,

$M$	=	number of open connections in the well,

$i$	=	the open connection index,

$p$	= 	the phase index, oil, water and gas.

$r$	= 	indicating that the parameter is evaluated at reservoir conditions,

$T$ 	=	temperature (K),

$q$	=	connection flow rate (m3/s),

$ρ$	=	fluid density (kg/m3), and

$c$	=	specific heat capacity (J/(K kg))

(see the SPECHEAT keyword in the PROPS section).


The current implementation makes use of the specific internal energy:


$$
{e}_{\mathit{pi}} = {c}_{p} ⋅ {T}_{i}
$$ {#eq-5-3}

derived from the specific enthalpy, hpi


$$
{e}_{\mathit{pi}} = {h}_{\mathit{pi}} - \frac{{P}_{\mathit{pi}}}{{{ρ}^{r}}_{\mathit{pi}}}
$$ {#eq-5-4}

where ${P}_{\mathit{pi}}$ is connection grid block pressure of phase p.

The phase rates at surface conditions$({{q}^{s}}_{pi})$are converted to reservoir in situ rates$({{q}^{r}}_{pi})$using the phase formation volume factor, Bpi, via:


$$
{{q}^{r}}_{\mathit{pi}} = \frac{{{q}^{s}}_{\mathit{pi}} }{{{B}^{-1}}_{\mathit{pi}}}
$$ {#eq-5-5}

And thus equation (5.2) can be simplified to:


$$
{W}_{i} = {\sum }_{p}^{N}({{ρ}^{r}}_{\mathit{pi}}) (\frac{{{q}^{s}}_{\mathit{pi}} {e}_{\mathit{pi}}}{{{B}^{-1}}_{\mathit{pi}} ⋅ {T}_{i}})
$$ {#eq-5-6}


#### Example


```
--
--       ACTIVATE THE THERMAL MODELING OPTION (OPM FLOW THERMAL OPTION ONLY)
--
THERMAL

```

The above example activates the thermal modeling option.
