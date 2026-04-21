### GUIDERAT – Define Group Guide Rate Formula


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines a general formulae used to define a group’s and well’s guide rate as a function of the their potential.  The default behavior, that is when this keyword is not invoked,  is to set the target control mode and rate via the GCONPROD keyword in the SCHEDULE section.  In this case the target rate is distributed between the group’s wells that are under group control using a well’s guide rate. If a well’s guide rate has not been defined, for example by this keyword, then the well potential of the group controlling phase at the beginning of the time step is used.  For example, if the group target rate and phase is oil, then the well’s under group control will have their oil rates determined by their oil rate potential^[Production and injection potentials are based on rates that are unrestricted. For wells this implies that well potential is calculated based on either the BHP or THP limit, which ever is the more constraining.]. The GUIDERAT keyword substitutes the potential calculation with a more general formulae in the aforementioned distribution and allocation of the rates:


$$
\mathit{Phase}\mathit{Guide}\mathit{Rate} =\frac{{({\mathit{Potential}}_{\mathit{Phase}})}^{A}}{B + C{(\mathit{Potential}{\mathit{Ratio}}_{1})}^{D} + E{(\mathit{Potential}{\mathit{Ratio}}_{2})}^{F}}
$$ {#eq-12-28}

Where:

PotentialPhase		= the potential of the phase,

A to F		= constants defined on this keyword,

Potential Ratio1	= the potential phase ratio as defined by this keyword,

Potential Ratio2	= the potential phase ratio as defined by this keyword.


The formulae can be used to control high water cut or high GOR wells in an oil field, such as the offending wells are given progressively smaller guide rates as they water out or gas out.


Note that groups can only have potential guide rates if they are subordinate in another group and required to produce a proportion of the superior group’s target rate. In this case the GUIDERAT keyword can optionally be applied by setting GUIPHASE variable on the GCONPROD keyword in the SCHEDULE section.  Group potentials are the sum of the potentials of their subordinate open wells.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | TSTEP | A real positive value that defines the minimum time interval to re-calculate the guide rates.  The guide rates are calculated at the start of a time step and the default value of zero means that the guide rates are calculated for each time step. A non-zero value for TSTEP resets the minimum interval, for example setting TSTEP equal to 30 would mean the guide rates are calculate every 30 days, or to the nearest associated time step. Calculating guide rates every time step may cause issues due to the rate dependent behavior, for example gas cusping or water coning causing the well rates to oscillate. In this case using a non-zero value of TSTEP may eliminate this oscillating behavior. | 0.0 |
| days | days | hours |  |
| 2 | PHASE | A defined character string that sets the potential phase guide rate for the group and well, the resulting Phase Guide Rate in equation (12.28).  PHASE should be set to one of the following character strings: For reference, the units for the various options is given below . | None |
| WOR: dimensionless WCT: dimensionless WGR: stb/Mscf | dimensionless dimensionless dimensionless | dimensionless dimensionless dimensionless |  |
| GOR: Mscf/stb GLR: Mscf/stb OGR: stb/Mscf | dimensionless dimensionless dimensionless | dimensionless dimensionless dimensionless |  |
| 3 | A | A real value greater than or equal to -3 and less than or equal to 3, that defines coefficient A in equation (12.28). | 0.0 |
| 4 | B | B is a real positive value that defines coefficient B in equation (12.28). | 0.0 |
| 5 | C | C is a real value that defines coefficient C in equation (12.28). | 0.0 |
| 6 | D | D is a real value greater than or equal to -3 and less than or equal to 3, that defines coefficient D in equation (12.28). | 0.0 |
| 7 | E | E is a real value that defines coefficient E in equation (12.28). | 0.0 |
| 8 | F | F is a real value greater than or equal to -3 and less than or equal to 3, that defines coefficient F in equation (12.28). | 0.0 |
| 9 | GROPT01 | A defined character string that determines if calculated phase guide rates should be allowed to increase (YES) or not (NO), and should be set to one of the following: Note only the default value is currently supported by OPM Flow. | YES |
| 10 | GROPT02 | A real positive value greater than or equal to zero and less than or equal to one that “dampens” the calculated phase guide rate based on the following formula: $\begin{matrix}{(\mathit{Phase} \mathit{Guide} \mathit{Rate})}_{t}^{\mathit{new}} = \mathit{GROPT}02\times {(\mathit{Phase} \mathit{Guide} \mathit{Rate})}_{t} +  \\ (1 - \mathit{GROPT}02)\times {(\mathit{Phase} \mathit{Guide} \mathit{Rate})}_{(t-1)}\end{matrix}$ The option is intended to have a similar effect as the GROPT01 NO option to reduce oscillations as a result of either the water cut or GOR being rate dependent. Values approaching one allows the calculated phase guide rates to change instantaneously with the phase potentials, whereas values approaching zero dampen the potential guide rates towards the previously calculated values, thereby reducing the potential for oscillating behavior. | 1.0 |
| 11 | GROPT03 | A defined character string that determines if “free” gas potential rates for the Potential Ratio2 variable in equation (12.28) should be used (YES), or if “free and associated” gas should be used (NO), and should be set to one of the following: | NO |
| 12 | GROPT04 | A real positive value that sets the minimum potential guide rate. If the calculated potential guide is below this value it will be reset to GROPT04. The option is meant to avoid groups and wells being ignored due to the calculated potential guide rates being minuscule. | 1.0 x10-6 |
| Notes: |  |  |  |

*Table 12.47: GUIDERAT Keyword Description*


Note that the GUIDERAT keyword only applies to production groups and wells. Injection groups and wells are still controlled by their potential guide rates.


Finally, as mentioned previously, if the GUIDERAT or WGRUPCON keywords are not present in the input deck then the group and well potential guide rates will be calculated using the well’s potential rates. The WGRUPCON keyword in the SCHEDULE section can be used to set a constant potential guide rate for a well.


::: {.callout-note}
GUIDERAT can be used to penalize wells producing excessive water by utilizing the C and D coefficients in equation (12.28), and to discriminate against wells that are gassing out by setting the E and F coefficients. Note that the value range through which Potential Ratio1 and Potential Ratio2 vary is variable. For example, if Potential Ratio1 is water cut,  then the value should be between zero and one, whereas for the water-oil ratio the value can vary between zero and infinity. The same applies to the units of Potential Ratio2 which are dependent on if the GOR, GLR or OGR ratio is used in the calculation. One can use the C and E coefficients to scale these terms to the required relative magnitudes in the denominator and the D and F powers to influence how quickly the penalty increases with increasing water and gas fractions.  High positive value for D and F coefficients will make production fall off rapidly as the water or gas fraction increases, while a negative values will favor producing these type of wells. Note that the B coefficient should always be positive to prevent the denominator's going to zero. Finally, if one wishes each well to produce in proportion to its potential when the water fraction and gas fraction are equal (the usual case), then the A coefficient should be set to one.
:::


#### Examples

The first example sets the guide phase to oil and the resulting Phase Guide Rate based on oil potential based on setting the A and B coefficients to to one, that is:


$$
\begin{matrix}\mathit{Phase}\mathit{Guide}\mathit{Rate} =\frac{{({\mathit{Potental}}_{\mathit{Phase}})}^{A}}{B + C{(\mathit{Potential}{\mathit{Ratio}}_{1})}^{D} + E{(\mathit{Potential}{\mathit{Ratio}}_{2})}^{F}} \\  \\  = \frac{\mathit{Oil}{\mathit{Potential}}^{1.0}}{1.0}\end{matrix}
$$ {#eq-12-29}


with all the other parameters defaulted, except for the minimum time interval to re-calculate the guide rates which is set to 30 days.


```
--
--       SETS GUIDE RATES FOR GROUPS AND WELLS UNDER GUIDE RATE CONTROL
--
--       TIME  GUIDE  A      B     C     D     E    F     INCR   DAMP   FREE
--       STEP  PHASE  POW    CON   CON   POW   CON  POW   OPTN   OPTN   GAS
GUIDERAT
         30    'OIL'  1.0    1.0    1*   1*    1*   1*    1*     1*     1*      /
```


The next example sets the Phase Guide Rate to the reservoir fluid volume rate, with preference given to low GOR wells and with high GOR wells penalized, based on setting A and B to one, C and D to zero, E equal to 10 and F equal to two, that is:


$$
\begin{matrix}\mathit{Phase}\mathit{Guide}\mathit{Rate} =\frac{{({\mathit{Potental}}_{\mathit{Phase}})}^{A}}{B + C{(\mathit{Potential}{\mathit{Ratio}}_{1})}^{D} + E{(\mathit{Potential}{\mathit{Ratio}}_{2})}^{F}}  \\  \\  = \frac{\mathit{Reservoir} \mathit{Fluid} \mathit{Volume} {\mathit{Potential}}^{1.0}}{1.0 + 10\times {(\mathit{GOR})}^{2}}\end{matrix}
$$ {#eq-12-30}


with all the other parameters defaulted.


```
--
--       SETS GUIDE RATES FOR GROUPS AND WELLS UNDER GUIDE RATE CONTROL
--
--       TIME  GUIDE  A      B     C     D     E    F     INCR   DAMP   FREE
--       STEP  PHASE  POW    CON   CON   POW   CON  POW   OPTN   OPTN   GAS
GUIDERAT
         1*    'RES'  1.0    1.0    1*   1*    10   2     1*     1*     1*      /
```


The GUIDERAT keyword is very flexible but can also lead to unexpected results, thus it is probably useful to perform some manual calculations outside of the simulator before implementing the selected scheme in the input deck.
