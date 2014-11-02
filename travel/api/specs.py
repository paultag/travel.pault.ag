

SERVICE_PROVIDER_SPEC = {
    "exclude": [
        "rewards_account",
    ]
}

STOP_SPEC = {}
PLACE_SPEC = {}

USER_SPEC = {
    "fields": [
        "username",
        "first_name",
        "last_name"
    ]
}

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
        ("user", USER_SPEC),
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
        "number",
    ]
}


TRIP_SPEC = {
    "fields": [
        ("user", USER_SPEC),
        "name",
        "reason",
        "start",
        "end",
        "id",
        ("legs", LEG_SPEC),
        ("stays", STAY_SPEC),
    ]
}
