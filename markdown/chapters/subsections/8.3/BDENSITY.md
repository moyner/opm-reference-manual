### BDENSITY – Define the Surface Brine Density for the Fluid {#kw-BDENSITY}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

BDENSITY defines the brine surface density for when the brine phase has been activated in the model by the [BRINE](#kw-BRINE) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The number of BDENSITY vector data sets is defined by the NTPVT parameter on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Each record consists of a maximum of NPPVT values, as declared on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, with each value representing a brine surface density.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

The keyword is used in conjunction with the [PVTWSALT](#kw-PVTWSALT) keyword in the [PROPS](#kw-PROPS) section, with each brine density value matching with the salt concentration values in column 1 of each table in the [PVTWSALT](#kw-PVTWSALT) keyword.  Note that the BDENSITY keyword is optional, and if absent from the input file, then the brine surface densities will be set to the water density values declared via the [DENSITY](#kw-DENSITY) keyword in the [PROPS](#kw-PROPS) section. In this case there is no variation in brine surface density with respect to salt concentration.


| No. | Name | Description | Default |  |  |
| --- | --- | :------ | --- | --- | --- |
| 1 | WATDEN | Field | Metric | Laboratory | None |
| WATDEN is a real monotonically increasing positive row vector that defines the brine density at surface conditions for the given salt concentrations on the corresponding [PVTWSALT](#kw-PVTWSALT) keyword in the [PROPS](#kw-PROPS) section. There should be one row element for each salt concentration columnar element (SALTCON) on the [PVTWSALT](#kw-PVTWSALT) keyword. |  |  |  |  |  |
| lb/ft3 | kg/m | gm/cc |  |  |  |
| Notes: |  |  |  |  |  |
: BDENSITY Keyword Description {#tbl-8-24}
::: {.callout-note}
In OPM Flow the tracer equations are solved decoupled from the reservoir equations at the end of a time step. For each tracer an implicit system is solved, however,  the tracer equations are linear, resulting in converge in two iterations.  However, the Brine phase is solved fully implicitly and is fully coupled with the other flow equations. This is different to the commercial simulator,  where the tracer equations are solved explicitly after the flow equations have converged at the end of a time step. This can lead to numerical instabilities if there are large variations in brine densities.
:::


#### Example

The following shows the BDENSITY and [PVTWSALT](#kw-PVTWSALT) keywords for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set equal to two and NPPVT is set to greater than four on the [TABDIMS](#kw-TABDIMS) keyword.


```
--
--       BRINE WATER DENSITY DATA FOR PVTWSALT KEYWORD
--
--       SALTCON  SALTCON  SALTCON  SALTCON  SALTCON                                          --       DENSITY  DENSITY  DENSITY  DENSITY  DENSITY
--       -------  -------  -------  -------  -------
BDENSITY
         62.20    63.50    64.75    65.90                / FOR PVTWSALT TABLE 1
         64.00    65.50    67.00                         / FOR PVTWSALT TABLE 2           --
--       WATER SALT PVT TABLE
--
PVTWSALT
--       REF PRES  REF SALT
--       PSIA      LB/STB
--       --------  --------
         4500.0    0.000                                 / TABLE NO. REF. DATA
--
--       SALTCONC  BW         CW        VISC     VISC
--       LB/STB    RB/STB     1/PSIA    CPOISE   GRAD
--       --------  --------   -------   ------   ------
            0.0    1.020      2.7E-6    0.370    0.0
            2.0    1.010      2.7E-6    0.370    0.0
            4.0    1.000      2.7E-6    0.370    0.0
           10.0    0.950      2.7E-6    0.370    0.0     / TABLE NO. 01 SALT DATA
--
--       REF PRES  REF SALT
--       PSIA      LB/STB
--       --------  --------
         4000.0    0.000                                 / TABLE NO. 02 REF. DATA
--
--       SALTCONC  BW         CW        VISC     VISC
--       LB/STB    RB/STB     1/PSIA    CPOISE   GRAD
--       --------  --------   -------   ------   ------
            0.0    1.005      2.5E-6    0.320    0.0
            6.0    0.985      2.5E-6    0.320    0.0
           12.0    0.930      2.5E-6    0.320    0.0     / TABLE NO. 02 SALT DATA


```