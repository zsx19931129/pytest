# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module", params = ["smtp.163.com", "mail.python.org"])
def smtp(request):
    smtp = smtplib.SMTP(request.param)

    def fin():
        print ("finalizing %s" % smtp)
        smtp.close()
    request.addfinalizer(fin)
    return smtp