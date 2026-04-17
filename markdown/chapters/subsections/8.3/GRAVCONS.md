### GRAVCONS – Re-Define Gravity Constant


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GRAVCONS keyword re-defines the gravity constant used in various calculations from the default value used by the simulator. Normally this keyword should not be used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | GRAVCONS | GRAVCONS is a positive real number number that defines the gravity constant used in various calculations. | Defined |
| ft2psi/lb 0.00694 | m2bars/kg 0.0000981 | cm2atm/gm 0.000968 |  |
| Notes: |  |  |  |

*Table 8.42: GRAVCONS Keyword Description*


#### Example


```
--
--       RE-DEFINE GRAVITY CONSTANT
--
GRAVITY
         0.0000980665                                      /

```

The above example re-defines the gravity constant to be 0.0000980665 ft2psi/lb from the default value of 0.00694  ft2psi/lb.
