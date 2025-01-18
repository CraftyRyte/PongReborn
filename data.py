from enum import Enum
import uuid

class EntityTypes(Enum):
    PADDLE=uuid.uuid5(uuid.NAMESPACE_X500, "paddletheplayer")
    BALL=uuid.uuid5(uuid.NAMESPACE_X500, "ballthebouncer")
