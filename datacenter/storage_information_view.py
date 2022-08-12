from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []

    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in active_visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': visit.get_formatted_duration(),
                'is_strange': 'Да' if visit.is_long() else 'Нет',
            }
        )

    # Add a special 'is_strange' value for the security guard,
    # since he is always inside the storage and his 'visit' is always long.
    security_guard_entry = non_closed_visits[0]
    security_guard_entry.update({'is_strange': 'Охранник всегда подозрителен'})

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
