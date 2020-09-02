import typing

from aioface.fb import types


class FacebookFactory:
    @staticmethod
    def _create_attachment_payload(
            template_type: str = None,
            text: str = None,
            top_element_style: str = None,
            elements: typing.List[types.FacebookTemplate] = None,
            buttons: typing.List[types.FacebookButton] = None,
            url: str = None,
            is_reusable: bool = None
    ) -> types.FacebookAttachmentPayload:
        return types.FacebookAttachmentPayload(
            template_type=template_type,
            text=text,
            top_element_style=top_element_style,
            elements=elements,
            buttons=buttons,
            url=url,
            is_reusable=is_reusable
        )

    @staticmethod
    def _create_attachment(
            attachment_type: str,
            payload: types.FacebookAttachmentPayload
    ) -> types.FacebookAttachment:
        return types.FacebookAttachment(type=attachment_type,
                                        payload=payload)

    @staticmethod
    def _create_button(button_type: str = None,
                       title: str = None,
                       payload: str = None,
                       url: str = None,
                       messenger_extensions: bool = None,
                       webview_height_ratio: str = None,
                       fallback_url: str = None) -> types.FacebookButton:
        return types.FacebookButton(type=button_type,
                                    title=title,
                                    payload=payload,
                                    url=url,
                                    messenger_extensions=messenger_extensions,
                                    webview_height_ratio=webview_height_ratio,
                                    fallback_url=fallback_url)

    @staticmethod
    def _create_template(title: str = None,
                         subtitle: str = None,
                         image_url: str = None,
                         default_action: types.FacebookButton = None,
                         buttons: typing.List[types.FacebookButton] = None
                         ) -> types.FacebookTemplate:
        return types.FacebookTemplate(title=title,
                                      subtitle=subtitle,
                                      image_url=image_url,
                                      default_action=default_action,
                                      buttons=buttons)

    def create_url_button(self,
                          title: str,
                          url: str) -> types.FacebookButton:
        return self._create_button(button_type='web_url',
                                   title=title,
                                   url=url)

    def create_postback_button(self,
                               title: str,
                               payload: str) -> types.FacebookButton:
        return self._create_button(button_type='postback',
                                   title=title,
                                   payload=payload)

    def create_phone_number_button(self,
                                   title: str,
                                   payload: str) -> types.FacebookButton:
        return self._create_button(button_type='phone_number',
                                   title=title,
                                   payload=payload)

    def create_log_in_button(self, url: str) -> types.FacebookButton:
        return self._create_button(button_type='account_link', url=url)

    def create_log_out_button(self) -> types.FacebookButton:
        return self._create_button(button_type='account_unlink')

    def create_image_attachment(
            self,
            url: str,
            is_reusable: bool = None) -> types.FacebookAttachment:
        attachment_payload = self._create_attachment_payload(
            url=url,
            is_reusable=is_reusable
        )
        return self._create_attachment(attachment_type='image',
                                       payload=attachment_payload)

    def create_generic_template_element(
            self,
            title: str,
            subtitle: str = None,
            image_url: str = None,
            default_action: types.FacebookButton = None,
            buttons: typing.List[types.FacebookButton] = None
    ) -> types.FacebookTemplate:
        return self._create_template(title=title,
                                     subtitle=subtitle,
                                     image_url=image_url,
                                     default_action=default_action,
                                     buttons=buttons)

    def create_generic_template_attachment(
            self,
            generic_template_elements: typing.List[types.FacebookTemplate]
    ) -> types.FacebookAttachment:
        attachment_payload = self._create_attachment_payload(
            template_type='generic',
            elements=generic_template_elements
        )
        return self._create_attachment(attachment_type='template',
                                       payload=attachment_payload)

    def create_list_template_element(
            self,
            title: str = None,
            subtitle: str = None,
            image_url: str = None,
            default_action: types.FacebookButton = None,
            buttons: typing.List[types.FacebookButton] = None
    ) -> types.FacebookTemplate:
        return self._create_template(title=title,
                                     subtitle=subtitle,
                                     image_url=image_url,
                                     default_action=default_action,
                                     buttons=buttons)

    def create_list_template_attachment(
            self,
            list_template_elements: typing.List[types.FacebookTemplate],
            top_element_style: str = None,
            button: types.FacebookButton = None,
    ) -> types.FacebookAttachment:
        attachment_payload = self._create_attachment_payload(
            template_type='list',
            top_element_style=top_element_style,
            buttons=[button],
            elements=list_template_elements
        )
        return self._create_attachment(attachment_type='template',
                                       payload=attachment_payload)

    def create_button_template_attachment(
            self,
            text: str,
            buttons: typing.List[types.FacebookButton]
    ) -> types.FacebookAttachment:
        attachment_payload = self._create_attachment_payload(
            template_type='button',
            text=text,
            buttons=buttons
        )
        return self._create_attachment(attachment_type='template',
                                       payload=attachment_payload)
