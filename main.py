import pyautogui
import time

# Text you want to paste
text_to_paste = """


{% extends 'Shop/base.html' %}
{% load static %}
{% block title %}Buy Now{% endblock title %}
{% block main-content %}
<div class="container my-5">
    <div class="row">
        <h3>Welcome aiQuest</h3>
        <div class="col-sm-2 border-end">
            <ul class="list-unstyled">
                <li class="d-grid"><a href="{% url 'profile' %}" class="btn btn-primary">Profile</a></li>
                <li class="d-grid"><a href="{% url 'address' %}" class="btn">Address</a></li>
            </ul>
        </div>
        <div class="col-sm-9 offset-sm-1">
            <div class="row">
                <div class="col-sm-6">
                    <div class="card">
                        <div class="card-body">
                            <h3>Address 1</h3>
                            <p>Name: Ripon Mia</p>
                            <p>Division: Dhaka</p>
                            <p>District: Dhaka</p>
                            <p>Thana: Dhaka</p>
                            <p>Vill/Road No: 152/2k, Green Road</p>
                            <p>Contact No: 01765656....</p>
                            <p>Zipcode: 1205</p>

                        </div>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="card">
                        <div class="card-body">
                            <h3>Address 2</h3>
                            <p>Name: Imam Hossain</p>
                            <p>Division: Rajshahi</p>
                            <p>District: Rajshahi</p>
                            <p>Thana: Rajshahi</p>
                            <p>Vill/Road No: University Road</p>
                            <p>Contact No: 01765656....</p>
                            <p>Zipcode: 70...</p>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock main-content %}

"""


# Loop through the text in chunks of 10 characters
for i in range(0, len(text_to_paste), 10):
    # Get the next 10 characters
    chunk = text_to_paste[i:i+50]
    # Type the chunk
    pyautogui.typewrite(chunk)
    # Wait 5 seconds before typing the next chunk
    time.sleep(5)
