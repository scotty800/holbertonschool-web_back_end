#!/usr/bin/env python3
"""log stats from collection"""


from pymongo import MongoClient

client = MongoClient()

db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})

methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
method_counts = {}
for method in methods:
    method_counts[method] = collection.count_documents({'method': method})

status_check = collection.count_documents({'method': 'GET', 'path': '/status'})

print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check} status check")
