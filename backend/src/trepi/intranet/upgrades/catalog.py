from plone import api
from Products.GenericSetup.tool import SetupTool
from Products.ZCatalog.CatalogBrains import AbstractCatalogBrain
from trepi.intranet import logger
from trepi.intranet.content.pessoa import Pessoa


def reindexa_pessoa(portal_setup: SetupTool) -> None:
    """Reindexa todos os objetos do tipo Pessoa."""
    brains: list[AbstractCatalogBrain] = api.content.find(portal_type=Pessoa)
    for brain in brains:
        pessoa: Pessoa = brain.getObject()
        pessoa.reindexObject(idxs=["area", "cargo"])
        logger.info(
            f"- Reidexa os campos area e cargo do objeto {pessoa.absolite_url()}"
        )
    logger.info("Reindexação completa")
