### PCW – End-Point Scaling of Grid Cell Water Capillary Pressure (Drainage) {#kw-PCW}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PCW defines the maximum drainage water-oil or water-gas capillary pressure values for all the cells in the model via an array.  The [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section should be activated to enable end-point scaling and the use of this keyword. The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PCW | PCW is an array of positive real numbers assigning the maximum drainage water capillary pressure values for each cell in the model. Repeat counts may be used, for example 30*100.0. | None |
| psia | bars | atm |  |
| Notes: |  |  |  |
: PCW Keyword Description {#tbl-8-96}
See also the [IPCW](#kw-IPCW) keyword for the equivalent imbibition functionality.

The capillary pressure for a grid block is scaled by:


$$
{P}_{c} = {P}_{{c}_{\mathit{TABLE}}}(\frac{\mathit{PCW}}{{P}_{{c}_{\mathit{TABLE}-\mathit{MAX}}}})
$$ {#eq-8-70}

Where:

${P}_{c}$	=	the resulting drainage water capillary pressure for a grid cell.

$\mathit{PCW}$	=	the maximum capillary pressure from the PCW array for a given cell.

${P}_{{c}_{\mathit{TABLE}}}$	=	the capillary pressure in the drainage capillary pressure table allocated

to the grid block.

${P}_{{c}_{\mathit{TABLE}-\mathit{MAX}}}$	=	the maximum capillary pressure in the drainage capillary pressure table

allocated to the grid block (that is at the connate water saturation).


#### Example


```
--
--       DEFINE GRID BLOCK PCW DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
PCW
         100*50.0  100*75.0  100*125.0                                        /
```


The above example defines the PCW for 300 cells in the model as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.