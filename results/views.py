import io
from django.shortcuts import render
from polls.models import Poll
from candidates.models import Candidate
from votes.models import Vote
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from datetime import datetime

# Create your views here.
def poll_results(request, id):

    poll = Poll.objects.get(id=id)

    total_poll_votes = len(Vote.objects.filter(poll=poll))

    all_poll_candidates = Candidate.objects.filter(poll=poll)

    candidate_results = []

    for candidate in all_poll_candidates:

        result = {
            'candidate': f'{candidate.first_name} {candidate.last_name}',
            'image': candidate.image.url,
            'total': len(Vote.objects.filter(candidate=candidate)),
        }

        candidate_results.append(result)

    context = {
        'poll_votes': total_poll_votes,
        'candidate_votes': candidate_results,
        'id': id,
    }

    return render(request, 'results/poll_results.html', context)

def generate_report(request, id):

    # Getting the data to draw on the canvas
    poll = Poll.objects.get(id=id)

    total_poll_votes = len(Vote.objects.filter(poll=poll))

    all_poll_candidates = Candidate.objects.filter(poll=poll)

    candidate_results = []

    for candidate in all_poll_candidates:

        result = {
            'Candidate': f'{candidate.first_name} {candidate.last_name}',
            'Total votes': len(Vote.objects.filter(candidate=candidate)),
        }

        candidate_results.append(result)

    text_list = []

    for candidate in candidate_results:
        text_list.append("----------------------------------------------------------------")
        text_list.append(" ")

        for key, value in candidate.items():

            text_list.append(f'{key}: {value}')
            text_list.append(" ")

    print(text_list)

    report_date = datetime.now().strftime("%d-%b-%Y | %I:%M %p")

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)

    # Draw things on the PDF. Here's where the PDF generation happens.

    # Create a text object
    text_object = p.beginText()

    text_object.setTextOrigin(inch, inch)

    # title
    text_object.setFont("Times-Roman", 20, leading=None)
    text_object.textLine(f'Poll results for {poll.seat} election')
    text_object.textLine(" ")

    # body
    text_object.setFont("Times-Roman", 18, leading=None)
    text_object.textLine(f'Total poll votes: {total_poll_votes}')
    text_object.textLine(" ")

    for text in text_list:

        text_object.setFont("Helvetica", 13, leading=None)
        text_object.textLine(text)

    text_object.setFont("Times-Roman", 13, leading=None)
    text_object.textLine("----------------------------------------------------------------")
    text_object.setFont("Courier", 10, leading=None)
    text_object.textLine(" ")
    text_object.textLine(f'Report generated on: {report_date}')

    p.drawText(text_object)

    # Close the PDF object cleanly, and we're done.
    p.setTitle(f'{poll.seat} report')
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers present the option to save the file.
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=False, filename=f'{poll.seat}_report.pdf')