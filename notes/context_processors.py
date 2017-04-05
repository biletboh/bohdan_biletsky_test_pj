from notes.models import Notes


def notes_count_processor(request):
    notes = Notes.objects.all()            
    return {'all_notes': notes.count()}

