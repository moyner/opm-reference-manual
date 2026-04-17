### TPAMEPSS – Volumetric Strain versus Coal Solvent Concentration Tables {#kw-TPAMEPSS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

TPAMEPSS defines the volumetric strain versus coal solvent concentration tables, for when the Coal Bed Methane option has been activated via the [COAL](#kw-COAL) keyword, and PALM-MAN has been declared for the ROCKOPT variable on the [ROCKCOMP](#kw-ROCKCOMP) keyword; both keywords are in the [RUNSPEC](#kw-RUNSPEC) section. The Palmer-Mansoorii^[Palmer, I. and Mansoori, J. “How Permeability Depends on Stress and Pore Pressure in Coalbeds: A New Model,” paper SPE 52607, SPE Reservoir Evaluation & Engineering (1998) 1, No. 6, 539-544.] and ^[Clarkson, C.R., Pan, Z., Palmer, I. and Harpalani, S. "Predicting Sorption-Induced Strain and Permeability Increase With Depletion for Coalbed-Methane Reservoirs", SPE 114778-PA, SPE Journal (2010) 15, No. 1, 152–159.]  rock model is used to calculate the impact on pore volume and permeability due to rock compaction.

See also the ROCKPARMA keyword in the [PROPS](#kw-PROPS) section that defines the Palmer-Mansoori parameters.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.