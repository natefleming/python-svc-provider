

from  mck.datatwins.email import EmailService


def test_send(smtp_email_service: EmailService):
    smtp_email_service.send('foo')

