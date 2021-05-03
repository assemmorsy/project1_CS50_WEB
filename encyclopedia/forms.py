from django import forms


class NewPageform(forms.Form):
    title = forms.CharField(label="Title", max_length=50, required=True, widget=forms.TextInput(attrs={"class":"form-control" }))
    
    description = forms.CharField(
        required=True, widget=forms.Textarea(attrs={"class":"form-control" ,"rows": 4})
    )


class EditPageform(forms.Form):
    description = forms.CharField(
        required=True, widget=forms.Textarea(attrs={"class":"form-control" ,"rows": 4  })
    )
