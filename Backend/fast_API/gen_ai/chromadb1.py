import chromadb

client = chromadb.Client()

faq = client.get_or_create_collection(name="faq document")

faq.add(ids=["faq_1"],documents=["prepayment, reduce your emi"])

print(faq.count())
