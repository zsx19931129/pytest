def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert b"smtp.163.com" in msg
    assert 0  # for demo purposes

def test_noop(smtp):
    response, msg = smtp.noop()
    assert response == 250
    assert b"smtp.163.com" in msg
    assert 0  # for demo purposes