from django.db import models

class Scan(models.Model):
    name = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="nessus/")

    def __str__(self):
        return self.name


class Vulnerability(models.Model):
    SEVERITY = [
        ("Critical", "Critical"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
        ("Info", "Info"),
    ]

    scan = models.ForeignKey(Scan, on_delete=models.CASCADE)
    host = models.CharField(max_length=100)
    plugin_name = models.CharField(max_length=255)
    severity = models.CharField(max_length=10, choices=SEVERITY)

    def __str__(self):
        return f"{self.host} - {self.plugin_name}"

