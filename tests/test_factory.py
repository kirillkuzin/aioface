from dataclasses import asdict

from aioface import FacebookFactory
from aioface.fb import types
from aioface.fb.utils import fb_dict_factory

fb_factory = FacebookFactory()


class TestFactory:
    def test_create_url_button(self):
        url_button = fb_factory.create_url_button(title='Just a button',
                                                  url='awesome url')
        assert isinstance(url_button, types.FacebookButton)
        assert url_button.title == 'Just a button'
        assert url_button.url == 'awesome url'

    def test_create_postback_button(self):
        postback_button = fb_factory.create_postback_button(
            title='Just a button',
            payload='My payload'
        )
        assert isinstance(postback_button, types.FacebookButton)
        assert postback_button.title == 'Just a button'
        assert postback_button.payload == 'My payload'

    def test_create_generic_template_element(self):
        dab = fb_factory.create_url_button(title='Default action button',
                                           url='default url')
        url_button = fb_factory.create_url_button(title='Just a button',
                                                  url='awesome url')
        postback_button = fb_factory.create_postback_button(
            title='Just a button',
            payload='My payload'
        )
        gte = fb_factory.create_generic_template_element(
            title='Awesome template',
            subtitle='Cool subtitle',
            image_url='cats.jpg',
            default_action=dab,
            buttons=[url_button, postback_button]
        )
        assert isinstance(gte, types.FacebookTemplateElement)
        assert asdict(gte, dict_factory=fb_dict_factory) == {
            'title': 'Awesome template',
            'subtitle': 'Cool subtitle',
            'image_url': 'cats.jpg',
            'default_action': {'type': 'web_url',
                               'title': 'Default action button',
                               'url': 'default url'},
            'buttons': [{'type': 'web_url',
                         'title': 'Just a button',
                         'url': 'awesome url'},
                        {'type': 'postback',
                         'title': 'Just a button',
                         'payload': 'My payload'}]
        }
