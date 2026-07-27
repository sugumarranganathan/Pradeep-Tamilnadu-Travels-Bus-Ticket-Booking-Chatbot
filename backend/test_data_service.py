
from backend.services.data_service import DataService

service = DataService()

print(service.get_routes())
print(service.get_buses())
print(service.get_timings())
print(service.get_fares())
