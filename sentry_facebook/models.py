from sentry.plugins import Plugin, register


class FacebookPlugin(Plugin):
    title = 'Facebook'
    slug = 'facebook'
    version = '0.1'
    author = 'George Marshall'


register(FacebookPlugin)
