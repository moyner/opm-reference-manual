### ENDINC – Define the End of an Include File {#kw-ENDINC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword marks the end of an include file specified on the [INCLUDE](#kw-INCLUDE) keyword. When the ENDINC keyword is encountered in the [INCLUDE](#kw-INCLUDE) file, input data is read from the next keyword in the current file. Any keywords and data after the ENDINC keyword in the [INCLUDE](#kw-INCLUDE) file are ignored.

There is no data required for this keyword.


#### Example


```
-- ------------------------------------------------------------------------------
-- SCHEDULE SECTION - 2006-01-01
-- ------------------------------------------------------------------------------
RPTSCHED
'WELLS=2'    'WELSPECS'    'CPU=2'     'FIP=2'                                 /

DATES
 1  JAN   2006  /
/

RPTSCHED
'NOTHING'                                                                      /

DATES
 1  APR   2006  /
 1  JLY   2006  /
 1  OCT   2006  /
/
       ECHO
--
-- ******************************************************************************
-- END OF INCLUDE FILE PROCESSING
-- ******************************************************************************
ENDINC
-- ------------------------------------------------------------------------------
-- SCHEDULE SECTION - 2007-01-01
-- ------------------------------------------------------------------------------
RPTSCHED
'WELLS=2'    'WELSPECS'    'CPU=2'     'FIP=2'                                 /

DATES
 1  JAN   2007  /
/
```


In the above example OPM Flow will process the data up to October 1, 2006 only, and return control to the file that called the [INCLUDE](#kw-INCLUDE) keyword, and then continue processing the input files. All keywords after the ENDINC keyword in the [INCLUDE](#kw-INCLUDE) FILE will not be read or processed.