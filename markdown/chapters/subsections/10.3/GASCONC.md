### GASCONC – Define the Initial Equilibration Coal Gas Concentration for All Grid Blocks {#kw-GASCONC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GASCONC keyword defines the initial equilibration coal gas concentration values for all matrix grid cells in the model and should be used in conjunction with the [GCVD](#kw-GCVD) keyword in the [SOLUTION](#kw-SOLUTION) section, to fully describe the initial state of the model. The keyword should only be used if the coal phase has been activated in the model via the [COAL](#kw-COAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note both GASCONC and [GCVD](#kw-GCVD) are optional as the simulator will calculate the coal gas concentration based on the equilibrium concentration and the block pressure.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | GASCONC | GASCONC is an array of real positive numbers that define the initial equilibration coal gas concentration values to each matrix cell in the model. Repeat counts may be used, for example 20*75.0. | None |
| Mscf/ft3 | sm3/m3 | scc/cc |  |
| Notes: |  |  |  |
: GASCONC Keyword Description {#tbl-10-15}
See also the [GCVD](#kw-GCVD) keyword in the [SOLUTION](#kw-SOLUTION) section to fully define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION COAL GAS CONCENTRATION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 6
--
GASCONC
         1000*75.500    1000*65.500    1000*60.000                             /

```

The above example defines the initial equilibration coal gas concentration values to be 75.500 for all the matrix cells in the first layer, 65.500 for all the cells in the second layer, and finally 60.000 for all the cells in the third layer.