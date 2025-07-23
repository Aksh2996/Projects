import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
driver=None

# ✅ FIXTURE - Attach driver instance to the test item (request.node)
@pytest.fixture
def driver(request):
    global driver
    ser = Service(r"C:\Users\DELL\OneDrive\Desktop\5lv\chromedriver.exe")
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ser, options=options)
    driver.implicitly_wait(10)
    request.node.driver = driver  # ✅ Save driver instance to test node
    yield driver
    driver.quit()

# Register the HTML plugin
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Take a screenshot and embed it in the HTML report on failure."""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.failed and not xfail) or (report.skipped and xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)

            # Clean filename
            test_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            file_name = os.path.join(reports_dir, test_name + ".png")

            _capture_screenshot(file_name)
            if os.path.exists(file_name):
                html_report_path = item.config.option.htmlpath  # full path to the HTML report
                relative_path = os.path.relpath(file_name, os.path.dirname(html_report_path))

                html = f'<div><img src="{relative_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(file_name):
    if driver:
        driver.get_screenshot_as_file(file_name)