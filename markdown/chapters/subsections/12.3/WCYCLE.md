### WCYCLE – Define Automatic Well Opening and Closing Cycling Parameters


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WCYCLE keyword defines automatic well opening and closing cycling parameters. These are used to model for example “Huff and Puff” cyclic steam injection in heavy oil reservoirs or Water-Alternating-Gas (“WAG”) processes in enhanced oil recovery modeling. The keyword defines specific time periods for automatically cycling wells on and off. For example in a WAG scheme the water injection wells would have one set of cycling parameters and the gas injection wells another, such that only one type of well is active at a time.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well automatic cycling parameters are being defined. Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 4 | ONTIME | A real positive value that defines the length of time for the on period. The well will be turned off at the beginning of the first time step after the on period has elapsed. If ONTIME is zero or negative then the well will not be turned on by the automatic well cycling. | 0.0 |
| day | day | hour |  |
| 5 | OFFTIME | A real positive value that defines the length of time for the off period. If the well was turned off by automatic cycling then it will be turned on at the beginning of the first time step after the off period has elasped. If the well was turned off other than by automatic cycling then the well will remain turned off. If OFFTIME is zero or negative then the well will not be turned on by the automatic well cycling. | 0.0 |
| day | day | hour |  |
| 6 | STARTTIME | A real positive value that defines the length of time for the start-up period during which the well efficiency factor will be ramped up. The start-up period begins at the start of the on period. The well’s efficiency factor is ramped up linearly from zero at the start of the on period to the value specified previously by the WEFAC keyword after the start-up period has elasped. The well efficiency factor to apply during each time step is linearly interpolated based on the time at the end of the time step. If the time step size is small compared with STARTTIME then the rate will be ramped up gradually. Whereas, if the time step size is greater than STARTTIME then the rate will ramp up instantaneously potentially causing convergence problems. | 0.0 |
| day | day | hour |  |
| 7 | MAXTS | A real positive value that defines the maximum time step length when the well is turned on by automatic cycling. This overrides the standard maximum time step length. This can help to reduce potential convergence problems caused when a high rate well is opened. If MAXTS is zero then the standard maximum time step length applies. | 0.0 |
| day | day | hour |  |
| 13 | CTRLTS | A defined character string that specifies whether the time steps should be controlled to coincide exactly with the automatic cycling times for this well. CTRLTS should be set to one of the following: | NO |
| Notes: |  |  |  |

*Table 12.3.258.1: WCYCLE Keyword Description*


#### Example

The following example defines the cycle lengths for a Water-Alternating-Gas injection scheme with a water-gas slug length ratio of 1:2, and initiates automatic cycling in the water injection well. A maximum time step of 5 days has been specified following the start of each injection period. The simulation then proceeds to the end of the first water injection cycle when automatic cycling is initiated in the gas injection well.


```
--
-- AUTOMATIC CYCLING OF WELLS ON AND OFF
--
WCYCLE
--WELL     ON       OFF      STARTUP  STARTUP  CTRL
--NAME     PERIOD   PERIOD   TIME     MAXTS    TIMESTEP
  I01W     30.0     60.0     1*       5.0      YES  /
  I01G     60.0     30.0     1*       5.0      YES  /
--
-- OPEN WELLS
--
WELOPEN
--WELL     OPEN
--NAME     SHUT
  I01W     OPEN /
  I01G     SHUT /
/
--
-- REPORT STEPS
--
TSTEP
  30.0     /
--
-- OPEN WELLS
--
WELOPEN
--WELL     OPEN
--NAME     SHUT
  I01G     OPEN /
/
```


Note that the wells initially need to be opened manually in order to start the automatic cycling. In addition, this needs to be done at the correct times to ensure that the water and gas injection wells are syncronised.
