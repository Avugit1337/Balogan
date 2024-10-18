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
- `html(code)` - Log message as HTML code.
- `l_start(msg)` - Start a new log level (separated from other levels).
- `l_stop()` - Mark the end of the current level.

## Example
The following piece of code:
```python
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
    report.html("<span style=\"color: pink;\">THIS IS PURE HTML</span>")
finally:
    report.l_stop()
```
Will result with:
- Application stdout (set `Report(verbose=False)` to disable):
```
[18:20:34 | LEVEL +]: Message Indentation
=====================================
[18:20:34 | INFO   ]: Info message
[18:20:34 | INFO   ]: Info message
[18:20:34 | INFO   ]: Info message
[18:20:34 | WARNING]: >> WARNING! <<
[18:20:34 | HTML   ]: <span style="color: pink;">THIS IS PURE HTML</span>
[18:20:34 | LEVEL -]: ==========================

Saving report to "Templates/Report.js"
```
- Page:<br>
![image](https://github.com/user-attachments/assets/18ad6031-9067-404f-9536-e7b14b729fe5)

