from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from trepi.intranet import _
from trepi.intranet.utils import validadores
from zope import schema
from zope.interface import implementer


class IArea(model.Schema):
    """Definição de uma Área."""

    model.fieldset(
        "contato",
        _("Contato"),
        fields=[
            "email",
            "telefone",
        ],
    )
    email = Email(
        title=_("Email"),
        required=True,
        constraint=validadores.is_valid_email,
    )

    telefone = schema.TextLine(
        title=_("Telefone"),
        description=_("Informe o telefone de contato"),
        required=False,
        constraint=validadores.is_valid_telefone,
    )

    model.fieldset(
        "Endereço",
        _("Endereço"),
        fields=[
            "endereco",
            "complemento",
            "cidade",
            "estado",
            "cep",
        ],
    )

    endereco = schema.TextLine(
        title=_("Endereço"),
        description=_("Informe o endereço"),
        required=True,
    )

    complemento = schema.TextLine(
        title=_("Complemento"),
        description=_("Informe o complemento"),
        required=True,
    )

    cidade = schema.TextLine(
        title=_("Cidade"),
        description=_("Informe a cidade"),
        required=True,
    )

    estado = schema.TextLine(
        title=_("Estado"),
        description=_("Informe o estado"),
        required=True,
    )

    cep = schema.TextLine(
        title=_("CEP"),
        description=_("Informe o CEP"),
        required=True,
    )


@implementer(IArea)
class Area(Container):
    """Uma Área no TRE-PI."""
