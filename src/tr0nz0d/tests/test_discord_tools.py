# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

Created by: Gabriel Menezes de Antonio (TR0NZ0D)
"""
import unittest
from os import environ

from tr0nz0d.discord_tools.tools import WebhookTools


class TestWebhooks(unittest.TestCase):
    """Test case for webhooks"""
    url = environ.get('webhook_url', "")
    tools = WebhookTools()

    def test_webhook_sending(self):
        """Test for webhook sending"""
        fields_1 = [
            self.tools.build_embed_fields(title="Embed 01 Field title 01",
                                          content="Embed 01 Field content 01"),
            self.tools.build_embed_fields(title="Embed 01 Field title 02",
                                          content="Embed 01 Field content 02"),
            self.tools.build_embed_fields(title="Embed 01 Field title 03",
                                          content="Embed 01 Field content 03"),
            self.tools.build_embed_fields(title="Embed 01 Field title 04",
                                          content="Embed 01 Field content 04")
        ]
        fields_2 = [
            self.tools.build_embed_fields(title="Embed 02 Field title 01",
                                          content="Embed 02 Field content 01"),
            self.tools.build_embed_fields(title="Embed 02 Field title 02",
                                          content="Embed 02 Field content 02"),
            self.tools.build_embed_fields(title="Embed 02 Field title 03",
                                          content="Embed 02 Field content 03"),
            self.tools.build_embed_fields(title="Embed 02 Field title 04",
                                          content="Embed 02 Field content 04")
        ]
        fields_3 = [
            self.tools.build_embed_fields(title="Embed 02 Field title 01",
                                          content="Embed 02 Field content 01"),
            self.tools.build_embed_fields(title="Embed 02 Field title 02",
                                          content="Embed 02 Field content 02"),
            self.tools.build_embed_fields(title="Embed 02 Field title 03",
                                          content="Embed 02 Field content 03"),
            self.tools.build_embed_fields(title="Embed 02 Field title 04",
                                          content="Embed 02 Field content 04")
        ]
        embed_1 = self.tools.build_message_embeds(title="Embed 01 title",
                                                  description="Embed 01 description",
                                                  fields=fields_1)
        embed_2 = self.tools.build_message_embeds(title="Embed 02 title",
                                                  description="Embed 02 description",
                                                  fields=fields_2)
        embed_3 = self.tools.build_message_embeds(title="Embed 03 title",
                                                  description="Embed 03 description",
                                                  fields=fields_3)
        data = self.tools.build_message_data(content="Main message content",
                                             username="TR0NZ0D Lib unittests",
                                             embeds=[embed_1, embed_2, embed_3])
        message_response = self.tools.send_webhook_message(url=self.url, data=data)
        success_codes = [200, 201, 202, 203, 204]
        self.assertIn(message_response, success_codes)


if __name__ == "__main__":
    unittest.main()
