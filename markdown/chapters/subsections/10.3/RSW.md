### RSW – Define the Initial Equilibrium Solution Gas in Water Ratio for All Grid Blocks


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [RSW](#REF_HEADING_KEYWORD_RSW_10_3) keyword defines the initial equilibration solution gas in water ratio values for all grid cells in the model and should be used in conjunction with the PBUB, PDEW, PRESSURE, RS, SGAS, SOIL and SWAT keywords etc., to fully describe the initial state of the model. The keyword should only be used if both gas and water phases have been activated in the model via the GAS and WATER keywords, and the DISGASW keyword is also present activating OPM Flow’s Dissolved Gas in Water Model. All the aforementioned keywords are in the RUNSPEC section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | RSW | RSW is an array of positive real numbers assigning the initial equilibration solution gas-water ratio values to each cell in the model. Repeat counts may be used, for example 20*1.30. | None |
| Mscf/stb | sm3/sm3 | scc/scc |  |
| Notes: |  |  |  |

*Table 10.34: RSW Keyword Description*


See also the PBUB, PDEW, PRESSURE, RS, SGAS, SOIL and SWAT keywords to fully define the initial state of the model.


::: {.callout-note}
This is an OPM Flow specific keyword for the simulator’s Dissolved Gas in Water Model that is activated by declaring that dissolved gas in water is present in the run using the DISGASW keyword in the RUNSPEC section. Use the command line option --enable-opm-rst-file=true to output the [RSW](#REF_HEADING_KEYWORD_RSW_10_3) data to the RESTART file.
:::


#### Example


```
--
--       INITIAL EQUILIBRATION SOLUTION GAS IN WATER RATIO VALUES FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
RSW
         1000*0.0000   1000* 0.0000   1000*1.3000                               /

```

The above example defines the initial equilibration solution gas-water values to be 0.000 for all the cells in the first and second layers and 1.3000 for all the cells in the third layer.
