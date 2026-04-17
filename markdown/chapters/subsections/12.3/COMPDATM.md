### COMPDATM – Define Well Connections to an Amalgamated LGR Grid {#kw-COMPDATM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The COMPDATM keyword is an alias for the [COMPDATL](#kw-COMPDATL) keyword.  COMPDATM defines how a well in an amalgamated Local Grid Refinement (“[LGR](#kw-LGR)”) is connected to the reservoir by declaring the [LGR](#kw-LGR) and defining or modifying existing well connections. Ideally the connections should be declared in the correct sequence, starting with the connection nearest the well head and then working along the wellbore towards the bottom or toe of the well, however this may not be possible or convenient, for example when connections are added or removed from a well during the simulation (see the [COMPORD](#kw-COMPORD) keyword in the [SCHEDULE](#kw-SCHEDULE) section for options regarding connection ordering).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.