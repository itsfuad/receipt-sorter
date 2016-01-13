"""Calculate per-merchant spending from exported expense rows."""

def analyze(text):
    import csv,io,decimal
    totals={};skipped=0
    for row in csv.reader(io.StringIO(text)):
        if len(row)<3:skipped+=1;continue
        date,shop,value=[c.strip() for c in row[:3]]
        if not date or not shop:skipped+=1;continue
        try: amount=decimal.Decimal(value)
        except decimal.InvalidOperation:skipped+=1;continue
        totals[shop]=totals.get(shop,decimal.Decimal(0))+amount
    return {'merchants':{k:str(v) for k,v in sorted(totals.items())},'skipped':skipped}
