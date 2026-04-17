### WSALT – Define Water Injection Well Salt Concentrations


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WSALT keyword defines a water injection well’s salt injection stream concentration that is to be used for when the salt option has been activated by the BRINE keywords in the RUNSPEC section. Note that if the Polymer option has also been activated by the POLYMER keyword in the RUNSPEC section, then the WPOLYMER keyword in the SCHEDULE section should be used to enter both the polymer and salt concentrations.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the injection salt concentrations are being defined. Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 2 | SALTCON | A real positive vector of values that defines the salt concentration of the well’s injection stream and consists of: Only options (1) and (2) are currently supported. This value may be specified using a User Defined Argument (UDA). Note if SALTCON is defaulted (1*) then the well’s salt concentration will be equal to the well’s group salt concentration. | 1* |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |

*Table 12.117: WSALT Keyword Description*


Water injection wells that are not declared via this keyword have their concentrations defaulted to zero.

See also the GCONPROD and GCONINJE keywords to define a group’s production and injection targets and constraints, and the WCONINJE keyword to define an injection well’s targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.


#### Examples

The following example defines the salt injection stream concentration for three water injection wells for when the brine phase has been activated by the BRINE keyword in the RUNSPEC section.


```
--
--       DEFINE WATER INJECTION WELL SALT CONCENTRATIONS (STANDARD)
--
-- WELL  SALT-1     SALT-2     SALT-3     SALT-4
-- NAME  SALTCON    SALTCON    SALTCON    SALTCON
--       -------    -------    -------    -------
WSALT
WI01     0.2500                                            /
WI02     1*                                                /
WI03     0.2500                                            /
/
```


The salt concentration for both well WI01 and WI03 is set to 0.25, and for well WI02 the salt concentration will be taken from the well’s group salt concentration.


The next example is based on using the Multi-Component Brine option, that is the BRINE and ECLMC keywords have been used in the RUNSPEC section, and assuming three salts.


```
--
--       DEFINE WATER INJECTION WELL SALT CONCENTRATIONS (MULTIPLE)
--
-- WELL  SALT-1     SALT-2     SALT-3     SALT-4
-- NAME  SALTCON    SALTCON    SALTCON    SALTCON
--       -------    -------    -------    -------
WSALT
WI01     0.1500     0.0500     0.0500                      /
WI02     0.1500     0.0500     0.0500                      /
WI03     0.2000     0.0500     0.0600                      /
/
```


Here the salt concentrations for both well WI01 and WI02 are set to 0.1500, 0.0500, 0.0500 for the three salts and for well WI03 the salt concentrations are 0.2000, 0.0500 and 0.0600.


Note that OPM Flow does not currently support the Multi-Component brine model.
