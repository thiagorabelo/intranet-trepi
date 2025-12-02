from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from trepi.intranet import _
from trepi.intranet.utils import validadores
from zope import schema
from zope.interface import implementer


class IArea(model.Schema):
    """Definição de uma Área."""

    pass


@implementer(IArea)
class Area(Container):
    """Uma Área no TRE-PI."""

    pass
