Domain Name System
<p>phonebook of the Internet
<p>domain names(google.com), DNS is responsible finding correct IP address 
<p>Browsers use those addresses to communicate with origin servers or CDN edge servers to access website information
<p>server: device or program provids services to other programs(clients)
<p> DNS clients (built into most modern desktop and mobile operating systems) enable web browsers to interact with DNS servers
<p>typical DNS query: four servers, work together,deliver an IP address to the client: recursive resolvers, root nameservers, TLD nameservers, and authoritative nameservers.
<p>DNS recursor (= DNS resolver) a server receives the query from the DNS client, interacts with other DNS servers to hunt down the correct IP
<p>resolver receives request from client-> behaves as a client, querying the other three types of DNS servers in search of the right IP
<p>DNS-Recurser:responds to a DNS query, asks other DNS servers for the address or has already stored the IP address of the website 
<p>Root-Name-Server: Name-Server for the Root-zone, reacts on direct query, gives back a list of authoritative name server for the corresponding top-level domain 
<p>TLD-Name-Server: Top-Level-Domain-Server, belongs to the high-level DNS servers on the Internet
<p>Autoritativer Name-Server: endstation of a DNS query, the DNS record for the query is on it
<p>for www.beispiel.com, a TLD server for ".com" responds first, after that, DNS searches for "example"
<p>two types of DNS query
<p>Recursive DNS Resolver: DNS server that responds to the DNS query and looks for the authoritative name server or a cached DNS result for the requested name
<p>Authoritative DNS server: stores DNS query, if you ask for one of its IP addresses, it does not have to ask another server, final authority for these names and IP addresses
<p>
<p> some DNS Server are connected to adblock, they use server all over the world
<p> because of that they can track and block sites which are connected to advertising or non-serious