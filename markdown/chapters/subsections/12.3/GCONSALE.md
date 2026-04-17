### GCONSALE – Define Group Sales Gas Production Targets and Constraints


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

GCONSALE defines group sales gas production targets and constraints for when the gas production from an oil field group is exported under a Gas Sales Agreement (“GSA”) and the oil field group also has oil production targets and constraints.

Note that the keyword should not be used to control sales gas for a gas field group, as the gas injection rate is used to control the sales gas production with this keyword, that is:


$$
\begin{matrix}\text{Gas Sales Rate} = \text{Total Group Gas Production Rate} \\  - \text{Group Gas Injection Rate} \\  + \text{Total Group Gas Import Rate} \\  - \text{Total Group Gas Consumption}\end{matrix}
$$ {#eq-12-23}


Thus, surplus gas that cannot be sold is re-injected, which requires that there are active gas injectors in the model that are subordinate to groups with gas sales targets. Note that the surplus gas re-injection rates are automatically calculated by OPM Flow at each time step.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group gas sales target and constraints are being defined. The group named FIELD is the top most group and should be used to set the gas sales targets and constraints for the field. Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| 2 | GSALE | GSALE should either be set to: This value may be specified using a User Defined Argument (UDA). Note that if GSALE has been set to switch off both gas sales and gas re-injection, then the GCONINJE keyword in the SCHEDULE section may be used to re-enable gas re-injection again. | None |
| Mscf/d | sm3/day | scc/hour |  |
| 3 | GSALEMAX | A real positive value that must be greater than GSALE that defines the maximum allowed gas sales rate. If GSALE exceeds GSALEMAX then the action defined by the ACTION variable on this keyword is implemented at the end of the current time step. This value may be specified using a User Defined Argument (UDA). | 1 x 1020 |
| Mscf/d | sm3/day | scc/hour |  |
| 4 | GSALEMIN | A real positive value that must be less than GSALE that defines the minimum allowed gas sales rate. If GSALE is less than GSALEMIN then one of the following actions will be implemented at the end of the current time step: If none of the above actions can be implemented then the minimum gas sales rate will not be satisfied. This value may be specified using a User Defined Argument (UDA). | -1 x 1020 |
| 5 | ACTION | A defined character string that defines the action to be taken if the maximum gas sales rate, GSALEMAX, is violated. ACTION should be set to one of the following character strings: The corrective action takes places at the end of the time step in which the constraint is violated. | None |
| Notes: |  |  |  |

*Table 12.32: GCONSALE Keyword Description*


GCONSALE can also be used with the GCONINJE keyword in the SCHEDULE section in order to apply additional limits, for example by applying a maximum group injection rate. In this scenario, the TARGET variable on the GCONINJE keyword must be set to “REIN”, and if desired, a re-injection fraction (REIN on the GCONINJE keyword), or any other constraint.

See also the GCONSUMP in the SCHEDULE section that defines the fuel gas requirements for groups.


#### Example

The following examples sets the field gas sales target rate:


```
--
--       GROUP GAS SALES FOR OIL FIELDS
--
-- GRUP  GAS    MAX    MIN    CNTL
-- NAME  SALES  RATE   RATE   ACTN
GCONSALE
FIELD    40E3   50E3   20E3   RATE                                            /
/
```


Here the field has a gas sales target of 40 MMscf/d, with a maximum rate of 50 MMscf/d and a minimum of 20 MMscf/d. If the maximum gas sales rate is exceeded then the group’s gas production rate target is reduced to equal GSALEMAX, after accounting for fuel gas and the current rate of re-injection. This will also place the group on gas production control.


```

```
