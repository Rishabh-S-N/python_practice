#3 l3
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Rishabh", age=21, city="Kushalnagar")
