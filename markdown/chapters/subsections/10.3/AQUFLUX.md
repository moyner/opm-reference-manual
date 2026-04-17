### AQUFLUX – Define Constant Flux Analytical Aquifer {#kw-AQUFLUX}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The AQUFLUX keyword defines the properties of Constant Flux Analytical Aquifers, that allows for a constant water influx to the connected grid blocks. This type of aquifer is connected to the model using either the [AQUANCON](#kw-AQUANCON) keyword for global cells, or the AQUANCONL keyword for cells belonging to a Local Grid Refinement ("[LGR](#kw-LGR)"), both the aforementioned keywords are in the [GRID](#kw-GRID) and [SOLUTION](#kw-SOLUTION) sections. The keyword itself may be utilized in both the [SOLUTION](#kw-SOLUTION) and [SCHEDULE](#kw-SCHEDULE) sections, with subsequent entries overwriting the previous entry.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | AQUID | A positive integer greater than or equal to one and less than or equal to NANAQ on the [AQUDIMS](#kw-AQUDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, that defines the AQUFLUX aquifer number. | 1 |
| ‍2 ‍ | AQFLUX | A real positive value the defines the aquifer water influx rate, per unit area of the connected grid cell face. | None |
| stb/day/ft2 | sm3/day/m2 | scc/hour/cm2 |  |
| 3 | SALTCON | SALTCON is a real positive number that defines the initial salt concentration in the aquifer, for when with simulator's Brine Model has been activated via the [BRINE](#kw-BRINE) keyword in the [RUNSPEC](#kw-RUNSPEC) section. This variable is ignored by OPM Flow. | 0.0 |
| lb/stb | kg/sm3 | gm/scc |  |
| 4 | [TEMP](#kw-TEMP) | [TEMP](#kw-TEMP) is a real positive number that defines the initial temperature of the aquifer for use with OPM Flow's thermal option. The [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section must be activated to use this option.  If the [THERMAL](#kw-THERMAL) keyword is absent from the input deck, then the parameter is ignored. | 1* |
| oF | oC | oC |  |
| 5 | PRESS | PRESS is a single positive value that defines the aquifer pressure for use with OPM Flow's thermal option. The [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section must be activated to use this option. If the [THERMAL](#kw-THERMAL) keyword is absent from the input deck, then the parameter is ignored. | 1* |
| psia | barsa | atma |  |
| Notes: |  |  |  |
: AQUFLUX Keyword Description {#tbl-10-9}
The water flow rate into a connected grid cell for this type of aquifer, is calculated from:


$$
{q}_{w} = \mathit{AQUFLUX}(\mathit{AQFLUX}) \times  {A}_{(i,j,k)} \times  \mathit{[AQUANCON](#kw-AQUANCON)}(\mathit{AQUCOEF})
$$ {#eq-10-14}

Where:

AQUFLUX(AQFLUX)		= the AQFLUX parameter on the AQUFLUX keyword,

[AQUANCON](#kw-AQUANCON)(AQUCOEF)	= the AQUCOEF parameter on the [AQUANCON](#kw-AQUANCON) keyword


Note that ${A}_{(i,j,k)}$is calculated from the connected cell geometry, and thus the [AQUANCON](#kw-AQUANCON)(AQUFLUX) and the AQUANCONL(AQUFLUX) parameters are ignored for this type of aquifer.

The AQUFLUX keyword should only be used in runs that have been initialized by equilibration or with enumerated values, and should not be used in [RESTART](#kw-RESTART) runs.

See also the [BCCON](#REF_HEADING_KEYWORD_BCCON) keyword in the [GRID](#kw-GRID) section and the [BCPROP](#REF_HEADING_KEYWORD_BCPROP) keyword in the [SCHEDULE](#kw-SCHEDULE) section that can be used to specify boundary conditions.


#### Example

Given a total of five analytical aquifers as declared by the NANAQ parameter on the [AQUDIMS](#kw-AQUDIMS) keyword being set to five, of which three are Constant Flux Aquifers and two Carter-Tracy Aquifers, then:


```
--
--                      CONSTANT FLUX AQUIFER DESCRIPTION
--
--      ID   WATER    SALT   AQF    AQU
--      NUM  INFLUX   CONC   TEMP   PRES
--
AQUFLUX
         1   0.0004   1*     1*     1*                      /
         2   0.0005   1*     1*     1*                      /
         3   0.0003   1*     1*     1*                      /
/
--
--                      CARTER-TRACY AQUIFER DESCRIPTION
--
--      ID   DATUM   AQF    AQF    AQF    AQF     AQF   AQF   INFL   PVT  AQU
--      NUM  DEPTH   PRESS  PERM   PORO   RCOMP   RE    DZ    ANGLE  NUM  TAB
--
AQUCT
         4   2000.0  269    100.0  0.30   3.0e-5  330   10.0  360.0   1    2   /
         5   2000.0  269    100.0  0.30   3.0e-5  330   10.0  360.0   1    2   /
/

```

Defines three Constant Flux Aquifers and three Carter-Tracy Aquifers, and the connection of the aquifers are set in the [GRID](#kw-GRID) or [SOLUTION](#kw-SOLUTION) sections via:


```
--
--                      ANALYTIC AQUIFER CONNECTION
--
--       ID     ---------- BOX ---------   CONNECT  AQF    AQF      ADJOIN
--       NUMBER I1  I2   J1  J2   K1  K2   FACE     INFLX  MULTI    CELLS
AQUANCON
         1      1   198  1   14   1   10    J-      1*     1.0      'NO'        /
         2      1   198  1   14   12  22    J-      1*     1.0      'NO'        /
         3      1   198  1   14   23  54    J-      1*     1.0      'NO'        /
         4      1   198  1   14   61  70    J-      1*     1.0      'NO'        /
         5      1   198  15  172  71  71    K+      1*     1.0      'NO'        /
/


```