### REFINE – Start the Definition of a Local Grid Refinement {#kw-REFINE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The REFINE keyword defines the start of a Cartesian or radial Local Grid Refinement (“[LGR](#kw-LGR)”) definition that sets the properties of the selected [LGR](#kw-LGR). The keyword is then followed by the property keywords associated with the section where the keyword is being invoked. For example, if the REFINE keyword is used in the [GRID](#kw-GRID) section then most of the keywords in that section can be used to set the grid properties for the [LGR](#kw-LGR).

The [ENDFIN](#kw-ENDFIN) keyword is used to terminate the [LGR](#kw-LGR) definition.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.