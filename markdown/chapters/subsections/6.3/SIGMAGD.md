### SIGMAGD – Dual Porosity Matrix to Fracture Sigma for Gravity Drainage (All Cells) {#kw-SIGMAGD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SIGMAGD keyword defines the dual porosity matrix to fracture transmissibility multiplier, sigma, that is applied to all cells, for when the Dual Porosity model has been activated by either the [DUALPORO](#kw-DUALPORO) or the [DUALPERM](#kw-DUALPERM) keywords in the [RUNSPEC](#kw-RUNSPEC) section.  In addition, the [GRAVDR](#kw-GRAVDR) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be used to enable the Gravity Drainage model for the run. Sigma (σ) takes into account the matrix-fracture interface area per unit volume and was defined by Kazemi et al^[Kazemi, H., Merrill JR., L. S., Porterfield, K. L., and Zeman, P. R. “Numerical Simulation of Water-Oil Flow in Naturally Fractured Reservoirs,” paper SPE 5719, Society of Petroleum Engineers Journal (1976) 16, No. 6, 317-326.] to be:


$$
\mathrm{σ} = 4(\frac{1}{{{l}_{x}}^{2}} +\frac{1}{{{l}_{y}}^{2}} +\frac{1}{{{l}_{z}}^{2}} )
$$ {#eq-6-16}

Where lx, ly and lz are not the grid block dimensions in the model in the respective directions, but the dimensions of the blocks of the matrix material. In practice,  σ is used as a tuning parameter in dual porosity runs to match reservoir and well performance.

Note that SIGMAGD keyword data is used for areas being swept by gas and the [SIGMA](#kw-SIGMA) keyword data is used when the area is being invaded by water. See also the [SIGMAGDV](#kw-SIGMAGDV) keyword in the [GRID](#kw-GRID) section that supplies the sigma values on an individual cells basis

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.