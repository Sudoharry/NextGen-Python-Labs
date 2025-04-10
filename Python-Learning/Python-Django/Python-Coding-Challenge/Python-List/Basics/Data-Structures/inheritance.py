# Inheritance – Tool Usage by DevOps Engineers


class DevOps:
    def __init__(self, tool_name):
        self.tool_name = tool_name

    def use(self):
        return f"Use tools {self.tool_name}"

class TerraformTools(DevOps):
    def use(self):
        return f"Provision infrastructure using {self.tool_name}"
    
class AnsibleTools(DevOps):
    def use(self):
        return f"Configure the target machine using {self.tool_name}"
    
tools = [TerraformTools("Terraform"), AnsibleTools("Ansible")]

for t in tools:
    print(t.use())

#  Concepts: Inheritance, Method Overriding, Polymorphism