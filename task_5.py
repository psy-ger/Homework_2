events = []  # global list of events


def event_calendar():
    """event_calendar with nested functions to manage events"""
    def add_event(event):
        events.append(event)  # add the event
        return f"Додано подію: {event}"

    def remove_event(event):
        """remove_event function to remove an event"""
        if event in events:  # check if event exists
            events.remove(event)  # remove the event
            return f"Видалено подію: {event}"
        else:
            return f"Подія '{event}' не знайдена"

    def view_events():
        """view_events function to list all events"""
        return f"Майбутні події: {events if events else 'Немає подій'}"

    return add_event, remove_event, view_events


# example usage
add_event, remove_event, view_events = event_calendar()
print(add_event("Зустріч 05.09.2025"))
print(add_event("Семінар 12.09.2025"))
print(add_event("Вечірка 20.09.2025"))
print(view_events())
print(remove_event("Семінар 12.09.2025"))
print(view_events())
print(remove_event("Немає такої події"))
print(view_events())
