### MISCIBLE – Define Miscibility Todd-Longstaff Parameters {#kw-MISCIBLE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MISCIBLE keyword defines the options associated with the Todd-Longstaff^[M. R. Todd and W. J Longstaff, The Development, Testing, and Application Of a Numerical Simulator for Predicting Miscible Flood Performance". In: J. Petrol. Tech. 24.7 (1972), pages 874-882.] mixing parameters used for when polymer flooding or CO2  EOR simulation cases are being run.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NTMISC | A positive integer value that declares the number miscible residual oil saturations versus water saturations tables for [SORWMIS](#kw-SORWMIS) keyword and the number Todd-Longstaff mixing parameters entries on the [TLMIXPAR](#kw-TLMIXPAR) keyword. | 1 |
| 2 | NSMISC | A positive integer value that sets the maximum number of entries (or rows) for each [SORWMIS](#kw-SORWMIS) table defined by the [SORWMIS](#kw-SORWMIS) keyword. | 20 |
| 3 | MISOPT | A character string that defines the numerical dispersion control options for the oil and gas relative permeability curves, set to either NONE or TWOPOINT: Only the default value of NONE is supported. | NONE |
| Notes: |  |  |  |
: MISCIBLE Keyword Description {#tbl-5-21}
#### Example


```
--
--       NTAB    MAX     UPSTRM
--       NTMISC  NSMISC  MISOPT
MISCIBLE
         1       20      NONE                                                  /
```


The above example defines the default values for the MISCIBLE keyword, that is one table with a maximum of 20 rows per table using the standard one cell upstream option.