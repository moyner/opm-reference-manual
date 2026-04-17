### RVCONSTT – Define Constant CGR (Rv) for Each Dry Gas PVT Fluid {#kw-RVCONSTT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

RVCONSTT defines a constant Condensate-Gas Ratio (“CGR” or Rv), for each dry gas^[Natural gas that occurs in the absence of condensate or liquid hydrocarbons, or gas that had condensable hydrocarbons removed, is called dry gas. It is primarily methane with some intermediates. The hydrocarbon mixture is solely gas in the reservoir and there is no liquid (condensate surface liquid) formed either in the reservoir or at surface. The term dry indicates that the gas does not contain heavier hydrocarbons to form liquids at the surface conditions. Dry gas typically has GOR's greater than 100,000 scf/stb or 18,000 Sm3/m3.] PVT fluid. If the gas has a constant and uniform dissolved condensate concentration, and if the reservoir pressure never drops below the saturation pressure (dew point pressure), then the model can be run more efficiently by omitting the [OIL](#kw-OIL) and VAPGAS keywords from the [RUNSPEC](#kw-RUNSPEC) section, treating the gas as a dry gas, and defining a constant Rv (CGR) value with keywords [RVCONST](#kw-RVCONST) or RVCONSTT in the [PROPS](#kw-PROPS) section. This results in the model being run as a dry gas problem with no active oil phase. However, OPM Flow takes into account the constant Rv in the calculations and reporting.

This keyword is ignored by OPM Flow but is documented here for completeness.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [RS](#kw-RS) | A real positive value that defines the dry gas CGR for each dry gas PVT table in the model | None |
| stb/Mscf | sm3/sm3 | scc/scc |  |
| 2 | PRESS | A real positive value that defines that saturation pressure (dew point pressure) for each dry gas PVT table in the model. | 0.0 |
| psia | barsa | atma |  |
| Notes: |  |  |  |
: RVCONSTT Keyword Description {#tbl-8-138}
See also the [RVCONST](#kw-RVCONST) keyword to define a constant Rv to all the various dry gas PVT tables and the [PVDG](#kw-PVDG) keyword to enter the dry gas properties. All of the aforementioned keywords are in the [PROPS](#kw-PROPS) section.


#### Example

The example sets the dry gas CGR to 5, 6.5 and 8.0 stb/MMscf for PVT tables one, two and three, respectively and the bubble point pressure to 14.7 psia for all three tables.


```
--
--       DRY GAS PVT CONSTANT GCR AND SATURATION PRESSURE
--
RVCONSTT
--       RV        PSAT
--       STB/MSCF  PSIA
--       --------  ------
          0.0050     14.7                                  / TABLE NO. 01
          0.0065     14.7                                  / TABLE NO. 02
          0.0080     14.7                                  / TABLE NO. 03
```