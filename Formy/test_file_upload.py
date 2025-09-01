from playwright.sync_api import expect
from page_object.home_page import Home
from page_object.fileupload import Fileupload

def test_file_upload(formy_setup):
    page = formy_setup
    homepage = Home(page, expect)
    homepage.navigate()
    module = "File Upload"
    homepage.open_module(module)
    fileuploadpage = Fileupload(page, expect)
    fileuploadpage.validate_module_page("File upload")
    fileuploadpage.actions()
    homepage.redirect()