### WSEGMULT – Define Multi-Segment Well Frictional Pressure Loss Multipliers


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WSEGMULT supplies a set of constants used to modify (or scale) a multi-segment well’s segment frictional pressure drop between connecting segments The constants enable either a constant pressure to be applied, or for the pressure drop to vary as a function of the Gas-Oil Ratio (“GOR”) or the Water-Oil Ratio (“WOR”). The simulator calculated pressure drop is multiplied by the following resulting value:


| $\mathit{Frictional} \mathit{Loss} \mathit{Multipler} = \mathit{min}\left({x}_{1} + {x}_{2}{(\mathit{WOR})}^{{x}_{3}} + {x}_{4}{\left(\frac{\mathit{GOR}}{{\mathit{GOR}}_{\mathit{min}}}\right)}^{{x}^{5}}, 1.0\right)$ | (12.38) |
| --- | --- |


Where the constants x1 to x5 are defined by the values on this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
