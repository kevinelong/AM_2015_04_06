x = 6
total = 10 * x
print total

x = 45
total = 42 / x
print total

x = 749
total = 972 * x
print total

print(len("I am really tired"))

print(len("Today is the day."))

for person in ["Jade", "Margot", "Alexa", "Miranda"]:
    print (person)

data =[
    { "name": "Miranda" },

    {"name": "Alexa" }]

key_field = "name"
output = {}

for item in data:
     values = []
     output_key = ""

     for k in item.keys():
         if k == key_field:
             output_key = item[k]
         else:
             values.append(item[k])
         output[output_key] = values

print (output)