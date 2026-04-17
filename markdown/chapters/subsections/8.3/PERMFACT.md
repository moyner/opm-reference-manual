### PERMFACT – Permeability Multiplication Factor as a Function of Porosity Change


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PERMFACT defines the permeability multiplication factor due to a change in porosity. The keyword is used in conjunction with OPM Flow’s Salt Precipitation model, in which the pore space is reduced due to salt precipitating in the pore space, causing a reduction in porosity and an associated reduction in permeability. This keyword is also used for the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) and MICP model, where the pore space is reduced due to biofilm formation, and for the MICP model, also due to calcite precipitation.


::: {.callout-note}
This is an OPM Flow specific keyword.
:::


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | POROFAC | A real monotonically increasing positive columnar vector that defines the porosity ($\frac{ϕ}{{ϕ}_{0}}$) factor for the corresponding PERMFAC vector. In the simulator’s Salt Precipitation model, the maximum value of $ϕ$ is ${ϕ}_{0}$, implying a maximum value of one for POROFAC. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | PERMFAC | A real positive monotonically increasing columnar vector that defines the permeability (k) multiplier associated with POROFAC and used to scale a grid block's permeability due to the reduction in pore volume caused by salt precipitation.  Where: $\begin{matrix}\mathit{PERMFAC} = m\left(ϕ\right) \\ \mathit{with} k = m\left(ϕ\right){k}_{0}\end{matrix}$ | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 8.97: PERMFACT Keyword Description*


The porosity reduction can be written as a function proportional to the initial porosity, e.g., considering the volume fraction of salt (${s}_{s}$) precipitated out of the vaporized water phase, that is:


$$
\mathrm{ϕ} = (1 - {s}_{s}){\mathrm{ϕ}}_{o}
$$ {#eq-8-71}

The porosity and associated permeability factor data can be calculated using a permeability-porosity relationship, for example:


$$
\frac{k}{{k}_{o}} = {\left(\frac{\mathrm{ϕ}-{\mathrm{ϕ}}_{c}}{{\mathrm{ϕ}}_{o}-{\mathrm{ϕ}}_{c}}\right)}^{\mathrm{γ}}
$$ {#eq-8-72}

Where:

ko and${ϕ}_{o}$ 	=	the initial permeability and porosity,

k and$ϕ$ 	=	the actual permeability and porosity that changes due to the model dynamics (e.g., precipitation or dissolution of  salt, biofilm formation, calcite precipitation),

${ϕ}_{c}$	=	the residual porosity at which permeability is zero, and

$γ$	=	a positive exponent.


See also Kozeny-Carment (extended) [J. Kozeny, "Ueber kapillare Leitung des Wassers im Boden." Sitzungsber Akad. Wiss., Wien, 136(2a): 271-306, 1927.],  [P.C. Carman, "Fluid flow through granular beds." Transactions, Institution of Chemical Engineers, London, 15: 150-166, 1937.] and  [P.C. Carman, "Flow of gases through porous media." Butterworths, London, 1956.] and Verma-Pruess [Verma, A., & Pruess, K. (1988). Thermohydrological conditions and silica redistribution near high-level nuclear wastes emplaced in saturated geological formations. Journal of Geophysical Research,93, 1159–1173.] for additional functional forms that can be used to derive the tabulated data that can be entered via the PERMFACT keyword.


#### Example

The example below defines two PERMFACT tables assuming NTSFUN equals two and NSSFUN is greater than or equal to five on the TABDIMS keyword in the RUNSPEC section.


```
--
--       PERMEABILITY FACTOR AS A FUNCTION OF POROSITY REDUCTION
--       (OPM FLOW KEYWORD)
--
PERMFACT
--       PORO       PERM
--       FACTOR     FACTOR
--       -------    --------
         0.00        0.0000
         0.25        0.0625
         0.50        0.2500
         0.75        0.5625
         1.00        1.0000                    / TABLE NO. 01
--       -------    --------
         0.00        0.0000
         0.25        0.0625
         0.50        0.2500
         0.75        0.5625
         1.00        1.0000                    / TABLE NO. 02
```


Both tables use equation (8.72) with Φc equal to zero and ɣ equal to 2.0. Note that PERMFACT changes the permeability in all three dimensions, that is the PERMX, PERMY and PERMZ arrays are all modified.
