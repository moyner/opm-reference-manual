### RSCONSTT – Define Constant GOR (Rs) for Each Dead Oil PVT Fluid {#kw-RSCONSTT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

RSCONSTT defines a constant Gas-Oil Ratio (“GOR”), for each dead oil^[“Dead” oil is oil that it contains no dissolved gas or a relatively thick oil or residue that has lost its volatile components.] PVT fluid in the model. If the oil has a constant and uniform dissolved gas concentration, GOR, and if the reservoir pressure never drops below the saturation pressure (bubble point pressure), then the model can be run more efficiently by omitting the [GAS](#kw-GAS) and [DISGAS](#kw-DISGAS) keywords from the [RUNSPEC](#kw-RUNSPEC) section, treating the oil as a dead oil, and defining a constant Rs (GOR) value with keywords [RSCONST](#kw-RSCONST) or RSCONSTT in the [PROPS](#kw-PROPS) section. This results in the model being run as a dead oil problem with no active gas phase. However, OPM Flow takes into account the constant Rs in the calculations and reporting.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [RS](#kw-RS) | A real positive columnar vector that defines the dead oil GOR for each oil PVT table in the model | None |
| Mscf/stb | sm3/sm3 | scc/scc |  |
| 2 | PRESS | A real positive columnar vector that defines the saturation pressure (bubble point pressure) for each the oil PVT table in the model. | None |
| psia | barsa | atma |  |
| Notes: |  |  |  |
: RSCONSTT Keyword Description {#tbl-8-134}
See also the [RSCONST](#kw-RSCONST) keyword to define a constant Rs to all the various dead oil PVT tables and the [PVDO](#kw-PVDO) and [PVCDO](#kw-PVCDO) keywords to enter the dead oil properties. All of the aforementioned keywords are in the [PROPS](#kw-PROPS) section.


#### Example

The example sets the dead oil GOR to 5, 6.5 and 8.0 scf/stb for PVT tables one, two and three, respectively and the bubble point pressure to 14.7 psia for all three tables.


```
--
--       DEAD OIL PVT CONSTANT GOR AND SATURATION PRESSURE
--
RSCONSTT
--       RS        PSAT
--       MSCF/STB  PSIA
--       --------  ------
          0.0050     14.7                                  / TABLE NO. 01
          0.0065     14.7                                  / TABLE NO. 02
          0.0080     14.7                                  / TABLE NO. 03
```