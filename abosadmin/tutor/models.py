from django.db import models


class Human(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)

    class Meta(object):

        abstract = True


class Female(Human):
    boobs = models.IntegerField()


class Male(Human):
    salary = models.IntegerField()


class Monkey(models.Model):
    age = models.IntegerField()

    def __str__(self):
        return "n%8s" % self.age


class Human2(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    m2m = models.ManyToManyField(
        Monkey,
        related_name="%(app_label)s_%(class)s_related",
        verbose_name="monkeys"
    )

    class Meta(object):

        abstract = True

    def __str__(self):
        return "%s" % self.name


class Male2(Human2):
    salary = models.IntegerField()

    def __str__(self):
        return "%s" % self.name


class Female2(Human2):
    boobs = models.IntegerField()


class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small',),
        ('M', 'Medium',),
        ('L', 'Large',),
    )
    first_name = models.CharField('person\'s first name', max_length=32)
    last_name = models.CharField(max_length=32)
    shirt_size = models.CharField(
        max_length=1,
        choices=SHIRT_SIZE,
        default='S'
    )

    class Meta(object):

        ordering = ["first_name"]

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Picture(models.Model):
    url = models.URLField()
    # image = models.ImageField()  # no pillow package
    likers = models.ManyToManyField(Person, through='LikePicture')


class LikePicture(models.Model):
    person = models.ForeignKey(Person)
    picture = models.ForeignKey(Picture)
    date_liked = models.DateField()


class Place(models.Model):

    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s at %s" % (self.name, self.address)


class Supplier(Place):

    customers = models.ManyToManyField(Place, related_name="provider")


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "Restaurant: %s at %s" % (self.name, self.address)


class Zoo(Place):
    with_dog = models.BooleanField(default=False)
    with_dragon = models.BooleanField(default=False)
    with_money = models.BooleanField(default=False)

    def __str__(self):
        return "Zoo: %s at %s" % (self.name, self.address)


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Manufacturer(models.Model):
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)


class Topping(models.Model):
    pass


class Pizza(object):
    toppings = models.ManyToManyField(Topping)


class Group(models.Model):

    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):

    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return "%s in %s" % (self.person, self.group)


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class NewManager(models.Manager):

    pass


class ExtraManagers(models.Model):

    secondary = NewManager()

    class Meta:
        abstract = True


class MyPerson(Person, ExtraManagers):

    objects = NewManager()

    class Meta(object):
        proxy = True


class LastNamePerson(Person):
    class Meta:
        ordering = ["last_name"]
        proxy = True

    def do_something(self):
        pass

# Create your models here.
