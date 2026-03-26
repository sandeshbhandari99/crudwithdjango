from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Result
from .forms import ResultForm


def result_list(request):
    data = Result.objects.all().order_by('roll_number')
    total = data.count()
    passed = data.filter(marks__gte=40).count()
    failed = data.filter(marks__lt=40).count()
    avg = round(sum(r.marks for r in data) / total, 1) if total else 0
    context = {
        'data': data,
        'total': total,
        'passed': passed,
        'failed': failed,
        'avg': avg,
    }
    return render(request, 'results/result_list.html', context)


def add_result(request):
    form = ResultForm()
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Result added successfully!")
            return redirect('result_list')
    return render(request, 'results/result_form.html', {'form': form, 'action': 'Add'})


def edit_result(request, id):
    result = get_object_or_404(Result, id=id)
    form = ResultForm(instance=result)
    if request.method == "POST":
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            messages.success(request, "Result updated successfully!")
            return redirect('result_list')
    return render(request, 'results/result_form.html', {'form': form, 'action': 'Update'})


def delete_result(request, id):
    result = get_object_or_404(Result, id=id)
    if request.method == "POST":
        result.delete()
        messages.success(request, "Result deleted successfully!")
        return redirect('result_list')
    return render(request, 'results/confirm_delete.html', {'result': result})
