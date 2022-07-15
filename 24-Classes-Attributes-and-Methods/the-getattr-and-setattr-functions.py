
stats = {
    "name": "BBQ Chicken",
    "price": 19.99,
    "size": "Extra Large",
    "ingredients": ["Chicken", "Onion", "BBQ Sauce"]
}


class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)


bbq = Pizza(stats)

print(bbq.size)
print(bbq.ingredients)

for attr in ["price", "name", "diameter", "discounted"]:
    print(getattr(bbq, attr, "unknown"))

# print("======================")

# def _get_uri_params(self, spider):
#     params = {}
#     for k in dir(spider):
#         params[k] = getattr(spider, k)
#     ts = datetime.utcnow().replace(microsecond=0).isoformat().replace(":", "-")
#     params["time"] = ts
#     self._uripar(params, spider)
#     return params
