@rem Run the script in the rood project directory


@set APP_NAME=storydownloader
@set PATH=.venv\Scripts\;%PATH%

@python -m %APP_NAME% --main-page-url "http://write-valid-site-here.me/" --output-dir ./stories
