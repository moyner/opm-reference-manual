### MESSAGES – Define Message Print Limits and Stop Limits


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MESSAGES keyword defines the print and stops levels for various messages. The “print limits” set the maximum number of messages that will be printed, after which no more messages will be printed and the “stop limits” terminate the run when these limits are exceeded. There are six levels of message that increase in severity from informative all the way to programming errors, as outlined in Table 4.5.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | PRTSMESG | An integer defining the maximum number of MESSAGE type messages to be printed after which this type of message stops printing. | 1,000,000 |
| 2 | PRTSCOMT | An integer defining the maximum number of COMMENT type messages be printed after which this type of message stops printing. | 1,000,000 |
| 3 | PRTSWARN | An integer defining the maximum number of WARNING type messages be printed after which this type of message stops printing. | 10,000 |
| 4 | PRTSPROB | An integer defining the maximum number of PROBLEM type messages to be printed after which this type of message stops printing. | 100 |
| 5 | PRTSERRS | An integer defining the maximum number of ERROR type messages to be printed after which this type of message stops printing. | 100 |
| 6 | PRTSBUGS | An integer defining the maximum number of BUG type messages to be printed after which this type of message stops printing. | 100 |
| 7 | STOPMESG | An integer defining the maximum number of MESSAGE type messages to be printed after which OPM Flow terminates the run. Not used by OPM Flow. | 1,000,000 |
| 8 | STOPCOMT | An integer defining the maximum number of COMMENT type messages to be printed after which OPM Flow terminates the run. Not used by OPM Flow. | 1,000,000 |
| 9 | STOPWARN | An integer defining the maximum number of WARNING type messages to be printed after which OPM Flow terminates the run. Not used by OPM Flow. | 10,000 |
| 10 | STOPPROB | An integer defining the maximum number of PROBLEM type messages to be printed after which OPM Flow terminates the run. Not used by OPM Flow. | 100 |
| 11 | STOPERRS | An integer defining the maximum number of ERROR type messages to be printed after which OPM Flow terminates the run. Not used by OPM Flow. | 10 |
| 12 | STOPBUGS | An integer defining the maximum number of BUG type messages to be printed after which OPM Flow terminates the run. Not used by OPM Flow. | 1 |
| 13 | PRTGRPMS | An integer defining the maximum number of GROUP MESSAGE type messages to be printed after which this type of message stops printing. Not used by OPM Flow. | 10 |
| Notes: |  |  |  |

*Table 4.5: MESSAGES Keyword Description*


#### Example


```
--
--       MESS  COMMT WARN  PROBL ERROR BUG   MESS COMMT WARN  PROBL ERROR BUG
--       LIMIT LIMIT LIMIT LIMIT LIMIT LIMIT STOP STOP  STOP  STOP  STOP  STOP
MESSAGES
         1*    1*    1*    1500  1*    1*    1*   1*    1*    1000  1*    1*   /

```

The above example sets the PROBLEM type message print limit to 1,500 and the stop limit to 1,000.
