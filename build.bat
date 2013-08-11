@ECHO OFF

set OSGEO4W_ROOT=C:\OSGeo4W
PATH=%OSGEO4W_ROOT%\bin;%PATH%
for %%f in (%OSGEO4W_ROOT%\etc\ini\*.bat) do call %%f

pyrcc4 -o resources_rc.py resources.qrc