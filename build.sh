source .venv_chimalli/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate