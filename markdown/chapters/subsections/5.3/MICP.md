### MICP – Activate the Microbially Induced Calcite Precipitation Model {#kw-MICP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MICP keyword activates the Microbially Induced Calcite Precipitation (“MICP”) model for the run. MICP is a new and sustainable technology which utilizes biochemical processes to create barriers by calcium carbonate cementation, the technology has the potential to be used for sealing leakage zones in geological formations. Further information on the mathematical model can be found in the open-access publications Landa-Marbán et al^[Landa-Marbán, D., Tveit, S., Kumar, K., Gasda, S.E., 2021. Practical approaches to study microbially induced calcite precipitation at the eld scale. Int. J. Greenh. Gas Control 106, 103256. https://doi.org/10.1016/j.ijggc.2021.103256.] and ^[Landa-Marbán, D., Kumar, K., Tveit, S., Gasda, S.E., 2021. Numerical studies of CO2 leakage remediation by micp-based plugging technology. In: Røkke, N.A. and Knuutila, H.K. (Eds) Short Papers from the 11th International Trondheim CCS conference, ISBN: 978-82-536-1714-5, 284-290.].


::: {.callout-note}
This is an OPM Flow specific keyword used to investigate leakage remediation. The module requires that both the MICP and [WATER](#kw-WATER) keywords in the [RUNSPEC](#kw-RUNSPEC) to be active.
:::


There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
		--
--       ACTIVATE THE MICROBIAL INDUCED CALCITE PRECIPITATION MODEL
--
MICP
--
--       WATER PHASE IS PRESENT IN THE RUN
--
WATER

```

The above example declares that the MICP model is active for the run and activates the water phase for the MICP model. For a complete example of this model, see [MICP.DATA](https://github.com/OPM/opm-tests/blob/master/micp/MICP.DATA).