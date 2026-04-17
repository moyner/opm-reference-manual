### VDFLOW – Velocity Dependent Flow Coefficient for Grid Block Flow (Grid)


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

VDFLOW activates non-Darcy flow between grid blocks and defines a constant non-Darcy flow coefficient for the whole grid, the coefficient only applies to the gas phase. The coefficient is normally derived from well tests or calculated analytically based on the coefficient of inertial resistance, usually known as β, in Forchheimer’s flow equation, [Geertsma, J., 1974. Estimating the Coefficient of Inertial Resistance in Fluid Flow Through Porous Media. Soc.Pet.Eng.J., October: 445-450.],  [Gewers, C.W.W. and Nichol, L.R., 1969. Gas Turbulence Factor in a Microvugular Carbonate. J.Can.Pet.Tech., April.] and  [Wong, S.W., 1970. Effects of Liquid Saturation on Turbulence Factors for Gas Liquid Systems. J.Can.Pet.Tech., October].  Dake [Dake, L.P. Fundamentals of Reservoir Engineering, Amsterdam, The Netherlands, Elsevier Science BV (1978)  Chapter 8.6, pages 252-257.], in chapter eight, reports a typical value of β to be 10.07 cm-1.

See also the VDFLOWR keyword in the PROPS section that allows the non-Darcy coefficient to be entered for individual regions, and the WDFAC and WDFACCOR keywords in the SCHEDULE section that assigns the non-Darcy coefficient to well connections.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
