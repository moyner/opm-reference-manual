### PLYMAX – Define Polymer-Salt Viscosity Mixing Concentrations


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PLYMAX keyword defines maximum polymer and salt concentrations that are to be used in the mixing parameter calculation of the fluid component viscosities, for when the Polymer option has been activated by the POLYMER keyword in the RUNSPEC section.

Note that If the BRINE option has not be activated by the BRINE keyword in the RUNSPEC section, then the salt concentrations in the second column are ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | POLCON | A real value that defines the polymer concentration in the solution which is used to calculate maximum polymer fluid component viscosity. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| 2 | SALTCON | A real value that defines the salt concentration in the solution which is used to calculate maximum polymer fluid component viscosity. Note that If the BRINE option has not been activated by the BRINE keyword in the RUNSPEC section, then this variable is ignored; however, there should still be dummy entries in this case. This variable is ignored as the BRINE and POLYMER combination is not implemented in OPM Flow. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |

*Table 8.103: PLYMAX Keyword Description*


::: {.callout-note}
Currently, combining the BRINE and POLYMER models is not implemented in OPM Flow, and therefore SALTCON parameter on the PLYMAX keyword is ignored.
:::


#### Example


```
--
--       POLYMER-SALT VISCOSITY MIXING CONCENTRATIONS
--
PLYMAX
--       POLYMER    SALT
--       POLCON     SALTCON
--       -------    --------
         0.0100      0.0500                                / TABLE NO. 01
         0.0075      0.0400                                / TABLE NO. 02
         0.0050      0.0300                                / TABLE NO. 03
```


The above example defines three polymer-salt viscosity mixing concentrations, based on the NPLMIX variable on the REGDIMS keyword in the RUNSPEC section being equal to three.
