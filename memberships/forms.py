from allauth.account import app_settings
from allauth.account.forms import LoginForm
from allauth.utils import set_form_field_order, get_username_max_length
from django.utils.translation import pgettext
from allauth.account.app_settings import AuthenticationMethod
from django import forms





class JetLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(JetLoginForm, self).__init__(*args, **kwargs)
        if app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.EMAIL:
            login_widget = forms.TextInput(attrs={'type': 'email',
                                                  'placeholder':
                                                  _('E-mail address'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.EmailField(label=_("E-mail"),
                                           widget=login_widget)
        elif app_settings.AUTHENTICATION_METHOD \
                == AuthenticationMethod.USERNAME:
            login_widget = forms.TextInput(attrs={'placeholder':
                                                  _('Username'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.CharField(
                label=_("Username"),
                widget=login_widget,
                max_length=get_username_max_length())
        else:
            assert app_settings.AUTHENTICATION_METHOD \
                == AuthenticationMethod.USERNAME_EMAIL
            login_widget = forms.TextInput(attrs={'placeholder':
                                                  ('Username or e-mail'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.CharField(label=pgettext("field label",
                                                         "Username Or Email"),
                                          widget=login_widget)
        self.fields["login"] = login_field
        set_form_field_order(self, ["username", "password", "remember"])


