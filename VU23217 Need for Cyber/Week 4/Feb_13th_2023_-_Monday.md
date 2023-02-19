# Retail
## 1 - Details of the Environment
- Website
- Inventory Management
	- SKUs
	- Physical Product Management
	- Quantity
- CCTV
- Suppliers
	- Communication
	- Delivery
- POS
	- EFTPOS
	- Cash
	- Gift Cards
- Loyalty Programs
	- User Information
- Marketing
	- Social Media
	- Reviews

## 2 - Most Common Threat
- Data Breaches
- Physical Theft

## 3 - Create the Framework
- Identify
	- Physical Products
	- Customer Details
		- Financial Details?
- Protect
	- Servers
	- POS Devices
	- Domain Systems
- Detect
	- Central and Monitored Logging
	- IDS
- Respond
	- Relevant Procedures / Policies
	- Lock down affected devices
- Recover
	- Routine backups of all critical systems.

## 4 - CIS Controls
???

## 5 - Essential 8
???

# Risks
- Attackers Compromise the Website.
	- CIS 3.14 **Detect**: Log Sensitive Data Access
	- CIS 4.4 **Protect**: Implement and Manage a Firewall on Servers
	- CIS 5.2 **Protect**: Use Unique Passwords
	- CIS 5.3 **Respond**: Disable Dormant Accounts
	- CIS 6.3 **Protect**: Require MFA for Externally Exposed Applications
- Attackers gain access to POS/checkout systems.
	- ???
- Critical Systems Fail, causing a loss of service.
	- CIS 3.1 **Identify**: Establish and Maintain a Data Management Process
	- CIS 3.4 **Protect**: Enforce Data Retention
	- CIS 3.13 **Protect**: Deploy a Data Loss Prevention Solution
	- CIS 11.1 **Recover**: Establish and Maintain a Data Recovery Process
	- CIS 11.2 **Recover**: Perform Automated Backups


# Risk 1 Attackers compromise the website 
| CIS Controls                                                         | Essential 8                                                                                                                                                                                                                                                                                                             | ISM |     |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |
| CIS 3.14 **Detect**: Log Sensitive Data Access                       | Patch Applications - A vulnerability scanner with an up-to-date vulnerability database is used for vulnerability scanning activities. Patches, updates or vendor mitigations for security vulnerabilities in internet-facing services are applied within two weeks of release, or within 48 hours if an exploit exists. |ISM-0824 - Personnel are advised not to send or receive files via unauthorised online services.      |     |
| CIS 4.4 **Protect**: Implement and Manage a Firewall on Servers      | Restrict administrative privileges - Privileged users use separate privileged and unprivileged operating environments.                                                                                                                                                                                                  |ISM-1733 - Requests for privileged access to data repositories are validated when first requested.     |     |
| CIS 5.2 **Protect**: Use Unique Passwords                            | Multi Factor Authentication **Maturity Level 2** - Multi-factor authentication is used to authenticate privileged users of systems.                                                                                                                                                                                     |  ISM-0383 - Default accounts or credentials for operating systems, including for any pre-configured accounts, are changed.  |     |
| CIS 5.3 **Respond**: Disable Dormant Accounts                        | Restrict administrative privileges **Maturity Level 2** - Privileged access events are centrally logged. Privileged account and group management events are centrally logged.                                                                                                                                           |     |     |
| CIS 6.3 **Protect**: Require MFA for Externally Exposed Applications |                                                                                                                                                                                                                                                                                                                         |     |     |
