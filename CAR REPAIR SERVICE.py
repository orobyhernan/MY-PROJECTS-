#so James is a mechanic and he wants to keep a record of all the services
#he provides and the location in which each service is provded (given that the company has
#several sites for car repairs.


def car_repair():
 name_of_mechanic = "James"
 service = "changes tires"
 location = "Playa del Rey workshop"
 name_of_client = "Chris"

 car_repair = (f"{name_of_mechanic} {service} to {name_of_client} in the {location}")
 return(car_repair)


#Now let´s define how much does he charge for that service.


def service_amount():
    amount = "100"
    price_for_repair = (f" and charges {amount}$ for it")
    return(price_for_repair)

print(car_repair() + service_amount())

#Oh no !!! after a few months on the job James realizes that a lot of clients bring faulty cars that
#make his job way harder than it should be. Their cars either have no CPU to run diagnostics or have
#electrical failure. So James decides to charge a different interest rate for each type of failure
#which will be: "no cpu" or "electrical failure".

#let´s make a dictionary with a list of clients and what type of failure does their car have.



type_of_failure = {"Lucas": "no cpu" , "John": "no cpu", "Ronald": "electrical failure", "Harry": "no cpu",
             "Gonzalo": "electrical failure", "Javier": "electrical failure"}

#now let´s make a list with the different interest rates charged to each client depending of the
#default failure their cars have.

repair_amount = 100
no_cpu_interest_rate = 0.10
electrical_fail_interest_rate = 0.05

price_no_cpu = repair_amount + (repair_amount * no_cpu_interest_rate)
price_electrical_fail = repair_amount + (repair_amount * electrical_fail_interest_rate)

#now let´s make a loop in order to set how much each client will have to pay

def final_price(type_of_failure):
    for key in type_of_failure.keys():
        if type_of_failure[key] == "no cpu":
            print(f"{key} will have to pay an amount of {price_no_cpu} for a cair repair")
        if type_of_failure[key] == "electrical failure":
            print(f"{key} will have to pay an amount of {price_electrical_fail} for a car repair")


print(final_price(type_of_failure))














