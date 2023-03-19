An python script which reads the slicer version from the gcode and put the line: "; slicer_version = <your slicer version" at the end of the gcode.
This line can be used with the OctoPrint plugin: "ExtraFileInfo".The python script is converted to an .exe with "PyInstaller".
Currently only PrusaSlicer is supported.

## How to use
### PrusaSlicer:
    1. download "SlicerVersion.exe" to an folder of your choosing.
    2. In PrusaSlicer under "Print settings" -> "Output options", add "<Your path\SlicerVersion.exe" to "Post-processing scripts".
![image](https://user-images.githubusercontent.com/10145631/226166141-4d2f764f-84df-4912-8c55-64bacb176417.png)

### ExtraFileInfo plugin:
    1. add a key "slicer_version".
![image](https://user-images.githubusercontent.com/10145631/226165438-656aaddd-6c2d-416e-9327-90be0a049497.png)



#### References:
- Link to PyInstaller:    https://pypi.org/project/pyinstaller/
- Link to ExtraFileInfo:  https://plugins.octoprint.org/plugins/extrafileinfo/
