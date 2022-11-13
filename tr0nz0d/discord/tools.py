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
"""

from typing import List, Dict, Optional
import requests


class EmbedField:
    title: str
    content: str

    def __init__(self, title: str, content: str) -> None:
        """ Creates an EmbedField with informed title and content

        Args:
            title (str): Title of your field
            content (str): Content of your field
        """
        self.title = title
        self.content = content

    def as_json(self) -> Dict[str, str]:
        """ Converts stored data to a json seriable dictionary

        Returns:
            Dict[str, str]: Stored data json seriable dict with proper keys
        """
        json_field: Dict[str, str] = {
            "name": self.title,
            "value": self.content
        }

        return json_field


class EmbedData:
    title: str
    description: str
    fields: Optional[List[EmbedField]]

    def __init__(self, title: str, description: str, fields: Optional[List[EmbedField]] = None) -> None:
        """ Creates an EmbedData with informed title, description and includes EmbedField list if not None

        Args:
            title (str): Embed message title
            description (str): Embed message description
            fields (List[EmbedField] | None): Optional list of EmbedFields. Defaults to None.
        """
        self.title = title
        self.description = description
        self.fields = fields

    def as_json(self) -> Dict[str, str | List[Dict[str, str]]]:
        """ Converts stored data to a json serializable dictionary

        Returns:
            Dict[str, str | List[Dict[str, str]]]: Stored data as json serializable dict
        """
        json_embed: Dict[str, str | List[Dict[str, str]]] = {}

        json_embed["title"] = self.title
        json_embed["description"] = self.description

        if self.fields is not None:
            json_fields: List[Dict[str, str]] = []
            for field in self.fields:
                json_fields.append(field.as_json())

            json_embed["fields"] = json_fields

        return json_embed


class Data:
    content: str
    username: str
    embeds: Optional[List[EmbedData]]

    def __init__(self, content: str, username: str, embed: Optional[List[EmbedData]] = None) -> None:
        """ Creates a Data with the informed content, username and includes embed messages if not none

        Args:
            content (str): Message's main content
            username (str): Webhook's display username
            embed (List[EmbedData] | None): Optional list of EmbedData. Defaults to None.
        """
        self.content = content
        self.username = username
        self.embeds = embed

    def as_json(self) -> Dict[str, str | List[Dict[str, str | List[Dict[str, str]]]]]:
        """ Converts stored data to a json serializable dict

        Returns:
            Dict[str, str | List[Dict[str, str | List[Dict[str, str]]]]]: Stored data json serializable dict
        """
        json_data: Dict[str, str | List[Dict[str, str | List[Dict[str, str]]]]] = {}

        json_data["content"] = self.content
        json_data["username"] = self.username

        if self.embeds is not None:
            json_embeds: List[Dict[str, str | List[Dict[str, str]]]] = []

            for embed in self.embeds:
                json_embeds.append(embed.as_json())

            json_data["embeds"] = json_embeds

        return json_data


class WebhookTools:

    def build_message_data(self, content: str, username: str, embeds: Optional[List[EmbedData]] = None) -> Data:
        """ Builds a message data class. Build embed data before if using embeds (build_message_embeds).

        Args:
            content (str): Message's main content
            username (str): Webhook's display username
            embeds (List[EmbedData] | None): Optional EmbedData list (build it first). Defaults to None.

        Returns:
            Data: Built message Data class
        """
        return Data(content=content, username=username, embed=embeds)

    def build_message_embeds(self, title: str, description: str, fields: Optional[List[EmbedField]] = None) -> EmbedData:
        """ Builds an EmbedData class. Build embed fields before if using fields (build_embed_fields).

        Args:
            title (str): Embed message's title
            description (str): Embed message's description
            fields (List[EmbedField] | None): Optional list of embed fields (build it first). Defaults to None.

        Returns:
            EmbedData: Built EmbedData class
        """
        return EmbedData(title=title, description=description, fields=fields)

    def build_embed_fields(self, title: str, content: str) -> EmbedField:
        """ Builds an EmbedField class.

        Args:
            title (str): Embed field's title
            content (str): Embed field's content

        Returns:
            EmbedField: Build EmbedField class
        """
        return EmbedField(title=title, content=content)

    def send_webhook_message(self, url: str, data: Data) -> int:
        """ Serializes and sends a webhook message using a post method, sending such data. Build message data first (build_message_Data)

        Args:
            url (str): Webhook's URL
            data (Data): Message's data

        Raises:
            requests.exceptions.HTTPError: After posting data at URL

        Returns:
            int: Message's status code
        """
        post_result = requests.post(url=url, json=data.as_json())

        post_result.raise_for_status()

        return post_result.status_code
