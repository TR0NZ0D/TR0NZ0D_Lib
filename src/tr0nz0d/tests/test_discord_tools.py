import unittest
from tr0nz0d.discord_tools.tools import WebhookTools


class TestWebhooks(unittest.TestCase):
    url = ""
    tools = WebhookTools()

    def test_webhook_sending(self):
        fields_1 = [
            self.tools.build_embed_fields(title="Embed 01 Field title 01", content="Embed 01 Field content 01"),
            self.tools.build_embed_fields(title="Embed 01 Field title 02", content="Embed 01 Field content 02"),
            self.tools.build_embed_fields(title="Embed 01 Field title 03", content="Embed 01 Field content 03"),
            self.tools.build_embed_fields(title="Embed 01 Field title 04", content="Embed 01 Field content 04")
        ]
        fields_2 = [
            self.tools.build_embed_fields(title="Embed 02 Field title 01", content="Embed 02 Field content 01"),
            self.tools.build_embed_fields(title="Embed 02 Field title 02", content="Embed 02 Field content 02"),
            self.tools.build_embed_fields(title="Embed 02 Field title 03", content="Embed 02 Field content 03"),
            self.tools.build_embed_fields(title="Embed 02 Field title 04", content="Embed 02 Field content 04")
        ]
        fields_3 = [
            self.tools.build_embed_fields(title="Embed 02 Field title 01", content="Embed 02 Field content 01"),
            self.tools.build_embed_fields(title="Embed 02 Field title 02", content="Embed 02 Field content 02"),
            self.tools.build_embed_fields(title="Embed 02 Field title 03", content="Embed 02 Field content 03"),
            self.tools.build_embed_fields(title="Embed 02 Field title 04", content="Embed 02 Field content 04")
        ]
        embed_1 = self.tools.build_message_embeds(title="Embed 01 title", description="Embed 01 description", fields=fields_1)
        embed_2 = self.tools.build_message_embeds(title="Embed 02 title", description="Embed 02 description", fields=fields_2)
        embed_3 = self.tools.build_message_embeds(title="Embed 03 title", description="Embed 03 description", fields=fields_3)
        data = self.tools.build_message_data(content="Main message content", username="TR0NZ0D Lib unittests", embeds=[embed_1, embed_2, embed_3])
        message_response = self.tools.send_webhook_message(url=self.url, data=data)
        self.assertEqual(message_response, 204)


if __name__ == "__main__":
    unittest.main()
