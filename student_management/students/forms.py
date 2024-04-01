from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs) -> None:
        super(StudentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['full_name'].widget.attrs['placeholder'] = 'e.g. Tran Minh Yen'
        self.fields['birth_date'].widget.attrs['placeholder'] = 'e.g. 2024-03-19'
        self.fields['class_name'].widget.attrs['placeholder'] = 'Enter class'
        self.fields['average_score'].widget.attrs['placeholder'] = 'Enter average score'
