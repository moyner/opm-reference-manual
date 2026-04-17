### WSOLVENT – Define Gas Injection Well Solvent Fraction


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WSOLVENT defines a gas injection well’s solvent fraction in the injection stream that is to be used when the Solvent option has been activated by the SOLVENT keyword in the RUNSPEC section.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name of a gas injection well for which the solvent fraction data is being defined. Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 4 | SOLFRA | A real positive value greater than or equal to zero and less than or equal to one that defines the fraction of solvent in the gas well’s injection stream. This value may be specified using a User Defined Argument (UDA). | None |
| fraction | fraction | fraction |  |
| Notes: |  |  |  |

*Table 12.124: WSOLVENT Keyword Description*


Gas injection wells that are not declared via this keyword have their solvent fractions set to zero.

See also the GCONINJE keyword to define a group’s injection targets and constraints, and the WCONINJE keyword to define an injection well’s targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.


#### Example

The following example defines the solvent fractions for three gas injection wells for when the solvent option has been activated by the SOLVENT keyword in the RUNSPEC section.


```
--
--       DEFINE GAS INJECTION WELL SOLVENT FRACTION
--
-- WELL  SOLVENT
-- NAME  FRACTION
--       --------
WSOLVENT
GI01     0.0000                                            /
GI02     0.5000                                            /
GI03     0.5000                                            /
/
```


The solvent fraction for the GI01 gas injector is set to zero and both GI02 and GI03 gas injectors have solvent fraction values of 0.5 for their injection streams.
