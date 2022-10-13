from django.db import models

class Collection(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Promotions(models.Model):
    description=models.TextField(null=True)
    discount=models.FloatField()

class Product(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.PositiveSmallIntegerField(null=True)
    last_updated=models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) #one-to-many relation
    promotions=models.ManyToManyField(Promotions) #many-to-many-relation
    def __str__(self):
        return self.title

class Order(models.Model):
    PENDING='P'
    COMPLETED='C'
    FAILED='F'
    ORDER_CHOICES=[
        (PENDING,'Pending'),
        (COMPLETED,'Completed'),
        (FAILED,'Failed')
    ]
    placed_at=models.DateTimeField(help_text='Ordered date')
    payment_status=models.CharField(max_length=1,choices=ORDER_CHOICES,default=PENDING)

class Customer(models.Model):
    NO_MEMBERSHIP='N'
    PRIME_MEMBERSHIP='P'
    ELITE_MEMBERSHIP='E'
    MEMBERSHIP_CHOICES=[
        (NO_MEMBERSHIP,'NO'),
        (PRIME_MEMBERSHIP,'PRIME'),
        (ELITE_MEMBERSHIP,'ELITE')
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.IntegerField(null=True)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=NO_MEMBERSHIP)
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    def __str__(self):
        return self.first_name+' '+self.last_name

class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=20)
    customer=models.OneToOneField(Customer ,on_delete=models.CASCADE) #one-to-many relationship



class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
    def __str__(self):
        return self.product.title

