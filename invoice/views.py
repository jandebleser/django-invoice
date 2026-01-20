from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from invoice.models import Invoice, CreditNote
from invoice.pdf import draw_pdf
from invoice.utils import pdf_response


def pdf_view(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return pdf_response(draw_pdf, invoice.file_name(), invoice)

def credit_note_pdf_view(request, pk):
    credit_note = get_object_or_404(CreditNote, pk=pk)
    return pdf_response(draw_pdf, credit_note.file_name(), credit_note)

@login_required
def pdf_user_view(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id, user=request.user)
    return pdf_response(draw_pdf, invoice.file_name(), invoice)
