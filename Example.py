# from Core.Execution import Execution
# from Core.Misc import load_from_file, SaveAs
import time

from Core.Misc import SaveAs
from Core.Report import Report
from Core.Scenario import Scenario

# from Core.Scenario import Scenario
# from Core.Source import Source

if __name__ in '__main__':
    report = Report(name="Example Report",
                    description="Example Description",
                    properties={'Version': 1.0, 'Core': None},
                    parameters={'Param 1': 'Example Param', 'Age': 15})
    report.l_start("Message Indentation")
    try:
        report.info("Info message")
        report.info("Info message")
        report.info("Info message")
        report.info("Info message")
        report.info("Info message")
    finally:
        report.l_stop()

    time.sleep(1)

    report1 = Report(name="Example Second Report",
                     description="Example Second Description",
                     properties={'Version': 2.0, 'Core': None},
                     parameters={'Param 1': 'Example Param 2', 'Age': 15})
    report1.l_start("Message Indentation")
    try:
        report1.info("Info message")
        report1.info("Info message")
        report1.l_start("Message Indentation")
        try:
            report1.info("Info message")
            report1.info("Info message")
            report1.err("ERR!")
            report1.info("Info message")
            report1.info("Info message")
            report1.l_start("Message Indentation")
            try:
                report1.info("Info message")
                report1.info("Info message")
                report1.fail("FAIL!")
                report1.info("Info message")
                report1.info("Info message")
                report1.l_start("Message Indentation")
                try:
                    report1.info("Info message")
                    report1.info("Info message")
                    report1.warn("WARN!")
                    report1.info("Info message")
                    report1.info("Info message")
                    report1.l_start("Message Indentation")
                    try:
                        report1.info("Info message")
                        report1.info("Info message")
                        report1.success("SUCCESS!")
                        report1.info("Info message")
                        report1.info("Info message")
                        report1.l_start("Message Indentation")
                        try:
                            report1.info("Info message")
                            report1.info("Info message")
                            report1.info("Info message")
                            report1.info("Info message")
                            report1.info("Info message")
                            report1.img("example.PNG", ';)')
                        finally:
                            report1.l_stop()
                        report1.info("Info message")
                        report1.info("Info message")
                    finally:
                        report1.l_stop()
                    report1.info("Info message")
                    report1.info("Info message")
                finally:
                    report1.l_stop()
                report1.info("Info message")
                report1.info("Info message")
            finally:
                report1.l_stop()
            report1.info("Info message")
            report1.info("Info message")
        finally:
            report1.l_stop()
        report1.info("Info message")
        report1.info("Info message")
        report1.info("Info message")
    finally:
        report1.l_stop()

    report2 = Report(name="THIRD Report",
                     description="THIRD Description",
                     properties={'Version': 3.0, 'Core': None},
                     parameters={'Param 1': 'Example Param 2', 'Age': 35})
    report2.info("This is report2")
    report3 = Report(name="FOURTH Report",
                     description="FOURTH Description",
                     properties={'Version': 4.0, 'Core': None},
                     parameters={'Param 1': 'Example Param 2', 'Age': 35})
    report3.warn("This is report3!!!")
    scenario = Scenario(name="Nested2 Scenario", children=[report2, report3],
                        properties={'Nested2 Scenario property': 'Prop val'},
                        parameters={'Nested 2Scenario param': 'Param val'})

    report4 = Report(name="FIFTH Report",
                     description="FIFTH Description",
                     properties={'Version': 5.0, 'Core': None},
                     parameters={'Param 1': 'Example Param 2', 'Age': 35})
    report4.err("This is report4!!!")

    scenario1 = Scenario(name="Example1 Scenario", children=[report, report1, scenario, report4],
                         properties={'Scenario1 property': 'Prop val'},
                         parameters={'Scenario1 param': 'Param val'})
    scenario1.save_to_file(save_as=SaveAs.JS, file_abs='Templates/Scenario.js')

    # scenario = Scenario("Stam Scenario", children=[report])
    # source = Source("Stam Source", [scenario])
    # execution = Execution("Stam Execution", [source])
    # print(f'Execution: {execution}')
    # execution.save_to_file(file_abs='Templates\\Execution.js', save_as=SaveAs.JS)
    #
    # print("============================\n"
    #       "============================\n"
    #       "========= Loading ==========\n"
    #       "============================\n"
    #       "============================")
    #
    # report = load_from_file('Templates\\Report.json', Report)
    # print(f'Loaded Report: {report}')
    #
    # execution = load_from_file('Templates\\Execution.json', Execution)
    # print(f'Loaded Execution: {execution}')
