### SOF32D – Oil Saturation Tables with Respect to Water and Gas (Three Phase) {#kw-SOF32D}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SOF32D keyword defines the three phase oil relative permeability versus water and gas saturation tables for when oil, gas and water are present in the input deck.  The keyword should only be used if oil, gas and water are present in the input deck.  Normally the simulator calculates the three-phase oil relative permeabilities based on the entered two phase tables of water-oil and gas-oil, combined with the [STONE1](#kw-STONE1) and [STONE2](#kw-STONE2) keywords in the [PROPS](#kw-PROPS) section that determine the method used to generate the thee phase oil relative permeability curves.  SOF32D allows for the direct input of the three phase tables, as such the [STONE1](#kw-STONE1) and [STONE2](#kw-STONE2) keywords should not be entered if SOF32D is used in the input deck.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.