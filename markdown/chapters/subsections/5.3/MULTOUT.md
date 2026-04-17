### MULTOUT – Activate the Non-Unified Multiple Output File Option


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword switches on the Multiple Output Files option for all output files. Similar to the commercial simulator, OPM Flow has various options for reading various input files and writing the resulting OPM Flow  output files as described in Table 5.24.


| Process | Keyword | Description | Files |
| --- | --- | --- | --- |
| Input | FMTIN | A character string that defines the input files to be formatted as ASCII i.e. text files, as oppose to binary files.  The input deck file is always of this type. The option relates to the OPM Flow derived files that used as input, for  for example when restarting from another case. If the keyword is omitted then the default is for binary file input. | *.FEGRID *.FINSPEC *.FINIT *.FRSSPEC *.FUNRST *.FSMSPEC *.FUNSMRY |
| MULTIN | A character string that defines the input files to be non-unified multiple files, as opposed to unified files. In this case, one file is read in per  reporting time step, as opposed to all time steps reports being read from  one file. If the keyword is omitted then the default is for one file per reporting time step. | *.RSSPEC *.X0001 *.SMSPEC *.S0001 |  |
| UNIFIN | A character string that defines the input files to be unified files, as opposed to non-unified multiple files. A unified file is a single file containing output for each reporting time step.  For this option a single summary file and a single restart file will be read. If the keyword is omitted then the default is for one file per reporting time step. | *.RSSPEC *.UNRST *.SMSPEC *.UNSMRY |  |
| Output | FMTOUT | A character string that sets all output files to be formatted as ASCII i.e. text files, as opposed to binary files. The *.PRT, *.LOG and *.DBG files are always of this type. The option relates to the OPM Flow output files only. In this case the files will be portable across operating systems, but will also be very large in terms of hard disk space. For this reason it is recommend that the default option is used so that binary files are outputted. If the keyword is omitted then the default is for binary file input. | *.FEGRID *.FINSPEC *.FINIT *.FRSSPEC *.FUNRST *.FSMSPEC *.FUNSMRY |
| MULTOUT | A character string that defines the output files to be non-unified multiple files, as opposed to unified files. In this case, one file is written for each reporting time step, as opposed to all time steps reports being written in one file. If the keyword is omitted then the default is for one file per reporting time step. | *.RSSPEC *.X0001 *.SMSPEC *.S0001 |  |
| UNIFOUT | A character string that defines the output files to be unified files, as opposed to non-unified multiple files. A unified file is a single file containing output for each reporting time step. Here a single summary file and a single restart file will be generated, as opposed to one file per report time step. If the keyword is omitted then the default is for one file per reporting time step. | *.RSSPEC *.UNRST *.SMSPEC *.UNSMRY |  |
| Notes: |  |  |  |

*Table 5.24: MULTOUT Keyword Description*


There is no data required for this keyword.

See also OPM FLOW OUTPUT FILE FORMATS for a more detailed description of the various file types (ASCII or binary) and file structure formats (unified or non-unified formats).


#### Example


```
--
--       ACTIVATE THE MULTIPLE OUTPUT FILES OPTION
--
MULTOUT
```


The above example switches on the multiple output file option.
