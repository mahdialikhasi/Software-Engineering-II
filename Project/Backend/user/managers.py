from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **other_fields):
        user = self.model(
            username=username,
            **other_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            password=password,
            first_name=username,
            last_name=username,
            role=1,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
