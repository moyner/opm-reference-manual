### DRSDTCON – CO2 Convective Dissolution Parameters {#kw-DRSDTCON}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The DRSDTCON keyword defines the parameters that control the convective dissolution of carbon dioxide (CO2) into the in-situ brine within a grid cell, as described by Mykkeltvedt et al.^[Mykkeltvedt, T.S., Sandve, T.H. & Gasda, S.E. New Sub-grid Model for Convective Mixing in Field-Scale CO2 Storage Simulation. Transp Porous Med 152, 9 (2025). https://doi.org/10.1007/s11242-024-02141-5], based on an assumption of vertical equilibrium.  The keyword internally causes the simulator to calculate the solution gas-oil ratio (Rs),  normally controlled by the DRSDT1 parameter on the [DRSDT](#kw-DRSDT) keyword in the [SCHEDULE](#kw-SCHEDULE) section, making the [DRSDT](#kw-DRSDT) keyword redundant.

The keyword should only be used if the [CO2STORE](#kw-CO2STORE) keyword in the [RUNSPEC](#kw-RUNSPEC) section has been activated to model CO2 storage via OPM Flow’s CO2-Brine PVT model. Note that the [CO2STORE](#kw-CO2STORE) keyword must be used together with either: (1) the [GAS](#kw-GAS), [WATER](#kw-WATER) and [DISGASW](#kw-DISGASW) keywords (or alternatively the [GASWAT](#kw-GASWAT) and [DISGASW](#kw-DISGASW) keywords), or (2) the [GAS](#kw-GAS), [OIL](#kw-OIL) and [DISGAS](#kw-DISGAS) keywords in the [RUNSPEC](#kw-RUNSPEC) section. See the [CO2STORE](#kw-CO2STORE) keyword for details.

The DRSDTCON keyword is an OPM Flow specific keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | CHI | A real positive value () that defines the proportionality constant related to the maximum rate of increase of CO2 solution gas-oil ratio (Rs) in the Linear regime. A value of zero means that convective dissolution of CO2 into in-situ brine does not occur and free CO2 cannot dissolve into the brine.  Alternatively, a non-zero value of CHI allows convective dissolution of CO2. Note if the [CO2STORE](#kw-CO2STORE) keyword is present but the DRSDTCON keyword is absent from the input deck, then this results in instantaneous dissolution of CO2 into the available undersaturated in-situ brine. | 0.04 |
| dimensionless | dimensionless | dimensionless |  |
| 1 | PSI | A real positive value () that defines the normalised CO2 solution gas-oil ratio ($\overset{~}{X}$) at the transition between the Linear and the Steady-State regimes. | 0.34 |
| dimensionless | dimensionless | dimensionless |  |
| 1 | OMEGA | A real positive value () that defines the maximum rate of increase in CO2 solution gas-oil ratio (Rs) in the Steady-State regime. | 3.0e-9 |
| 1/s | 1/s | 1/s |  |
| 1 | OPTION | A defined character string that specifies in which cells the convective dissolution rate limit is applied, and should be set to one of the following character strings: | [ALL](#kw-ALL) |
| Notes: |  |  |  |
: DRSDTCON Keyword Description {#tbl-12-3-53-1}
Mykkeltvedt et al. describe four regimes that characterise the evolution of the CO2 solution gas-oil ratio in a control volume:

- Initial Phase: Near instantaneous equilibrium partitioning and diffusion.
- Linear Phase: Fingers of CO2-rich brine propagate downwards towards the base of the control volume.
- Steady-State Phase: Fingers have passed through the base of the control volume.
- Decline Phase: Gas phase CO2 has been completely dissolved in the brine.

In the Initial phase a near instantaneous jump in dissolved CO2 is assumed if the control volume spans the CO2-brine interface (otherwise the solution gas-oil ratio is zero). The initial jump comes from the capillary transition zone, the height of which depends on the capillary pressure function. Capillary equilibrium happens almost immediately and therefore the CO2 solution gas-oil ratio is allowed to increase at unlimited rate until capillary equilibrium is reached. Capillary equilibrium is assumed when:


$$
{R}_{s} > {R}_{s,\mathit{sat}}{S}_{o}
$$ {#eq-12-3-53-1}

Where:

Rs	=	solution gas-oil ratio,

Rs,sat 	=	saturated solution gas-oil ratio,

So 	=	oil saturation.


This is followed by the Linear phase where the finger speed is assumed to be relatively constant and therefore it is reasonable to assume that the CO2 gas-oil ratio will increase at a constant rate (Linear regime). The maximum dissolution rate, as per the [DRSDT](#kw-DRSDT) keyword in the [SCHEDULE](#kw-SCHEDULE) section during the Linear regime (Flin) is given by:


$$
{F}_{\mathit{lin}} = χ(\frac{{R}_{s,\mathit{sat}}{K}_{z}\mathrm{Δ}{ρ}_{c}g}{{μ}_{o}{S}_{o} {D}_{z}ϕ})
$$ {#eq-12-3-53-2}

Where:

χ	=	the non-dimensional parameter CHI controlling the dissolution rate,

Rs,sat 	=	the maximum gas-oil ratio at the CO2 solubility limit in the brine,

Kz 	=	the vertical permeability,

∆ρc	=	the difference between the brine density saturated with CO2 at Rs,sat and

the brine density without dissolved CO2,

g	=	the gravity constant,

μo	=	the oil (brine) viscosity, and

So	= 	the oil (brine) saturation.


The third phase is characterised by a change in slope of the rate of dissolution as the system transitions from linear build-up to quasi-steady state (Steady-State regime). The parameter PSI defines the normalised gas-oil ratio at the transition from the Linear to the Steady-State regime, where the normalised gas-oil ratio is given by:


$$
\overset{~}{X} = \frac{{R}_{s}-{R}_{s,\mathit{sat}}{S}_{g}}{{R}_{s,\mathit{sat}}(1-{S}_{g})}
$$ {#eq-12-3-53-3}


The rate of dissolution during the Steady-State regime is defined by the parameter OMEGA.

The final Decline phase occurs when the CO2 has been completely dissolved in the brine at which point the rate of dissolution is zero.

The values of CHI, PSI and OMEGA can either be estimated from fine-scale simulation, historical data, or from laboratory tests^[Taheri, A., Torsæter, O., Lindeberg, E., Hadia, N. J., & Wessel-Berg, D. (2018). Qualitative and quantitative experimental study of convective mixing process during storage of CO2 in heterogeneous saline aquifers. International Journal of Greenhouse Gas Control, 71, 212-226.]. Analysis of fine-scale simulation results by Mykkeltvedt et al indicates that 0.04 +/-0.01 is a reasonable value for CHI. Elenius et al.^[Elenius, M. T., Nordbotten, J. M., & Kalisch, H. (2014). Convective mixing influenced by the capillary transition zone. Computational Geosciences, 18(3-4), 417-431] also state that 0.04 is a reasonable value for CHI for the Utsira formation.


::: {.callout-note}
In the commercial simulator a constant or regional value for [DRSDT](#kw-DRSDT) can be given as an input parameter.  This can be used to include the effect of convective mixing as shown by Thibeau and Dutin^[Thibeau, S., & Dutin, A. (2011). Large scale CO2 storage in unstructured aquifers: Modeling study of the ultimate CO2 migration distance. Energy Procedia, 4, 4230-4237.]. OPM Flow’s approach differs from this in that the [DRSDT](#kw-DRSDT) value is computed internally and is dependent on both the static and dynamic cell properties.
:::


#### Example

The example below is similar to that shown under the [CO2STORE](#kw-CO2STORE) keyword in the [RUNSPEC](#kw-RUNSPEC) section. In the [RUNSPEC](#kw-RUNSPEC) section one declares that the carbon dioxide storage model is active for the run to account for both carbon dioxide and water phase solubility using OPM Flow’s CO2-Brine PVT model.


```
-- ==============================================================================
--
-- RUNSPEC SECTION
--
-- ==============================================================================
RUNSPEC
-- ------------------------------------------------------------------------------
--  FLUID TYPES AND TRACER OPTIONS
-- ------------------------------------------------------------------------------
--
--       ACTIVATE CO2 STORAGE IN THE MODEL (OPM FLOW CO2 STORAGE KEYWORD)
--
CO2STORE
--
--       ACTIVATE GAS-WATER THE MODEL (OPM FLOW KEYWORD)
--
GASWAT
--
--       DISSOLVED GAS IN WATER IS PRESENT IN THE RUN (OPM FLOW KEYWORD)
--
DISGASW
--
--       VAPORIZED WATER IN DRY/WET GAS IS PRESENT IN THE RUN (OPM FLOW KEYWORD)
--
VAPWAT

```

The second part of the example sets the maximum dissolution rate for convective CO2 mixing via the DRSDTCON keyword in the [SCHEDULE](#kw-SCHEDULE) section using the base case parameters calculated by Mykkeltvedt et al from fine-scale simulations.


```
-- ==============================================================================
--
-- SCHEDULE SECTION
--
-- ==============================================================================
SCHEDULE
--
--       CO2 CONVECTIVE DISSOLUTION PARAMETERS
--
DRSDTCON
--       CHI      PSI      OMEGA    OPTION
         0.04     0.34     3.0E-09  ALL                             /

```

See also the [CO2STORE](#kw-CO2STORE) keyword in the [RUNSPEC](#kw-RUNSPEC) section for further information on OPM Flow’s CO2 storage facility.