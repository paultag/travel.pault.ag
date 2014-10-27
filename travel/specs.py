

SERVICE_PROVIDER_SPEC = {
    "exclude": [
        "rewards_account",
    ]
}

STOP_SPEC = {}
PLACE_SPEC = {}

LODGING_SPEC = {
    "include": [
        ("place", PLACE_SPEC),
    ],
    "exclude": [
        "rewards_account"
    ]
}

STAY_SPEC = {
    "fields": [
        ("lodging", LODGING_SPEC),
        "checkin",
        "checkout",
        "id",
        "complete",
    ]
}


LEG_SPEC = {
    "fields": [
        ("carrier", SERVICE_PROVIDER_SPEC),
        ("origin", STOP_SPEC),
        ("destination", STOP_SPEC),
        "departure",
        "arrival",
        "type",
        "complete",
        "active",
        "length",
        "percent",
    ]
}


TRIP_SPEC = {
    "fields": [
        ("user", {"fields": ["username"]}),
        "name",
        "reason",
        "start",
        "end",
        "id",
        ("legs", LEG_SPEC),
        ("stays", STAY_SPEC),
    ]
}
