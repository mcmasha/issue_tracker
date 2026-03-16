from django.shortcuts import redirect, render
from .forms import AddIssueForm

# Create your views here.

def list (request): #list of all issues as a homepage
    pass 


def view (request, issue_id): #view of a single issue
    pass

def add (request): #add a new issue
    if request.method == 'POST':
        form = AddIssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user #If we wanna know by whom the issue was created, we need to set 
                                            #the created_by field to the current user. This is done by assigning 
                                            # request.user to issue.created_by before saving the issue.
            issue.save()
            return redirect('/')
            # Redirect to the issue list or detail page after saving
    else:
        form = AddIssueForm()
    return render(request, 'add.html', {'form': form})