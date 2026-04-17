### PCFACT – Capillary Pressure Multiplication Factor as a Function of Porosity Change


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

[PCFACT](#REF_HEADING_KEYWORD_PCFACT_8_3) defines the capillary pressure multiplication factor due to a change in porosity. Currently the keyword is used in conjunction with OPM Flow’s Salt Precipitation model, in which the pore space is reduced due to salt precipitating in the pore space, causing a reduction in porosity and an associated increase in capillary pressure.


| Note This is an OPM Flow specific keyword for the simulator’s Salt Precipitation model that is activated by the BRINE and PRECSALT keywords and declaring that vaporized water is present in the run via the VAPWAT keyword. All three keywords are in the RUNSPEC section. |
| --- |


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | POROFAC | A real monotonically increasing positive columnar vector that defines the porosity factor ($\frac{ϕ}{{ϕ}_{0}}$) for the corresponding PCFAC vector. In the simulator’s Salt Precipitation model, the maximum value of $ϕ$ is ${ϕ}_{0}$, implying a maximum value of one for POROFAC. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | PCFAC | A real positive monotonically decreasing columnar vector that defines the capillary pressure (${p}_{c}$) multiplier associated with POROFAC and used to scale a grid block's capillary pressure due to the reduction in pore volume caused by salt precipitation.  Where: $\begin{matrix}\mathit{PCFAC} = m\left(\frac{ϕ}{{ϕ}_{0}}\right) \\ \mathit{with} {p}_{c} = m\left(\frac{ϕ}{{ϕ}_{0}}\right){p}_{c0}\end{matrix}$ | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 8.3.199.1: PCFACT Keyword Description*


The porosity reduction is a function of the volume fraction of salt (${s}_{s}$) precipitated out of the vaporized water phase, that is:


| $ϕ = (1 - {s}_{s}){ϕ}_{0}$ | (8.3.199.1) |
| --- | --- |

The capillary pressure factor data can be estimated from the permeability and porosity factors defined by the PERMFACT keyword in the PROPS section using the Leverett J-function, for example:


| $\frac{{p}_{c}}{{p}_{c0}} = {\left(\frac{ϕ}{{ϕ}_{0}}\frac{{k}_{0}}{k}\right)}^{\frac{1}{2}}$ | (8.3.199.2) |
| --- | --- |

Where:

${ϕ}_{0}$, $ϕ$ 	=	the initial and scaled porosity,

${k}_{0}$, $k$ 	=	the initial and scaled permeability, and

${p}_{c0}$, ${p}_{c}$ 	=	the initial and scaled capillary pressure.


#### Example

The example below defines two [PCFACT](#REF_HEADING_KEYWORD_PCFACT_8_3) tables assuming NTSFUN equals two and NSSFUN is greater than or equal to five on the TABDIMS keyword in the RUNSPEC section.


```
--
--       CAPILLARY PRESSURE FACTOR INCREASE DUE TO SALT PRECIPITATION
--       (OPM FLOW KEYWORD)
--
PCFACT
--       PORO       PC
--       FACTOR     FACTOR
--       -------    --------
         0.00        2.0000
         0.25        2.0000
         0.50        1.4142
         0.75        1.1547
         1.00        1.0000                    / TABLE NO. 01
--       -------    --------
         0.00        2.0000
         0.25        2.0000
         0.50        1.4142
         0.75        1.1547
         1.00        1.0000                    / TABLE NO. 02
```


Note that the capillary pressure factor has been capped for POROFAC less than 0.25.
