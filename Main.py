from LogModel.Report import Report

if __name__ in '__main__':
    report = Report(name="Init This Thing",
                    description="Initializes this thing",
                    properties={'Version': 1.0, 'Model': None},
                    parameters={'Name': 'Ah YakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrYakarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr', 'Age': 15})

    report.l_start("Message Status")
    try:
        report.info("Info message")
        report.bold("Bold message")
        report.success("Success message")
        report.warn("Warning message")
        report.fail("Failure message")
        report.err("Error message")
        report.img('example.PNG', "Example Image")
        report.link('https://google.com', 'Link to "https://google.com"')
        report.html('<span style="background-color: yellow; color: red;">This is pure html code</span>')
    finally:
        report.l_stop()

    report.l_start("Message Indentation")
    try:
        report.info("Info message")
        report.info("Info message")
        report.l_start("Nested Level")
        try:
            report.info("Info message")
            report.info("Info message")
            report.info("Info message")
            report.l_start("Nested Level")
            try:
                report.info("Info message")
                report.info("Info message")
                report.info("Info message")
                report.l_start("Nested Level")
                try:
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.info("Info message")
                    report.warn("Warning message with two lines\nNext line")
                    report.info("Info message")
                    report.l_start("Nested Level")
                    report.l_stop()
                finally:
                    report.l_stop()
                report.info("Info message")
            finally:
                report.l_stop()
            report.info("Info message")
        finally:
            report.l_stop()
        report.info("Info message")
        report.info("Info message")
    finally:
        report.l_stop()

    report.l_start("Message Indentation")
    try:
        report.info("Info message")
        report.info("Info message")
        report.info("Info message")
    finally:
        report.l_stop()

    report.l_start("Message Indentation")
    try:
        report.info("Info message")
        report.info("Info message")
        report.info("Info message")
    finally:
        report.l_stop()
