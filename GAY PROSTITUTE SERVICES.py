#so James is a gay prostitute and he wants to keep a record of what services he provides to
#his clients and where does he provide them.

#let´s define the service, in this case, our prostitute will be called James and he will be giving a blowjob
#to his favorite and regular client Chris. Yummy !!!
def prostitute_provides():
    name_of_prostitute = "James"
    service = "gives sloppy blowjob"
    location = "public restroom"
    name_of_client = "Chris"

    prostitute_provides = (f"{name_of_prostitute} {service} to {name_of_client} in the {location}")
    return(prostitute_provides)

#Now let´s define how much does he charge for that service.
def service_price(amount):

    wart_interest_rate_price = 0.10
    service_price = (f" and charges {amount}$ for it")
    return(service_price)

#Let´s print both strings.
amount_for_blowjob = 100
print((prostitute_provides()) + (service_price(amount_for_blowjob)))


#oh no !! After a few months on the job, most of the clients didn´t have a proper hygene down there
#or had warts, but hey, this is a business and there´s money to be made, so the prostitute is gonna charge
#a different interest rate depending on the type of dick: unclean or "warted"

#let´s make a dictionary with a list of clients and what type of dick they have

dick_type = {"Lucas": "unclean" , "John": "unclean", "Ronald": "unclean", "Harry": "warts",
             "Gonzalo": "unclean", "Javier": "warts"}
#10 = "warts"
#20 = "unclean""
#let´s define the interest rate first and the prices:


wart_interest_rate = 0.10
unclean_interest_rate = 0.05

price_wart_interest_rate = amount_for_blowjob + (amount_for_blowjob * wart_interest_rate)
price_unclean_interest_rate = amount_for_blowjob + (amount_for_blowjob * unclean_interest_rate)

def final_price(dick_type):
    for key in dick_type.keys():
        if dick_type[key] == "warts" :
           print(f" {key} will have to pay an amount of {price_wart_interest_rate}$ for a blowjob")
        elif dick_type[key] == "unclean":
           print(f"{key} will have to pay an amount of {price_unclean_interest_rate}$ for a blowjob")

final_price(dick_type)























