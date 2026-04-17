### WSEGDFPA – Define Multi-Segment Well Drift Flux Slip Model Parameters {#kw-WSEGDFPA}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, WSEGDFPA, enables modification of a multi-segment well’s drift flux slip model default parameters used by the WSEGDFMA keyword in the [SCHEDULE](#kw-SCHEDULE) section to define the model. A slip model^[Shi, H., Holmes, J.A., Durlofsky, L. J., Aziz, K., Diaz, L. R., Alkaya, B., and Oddie, G. “Drift-Flux Modeling of Two-Phase Flow in Wellbores,” paper SPE 84228, Society of Petroleum Engineers Journal (2005) 10, No. 1, 24-33; also presented as “Drift-Flux Modeling of Multiphase Flow in Wellbores,” at the SPE Annual Technical Conference and Exhibition, Denver, Colorado, USA(October 5-8, 2003).] and ^[Shi, H., Holmes, J.A., Diaz, L. R., Durlofsky, L. J., and Aziz, K. “Drift-Flux Parameters for Three-Phase Steady-State Flow in Wellbores,” paper SPE 89836, Society of Petroleum Engineers Journal(2005) 10, No. 2, 130-137; also presented at the SPE Annual Technical Conference and Exhibition, Houston, Texas, USA (September 26-29, 2004).] enables the different phases in the wellbore to flow at different velocities, for example gas will flow up the tubing at a higher velocity than oil and water. The option is activated by the FLOWOPT parameter on the [WELSEGS](#kw-WELSEGS) keyword in the [SCHEDULE](#kw-SCHEDULE) section; however, the slip model flow calculation is not available in OPM Flow.

See also the [WSEGDFIN](#kw-WSEGDFIN) keyword that sets the slip model’s input parameters and the [WSEGDFMD](#kw-WSEGDFMD) keyword that sets which drift flux slip model should be used. Note if the WSEGDFPA keyword is used than it must be placed after the [WSEGDFMD](#kw-WSEGDFMD) keyword, but before the [WELSEGS](#kw-WELSEGS) keyword that defines a multi-segment well. All the aforementioned keywords are in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.