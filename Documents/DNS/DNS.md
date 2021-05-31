- Domain Name System
- phonebook of the Internet
- domain names(google.com), DNS is responsible finding correct IP address 
- Browsers use those addresses to communicate with origin servers or CDN edge servers to access website information
- server: device or program provids services to other programs(clients)
- DNS clients (built into most modern desktop and mobile operating systems) enable web browsers to interact with DNS servers
- typical DNS query: four servers, work together,deliver an IP address to the client: recursive resolvers, root nameservers, TLD nameservers, and authoritative nameservers.
- DNS recursor (= DNS resolver) a server receives the query from the DNS client, interacts with other DNS servers to hunt down the correct IP
- resolver receives request from client-> behaves as a client, querying the other three types of DNS servers in search of the right IP
- DNS-Recurser:responds to a DNS query, asks other DNS servers for the address or has already stored the IP address of the website 
- Root-Name-Server: Name-Server for the Root-zone, reacts on direct query, gives back a list of authoritative name server for the corresponding top-level domain 
- TLD-Name-Server: Top-Level-Domain-Server, belongs to the high-level DNS servers on the Internet
- Autoritativer Name-Server: endstation of a DNS query, the DNS record for the query is on it
- for www.beispiel.com, a TLD server for ".com" responds first, after that, DNS searches for "example"
- two types of DNS query
- Recursive DNS Resolver: DNS server that responds to the DNS query and looks for the authoritative name server or a cached DNS result for the requested name
- Authoritative DNS server: stores DNS query, if you ask for one of its IP addresses, it does not have to ask another server, final authority for these names and IP addresses
- some DNS Server are connected to adblock, they use server all over the world
- because of that they can track and block sites which are connected to advertising or non-serious