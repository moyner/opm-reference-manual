### PYACTION – Define Python Based Action Conditions and Command Processing {#kw-PYACTION}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PYACTION keyword is part of OPM Flow’s Python scripting facility that loads a standard Python script file that can be used to define a series of conditions and actions as the simulation proceeds through time. The “included” Python script file is executed by the standard Python interpreter. Thus, OPM Flow’s Python scripting facility offers greater flexibility compared to the commercial simulator’s [ACTION](#kw-ACTION) series of keywords ([ACTION](#kw-ACTION), [ACTIONG](#kw-ACTIONG), [ACTIONR](#kw-ACTIONR), [ACTIONS](#kw-ACTIONS), [ACTIONW](#kw-ACTIONW) and [ACTIONX](#kw-ACTIONX)) that can apply Boolean conditional tests to variables at the field, group, region, well segment and well levels. Note that OPM Flow has also implemented the commercial simulator’s [ACTIONX](#kw-ACTIONX) keyword, but not the [ACTION](#kw-ACTION), [ACTIONG](#kw-ACTIONG), [ACTIONR](#kw-ACTIONR), [ACTIONS](#kw-ACTIONS) and [ACTIONW](#kw-ACTIONW) keywords, as the [ACTIONX](#kw-ACTIONX) keyword implements their functionality with greater flexibility. For a python class documentation and for further documentation and examples, also refer to the [OPM Online Python Documentation](https://opm.github.io/opm-python-documentation/index.html).

This keyword starts the definition of a PYACTION section that specifies the name of the action and a string indicating the number of times the action should be run; this is then followed by the name of the file containing the Python script. Note that unlike an [ACTIONX](#kw-ACTIONX) block that is terminated by the [ENDACTIO](#kw-ENDACTIO) keyword the PYACTION section has no terminating keyword.

Although this keyword is read by OPM Flow and the script processing has been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the PYACTION facility allows the user to implement complex functionality and the implementation was new for the 2020-04 release. Users should therefore use caution when using this facility.


::: {.callout-note}
This is an OPM Flow specific keyword for the simulator’s scripting facility using the standard Python interpreter, as such it gives more flexibility than the commercial simulator’s [ACTIONX](#kw-ACTIONX) keyword, although OPM Flow also supports this as well. The keyword should be considered experimental as details of the OPM Flow - Python interface might change for future releases. In particular, the current implementation is quite minimal; however, future releases are expected to add more entry points in the Schedule class which can be used to manipulate the reservoir model as the simulation progresses.  Users are encouraged to make suggestions for new features in this regard. The PYACTION keyword is a very powerful keyword and allows any piece of Python code to be included and run, including potentially malicious code. The important point is to scrutinize any PYACTION keyword in a deck you receive from other parties.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| PYACTION | PYACTION declares the start of a PYACTION Definition Section.  This is then followed by one record that defines the name of the action and a string indicating the number of times the action should be run; this is then followed by a second record indicating the file containing the Python script. | Not Applicable |  |
| 1-1 | ACTNAME | ACTNAME is a character sting of any length enclose in quotes that defines the name of this action definition. | None |
| 1-2 | ACTNSTEP | ACTNSTEP is a defined character string that indicates the number of times the action should be performed, and should be set to one of the following: Note that the FIRST_TRUE option is only supported for back compatibility when using the deprecated run() function style Python scripts. | SINGLE |
| 1-4 | / | Record terminated by a “/” | Not Applicable |
| 2-1 | FILENAME | A character string enclosed in quotes that defines the Python module/script file to read in and to be processed by OPM Flow. | None |
| 2-2 | / | Record terminated by a “/” | Not Applicable |
| Notes: |  |  |  |
: PYACTION Keyword Description {#tbl-12-60}
The PYACTION keyword is a result of combining two programming languages, the interactive Python interpreter and OPM Flow’s source code language C++. When combing two languages one extends and embeds one into the other. When extending Python with C++ the functionality implemented in C++ is made available to Python applications, when embedding Python in C++ one can call Python functions from within C++. The PYACTION keyword is based on embedding a Python interpreter in the C++ OPM Flow simulator, such that Python code is run from within the simulator.

Note that to use the PYACTION keyword OPM Flow must be built with embedded python enabled in opm-common/CMakeLists.txt.


```
option(OPM_ENABLE_EMBEDDED_PYTHON "Enable embedded python?" ON)

```

In order to fully benefit from the power of the PYACTION keyword one should familiarize oneself with the Python wrapper classes for the various OPM Flow C++ classes. These classes are essential to share the  simulator state with the PYACTION script. That is, the function provides the interface between the two programming languages.

To learn more about these classes you can use the pydoc utility, for example, to learn more about the SummaryState class, in a Linux terminal one would issue the following bash command:


```
bash% pydoc opm.io.sim.SummaryState

```

The Python script file (FILENAME in the PYACTION keyword) should be a standard Python module^[A Python module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.] that defines the PYACTION script and should consist of 100% pure Python.  The PYACTION Python module (FILENAME) is imported during processing of the input deck and as such this implies:

- Basic Python syntax checking is performed when the Python module (FILENAME) is read in.
- It is verified that the module has the correct format.

The syntax of the Python module (FILENAME) is given in @tbl-12-61 together with a description of the Python module opm_embedded.


| Python Script Definition |  |  |
| --- | --- | --- |
| # # OPM Flow PYACTION Module Script # import opm_embedded ecl_state = opm_embedded.current_ecl_state schedule = opm_embedded.current_schedule report_step = opm_embedded.current_report_step summary_state = opm_embedded.current_summary_state ... |  |  |
| No. | Name | Description |
| 1 | ecl_state | The ecl_state variable is an instance of the opm.io.ecl_state.EclipseState class which is initialized with all the static information in the simulation, for example the 3D grid properties and the PVT and saturation tables. This object can be read by the Python script but the available data should not be modified as any updates will not be passed back to the simulator. |
| 2 | schedule | The schedule variable is an instance of the opm.io.sched.Schedule class which has all the [SCHEDULE](#kw-SCHEDULE) information internalized (Schedule object). For a complete documentation of the available call points of opm.io.schedule.Schedule, we refer to [https://opm.github.io/opm-python-documentation/master/common.html#opm.io.schedule.Schedule](https://opm.github.io/opm-python-documentation/master/common.html#opm.io.schedule.Schedule). The most notable ones are: schedule.open_well(well_name, report_step) schedule.shut_well(well_name, report_step) schedule.stop_well(well_name, report_step) Which can be used to open, shut or stop a well at a particular report step (or at the current report step if the report_step argument is not specified), and: schedule.insert_keywords(kw) Which can be used to insert various keywords where kw is a string defining the keyword and associated records. For the 2024.10 release this has been tested with the following keywords: [BOX](#kw-BOX), [COMPSEGS](#kw-COMPSEGS), [ENDBOX](#kw-ENDBOX), [EXIT](#kw-EXIT), [FIELD](#kw-FIELD), [INCLUDE](#kw-INCLUDE), [GCONINJE](#kw-GCONINJE), [GCONPROD](#kw-GCONPROD), [GCONSUMP](#kw-GCONSUMP), [GEFAC](#kw-GEFAC), [GRUPTREE](#kw-GRUPTREE), [METRIC](#kw-METRIC), [MULTX](#kw-MULTX), [MULTX-](#kw-MULTX-), [MULTY](#kw-MULTY), [MULTY-](#kw-MULTY-), [MULTZ](#kw-MULTZ), [MULTZ-](#kw-MULTZ-), [NEXT](#kw-NEXT), [NEXTSTEP](#kw-NEXTSTEP), [WCONINJE](#kw-WCONINJE), [WCONPROD](#kw-WCONPROD), [WECON](#kw-WECON), [WEFAC](#kw-WEFAC), [WELOPEN](#kw-WELOPEN), [WELPI](#kw-WELPI), [WELTARG](#kw-WELTARG), [WGRUPCON](#kw-WGRUPCON), [WELSEGS](#kw-WELSEGS), [WELSPECS](#kw-WELSPECS), [WSEGVALV](#kw-WSEGVALV), [WLIST](#kw-WLIST), [WPIMULT](#kw-WPIMULT), [WTEST](#kw-WTEST), [WTMULT](#kw-WTMULT) This list is subject to change for future releases. The parsing strictness for the [ACTIONX](#kw-ACTIONX) and PYACTION keywords can be set using the --action-parsing-strictness command line option. If the default option --action-parsing-strictness="normal" has been set then OPM Flow will only apply keywords that have been tested, whereas if the option --action-parsing-strictness="low" has been set then OPM Flow will attempt to apply all keywords (however the simulation results may be incorrect). Adding additional call points to the opm.io.schedule.Schedule instance in order to update the Schedule object in more ways is an obvious candidate for improving the PYACTION functionality. |
| 3 | report_step | The current report step. |
| 4 | summary_state | The summary_state variable is an instance of the opm.io.sim.SummaryState class, the purpose of this class is to serve as a container for [SUMMARY](#kw-SUMMARY) variables that contain the simulation results; for example, the Field Oil Rate (FOPR) or a Well’s Water CuT (WWCT). See the [SUMMARY](#kw-SUMMARY) SECTION for a detailed description of the variables available. The summary_state variable will typically be the variable one will use to access the state of the simulation. For example, to check if the water cut in well OP01 exceeds 0.5 one would use the following statement: if summary_state.well_var("OP01", "WWCT") > 0.50: ... The summary_state variable can also be use to update variables including [UDQ](#kw-UDQ) variables, i.e: summary_state.update_well_var("OP01", "WUXX", 0.25) The above assigns a value of 0.25 to the well [UDQ](#kw-UDQ) variable WUXX for well OP01. |
: PYACTION Module Script Definition {#tbl-12-61}
See also the [PYINPUT](#kw-PYINPUT) and [PYEND](#kw-PYEND) keywords in the [GRID](#kw-GRID)^[Note the PYINPUT and PYEND keywords can be used in the GRID, EDIT, PROPS, SOLUTION, SUMMARY and SCHEDULE sections, but are described in the GRID section.] section which are also part of OPM Flow’s Python scripting facility, that process standard Python commands that can be used to manipulate and define the simulators input parameters during processing of the input deck.  The main purpose of the facility is to script the construction of the various keywords.


#### Examples

The first example checks if well OP01 has a water cut greater than 0.8 and if so then the well is shut in. In the input deck we would have:


```
--
--       START OF PYACTION SECTION
--
--       ACTNAME       ACTNSTEP
PYACTION
         'MAXWCUT'     'UNLIMITED'                          /
         'pthon/script/MAXWCUT.py'                          /
--
--       END OF PYACTION SECTION
--
```

And then in the Python module file 'pthon/script/MAXWCUT.py' one would have:


```
#
# OPM Flow PYACTION Module Script
#
import opm_embedded
schedule = opm_embedded.current_schedule
summary_state = opm_embedded.current_summary_state

if (not 'setup_done' in locals()):
    executed = False
    setup_done = True

if (not executed and summary_state.well_var("OP1", "WWCT") > 0.80):
    message = "Well OP01 has been shut-in due to WWCT > 0.80\n"
    opm_embedded.OpmLog.info(message)
    schedule.shut_well("OP1")
    executed = True

```

Note how the 'executed' variable is used to ensure that the action is only executed once the first time the water cut is greater than 0.8.

The next example is based on the first example from the [ACTIONX](#kw-ACTIONX) keyword ([ACTIONX](#kw-ACTIONX) – Define Action Conditions and Command Processing). The Python script first checks if the field’s water production is greater than 30,000 stb/d, and if not returns control back to the simulator. If the field water production is greater than 30,000 stb/d then the script uses a Python variable count to keep track of the number of times the script has been executed, and then sorts the wells from high water cut to low, via the wct_list variable, and then shuts in the worst offending well. If a well is shut-in the count variable is increased by one and control is passed back to the simulator. The script is executed as maximum of ten times.


```
--
--       START OF PYACTION SECTION
--
--       ACTNAME       ACTNSTEP
PYACTION
         'WSHUTIN'     'UNLIMITED'                          /
         'pthon/script/WSHUTIN.py'                          /
--
--       END OF PYACTION SECTION
--
```

And then in the Python module file 'pthon/script/WSHUTIN.py' one would have:


```
#
# OPM Flow PYACTION Module Script
#
import opm_embedded

schedule = opm_embedded.current_schedule
summary_state = opm_embedded.current_summary_state

if (not 'setup_done' in locals()):
    execution_counter = 0
    setup_done = True

if (execution_counter < 10 and summary_state["FWPR"] >= 30000):
    #
    # Get Sorted Well List
    #
    wct_list = sorted( [ (well, summary_state.well_var(well, "WWCT"))
                       for well in summary_state.wells], reverse=True )
    #
    # Shut-in Well with Highest Water Cut
    #
    well, wwct = wct_list[0]
    if wwct > 0:
        schedule.shut_well(well)
        execution_counter += 1

```

Note that by using PYACTION it makes sense to combine the [UDQ](#kw-UDQ) variable into the PYACTION statement, like shown in the example above, although this is not necessary, as one could in principle use a normal [UDQ](#kw-UDQ) statement and then access the variables in the PYACTION script using the summary_state variable.

The final example checks to see if the field’s gas rate is below 600 MMscf/d and if the simulation time is greater that January 1, 2030. If it is, then compression is installed by re-setting all the gas producing well’s THP and BHP pressures to 450 psia and 300 psia respectively. In addition all gas wells currently shut-in are tested to see if they can be opened up under the new THP and BHP constraints.


```
--
--       START OF PYACTION SECTION
--
--       ACTNAME       ACTNSTEP
PYACTION
         'WSHUTIN'     'UNLIMITED'                          /
         'pthon/script/PHASE3.py'                           /
--
--       END OF PYACTION SECTION
--
```

And then in the Python module file 'pthon/script/PHASE3.py' one would have:


```
#
# OPM Flow PYACTION Module Script
#
import datetime
import opm_embedded

schedule = opm_embedded.current_schedule
summary_state = opm_embedded.current_summary_state

if (not 'setup_done' in locals()):
    executed = False
    setup_done = True

if not executed:
    sim_time = schedule.start +
               datetime.timedelta( seconds = summary_state.elapsed() )

    if (summary_state["FGPR"] < 600000 and
        sim_time > datetime.datetime(2030, 1, 1)):
        #
        # Do WELTARG and WTEST action
        #
        ...
        executed = True

```

Note how the current simulation time (sim_time) is evaluated from the simulation start time (schedule.start) and elapsed time (summary_state.elapsed); and how it is compared with 00:00 on 1 January 2030 using the Python datetime module.