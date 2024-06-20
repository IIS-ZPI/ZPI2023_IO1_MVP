# MVP
## Tech Stack
- Python with libraries:
    - requests version 2.31.0 
    - pytest version 7.4.0
    - numpy version 1.26.4 
    - freezegun version 1.1.0 
    - PySide6 version 6.7.1 
    - matplotlib version 3.9.0 
    - pyinstaller version 6.8.0
## Local Preview
1. Install Python (install at least version 3.12)
2. Install all dependencies (python libraries in [.requirements.txt](requirements.txt))
    - with <b> pip install -r [.requirements.txt](requirements.txt) <b> command
    - with <b> pip install "module_name" <b> command for every module in [.requirements.txt](requirements.txt)
    - using specific IDE tools for example PyCharm Python Packages 
3. Run [.app/main.py](app/main.py) using command line or IDE or create executable with following command:
    - pyinstaller --onefile --noupx --noconsole app/main.py
## Project documentation
Project documentation available at [documentation](https://tulodz-my.sharepoint.com/:w:/r/personal/240664_edu_p_lodz_pl/_layouts/15/Doc.aspx?sourcedoc=%7B8F73AE95-2F40-4615-AA85-ED68C0AFAD9A%7D&file=Requirements%20specification.docx&action=default&mobileredirect=true&DefaultItemOpen=1&wdsle=0)
## Backlog
Project backlog available at: https://trello.com/b/rRiilgsa/zpinf
## CI System
GitHub Actions is used to test if project builds successfully after every new PR on main, release and develop branches. After PR on branch release automatically create new release with new tag.<br>
Workflow scripts you can find in: [.github/workflows](https://github.com/IIS-ZPI/ZPI2023_IO1_MVP/tree/release/.github/workflows) in project files.
## CI Raports
Project raports available at: https://github.com/IIS-ZPI/ZPI2023_IO1_MVP/actions
