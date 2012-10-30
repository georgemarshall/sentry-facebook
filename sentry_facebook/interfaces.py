from sentry.interfaces import Interface
from sentry.web.helpers import render_to_string


class User(Interface):
    def __init__(self, is_authenticated, **kwargs):
        self.is_authenticated = is_authenticated
        self.id = kwargs.get('id')
        self.username = kwargs.get('username')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')

    def serialize(self):
        user_info = {'is_authenticated': self.is_authenticated}
        if self.is_authenticated:
            user_info.update({
                'id': self.id,
                'username': self.username,
                'name': self.name,
                'email': self.email,
            })
        return user_info

    def get_hash(self):
        return []

    def to_html(self, event):
        return render_to_string('sentry_facebook/facebook.html', {
            'event': event,
            'user_authenticated': self.is_authenticated,
            'user_id': self.id,
            'user_username': self.username,
            'user_name': self.name,
            'user_email': self.email
        })

    def get_search_context(self, event):
        if not self.is_authenticated:
            return {}
        return {
            'text': [self.id, self.username, self.name, self.email]
        }
