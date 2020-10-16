from ..models import Document


def get_all_documents():
    documents = Document.objects.all()
    return documents
