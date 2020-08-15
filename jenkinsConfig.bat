
VER
echo "Global python version"
C:/Users/deb/AppData/Local/Programs/Python/Python37-32/python --version
echo "Global PIP version"
C:/Users/deb/AppData/Local/Programs/Python/Python37-32/Scripts/pip --version
echo "Creating venv"

=

::C:/Users/deb/AppData/Local/Programs/Python/Python37-32/python -m venv "C:/Program Files (x86)/Jenkins/workspace/pythonTest/venv"
echo "importing requirements"
"C:/Program Files (x86)/Jenkins/workspace/pythonTest/venv/Scripts/pip" install -r "C:/Program Files (x86)/Jenkins/workspace/pythonTest/requirements.txt"
REM echo "acitvating venv"
REM "C:/Program Files (x86)/Jenkins/workspace/pythonTest/venv/Scripts/activate"
echo "Executing pytest"
"C:/Program Files (x86)/Jenkins/workspace/pythonTest/venv/Scripts/python" -m pytest "C:/Program Files (x86)/Jenkins/workspace/pythonTest/Tests/Selenium/test_YT.py"
