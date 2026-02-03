import json
import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List

def _sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

@dataclass
class AuditEvent:
    ts: str
    type: str
    payload: Dict[str, Any]
    prev_hash: str
    hash: str

class AuditTrail:
    def __init__(self):
        self._events: List[AuditEvent] = []
        self._last_hash = "GENESIS"

    def add(self, event_type: str, payload: Dict[str, Any]):
        ts = datetime.now(timezone.utc).isoformat()
        body = {
            "ts": ts,
            "type": event_type,
            "payload": payload,
            "prev_hash": self._last_hash,
        }
        h = _sha256(json.dumps(body, sort_keys=True))
        evt = AuditEvent(ts, event_type, payload, self._last_hash, h)
        self._events.append(evt)
        self._last_hash = h

    def export(self) -> List[Dict[str, Any]]:
        return [
            {
                "ts": e.ts,
                "type": e.type,
                "payload": e.payload,
                "prev_hash": e.prev_hash,
                "hash": e.hash,
            }
            for e in self._events
        ]

    def root_hash(self) -> str:
        return self._last_hash
