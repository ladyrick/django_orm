from django_orm.test import SimpleTestCase
from django_orm.test.client import FakePayload


class FakePayloadTests(SimpleTestCase):
    def test_write_after_read(self):
        payload = FakePayload()
        payload.read()
        msg = "Unable to write a payload after it's been read"
        with self.assertRaisesMessage(ValueError, msg):
            payload.write(b"abc")
