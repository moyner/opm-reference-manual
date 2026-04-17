### WFOAM – Define Well Foam Injection Concentrations {#kw-WFOAM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WFOAM keyword defines an injection wells foam concentration.  The foam option must be activated by the [FOAM](#kw-FOAM) keyword in the [RUNSPEC](#kw-RUNSPEC) section in order to use this keyword. Note if a well’s foam concentration is not set with this keyword then default value of zero is assigned to a well.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well injection foam concentration is being defined. | None |
| 2 | FOAMCON | A real positive value that defines the well’s injection foam concentration. This value may be specified using a User Defined Argument (UDA). Units are dependent on the transport phase specified via the FOAMOPT1 variable on the [FOAMOPTS](#kw-FOAMOPTS) keyword in the [PROPS](#kw-PROPS) section. FOAMOPT1 should be set to either [GAS](#kw-GAS) or [WATER](#kw-WATER). Currently OPM Flow only supports injecting foam via the [GAS](#kw-GAS) phase. | None |
| Gas: lb/Mscf Water: lb/stb | Gas: kg/sm3 Water: kg/sm3 | Gas: gm/scc Water: gm/scc |  |
| Notes: |  |  |  |
: WFOAM Keyword Description {#tbl-12-95}
See also the [FOAM](#kw-FOAM) keyword in the [RUNSPEC](#kw-RUNSPEC) section, the [FOAMADS](#kw-FOAMADS), [FOAMOPTS](#kw-FOAMOPTS) and [FOAMROCK](#kw-FOAMROCK) keywords in the [PROPS](#kw-PROPS) section.


#### Example


```
--
--       WELL INJECTION FOAM CONCENTRATION
--
-- WELL  FOAM
-- NAME  FOAMCON
WFOAM
GI01     0.020                                                                 /
GI02     0.020                                                                 /
GI03     0.020                                                                 /
/
```


Here three gas wells are given an injection foam concentration of 0.020 lb/Mscf, assuming field units.