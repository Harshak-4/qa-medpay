QA assignment submission -

1. The automation code is committed and Test Scenarios are available in Medpay-Test-Scenarios.xlsx file
2. The CHROME_EXECUTABLE_PATH under Config/config.py needs to be changed to run the automation script

To run the automation script:
1. change directory to qa-medpay/ from terminal
2. Run following command for all tests to execute - 'pytest -v --html=report.html --self-contained-html'
3. Run following command to execute Place order and check in assigned page - 'pytest -v -m placeorder --html=placeorder-report.html --self-contained-html'

