from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class TimestampedModel(models.Model):
    """Metamodelo que registra fecha de creación y última modificación"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="fecha de creación",
    )
    last_update = models.DateTimeField(
        auto_now=True,
        verbose_name="última actualización",
    )

    class Meta:
        abstract = True


class CategoriesChoices(models.TextChoices):
    accesorios = ("accesorios", _("Accesorios"))
    buzos = ("buzos", _("Buzos"))
    camisas = ("camisas", _("Camisas, remeras y tops"))
    camperas = ("camperas", _("Camperas y sacos"))
    pantalones = ("pantalones", _("Pantalones y shorts"))


class ProductsModel(TimestampedModel):
    """Modelo de productos"""

    name = models.CharField(max_length=145, verbose_name="Nombre del producto")
    description = models.CharField(
        max_length=145,
        verbose_name="Descripcion del producto",
    )
    price = models.FloatField(verbose_name="Precio del producto")
    category = models.CharField(
        max_length=16,
        choices=CategoriesChoices,
        verbose_name="Categoria",
    )
    quantity = models.IntegerField(verbose_name="Cantidad disponible")


class StatusChoices(models.TextChoices):
    iniciado = ("iniciado", _("Pedido inciado"))
    cancelado = ("cancelado", _("Cancelado"))
    confirmado = ("confirmado", _("Confirmado por el vendedor"))
    empaquetado = ("empaquetado", _("Empaquetado"))
    enviado = ("enviado", _("Enviado"))
    finalizado = ("finalizado", _("Finalizado"))
    recibido = ("recibido", _("Recibido"))


class sizesChoices(models.TextChoices):
    XS = ("XS", _("Extra small"))
    S = ("S", _("Small"))
    M = ("M", _("Medium"))
    L = ("L", _("Large"))
    XL = ("XL", _("Extra Large"))
    XXL = ("XXL", _("Extra Extra Large"))


class ProductsData(models.Model):
    nota = models.ForeignKey("ProductsModel", on_delete=models.CASCADE)

    # Generic FK fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    quantity = models.IntegerField(verbose_name="Cantidad")
    variant = models.CharField(max_length=16, choices=sizesChoices)

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]


class OrdenModel(TimestampedModel):
    """Modelo de ordenes de productos"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(
        max_length=145,
        verbose_name="Nota del usuario",
        null=True,
        blank=True,
    )
    status = models.charField(
        max_length=9,
        choices=StatusChoices,
        verbose_name="Estado de la orden",
    )
    products = GenericRelation(ProductsData)
    delivery_details = models.CharField(
        max_length=300,
        verbose_name="Detalles de envio",
    )
    payment_status = models.CharField(max_length=145, verbose_name="Estado del pago")
