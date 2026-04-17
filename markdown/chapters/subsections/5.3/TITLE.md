### TITLE – Define the Title for the Input Deck {#kw-TITLE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The TITLE keyword defines the title for the input deck. The title text will be printed on all reports so as to act as a reference for the run.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | TITLE | A character string that defines the title for the input deck | None￹ |
| Notes: |  |  |  |
: TITLE Keyword Description {#tbl-5-47}
::: {.callout-note}
It is good practice to include the name of the input file in the tittle (without the extension) for when cross checking results from multiple cases.
:::


#### Example


```
--
--       DEFINE THE TITLE FOR THE RUN
TITLE
SPE01-THEM01-OPM1810-R01 - OPM THERMAL OPTION RUN

```

The above example defines the title for the run to be “SPE01-THEM01-OPM1810-R01 - OPM [THERMAL](#kw-THERMAL) OPTION RUN”.