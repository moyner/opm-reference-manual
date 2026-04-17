### RVW – Define the Initial Equilibration Vaporized Water in Gas Ratio for All Grid Blocks {#kw-RVW}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RVW keyword defines the initial equilibration vaporized water in gas ratio values for all grid cells in the model and should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model. The keyword should only be used if both gas and water phases have been activated in the model via the [GAS](#kw-GAS) and [WATER](#kw-WATER) keywords, and the [VAPWAT](#kw-VAPWAT) is also present activating OPM Flow’s Vaporized Water Model. All the aforementioned keywords are in the [RUNSPEC](#kw-RUNSPEC) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | RVW | RVW is an array of real positive numbers assigning the initial equilibration gas-vaporized water ratio values to each cell in the model. Repeat counts may be used, for example 20*1.30. | None |
| stb/Mscf | sm3/sm3 | rcc/scc |  |
| Notes: |  |  |  |
: RVW Keyword Description {#tbl-10-34}
See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


::: {.callout-note}
This is an OPM Flow specific keyword for the simulator’s Water Vaporization Model that is activated by declaring that vaporized water is present in the run using the [VAPWAT](#kw-VAPWAT) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Use the command line option --enable-opm-rst-file=true to output the RVW data to the [RESTART](#kw-RESTART) file.
:::


#### Example


```
--
--       INITIAL EQUILIBRATION WATER VAPOR IN GAS RATIO VALUES FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
RVW
         1000*0.0000   1000* 0.0000   1000*1.3000                               /

```

The above example defines the initial equilibration gas-vaporized water values to be 0.000 for all the cells in the first and second layers and 1.3000 for all the cells in the third layer.