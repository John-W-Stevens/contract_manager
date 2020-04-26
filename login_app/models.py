from django.db import models
import re
import datetime
import bcrypt

class UserManager(models.Manager):
    def registration_validations(self,postData):
        errors = {}

        # first_name
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "must have 2 or more letters"
        if len(postData["first_name"]) >= 2 and not postData["first_name"].isalpha():
            errors["first_name"] = "must only contain letters"
        
        # last_name
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "must have 2 or more letters"
        if len(postData["last_name"]) >= 2 and not postData["last_name"].isalpha():
            errors["last_name"] = "must only contain letters"
        
        # email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if User.objects.filter(email=postData["email"]):
            errors["email"] = "This user already has an account"
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
            
        # password
        if len(postData["password"]) < 8:
            errors["password"] = "must be 8 or more characters"
        if postData["password"] != postData["pw_confirm"]:
            errors["pw_confirm"] = "Passwords need to match"
        return errors
    
    def login_validations(self, postData):
        errors = {}
        users = User.objects.filter(email=postData["email"])

        if not users:
            errors["email"] = "Invalid email address"
            return errors
        else:
            pw = postData["password"]
            if not bcrypt.checkpw(pw.encode(), users[0].password.encode()):
                errors["password"] = "Invalid password"
        return errors


    def confirm_credentials(self, sessionData, postData):
        user = User.objects.filter(id=sessionData["user_id"])[0]
        pw = postData["password"]
        if bcrypt.checkpw(pw.encode(), user.password.encode()):
            return True
        return False

    def update_profile_validations(self, postData, profile_id):
        profile = User.objects.filter(id=profile_id)[0]
        errors = {}

        # first name
        if postData["first_name"] != profile.first_name: # change has been made
            if len(postData["first_name"]) < 2:
                errors["first_name"] = "must have 2 or more letters"
            if len(postData["first_name"]) >= 2 and not postData["first_name"].isalpha():
                errors["first_name"] = "must only contain letters"

        # last name
        if postData["last_name"] != profile.last_name:
            if len(postData["last_name"]) < 2:
                errors["last_name"] = "must have 2 or more letters"
            if len(postData["last_name"]) >= 2 and not postData["last_name"].isalpha():
                errors["last_name"] = "must only contain letters"
    
        # email
        if postData["email"] != profile.email:
            # make sure new email is valid
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']): # test whether a field matches the pattern            
                errors['email'] = "Invalid email address!"
            # make sure email account isn't already registered
            else:
            # if "email" not in errors:
                for user in User.objects.all():
                    if user.email == postData["email"]:
                        errors["email"] = "This account is already registered"
                        break

        # password
        if postData["password"] != "": # a change was made
            if len(postData["password"]) < 8:
                errors["password"] = "must be 8 or more characters"
            if postData["password"] != postData["pw_confirm"]:
                errors["pw_confirm"] = "Passwords need to match"
        if postData["password"] == "" and postData["pw_confirm"] != "":
            errors["pw_confirm"] = "Passwords need to match"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    level = models.IntegerField(default=1)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()