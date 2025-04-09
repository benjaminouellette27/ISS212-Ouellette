#Benjamin M Ouellette
#Citations
#----------
#Week 11 - Tool Development 7 Walkthrough
#used chatgpt to fix my indentation within the try statement.

#importing modules.
import dns.resolver

# LEAVE THESE LINES: Force the resolver to use Cloudflare DNS
dns.resolver.default_resolver = dns.resolver.Resolver()
dns.resolver.default_resolver.nameservers = ['1.1.1.1']

#Target Domain.
domain = "wikipedia.com"

try:
    #Getting the A and AAAA records from the target domain.
    a_records = dns.resolver.resolve(domain, 'A')
    aaaa_records = dns.resolver.resolve(domain, 'AAAA')

    #opening the file.
    with open("domain3script2.txt", "w") as f:
        #writing records to file.
        f.write(f"A Records for {domain}:\n")
        for record in a_records:
            f.write(record.to_text() + "\n")

        #writing records to file.
        f.write(f"AAAA Records for {domain}:\n")
        for record in aaaa_records:
            f.write(record.to_text() + "\n")

    #output.
    print("DNS records written to text file")
    #error handling.
except Exception as e:
    print("Error:", e)
