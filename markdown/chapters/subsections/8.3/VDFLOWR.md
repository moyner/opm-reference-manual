### VDFLOWR – Velocity Dependent Flow Coefficient for Grid Block Flow (Region) {#kw-VDFLOWR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

[VDFLOW](#kw-VDFLOW) activates non-Darcy flow between grid blocks and defines a constant non-Darcy flow coefficient for individual regions allocated by the [SATNUM](#kw-SATNUM) keyword in the [REGIONS](#kw-REGIONS) section. Note that the coefficient only applies to the gas phase. The coefficient is normally derived from well tests or calculated analytically based on the coefficient of inertial resistance, usually known as β, in Forchheimer’s flow equation,^[Geertsma, J., 1974. Estimating the Coefficient of Inertial Resistance in Fluid Flow Through Porous Media. Soc.Pet.Eng.J., October: 445-450.], ^[Gewers, C.W.W. and Nichol, L.R., 1969. Gas Turbulence Factor in a Microvugular Carbonate. J.Can.Pet.Tech., April.] and ^[Wong, S.W., 1970. Effects of Liquid Saturation on Turbulence Factors for Gas Liquid Systems. J.Can.Pet.Tech., October].  Dake^[Dake, L.P. Fundamentals of Reservoir Engineering, Amsterdam, The Netherlands, Elsevier Science BV (1978)  Chapter 8.6, pages 252-257.], in chapter eight, reports a typical value of β to be 10.07 cm-1.

See also the [VDFLOW](#kw-VDFLOW) keyword in the [PROPS](#kw-PROPS) section that allows the non-Darcy coefficient to be entered for the whole grid, and the [WDFAC](#kw-WDFAC) and [WDFACCOR](#kw-WDFACCOR) keywords in the [SCHEDULE](#kw-SCHEDULE) section that assigns the non-Darcy coefficient to well connections.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.