ACTIVE = "ACTIVE"
SUSPENDED = "SUSPENDED"
WAITING = "WAITING"
STOPPED = "STOPPED"
MEMBERSHIP_STATUS = (
    (WAITING, "WAITING"),
    (ACTIVE, "ACTIVE"),
    (SUSPENDED, "SUSPENDED"),
    (STOPPED, "STOPPED")
)

POST_WITHOUT_REVIEW = "POST+"
POST_AFTER_REVIEW = "POST"
CANT_POST = "UNPOST"
NON = "NON"
MEMBER_ROLE = (
    (POST_WITHOUT_REVIEW, "post without review from editor"),
    (POST_AFTER_REVIEW, "post after review approve from editor"),
    (CANT_POST, "can't post"),
    (NON, "not")
)
