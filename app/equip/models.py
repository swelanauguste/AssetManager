from django.db import models


class Make(models.Model):
    make = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("make",)

    def __str__(self):
        return self.make.upper()


class EquipmentModel(models.Model):
    computer_model = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    make = models.ForeignKey(
        Make, on_delete=models.CASCADE, related_name="makes", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("computer_model",)

    def __str__(self):
        return f"{self.make} {self.computer_model.upper()}"


class Status(models.Model):
    status = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses"
        ordering = ("status",)

    def __str__(self):
        return self.status.capitalize()


class EquipmentType(models.Model):
    equip_type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.equip_type.upper()


class Equipment(models.Model):
    equip_type = models.ForeignKey(
        EquipmentType,
        on_delete=models.CASCADE,
        related_name="equipment_types",
        null=True,
        blank=True,
    )
    serial_number = models.CharField(max_length=100, unique=True)
    model = models.ForeignKey(
        EquipmentModel,
        on_delete=models.CASCADE,
        related_name="computer_models",
        null=True,
        blank=True,
    )
    branch = models.CharField(max_length=100, default="head office")
    location = models.TextField(blank=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name="computer_statuses",
        null=True,
        blank=True,
    )
    date_received = models.DateField()
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "equipment"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.model} (S/N: {self.serial_number})"


class EquipmentNote(models.Model):
    equip = models.ForeignKey(
        "Equipment", on_delete=models.CASCADE, related_name="equipment_notes"
    )
    summary = models.CharField(max_length=255)
    note = models.TextField()
    attachment = models.FileField(
        null=True, blank=True, verbose_name="file",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated_at",)

    def __str__(self):
        return f"{self.equip} {self.summary}"


class IPAddress(models.Model):
    address = models.CharField(max_length=32, unique=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated_at",)

    def __str__(self):
        return f"{self.address}"

