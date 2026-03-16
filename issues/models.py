from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IssueType(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __strt__(self):
        return self.title

class Resolution(models.Model):
    title = models.CharField(max_length=255, unique=True)



class Issue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description_md = models.TextField()
    description_html = models.TextField(editable=False) # A user cant edit
    issue_type = models.ForeignKey('IssueType', on_delete=models.PROTECT)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    due_date = models.DateField(null=True, blank=True)
    resolution = models.ForeignKey('Resolution', on_delete=models.PROTECT)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    duplicate_of = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Issue: {self.id}"

class Comment(models.Model):
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description_md = models.TextField()
    description_html = models.TextField(editable=False) # A user cant edit

    class Meta: 
        ordering = ['-issue__created_at','created_at']#the first "" is the sorting by issue created date and the second is sorting by comment created date
    
    def __str__(self):
        return f"Comment: #{self.id}"
