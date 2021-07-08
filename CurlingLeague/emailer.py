import yagmail
import keyring


class Emailer:
    _sole_instance = None
    _sender_address = None

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def configure(cls, sender_address):
        cls._sender_address = sender_address

    def send_plain_email(self, recipients, subject, message, keyring_service=None):
        address = self._sender_address
        saved_password = keyring.get_password(keyring_service, address)
        if keyring_service is None:
            for rec in recipients:
                yagmail.SMTP(self._sender_address).send(rec, subject, message)
        elif keyring_service == "gmail":
            for rec in recipients:
                # print(f"Sending mail to: {rec}")
                yagmail.SMTP(self._sender_address, saved_password).send(rec, subject, message)

