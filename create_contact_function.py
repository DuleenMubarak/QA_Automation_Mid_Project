import random
from faker import Faker



def generate_random_contact(): #Generating random contacts list, count==the number of contacts
    fake=Faker() #Initialize Faker
    contact={"first_name":fake.first_name(),
            "last_name":fake.last_name(),
            "birthday":fake.date_of_birth(minimum_age=10,maximum_age=90).isoformat(),
            "email":fake.email(),
            "phone": "".join(random.choices("0123456789", k=10)),
            "street_address_1":fake.street_address(),
            "street_address_2":fake.secondary_address(),
            "city":fake.city(),
            "state":fake.state(),
            "postal_code":fake.zipcode(),
            "country":fake.country()
    }
        
    return contact