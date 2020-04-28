from django.shortcuts import render, redirect
from . import models
from login_app.models import User
from .models import Customer
# Create your views here.

##### DEVELOPMENT ######
def display_post(request):
    print("..........................")
    print("Printing data from request.POST.......")
    for k,v in request.POST.items():
        print(f"Key: {k}, Value: {v}")
    print("..........................")
    print("Printing data from request.FILES.......")
    if request.FILES == {}:
        print("No files uploaded")
    else:
        for k,v in request.FILES.items():
            print(f"Key: {k}, Value: {v}")
    print("..........................")

##### DEVELOPMENT ######


####### Helper Functions ########

def logged_user(request):    
    """ Get logged-in User object """
    return User.objects.filter(id=request.session["user_id"])[0]
####### Helper Functions #########

def index(request):
    """
    GET -> Renders dashboard.html
    POST -> Handles the following requests:
      a. Create Customer
      b. Create Carrier
      c. Create Contract
    """
    #### HELPER FUNCTION #####
    def format_datetime_input(astring):
        output = astring.split("/")
        output.append(output[0])
        output.append(output[1])
        output = output[2::]
        return "-".join(output)

    # POST Request ->
    if request.POST:
        display_post(request)
        try:
            request.POST["add_carrier"]
            carrier_address = models.Address.objects.create(
                name=request.POST["name"],
                street=request.POST["street_address"],
                city=request.POST["city"],
                state=request.POST["state"],
                zip_code=request.POST["zip_code"]
            )

            carrier = models.Carrier.objects.create(
                name = request.POST["name"],
                website = request.POST["website"],
                email = request.POST["email"],
                address = carrier_address
            )

            carrier_phone_number = models.PhoneNumber.objects.create(
                number_type = request.POST["number_type"],
                number = request.POST["phone_number"],
                carrier = carrier
            )

            comment = models.Comment.objects.create(
                content = request.POST["content"],
                user = logged_user(request),
                carrier = carrier,
            )
            
            carrier.save()
            carrier_address.save()
            carrier_phone_number.save()
            comment.save()

            print("Customer successfully entered into the database")
            return redirect(f"/dashboard/carrier/{carrier.id}")

        except KeyError:
            pass

        try:
            request.POST["add_customer"]
            customer_address = models.Address.objects.create(
                name=request.POST["name"],
                street=request.POST["street_address"],
                city=request.POST["city"],
                state=request.POST["state"],
                zip_code=request.POST["zip_code"]
            )

            customer = models.Customer.objects.create(
                name = request.POST["name"],
                website = request.POST["website"],
                email = request.POST["email"],
                address = customer_address
            )

            customer_phone_number = models.PhoneNumber.objects.create(
                number_type = request.POST["number_type"],
                number = request.POST["phone_number"],
                customer = customer
            )

            comment = models.Comment.objects.create(
                content = request.POST["content"],
                user = logged_user(request),
                customer = customer,
            )
            
            customer.save()
            customer_address.save()
            customer_phone_number.save()
            comment.save()

            print("Customer successfully entered into the database")
            return redirect(f"/dashboard/customer/{customer.id}")

        except KeyError:
            pass

        try:
            request.POST["add_contract"]
            pick_up_address = models.Address.objects.create(
                name = "Pickup address",
                street = request.POST["pickup_street_address"],
                city = request.POST["pickup_city"],
                state = request.POST["pickup_state"],
                zip_code = request.POST["pickup_zip_code"]    
            )
            delivery_address = models.Address.objects.create(
                name = "Delivery address",
                street = request.POST["delivery_street_address"],
                city = request.POST["delivery_city"],
                state = request.POST["delivery_state"],
                zip_code = request.POST["delivery_zip_code"] 
            )
            customer = models.Customer.objects.filter(name=request.POST["customer"])[0]
            carrier = models.Carrier.objects.filter(name=request.POST["carrier"])[0]
            contract = models.Contract.objects.create(
                status = request.POST["status"],
                customer = customer,
                carrier = carrier,
                customer_price = request.POST["customer_cost"],
                carrier_cost = request.POST["carrier_cost"],
                pick_up_time = format_datetime_input(request.POST["pickup_date"]) + " " + str(request.POST["pickup_time"]),
                delivery_time = format_datetime_input(request.POST["delivery_date"]) + " " + str(request.POST["delivery_time"])
            )
            comment = models.Comment.objects.create(
                content = request.POST["comments"],
                user = logged_user(request),
                contract = contract
            )
            route = models.Route.objects.create(
                start = pick_up_address,
                end = delivery_address,
                contract = contract
            )

            contract.save()
            comment.save()
            route.save()
            pick_up_address.save()
            delivery_address.save()
            print("Contract successfully added to the database")
            return redirect(f"/dashboard/contract/{contract.id}")

        except KeyError:
            pass

        return redirect("/dashboard")
    
    
    # GET Request -> Render dashboard.html
    else:
        context = {
            "user": logged_user(request),
            "carriers": models.Carrier.objects.all(),
            "customers": models.Customer.objects.all(),
            "contracts": models.Contract.objects.all(),
        }
        
        return render(request, "dashboard.html", context)

def carrier(request, carrier_id):
    pass

def contract(request, contract_id):
    pass

def customer(request, customer_id):
    # POST data
    if request.POST:
        try:
            if request.POST['comment']:
                # Comment validation
                # Comment.objects.create(content = request.POST["content"], user=logged_user(request))
                return redirect(f"/dashboard/customer/{customer_id}")
        except:
            pass
        try:
            if request.POST['update']:
                print("In the update function. Let's get some validations here")
                print(request.POST)
                # errors=models.Customer.objects.validation(request.POST)
                # if len(errors) > 0:
                    # request.session["errors"] = errors
                    # return redirect(f"/dashboard/customer/{customer_id}")
                customer_to_change = Customer.objects.get(id=customer_id)
                customer_to_change.name = request.POST["name"]
                customer_to_change.website = request.POST["website"]
                customer_to_change.email = request.POST["email"]
                customer_to_change.address.address_name = request.POST["address_name"]
                customer_to_change.address.street = request.POST["street"]
                customer_to_change.address.city = request.POST["city"]
                customer_to_change.address.state = request.POST["state"]
                customer_to_change.address.zip_code = request.POST["zip_code"]
                customer_to_change.save()
                customer_to_change.address.save()
                return redirect(f"/dashboard/customer/{customer_id}")
        except:
            pass
        try:
            if request.POST['delete']:
                customer_to_delete=Customer.objects.get(id=customer_id)
                # customer_to_delete.delete()
                # return redirect("/dashboard")
                print(customer_to_delete)
                return redirect(f"/dashboard/customer/{customer_id}")
        except:
            pass
    
    # No POST data
    else:
        context = {
            "customer": Customer.objects.get(id=customer_id),
            "user": logged_user(request)
        }
        return render(request, "customer.html", context)