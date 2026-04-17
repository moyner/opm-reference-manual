### WELSOMIN – Define Well Connection Minimum Oil Saturation for Opening {#kw-WELSOMIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

WELSOMIN defines a minimum oil saturation for a well connection above which the connection will be opened automatically. If the grid block connection is below WELSOMIN then connection will not be automatically opened.  Automatic opening of connection is controlled by the STATUS parameter on the [COMPDAT](#kw-COMPDAT) keyword in the [SCHEDULE](#kw-SCHEDULE) section. Note that if the [COMPLUMP](#kw-COMPLUMP) keyword in the [SCHEDULE](#kw-SCHEDULE) section has been used to lump connections into completions then WELSOMIN is compared to the average oil saturation of the completion.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.