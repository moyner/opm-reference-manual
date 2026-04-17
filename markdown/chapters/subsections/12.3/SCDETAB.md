### SCDETAB – Well Connection Karst Aquifer Properties for Scale Deposit {#kw-SCDETAB}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

SCDETAB defines well connection karst^[Karst is a topography formed from the dissolution of soluble rocks such as limestone, dolomite, and gypsum. Karst aquifers are characterized by a network of conduits and caves, with the conduits and caves draining the pore space between the limestone grains (intergranular or primary porosity) and the fractures (secondary porosity) formed by joints, bedding planes, and faults.] aquifer properties for modeling scale deposited by dissolution of calcite from the aquifer water, for when the Scale Deposition option has been activated by declaring the dimensions of the scaling deposition tables using the [SCDPDIMS](#kw-SCDPDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The SCDETAB tables are allocated to individual wells using the [WSCTAB](#kw-WSCTAB) keyword in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.