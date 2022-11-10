from django.db import models


class Fractal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        "auth.User", related_name="fractals", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ["created"]
