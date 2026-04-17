### IPCG – End-Point Scaling of Grid Cell Gas Capillary Pressure (Imbibition)


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

IPCG defines the maximum imbibition gas-oil capillary pressure values for all the cells in the model via an array.  The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. In addition, the HYSTER option on the SATOPTS keyword in the RUNSPEC section has to be activated to invoke the hysteresis option. The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | IPCG | IPCG is an array of positive real numbers assigning the maximum imbibition gas capillary pressure values for each cell in the model. Repeat counts may be used, for example 30*100.0. | None |
| psia | bars | atm |  |
| Notes: |  |  |  |

*Table 8.61: IPCG Keyword Description*


The capillary pressure for a grid block is scaled by:


$$
{P}_{c} = {P}_{{c}_{\mathit{TABLE}}}\left(\frac{\mathit{IPCG}}{{P}_{{c}_{\mathit{TABLE}-\mathit{MAX}}}}\right)
$$ {#eq-8-59}

Where:

$\mathit{Pc}$	= 	the resulting imbibition gas-oil capillary pressure for a grid cell.

$\mathit{IPCG}$	= 	the maximum capillary pressure from the IPCG array for a given cell.

${P}_{{c}_{\mathit{TABLE}}}$	= 	the capillary pressure in the imbibition capillary pressure table

allocated to the grid block.

${P}_{{c}_{\mathit{TABLE}-\mathit{MAX}}}$	= 	the maximum capillary pressure in the imbibition capillary pressure table

allocated to the grid block at${S}_{g}=1-{S}_{\mathit{wco}}$.


See also the PCG keyword for the equivalent drainage functionality.


#### Example


```
--
--        DEFINE GRID BLOCK IPCG DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
IPCG
          100*50.0  100*75.0  100*125.0                                         /

```

The above example defines the IPCG for 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
