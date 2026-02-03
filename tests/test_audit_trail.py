from ironclad.core.audit import AuditTrail

def test_hash_chain_changes_on_payload_change():
    a = AuditTrail()
    a.add("X", {"v": 1})
    h1 = a.root_hash()

    b = AuditTrail()
    b.add("X", {"v": 2})
    h2 = b.root_hash()

    assert h1 != h2
