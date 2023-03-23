from django import forms




    
    
   


    
    
    
    
    
    
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50, label="Hasap Ady")
    password=forms.CharField(max_length=20, label="Parol", widget=forms.PasswordInput)
    
    

