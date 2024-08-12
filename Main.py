from LogModel.Execution import Execution
from LogModel.Misc import SaveAs
from LogModel.Scenario import Scenario
from LogModel.Source import Source
from LogModel.Report import Report

if __name__ in '__main__':
    execution = Execution()

    source = Source(name="Server Machine")

    scenario = Scenario(
        name="Server Initialization",
        properties={
            'Stam propr key': 'Stam prop val'})

    report = Report(
        name="Init This Thing",
        description="Initializes this thing",
        properties={
            'Version': 1.0,
            'Model': None},
        parameters={
            'Name': 'Ah Yakar',
            'Age': 15})

    report.l_start("Test initialization")
    try:
        report.bold("Sup ah yakar")
        report.info("Sup ah yakar")
        report.info("Sup ah yakar")
        report.info("Sup ah yakar")
    finally:
        report.l_stop()
    report.l_start("Test - Actual Test")
    try:
        report.info("Sup ah yakar")
        report.info("Sup ah yakar")
        report.l_start("Stam nested level")
        try:
            report.info("Sup ah yakar")
            report.info("Sup ah yakar")
            report.info("Sup ah yakar")
            report.l_start("Stam nested level")
            try:
                report.info("Sup ah yakar")
                report.info("Sup ah yakar")
                report.info("Sup ah yakar")
                report.l_start("Stam nested level")
                try:
                    report.info("Sup ah yakar")
                    report.info("Sup ah yakar")
                    report.info("Sup ah yakar")
                    report.l_start("Stam nested level")
                    try:
                        report.info("Sup ah yakar")
                        report.info("Sup ah yakar")
                        report.err("err ah yakar")
                        report.info("Sup ah yakar")
                    finally:
                        report.l_stop()
                    report.info("Sup ah yakar")
                finally:
                    report.l_stop()
                report.info("Sup ah yakar")
            finally:
                report.l_stop()
            report.info("Sup ah yakar")
        finally:
            report.l_stop()
        report.info("Sup ah yakar")
        report.info("Sup ah yakar")
    finally:
        report.l_stop()
    report.l_start("Test Cleanup")
    try:
        report.info("Sup ah yakar")
        report.info("Sup ah yakar")
        report.info("Sup ah yakar")
        report.warn("Warn ah yakar")
    finally:
        report.l_stop()
    scenario.append_child(report)
    source.append_child(scenario)
    execution.append_source(source)

    report.save_to_file(save_as=SaveAs.JSON, file_abs='Templates/Report.json')
    report.save_to_file(save_as=SaveAs.JS, file_abs='Templates/Report.js')
