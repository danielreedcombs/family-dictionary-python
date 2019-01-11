# Define a dictionary that contains information about several members of your family.

my_family = {
    'Mom': {
        'name': 'Lisa',
        'age': 56
    },
    'Dad': {
        'name': 'Randy',
        'age': 62
    },
    'Wife':{
        'name': 'Ruthy',
        'age': 26
    }
}
# Using a dictionary comprehension, produce output that looks like the following example.
for family_member, member_values in my_family.items():
    print(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old')

