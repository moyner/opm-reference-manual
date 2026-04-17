### RVWVD – Equilibration Vaporized Water-Gas Ratio (Rvw) versus Depth Tables {#kw-RVWVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RVWVD keyword defines the vaporized water-gas ratio (Rvw) versus depth tables for each equilibration region that should be used when there is vaporized water in the model and the EQLOPT6 variable has been set to a positive integer on the [EQUIL](#kw-EQUIL) keyword in the [SOLUTION](#kw-SOLUTION) section.

The keyword should only be used if both gas and water phases haves been activated in the model via the [GAS](#kw-GAS) and [WATER](#kw-WATER) keywords, and the [VAPWAT](#kw-VAPWAT) is also present activating OPM Flow’s Vaporized Water Model. All the aforementioned keywords are in the [RUNSPEC](#kw-RUNSPEC) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding vaporized oil-gas ratio values, [RVW](#kw-RVW) | None |
| feet | m | cm |  |
| 2 | [RVW](#kw-RVW) | A columnar vector of real values that defines the vaporized water-gas ratio values,  values at the corresponding [DEPTH](#kw-DEPTH). | None |
| stb/Mscf | sm3/sm3 | scc/scc |  |
| Notes: |  |  |  |
: RVWVD Keyword Description {#tbl-10-35}
Alternatively, the vaporized water-gas ratio for each cell may be set via the [RVW](#kw-RVW) keyword in the [SOLUTION](#kw-SOLUTION) section, if the non-standard method to initialize the model via enumeration is being employed.

See also the [EQUIL](#kw-EQUIL) keywords in the [SOLUTION](#kw-SOLUTION) section.


::: {.callout-note}
This is an OPM Flow specific keyword for the simulator’s Water Vaporization Model that is activated by declaring that vaporized water is present in the run using the [VAPWAT](#kw-VAPWAT) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Use the command line option --enable-opm-rst-file=true to output the [RVW](#kw-RVW) data to the [RESTART](#kw-RESTART) file.
:::


#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the following example defines the vaporized water-gas ratio versus depth functions.


```
--
--       DEPTH    RVW
--                STB/MSCF
--       ------   --------
RVWVD
         3000.0   0.00000
         8000.0   0.00000                            / RVW VS DEPTH EQUIL REGN 01
--       ------   --------
         3000.0   0.00000
         8000.0   0.00000                            / RVW VS DEPTH EQUIL REGN 02
--       ------   --------
         3000.0   0.00100
         8000.0   0.00100                            / RVW VS DEPTH EQUIL REGN 03
```


The example shows three tables for three regions with constant [RVW](#kw-RVW) versus depth relationships for each equilibration region, with the first two tables having a zero vaporized water-gas ratio and the last region having a constant 0.001 stb/Mscf versus depth relationship.