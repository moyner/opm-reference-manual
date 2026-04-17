### EQLOPTS – Activate the Equilibration Options {#kw-EQLOPTS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The EQLOPTS keyword defines the equilibration options by stating the character command to activate an option to be used for initializing the model. Multiple commands may be utilized to activate several  equilibration options following the keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MOBILE | A character string that activates the mobile fluid critical saturation end point correction. If the MOBILE command is stated then this option is activated. This option is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. Therefore this character string should be omitted. | None |
| 2 | QUIESC | A character string that activates the initial quiescence option that modifies the equilibrium calculated phase pressures to ensure that a steady state solution is obtained. This options ensures that there is no flow potential between the grid blocks in a given region, which is the normal case when block-centered equilibration is used by setting BOINIT on the [EQUIL](#kw-EQUIL) keyword to zero in the [SOLUTION](#kw-SOLUTION) section. If the QUIESC command is stated then this option is activated. This option is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. Therefore this character string should be omitted. | None |
| 3 | [THPRES](#kw-THPRES) | A character string that activates the inter-region equilibration flow option. This option allows for a threshold pressure variable entered via the [THPRES](#kw-THPRES) keyword to define a pressure which prevents flow between regions until the [THPRES](#kw-THPRES) value between regions is exceeded. If the [THPRES](#kw-THPRES) command is stated then this option is activated. | None |
| 4 | IRREVERS | A character string that activates the irreversible inter-region equilibration flow option. This option can only be invoked if the [THPRES](#kw-THPRES) command has been stated. The option allows for different [THPRES](#kw-THPRES) values for different directions. If the IRREVERS command is stated then this option is activated. This option is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. Therefore this character string should be omitted. | None |
| Notes: |  |  |  |
: EQLOPTS Keyword Description {#tbl-5-3-37-1}
#### Example


```
--
--       ACTIVATE EQUILIBRATION OPTIONS
--       MOBILE END-POINT(MOBILE) STEADY STATE(QUIESC) THRESHOLD(THPRES)
--       IRREVERSIBLE THRESHOLD(IRREVERS)
EQLOPTS
         'THPRES'  'IRREVERS'                                                   /
```

The above example activates the threshold pressure option with different threshold pressure for different directions.