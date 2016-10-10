from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericReadOnlyResource
)
from .models import (
    PlayerEventTitle, PlayerEventValue, PlayerEventDirectory, Event
)


class PlayerEventTitleResource(GenericReadOnlyResource):
    model_cls = PlayerEventTitle
    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)


class PlayerEventValueResource(GenericReadOnlyResource):
    model_cls = PlayerEventValue
    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)


class PlayerEventDirectoryResource(GenericReadOnlyResource):
    model_cls = PlayerEventDirectory
    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)


class EventResource(GenericReadOnlyResource):
    model_cls = Event
    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)