#Type Alias
from typing import Dict, List, NewType

#Type Alias
Hostname=str
Address=str
Server=Dict[Hostname, Address]
Network=List[Server]


#New Type
Hostname2=NewType('Local', str)
Address2=NewType('127.0.25.6', str)
Server2=NewType('Server2',Dict[Hostname2, Address2])
Network2=NewType('Network2',List[Server2])
print(Hostname2,'\n',Address2,'\n',Server2,'\n',Network2)

#use2
hostname=Hostname2('Local2')
address=Address('120.3.56.1')
server= Server2({hostname:address})
network=Network2([server])
print(hostname,'\n',address,'\n',server,'\n',network)
