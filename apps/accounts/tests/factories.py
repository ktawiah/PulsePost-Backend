import factory
from faker import Faker

from ..models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        skip_postgeneration_save = True

    id = fake.uuid4()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.unique.email()
    created_at = fake.date_time_this_decade()
    updated_at = fake.date_time_this_decade()

    @factory.post_generation
    def password(self, created, extracted, **kwargs):
        if created:
            return
        elif extracted:
            self.set_password(extracted)
        else:
            self.set_password(fake.password())
