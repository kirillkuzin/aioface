# FacebookFactory

```python
from aioface import FacebookFactory


fb_factory = FacebookFactory()
```

## [Buttons](https://developers.facebook.com/docs/messenger-platform/reference/buttons)

### [URL Button](https://developers.facebook.com/docs/messenger-platform/reference/buttons/url)

```python
button = fb_factory.create_url_button(
    title='Just button',
    url='awesome_url'
)

```

### [Postback Button](https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback)

### [Call Button](https://developers.facebook.com/docs/messenger-platform/reference/buttons/call/)

### [Log In Button](https://developers.facebook.com/docs/messenger-platform/reference/buttons/login/)

### [Log Out Button](https://developers.facebook.com/docs/messenger-platform/reference/buttons/logout/)

## [Templates](https://developers.facebook.com/docs/messenger-platform/reference/templates)

### [Generic Template](https://developers.facebook.com/docs/messenger-platform/reference/template/generic)

### [Button Template](https://developers.facebook.com/docs/messenger-platform/reference/template/button)

### [Media Template](https://developers.facebook.com/docs/messenger-platform/reference/template/media)

```python
raise NotImplementedError
```

### [Receipt Template](https://developers.facebook.com/docs/messenger-platform/reference/template/receipt)

### [Airline Boarding Pass Template](https://developers.facebook.com/docs/messenger-platform/reference/template/airline-boarding-pass)

### [Airline Check-in Template](https://developers.facebook.com/docs/messenger-platform/reference/template/airline-checkin/)

### [Airline Itinerary Template](https://developers.facebook.com/docs/messenger-platform/reference/template/airline-itinerary)

### [Airline Update Template](https://developers.facebook.com/docs/messenger-platform/reference/templates/airline-flight-update)

## [Quick Replies](https://developers.facebook.com/docs/messenger-platform/reference/buttons/quick-replies)

### Text Quick Reply

### User Phone Number Quick Reply

### User Email Quick Reply

## [Attachment Upload API](https://developers.facebook.com/docs/messenger-platform/reference/attachment-upload-api)

### Image

### Video

### Audio

### File
