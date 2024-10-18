# Balogan
Visualize python logs over a simple web page.

## Usage
- `log(msg, severity=INFO)` - Log a message (severities: `NA/INFO/SUCCESS/WARNING/FAILURE/ERROR`).
- `info(msg)` - Log an info message (light-gray).
- `bold(msg)` - Log a bold message (bold light-gray).
- `success(msg)` - Log a success message (bold green).
- `warn(msg)` - Log a warning message (bold yellow).
- `fail(msg)` - Log a failure message (bold orange).
- `err(msg)` - Log an error message (bold red).
- `img(addr, alt)` - Log an image.
- `link(addr, replace)` - Log an address as link (href).
- `l_start(msg)` - Start a new log level (separated from other levels).
- `l_stop()` - Mark the end of the current level.

## Example
The following piece of code:
```
report = Report(name="Example Report",
                description="Example Description",
                properties={'Version': 1.0, 'Core': None},
                parameters={'Param 1': 'Example Param', 'Age': 15},
                save_on_exit=True)
report.l_start("Message Indentation")
try:
    report.info("Info message")
    report.info("Info message")
    report.info("Info message")
    report.warn("WARNING!")
finally:
    report.l_stop()
```
Will result with:
- Application stdout (set `Report(verbose=False)` to disable):
```
[17:39:48 | LEVEL +]: Message Indentation
=====================================
[17:39:48 | INFO   ]: Info message
[17:39:48 | INFO   ]: Info message
[17:39:48 | INFO   ]: Info message
[17:39:48 | WARNING]: >> WARNING! <<
[17:39:48 | LEVEL -]: ==========================

Saving report to "Templates/Report.js"
```
- Page:<br>
![image](https://github.com/user-attachments/assets/5ec067e1-609d-4a84-93c1-51bafdea01f3)
