### SUMTHIN – Define SUMMARY DATA Reporting Time Steps

This keyword defines a time interval for writing out the SUMMARY data to the SUMMARY file and the
      Atgeirr Rasmussen
      2017-09-22T12:19:56.742970000
      AFR
      We don’t write any RSM files (what are those?)
     RSM
      David Baxendale
      2017-10-02T18:55:45.272000000
      DBx
      Reply to Atgeirr Rasmussen (09/22/2017, 12:19): "..."
      We should write RSM files, as they contain the production and injection data from the SUMMARY files in ASCII format. Engineers normally load this file into EXCEL to generate plots and economic production forecasts.
      file, if the RUNSUM keyword has been has also been activated in the SUMMARY section. Only the data for the first time step in the time interval is written out and the other time steps are skipped until the next time interval.  This enable the size of the SUMMARY files to be reduced depending on the size of the time interval. However, the keyword will produce irregular time steps reports of the SUMMARY data.

See SUMTHIN – Define SUMMARY Data Reporting Time Steps in the SUMMARY section for a full description.
