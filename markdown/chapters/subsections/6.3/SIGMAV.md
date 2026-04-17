### SIGMAV – Dual Porosity Matrix to Fracture Sigma (Individual Cells) {#kw-SIGMAV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SIGMAV keyword defines a dual porosity matrix to fracture multiplier, sigma, that is applied to individual cells, for when the Dual Porosity model has been invoked by either the [DUALPORO](#kw-DUALPORO) or the [DUALPERM](#kw-DUALPERM) keywords in the [RUNSPEC](#kw-RUNSPEC) section. Sigma (σ) takes into account the matrix-fracture interface area per unit volume and was defined by Kazemi et al^[Kazemi, H., Merrill JR., L. S., Porterfield, K. L., and Zeman, P. R. “Numerical Simulation of Water-Oil Flow in Naturally Fractured Reservoirs,” paper SPE 5719, Society of Petroleum Engineers Journal (1976) 16, No. 6, 317-326.] to be:


$$
\mathrm{σ} = 4(\frac{1}{{{l}_{x}}^{2}} +\frac{1}{{{l}_{y}}^{2}} +\frac{1}{{{l}_{z}}^{2}} )
$$ {#eq-6-18}

Where lx, ly and lz are not the grid block dimensions in the model in the respective directions, but the dimensions of the blocks of the matrix material. In practice,  σ is used as a tuning parameter in dual porosity runs to match reservoir and well performance.

See also the [SIGMA](#kw-SIGMA) keyword in the [GRID](#kw-GRID) section that supplies a constant sigma to all cells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.