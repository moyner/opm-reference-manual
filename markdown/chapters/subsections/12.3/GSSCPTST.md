### GSSCPTST – Perform Sustainable Capacity Test {#kw-GSSCPTST}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GSSCPTST keyword instructs the simulator to perform a sustainable capacity test. This causes the model to be saved in it’s current state via the [RESTART](#kw-RESTART) file, and the test performed by running the simulation under the current conditions combine with the parameters on this keyword.  After the test is perform, the simulator will restart from the point prior to the test by loading in the [RESTART](#kw-RESTART) file. This type of testing is normally applied to gas fields for which the gas sales contracts stipulate that the gas sales rates are based on a sustainable capacity rate over a fixed period of time.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.