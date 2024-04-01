from django.shortcuts import render, redirect
from .models import Student, student_collection
from .forms import StudentForm

# Create your views here.
def students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/student_list.html', context)


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/student_detail.html', {'student': student})


def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_data = form.cleaned_data
            student_data['birth_date'] = student_data['birth_date'].strftime(
                '%Y-%m-%d')
            student_data['average_score'] = float(student_data['average_score'])
            # Thêm dữ liệu vào cơ sở dữ liệu
            student_collection.insert_one(student_data)
            form.save()
            return redirect("students")
    context = {'form': form}
    return render(request, 'students/student_form.html', context=context)


def update_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    context = {'form': form}
    return render(request, 'students/student_form.html', context=context)


def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect(request.META.get('HTTP_REFERER'))
