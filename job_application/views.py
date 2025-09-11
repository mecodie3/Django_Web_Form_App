from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    # Check if the request is a form submission (POST request)
    if request.method == "POST":
        # Bind the submitted POST data to the ApplicationForm
        form = ApplicationForm(request.POST)

        # Validate the form data (check required fields, data types, etc.)
        if form.is_valid():
            # Extract cleaned (validated and sanitized) data from the form
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # Save a new record into the database using the Form model
            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )


            message_body = f"A new job application was submitted. Thank you, {first_name}."

            email_message = EmailMessage(
                subject="Form submission confirmation",
                body=message_body,
                to=[email]
            )
            email_message.content_subtype = "plain"  # Or "html" if you're using HTML
            email_message.send()



            # Print the message once the data was loaded into the DB
            messages.success(request,"Form submitted successfully")

    # Render the "index.html" template for both GET and POST requests
    return render(request, "index.html")

def about(request):
    return render(request,"about.html")
