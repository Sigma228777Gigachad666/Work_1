def is_interesting_number():
    digits=[int(d) for d in input()]
    mx,mn =max(digits),min(digits)
    mid =sum(digits) - mx - mn
    print("Число интересное" if mx - mn ==mid else
    "Число неинтересное")
is_interesting_number()
