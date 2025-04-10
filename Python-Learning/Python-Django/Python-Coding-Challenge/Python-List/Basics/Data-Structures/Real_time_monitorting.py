class Monitor():
    def __init__(self, name):
        self.name = name
        self.status = "Unknown"
    
    def update_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return f"{self.name} service status: {self.status}"
    
    

class Prometheus(Monitor):
    def get_status(self):
        return f"[Promethus]: Scraping metrics — Status:  {self.status}"


class Grafana(Monitor):
    def get_status(self):
        return f"[Grafana]: Displaying dashboards — Status: {self.status}"


services = [Prometheus("Prometheus"), Grafana("Grafana")] 

services[0].update_status("Healthy ✅")
services[1].update_status("Running with alerts ⚠️")

for s in services:
    print(s.get_status())


        
