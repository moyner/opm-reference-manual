### GDIMS – Activate Instantaneous Gradient Option and Define Dimensions {#kw-GDIMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GDIMS keyword activates the Instantaneous Gradient option and defines the maximum dimensions as used by the [GWRTWCV](#kw-GWRTWCV) keyword in the [SCHEDULE](#kw-SCHEDULE) section. The Instantaneous Gradient option calculates derivatives of solution quantities at the current time step with respect to variations in the variables at the current time step. This is different to Gradient option that calculates the derivatives of solution quantities at the current time step with respect to variations in the variables at the initial time step, that is a time equal to zero. Consequently, the Instantaneous Gradient option can be switched on and off by the [GUPFREQ](#kw-GUPFREQ) keyword in the [SCHEDULE](#kw-SCHEDULE) section, whereas the Gradient option cannot.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.