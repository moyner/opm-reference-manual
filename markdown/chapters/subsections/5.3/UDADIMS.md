### UDADIMS – Define the Dimensions of the User Defined Arguments {#kw-UDADIMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the dimensions of the User Defined Arguments (“UDA”) used by OPM Flow that can be applied to various connection, group, and well keywords in the [SCHEDULE](#kw-SCHEDULE) section. UDAs are defined by the [UDQ](#kw-UDQ) keyword that is used to specify values to be constants, [SUMMARY](#kw-SUMMARY) variables, as defined in [SUMMARY](#kw-SUMMARY) section, or a formula using various mathematical functions together with constants and [SUMMARY](#kw-SUMMARY) variables.

Although this keyword is read by OPM Flow and the [ACTION](#kw-ACTION) and [UDQ](#kw-UDQ) computational logic and calculations have been implemented, one should used caution using this facility as it may result in OPM Flow aborting.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NMUDA | NMUDA is a positive integer that defines the number of arguments in a [SCHEDULE](#kw-SCHEDULE) section keyword, that are replaced by numeric [UDQ](#kw-UDQ) values. | 0 |
| 2 | IGNORED | Not used and should be defaulted. | 1* |
| 3 | MXUDA | MXUDA is a positive integer that defines the maximum number of unique arguments in a keyword that are replaced by numeric UDA values. Note that MXUDA differs from NMUDA, for example: As MXUDA’s default value is 100 then this only needs to be increased  where the same UDA is used more than 100 times. | 100 |
| Notes: |  |  |  |
: UDADIMS Keyword Description {#tbl-5-50}
Note that OPM Flow has a more restricted [UDQ](#kw-UDQ) feature set than the commercial simulator, so not all options and functions are currently available.


#### Example


```
--
--       USER DEFINED ARGUMENT DIMENSIONS
--       NO.     NOT     TOTAL
--       ARGS    USED    UDQ
UDADIMS
         10       1*     10                                                    /
```


In the above example both NMUDA and MXUDA are set equal to ten.