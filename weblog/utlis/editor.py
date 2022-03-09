DEL_ARTICLE = "DEL"
SUS_ARTICLE = "SUS"
REVIEW_ARTICLE = "REVIEW"
NON = "NON"

EDITOR_PERMISSION = (
    (DEL_ARTICLE, "can delete article"),
    (SUS_ARTICLE, "can suspend "),
    (REVIEW_ARTICLE, "can review and approve article"),
    (NON, "non")
)
