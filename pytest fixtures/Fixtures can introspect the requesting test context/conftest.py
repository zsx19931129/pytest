# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp(request):
    server = getattr(request.module, "smtpserver", "smtp.163.com")
    smtp = smtplib.SMTP(server)

    def fin():
        print ("finalizing %s (%s)" % (smtp, server))
        smtp.close()
    request.addfinalizer(fin)
    return smtp