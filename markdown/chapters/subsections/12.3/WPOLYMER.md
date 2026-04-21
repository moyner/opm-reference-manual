### WPOLYMER – Define Water Injection Well Polymer and Salt Concentrations


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WPOLYMER keyword defines a water injection well’s polymer and salt injection stream concentrations that are to be used for when the polymer and salt options have been activated by the POLYMER and BRINE keywords in the RUNSPEC section.

Note that if the Brine option has not be activated by the BRINE keyword in the RUNSPEC section, then the salt concentrations in the third column are ignored. Secondly, if the brine phase is declared but the polymer phase has not been made active, then the WSALT keyword in the SCHEDULE section can be used to set the salt concentration.

Currently the Brine option is not implemented in OPM Flow and therefore both the SALTCON and GRPSALT variables on this keyword are ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data is being defined. Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 2 | POLCON | A real positive value that defines the polymer concentration of the well’s injection stream. This value may be specified using a User Defined Argument (UDA). | None |
| lb/stb | kg/sm3 | gm/scc |  |
| 3 | SALTCON | A real positive value that defines the salt concentration of the well’s injection stream. This value may be specified using a User Defined Argument (UDA). This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| 4 | GRPPOL | A character string of up to eight characters in length that defines the group name for which the group’s produced polymer concentration should be used instead of the well’s POLCON value stated on this keyword. | None |
| 5 | GRPSALT | A character string of up to eight characters in length that defines the group name for which the group’s produced salt concentration should be used instead of the well’s SALTCON value stated on this keyword. This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored. | None |
| Notes: |  |  |  |

*Table 12.114: WPOLYMER Keyword Description*


Water injection wells that are not declared via this keyword have their concentrations defaulted to zero.


See also the GCONPROD and GCONINJE keywords to define a group’s production and injection targets and constraints, and the WCONINJE keyword to define an injection well’s targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.


#### Example

The following example defines the polymer and salt injection stream concentrations for three water injection wells for when the polymer option has been activated by the POLYMER keyword in the RUNSPEC section.


```
--
--       DEFINE WATER INJECTION WELL POLYMER AND SALT CONCENTRATIONS
--
-- WELL  POLYMER    SALT       POLYMER    SALT
-- NAME  POLCON     SALTCON    GROUP      GROUP
--       -------    --------   --------   --------
WPOLYMER
WI01     0.2500                                            /
WI02     1*         1*         GRPINJ1                     /
WI03     0.2500     1*         GRPINJ1                     /
/
```


The polymer concentration for well WI01 is set to 0.25 and the stated polymer concentration for well WI02 will be ignored, as both WI02 and WI03 will re-inject the produced polymer from the GRPINJ1 group.
