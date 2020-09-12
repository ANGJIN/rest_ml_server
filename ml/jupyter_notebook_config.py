c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.allow_root = True

#from notebook.auth import passwd; passwd()
c.NotebookApp.password = 'sha1:ade705639dd1:3382d7c63fe3674db6a1d60325dffbd582462926'  # abc123
c.NotebookApp.token = ''

c.NotebookApp.base_url = '/ml'

c.NotebookApp.allow_origin = '*'
c.NotebookApp.disable_check_xsrf = True
