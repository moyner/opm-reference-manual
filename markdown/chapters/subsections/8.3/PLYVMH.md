### PLYVMH – Polymer Molecular Weight Model Polymer Viscosity Constants


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, PLYVMH, defines the constants used to calculate viscosity of the polymer solution as a function of the polymer molecular weight and the polymer concentration, for the simulator's Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity. The keyword consists of a series of row vectors, which each vector having four elements, that define the constants used in calculating the polymer viscosity

This keyword should only be used if the POLYMER and POLYMW keywords in the RUNSPEC section are also activated.


::: {.callout-note}
This is an OPM Flow specific keyword that employs an alternative polymer flood model based on a Polymer Molecular Weight Transport equation, that is not available in the commercial simulator. The model has been tested using metric units; however, using either field or laboratory units with the option should be considered experimental.
:::


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 ‍ | MHK | The Mark-Houwink K polymer specific constant in the Mark-Houwink equation, see equation (8.77). | None |
|  | ml/g |  |  |
| 2 | MHA | The Mark-Houwink exponent parameter a, in the Mark-Houwink equation, see equation  (8.77). | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | GAMMA | The ɣ intrinsic water-polymer viscosity constant in the Huggins equation, see equation (8.79). | None |
| 4 | KAPPA | The κ intrinsic water-polymer viscosity constant in the Huggins equation, see equation (8.79). | None |
| Notes: |  |  |  |

*Table 8.109: PLYVMH Keyword Description*


The high molecular weight of polymers greatly increase the viscosity of the injected water in which they are dissolved, thus adjusting the mobility ration of the displacing phase. The increase in viscosity is caused by strong internal friction between the randomly coiled and swollen macro molecules and the surrounding water molecules.  And is dependent on both the nature of the polymer and the injected water acting as the solvent.  There are several formulations of viscosity associated with polymer rheology, namely:


Relative viscosity is defined as:


$$
{\mathrm{η}}_{\mathit{rel}} = \frac{\mathrm{η}}{{\mathrm{η}}_{s}}
$$ {#eq-8-73}

where:

${η}_{\mathit{rel}}$	=	is the relative viscosity,

$η$	= 	is the viscosity of the solution, and

${η}_{s}$	=	is the viscosity of the solvent (injected water).


Specific viscosity is defined as:


$$
\begin{matrix}{\mathrm{η}}_{\text{sp}} = \frac{\left(\mathrm{η}-{\mathrm{η}}_{s}\right)}{{\mathrm{η}}_{s}} \\   = \frac{\mathrm{η}}{{\mathrm{η}}_{s}} - 1 \\   = {\mathrm{η}}_{\mathit{rel}} - 1\end{matrix}
$$ {#eq-8-74}

where:

${η}_{\text{sp}}$	=	is the specific water-polymer viscosity, and

${η}_{s}$	= 	is the viscosity of the solvent (injected water).


Reduced Specific Viscosity is given by:


$$
\begin{matrix}{\mathrm{η}}_{\text{red}} = \frac{{\mathrm{η}}_{\text{sp}}}{{C}_{p}} \\   = \frac{\left({\mathrm{η}}_{\mathit{rel}} - 1\right)}{{C}_{p}}\end{matrix}
$$ {#eq-8-75}

where:

${η}_{\text{red}}$	=	is the reduced specific water-polymer viscosity, and

${C}_{p}$	= 	is the polymer concentration.


Finally, the Intrinsic Velocity, which is defined as a measure for the internal friction in polymer solutions at the limit of zero polymer concentration. Thus, this quantity describes the effect of completely separated polymer chains on the solution viscosity, and is defined as:


$$
\begin{matrix}\left[\mathrm{η}\right] = \underset{{C}_{p}\rightarrow 0}{lim}\frac{{\mathrm{η}}_{\text{sp}}}{{C}_{p}} \\   = \underset{{C}_{p}\rightarrow 0}{lim}\frac{\mathrm{η}-{\mathrm{η}}_{0}}{{\mathrm{η}}_{0}{C}_{p}}\end{matrix}
$$ {#eq-8-76}

where:

$\left[η\right]$	=	is the intrinsic water-polymer viscosity and describes the increase in

viscosity arising from an individual polymer chain and is a measure of the polymers' thickening power,  and

${η}_{o}$	= 	zero-shear viscosity.


For any given solvent pair, the intrinsic viscosity increases as the molecular weight of the polymer increases; here, the Mark-Houwink equation, also known as the  Mark-Houwink-Staudinger equation [H. Mark, in R. Saenger, Der feste Koerper, Hirzel, Leipzig, 1938.],   [R. Houwink , J. Prakt. Chem., Vol. 157, Issue 1-3, p. 15 (1940).], and   [H. Staudinger, Die Hochmolekulare Organischen Verbindungen, Julius Springer, Berlin 1932.] is used to calculate [η], that is:


$$
\left[\mathrm{η}\right] = K ⋅ {{M}_{w}}^{a}
$$ {#eq-8-77}

where:

$K$	=	is the polymer specific constant in the Mark-Houwink equation, the MHK

parameter in  Table 8.109,

${M}_{w}$	= 	is the polymer molecular weight, and

$a$	=	the exponent constant in the Mark-Houwink equation, the MHA parameter

in  Table 8.109.


The Mark-Houwink parameters can be determined from a double logarithmic plot of intrinsic viscosity versus molecular weight which yields straight lines, that is:


$$
ln\left([\mathrm{η}]\right) = ln(K) + a \times  ln({M}_{w})
$$ {#eq-8-78}


OPM Flow uses a form of the Huggins [Huggins, M. L. 1942. The viscosity of dilute solutions of long-chain molecules. IV. Dependence on concentration.» Journal of the American Chemical Society 64 (11): 2716-2718.] equation to calculate the polymer apparent viscosity, as shown below:


$$
\begin{matrix} \frac{{\mathrm{η}}_{0}}{{\mathrm{η}}_{s}} = 1 + \mathrm{γ}\left(X + \mathrm{κ}{X}^{2}\right) \\ \text{where} X = \left[\mathrm{η}\right]{C}_{p}\end{matrix}
$$ {#eq-8-79}

where:

$γ$	=	a user defined constant, GAMMA in Table 8.109, and

$κ$	= 	a user defined constant, KAPPA in Table 8.109.


Which can be used to calculate the zero-shear viscosity, η0,  based on the quadratic function in equation (8.79) time polymer concentration(Cp) and polymer intrinsic viscosity described in equation (8.77).

In terms of the keyword units, given the intrinsic viscosity in ml/g, polymer concentration in kg/m3, and the molecular weight as kg/kg-M, then equation (8.77) becomes:


$$
\left[\mathrm{η}\right] = K{\left({M}_{w} ⋅ 1.0\times {10}^{-3}\right)}^{a}\overset{\dot}{ }1.0\times {10}^{-3}
$$ {#eq-8-80}

and equation (8.79) becomes:


$$
\begin{matrix} \frac{{\mathrm{η}}_{0}}{{\mathrm{η}}_{s}} = 1 + \mathrm{γ}\left(X + \mathrm{κ}{X}^{2}\right) \\ \text{where} X = 1.0\times {10}^{-6}\left[\mathrm{η}\right]{C}_{p}\end{matrix}
$$ {#eq-8-81}


Note that the model does not account for non-Newtonian flow; the apparent viscosity is simply set equal to the zero-shear viscosity, and that the model only considers the full mixing between the polymer and water.

See also the PLYMWINJ keyword in the PROPS section, that describes the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity.  Note that the standard polymer property data keywords: PLYROCK, PLYADS, PLYMAX, etc., are still required to fully describe the polymer fluid.


#### Example

Given NPLYVMH equals two on the PINTDIMS keyword in the RUNSPEC section, then:


```
--
--       POLYMER MOLECULAR WEIGHT MODEL POLYMER VISCOSITY CONSTANTS
--       (OPM FLOW PROPS KEYWORD)
--
--       MHK     MHA     VISC    VISC
--       CONST   EXPON   GAMMA   KAPPA
PLYVMH
         0.02    0.50    0.40    0.60                      /
         0.03    0.51    0.42    0.63                      /
/

```

Two sets of data should be entered with the PLYVMH keyword, as shown above.
