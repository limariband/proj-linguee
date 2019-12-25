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
        "deck": arg
        }
    }


def add_note(deck, model, *args, **kwargs):
    return {
    "action": "addNote",
    "version": 6,
    "params": {
        "note": {
            "deckName": deck,
            "modelName": model,
            "fields": kwargs,
            "options": {
                "allowDuplicate": False
            },
            "tags": args,
            }
        }
    }


def find_notes(arg):
    return {
    "action": "findNotes",
    "version": 6,
    "params": {
        "query": f"deck:{arg}"
        }
    }


def notes_info(*args):
    return {
    "action": "notesInfo",
    "version": 6,
    "params": {
        "notes": args
        }
    }


def find_cards(arg):
    return {
    "action": "findCards",
    "version": 6,
    "params": {
        "query": f"deck:{arg}"
        }
    }


def cards_info(*args):
    return {
    "action": "cardsInfo",
    "version": 6,
    "params": {
        "cards": args
        }
    }
