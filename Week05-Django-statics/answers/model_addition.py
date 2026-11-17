# Add this field and method inside the Student model from Week 04.
image = models.ImageField(upload_to="images/", blank=True)

def __str__(self):
    return f"{self.firstName.capitalize()}, {self.lastName.upper()}"

# Add this method inside Module as well:
# def __str__(self):
#     return f"{self.code.upper()} - {self.name}"
