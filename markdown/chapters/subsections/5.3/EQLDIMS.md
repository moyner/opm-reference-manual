### EQLDIMS – Define the Equilibration Data Dimensions {#kw-EQLDIMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The EQLDIMS keyword defines the maximum number of properties associated with equilibrating the model, that is initializing the model. A reservoir grid can be separated into separate regions in order to apply different pressure regimes and/or fluid contacts.  Care should be taken that the different regions are not in communication if the pressures or fluid contacts are different for the various regions, as this would lead to an unstable initialization and would also imply errors in the model description as implemented.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NTEQUL | A positive integer value that defines the number of equilibration regions entered using the [EQLNUM](#kw-EQLNUM) keyword in the [REGIONS](#kw-REGIONS) section and the number of entries associated with the [EQUIL](#kw-EQUIL) keyword in the [SOLUTION](#kw-SOLUTION) section. | 1 |
| 2 | NPRSVD | A positive integer value setting the number of pressure versus depth entries used by OPM Flow in determining equilibration parameters. Unless there is a requirement for a very fine equilibration this parameter should be defaulted. | 100 |
| 3 | NDRXVD | A positive integer value that defines the maximum number of depth entries in equilibration property versus depth tables ([RSVD](#kw-RSVD), [RVVD](#kw-RVVD), [PBVD](#kw-PBVD) or [PDVD](#kw-PDVD) etc.) as defined in the [SOLUTION](#kw-SOLUTION) section. | 20 |
| 4 | NTTRVD | A positive integer that defines the maximum number of [TVDP](#kw-TVDP) tables that describe the initial tracer concentration versus depth. | 1 |
| 5 | NSTRVD | A positive integer that defines the maximum number of depth entries in the [TVDP](#kw-TVDP) tables as described in (4) | 20 |
| Notes: |  |  |  |
: EQLDIMS Keyword Description {#tbl-5-11}
It is common that the [EQLNUM](#kw-EQLNUM) and [FIPNUM](#kw-FIPNUM) arrays are identical so that the fluid in-place reporting matches the equilibration regions. Thus, in order to avoid errors in this case, one should just use one array (say the [FIPNUM](#kw-FIPNUM) property array) and use the [COPY](#kw-COPY) keyword to generate the [EQLNUM](#kw-EQLNUM) array.


#### Example


```
--
--       MAX     MAX     RSVD    TVDP    TVDP
--       EQLNUM  DEPTH   NODES   TABLE   NODES
EQLDIMS
         9       1*      20      1*      1*                                    /
```


The above example defines nine equilibration regions the default values for the remaining parameters on the EQLDIMS keyword.