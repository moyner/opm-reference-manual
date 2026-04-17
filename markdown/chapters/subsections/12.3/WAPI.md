### WAPI – Define Oil Well Injection API Gravity {#kw-WAPI}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines an oil injection well’s [API](#kw-API) gravity for when [API](#kw-API) tracking has been made active via the [API](#kw-API) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The American Petroleum Institute ([API](#kw-API)) classifies oils based on an [API](#kw-API) gravity (γ[API](#kw-API)),  or degrees [API](#kw-API) (oAPI), the relationship between relative density (γo) of oil and [API](#kw-API) gravity (γ[API](#kw-API)) is given by:


$$
{\mathrm{γ}}_{\mathit{[API](#kw-API)}} = \frac{141.5}{{\mathrm{γ}}_{o}} - 131.5
$$ {#eq-12-33}


This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.