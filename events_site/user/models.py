# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# # from .managers import CustomUserManager


# class CustomUser(AbstractUser):
#     username = models.CharField(
#         _("username"),
#         max_length=150,
#         unique=True,
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         validators=[AbstractUser.username_validator],
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#         null=True,
#         blank=True,
#     )

#     email = models.EmailField(_("email address"), unique=True)

#     is_active = models.BooleanField(
#         _("active"),
#         default=False,
#         help_text=_(
#             "Designates whether this user should be treated as active. "
#             "Unselect this instead of deleting accounts."
#         ),
#     )

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ['username']

#     objects = CustomUserManager()

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def clean(self) -> None:
#         return super().clean()
        
