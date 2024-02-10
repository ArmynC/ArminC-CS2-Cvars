#### Outputing the path of sounds resource

* Get the latest [ReosurceFileFormat](https://github.com/ValveResourceFormat/ValveResourceFormat) as Source2Viewer.exe.
* Set it up and open **pak01_dir.vpk** file found in `\...\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo`.
* Right click on **sounds** folder and export it on Desktop.
* Make sure you have [Python installed](https://www.python.org/downloads/) and open the Terminal, where you should *cd* to the folder containing the script and extracted sounds then input the command as follows: `python generate_cvar.py sounds`.
* The file will be outputed in the same path as your script.