### RVCONST – Define Constant CGR (Rv) for All Dry Gas PVT Fluids {#kw-RVCONST}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

RVCONST defines a constant Condensate-Gas Ratio (“CGR” or Rv), for all dry gas^[Natural gas that occurs in the absence of condensate or liquid hydrocarbons, or gas that had condensable hydrocarbons removed, is called dry gas. It is primarily methane with some intermediates. The hydrocarbon mixture is solely gas in the reservoir and there is no liquid (condensate surface liquid) formed either in the reservoir or at surface. The term dry indicates that the gas does not contain heavier hydrocarbons to form liquids at the surface conditions. Dry gas typically has GOR's greater than 100,000 scf/stb or 18,000 Sm3/m3.] PVT fluids. If the gas has a constant and uniform dissolved condensate concentration, and if the reservoir pressure never drops below the saturation pressure (dew point pressure), then the model can be run more efficiently by omitting the [OIL](#kw-OIL) and [VAPOIL](#kw-VAPOIL) keywords from the [RUNSPEC](#kw-RUNSPEC) section, treating the gas as a dry gas, and defining a constant Rv (CGR) value with keywords RVCONST or [RVCONSTT](#kw-RVCONSTT) in the [PROPS](#kw-PROPS) section. This results in the model being run as a dry gas problem with no active oil phase. However, OPM Flow takes into account the constant Rv in the calculations and reporting.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [RV](#kw-RV) | A real positive value that defines the dry gas CGR for all dry gas PVT tables in the model | None |
| stb/Mscf | sm3/sm3 | scc/scc |  |
| 2 | PRESS | A real positive value that defines that saturation pressure (dew point pressure) for all the dry gas PVT tables in the model. | 0.0 |
| psia | barsa | atma |  |
| Notes: |  |  |  |
: RVCONST Keyword Description {#tbl-8-137}
See also the [RVCONSTT](#kw-RVCONSTT) keyword to define a different constant Rv to the various dry gas PVT tables and the [PVDG](#kw-PVDG) keyword to enter the dry gas properties. All of the aforementioned keywords are in the [PROPS](#kw-PROPS) section.


#### Example

The example sets the dry gas CGR to 5 stb/MMscf and the bubble point pressure to 14.7 psia.


```
--
--       DRY GAS PVT CONSTANT GCR AND SATURATION PRESSURE
--
RVCONST
--       RV        PSAT
--       STB/MSCF  PSIA
--       --------  ------
          0.0050    14.7                                   /
```