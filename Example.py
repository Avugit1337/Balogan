from Core.Execution import Execution
from Core.Misc import load_from_file, SaveAs
from Core.Report import Report
from Core.Scenario import Scenario
from Core.Source import Source

if __name__ in '__main__':
    report = Report(
        name="Init This Thing", description="Initializes this thing", properties={'Version': 1.0, 'Core': None},
        parameters={'Name': 'Ah Yakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr', 'Age': 15}, verbose=False)
    report.l_start("Message Indentation")
    try:
        report.info("Info message")
        report.info("Info message")
        report.info("Info message")
        report.warn("WARNING YOOOOOOOOOOOOOOOOOOOOOOOOOO!")
    finally:
        report.l_stop()

    report.l_start("Message Indentation")
    try:
        report.info("Info message")
        report.info("Info message")
        report.l_start("Message Indentation")
        try:
            report.info("Info message")
            report.info("Info message")
            report.l_start("Message Indentation")
            try:
                report.info("Info message")
                report.info("Info message")
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.l_start("Message Indentation")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("MESSAGE\nmessage")
                    report.link("https://google.com", "Link To Google")
                finally:
                    report.l_stop()
                report.info("Info message")
                report.info("MESSAGE\nmessage")
                report.link("https://google.com", "Link To Google")
            finally:
                report.l_stop()
            report.info("Info message")
            report.info("MESSAGE\nmessage")
            report.link("https://google.com", "Link To Google")
        finally:
            report.l_stop()
        report.info("Info message")
        report.info("Info message")
        report.img('example.PNG', "Test Image")
    finally:
        report.l_stop()
    report.info("Info message")
    report.info("Info message")
    report.err("Info message")
    report.bold("Bold message")

    print(f'Report: {report}')
    report.save_to_file(file_abs='Templates\\Report.js', save_as=SaveAs.JS)

    scenario = Scenario("Stam Scenario", children=[report])
    source = Source("Stam Source", [scenario])
    execution = Execution("Stam Execution", [source])
    print(f'Execution: {execution}')
    execution.save_to_file(file_abs='Templates\\Execution.js', save_as=SaveAs.JS)

    print("============================\n"
          "============================\n"
          "========= Loading ==========\n"
          "============================\n"
          "============================")

    report = load_from_file('Templates\\Report.json', Report)
    print(f'Loaded Report: {report}')

    execution = load_from_file('Templates\\Execution.json', Execution)
    print(f'Loaded Execution: {execution}')
