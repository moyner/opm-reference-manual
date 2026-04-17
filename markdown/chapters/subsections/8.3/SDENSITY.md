### SDENSITY – Define the Miscible or Solvent Surface Gas Density {#kw-SDENSITY}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SDENSITY keyword defines density at surface conditions of either the miscible injection gas for when the [MISCIBLE](#kw-MISCIBLE) option has been invoked in the [RUNSPEC](#kw-RUNSPEC) section, or the solvent for when the [SOLVENT](#kw-SOLVENT) option has been invoked in the [RUNSPEC](#kw-RUNSPEC) section. This keyword must be invoked if either the [MISCIBLE](#kw-MISCIBLE) or [SOLVENT](#kw-SOLVENT) options have been activated in the [RUNSPEC](#kw-RUNSPEC) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SDENSITY | SDENSITY is a real positive number defining the density at surface conditions of either: | None |
| lb/ft3 | kg/m3 | gm/cc |  |
| Notes: |  |  |  |
: SDENSITY Keyword Description {#tbl-8-145}
In addition to this keyword, the surface density or gravity of the in-place natural gas must be entered using either the [DENSITY](#kw-DENSITY) or [GRAVITY](#kw-GRAVITY) keywords.


#### Examples

The following shows the SDENSITY keyword for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set to one.


```
--
--       MIS-SOL
--       DENSITY
--       -------
SDENSITY
         0.04520                                           / MIS-SOL DENSITY
```


The next example shows the SDENSITY keyword for when NTPVT on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section is set to three.


```
--
--       MIS-SOL
--       DENSITY
--       -------
SDENSITY
         0.04520                                           / MIS-SOL DENSITY 1
         0.05520                                           / MIS-SOL DENSITY 2
         0.06420                                           / MIS-SOL DENSITY 3
```

There is no terminating “/” for this keyword.