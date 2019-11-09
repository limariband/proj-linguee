def sync():
    return {
    "action": "sync",
    "version": 6
    }


def create_deck(arg):
    return {
    "action": "createDeck",
    "version": 6,
    "params": {
        "deck": "Japanese::Tokyo"
        }
    }


def add_note(deck, model, *args, **kwargs):
    return {
    "action": "addNote",
    "version": 6,
    "params": {
        "note": {
            "deckName": "Default",
            "modelName": "Basic",
            "fields": kwargs,
            "options": {
                "allowDuplicate": False
            },
            "tags": args,
            }
        }
    }
