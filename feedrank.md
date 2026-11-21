# feedrank — 2026-11-21

_80 items, 5d window._

### 1. [Apache Roller: Apache Roller Deserialization of Untrusted Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-129448)
_CISA KEV · Nov 21 · score 1.626 · **CRITICAL 9.5** · ×8 reports · CVE-2025-42884, CVE-2026-123890, CVE-2026-129448_

Apache Roller contains a deserialization of untrusted data vulnerability that allows an unauthenticated remote attacker to execute arbitrary code via the XML-RPC endpoint, which accepts and deserializes vendor extension types before authentication. This CVE covers the same underlying vulnerability a…

`deserialization` `cve-`

_also: [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-123890), [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-76466), [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/20/cisa-adds-four-known-exploited-vulnerabilities-catalog), [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-critical-vmware-cisco.html), [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html)_

### 2. [GnuPG Warns Critical GPGME Flaw Could Expose App Data via Malicious OpenPGP Keys](https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html)
_The Hacker News · Nov 21 · score 0.464 · **CRITICAL 9.5** · CVE-2026-129975_

A malicious OpenPGP key with an unusually long user ID can trigger a critical memory bug in GPGME, the standard library that programs use to work with GnuPG. The GnuPG project warned yesterday that the flaw could be used to steal data from affected applications and has released fixed versions. The b…

`cve-`

### 3. [Attackers' AI Agents Found a Zero-Day in Medical-Imaging Software and Gained Root Access](https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html)
_The Hacker News · Nov 21 · score 0.242 · **CRITICAL 9.0**_

Suspected China-linked hackers used autonomous AI agents to find a previously unknown flaw in MONAI Label, an open-source medical imaging server, and gain root access to a university server, Amazon Threat Intelligence said this week. The flaw allows an attacker with no account to write files outside…

`zero-day`

### 4. [Unauthenticated Remote Code Execution in NGINX: CVE-2026-123633 and CVE-2026-123007](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
_Wiz Research · Nov 20 · score 2.051 · **CRITICAL 9.5** · ×3 reports · CVE-2026-123007, CVE-2026-123633_

Two critical HTTP/2 flaws can allow attackers to compromise NGINX servers, putting the websites, APIs, and sensitive data they handle at risk.

`cve-`

_also: [StepSecurity](https://www.stepsecurity.io/blog/cve-2026-123007-nginx-http2-rce), [The Hacker News](https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html)_

### 5. [F5 releases emergency patches for critical BIG-IP RCE flaws](https://www.bleepingcomputer.com/news/security/f5-releases-emergency-patches-for-critical-big-ip-rce-flaws/)
_BleepingComputer · Nov 20 · score 0.649 · **CRITICAL 9.5**_

US cybersecurity company F5 warned customers to patch five critical BIG-IP vulnerabilities that attackers can exploit to trigger denial-of-service (DoS) or gain remote code execution. [...]

`f5` `rce` `exploit`

### 6. [VMware patches vCenter zero-day exploited in attacks since September](https://www.bleepingcomputer.com/news/security/vmware-patches-vcenter-zero-day-exploited-in-attacks-since-september/)
_BleepingComputer · Nov 20 · score 0.532 · **CRITICAL 9.5**_

Broadcom has released security updates to fix a critical VMware vCenter Server authentication bypass vulnerability that Chinese-linked hackers have exploited in zero-day attacks since September 2026. [...]

`vmware` `vcenter` `zero-day` `authentication bypass`

### 7. [Hackers use autonomous AI tool Cairn to find zero-day, take over server](https://www.bleepingcomputer.com/news/security/hackers-use-autonomous-ai-tool-cairn-to-find-zero-day-take-over-server/)
_BleepingComputer · Nov 20 · score 0.231 · **CRITICAL 9.0**_

Threat actors used the open-source AI penetration-testing framework Cairn to find a previously unknown vulnerability in a medical imaging application. [...]

`zero-day`

### 8. [SonicWall Warns Gen 6 Firewalls Won't Get Security Patches, Even for Critical Flaws](https://thehackernews.com/2026/11/sonicwall-warns-gen-6-firewalls-wont.html)
_The Hacker News · Nov 20 · score 0.184 · **CRITICAL 9.5**_

SonicWall has urged all customers still running Generation 6 firewalls to retire and replace them immediately and stop exposing the devices on the internet edge, citing security risks fueled by AI-assisted attacks. "Attackers now use automation and AI to find and exploit unsupported edge devices fas…

`sonicwall` `edge` `exploit`

### 9. [New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs on It](https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html)
_The Hacker News · Nov 20 · score 0.128 · **CRITICAL 9.0**_

A newly disclosed unpatched zero-day technique called FastUnlock lets someone with physical access to a locked Windows computer start programs without signing in. Whoever uses it gets only a limited account, not administrator control of the machine. The method was posted yesterday by a researcher wh…

`windows` `zero-day`

### 10. [Bazuka Android Malware Uses Fake Screen Overlays to Hide Credential Theft and Device Control](https://thehackernews.com/2026/11/bazuka-android-malware-uses-fake-screen.html)
_The Hacker News · Nov 20 · score 0.315 · **HIGH 8.5**_

Cybersecurity researchers have disclosed details of a previously unknown Android malware framework called Bazuka that offers large language model (LLM) integration for victim management and control at scale. Dutch mobile security company ThreatFabric said it discovered the threat in late October 202…

`credential`

### 11. [Critical VMware vCenter Zero-Day Flaw Lets Network Attackers Bypass Authentication](https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html)
_The Hacker News · Nov 19 · score 0.569 · **CRITICAL 9.5**_

A critical flaw in VMware vCenter lets an attacker with network access bypass authentication and gain unauthorized access to the system, Broadcom, which owns VMware, said in an advisory published today. Fixed versions are out for all supported branches, and the company lists no workaround. vCenter i…

`vmware` `vcenter` `zero-day`

### 12. [PHP Fixes 7 Critical Flaws, Including Bugs That Could Allow Remote Code Execution](https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html)
_The Hacker News · Nov 19 · score 0.535 · **CRITICAL 9.5** · CVE-2026-115560_

The PHP Foundation has released security updates to address multiple critical security flaws that could be exploited to achieve remote code execution on affected deployments, including CVE-2026-115560. The release of the patch follows an advance notice in which the project maintainers alerted users …

`php` `cve-`

### 13. [Ruby2Shell: Ruby Memory Corruption Flaws Expose Applications to Remote Code Execution, But is it an Actual Risk?](https://www.ox.security/blog/ruby2shell-ruby-memory-corruption-flaws-expose-applications-to-remote-code-execution-but-is-it-an-actual-risk/)
_OX Security · Nov 19 · score 0.409 · **CRITICAL 9.0**_

A one-byte heap overflow in Ruby&#8217;s string case conversion, plus six related flaws in the regex engine, could let attackers crash or take over Ruby applications. Administrators are urged to upgrade to Ruby 4.0.10, 3.4.13 or 3.3.14. On November 18, 2026, the Ruby core team disclosed seven vulner…

`ruby`

### 14. [libumqtt](https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-03)
_CISA Advisories · Nov 19 · score 0.372 · **CRITICAL 9.5** · CVE-2026-125132_

View CSAF Summary Successful exploitation of this vulnerability could allow a remote attacker to cause a denial of service, memory corruption, or information disclosure. The following versions of libumqtt are affected: libumqtt &lt;=1.1.1 (CVE-2026-125132) CVSS Vendor Equipment v3 8.6 libumqtt libum…

`cve-` `cvss`

### 15. [Autonomy Logic OpenPLC Runtime](https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01)
_CISA Advisories · Nov 19 · score 0.320 · **CRITICAL 9.5** · CVE-2026-126088_

View CSAF Summary Successful exploitation of this vulnerability could allow several unauthenticated admin accounts to be created. The following versions of Autonomy Logic OpenPLC Runtime are affected: OpenPLC Runtime &lt;=4.2.4 (CVE-2026-126088) CVSS Vendor Equipment v3 8.1 Autonomy Logic OpenPLC Ru…

`cve-` `cvss`

### 16. [phpAfterShell and Critical PHP RCE Vulnerabilities: Everything You Need To Know](https://www.wiz.io/blog/phpaftershell-critical-php-rce-vulnerabilities-cve-2026-126714)
_Wiz Research · Nov 19 · score 0.305 · **CRITICAL 9.5**_

Detect and mitigate phpAfterShell, and additional critical vulnerabilities from PHP's November release that may enable remote code execution.

`php` `rce`

### 17. [NGINX2Root: Five RCE bugs in NGINX, a Linux kernel path to root, and how to detect exploitation](https://webflow.sysdig.com/blog/nginx2root)
_Sysdig · Nov 19 · score 0.272 · **CRITICAL 9.0**_

`linux` `kernel` `rce`

### 18. [Elecbrakes EB2, VM1, ELBC2000](https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-02)
_CISA Advisories · Nov 19 · score 0.240 · **CRITICAL 9.5** · CVE-2026-124281, CVE-2026-125273, CVE-2026-96805_

View CSAF Summary Successful exploitation of these vulnerabilities could allow an attacker to gain control of the brakes of a trailer, modify the firmware, disable the brake lights, modify the brake conditions or disable other critical safety features. The following versions of Elecbrakes EB2, VM1, …

`cve-` `cvss`

### 19. [The 2026 Vulnpocalypse Hits PHP: Four Critical RCEs, but How Dangerous Are They?](https://www.ox.security/blog/the-2026-vulnpocalypse-hits-php-four-critical-rces-but-how-dangerous-are-they/)
_OX Security · Nov 19 · score 0.216 · **CRITICAL 9.5**_

PHP has patched four critical remote code execution vulnerabilities, each rated 9.2. But exploiting them requires specific conditions, raising questions about their real-world risk. Here&#8217;s what security teams need to know. On November 19, 2026, PHP released security updates for versions 8.5, 8…

`php` `teams`

### 20. [Cry2Wolf: Not Every Branded Bug Deserves a Fire Drill](https://www.ox.security/blog/cry2wolf-not-every-branded-bug-deserves-a-fire-drill/)
_OX Security · Nov 19 · score 0.188 · **CRITICAL 9.5**_

Security teams are burning out on vulnerability hype. Here&#8217;s how to tell a real threat from a nothingburger. Every few days, sometimes every few hours, a new vulnerability arrives with a name, a logo, and a countdown clock. The headlines call it critical. The vendor emails follow within the ho…

`teams`

### 21. [Ruby Ships Fixes for 7 Flaws, Including Critical Ruby2Shell, Said to Hit Default Rails Apps Pre-Auth](https://thehackernews.com/2026/11/ruby-releases-fixes-for-7-regex-and.html)
_The Hacker News · Nov 19 · score 0.183 · **CRITICAL 9.5**_

Ruby contains seven memory-safety flaws in its regular expression engine and its string case-conversion code. For five of them, its maintainers say, proof-of-concept exploits, or PoCs, have shown that crafted input can run code on the machine. "We are aware of PoCs that prove some of them can be use…

`ruby`

### 22. [PHP Warns of Critical Security Flaws Affecting All Supported Versions, Fixes Coming November 19](https://thehackernews.com/2026/11/php-warns-of-critical-security-flaws.html)
_The Hacker News · Nov 19 · score 0.146 · **CRITICAL 9.5**_

The maintainers of the PHP programming language on Wednesday issued an advisory announcing an upcoming security release that addresses critical flaws. The release is scheduled for November 19, 2026, between 2 and 2:30 p.m. UTC. "These releases are part of PHP's regular four-week release cycle and wi…

`php`

### 23. [Researcher Demonstrates Database RCE Exploits Affecting PostgreSQL, MySQL and Oracle](https://thehackernews.com/2026/11/researcher-demonstrates-database-rce.html)
_The Hacker News · Nov 19 · score 0.114 · **CRITICAL 9.0**_

Low-privilege database accounts that cannot read a single application table can still be used to run code on the database server itself, a researcher has shown, by reaching memory-corruption bugs in the engine code behind ordinary SQL. The exploits, published yesterday, are the researcher's proofs o…

`postgresql` `mysql` `clickhouse` `rce`

### 24. [Attackers Compromise Microsoft's Agent Framework PyPI Package to Steal Cloud Credentials](https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html)
_The Hacker News · Nov 18 · score 0.757 · **CRITICAL 9.0**_

Threat actors have compromised Microsoft's agent-framework package to push a credential stealer, according to reports from Aikido, Chainguard, Endor Labs, OX Security, SafeDep, Socket, StepSecurity, and Google-owned Wiz. The malicious versions, 1.26.1 and 1.26.2, were published 33 minutes apart on N…

`pypi` `python` `credential` `stealer`

### 25. [CVE-2026-114938 OpenJDK RCE (Java4Shell): Everything You Need to Know](https://www.wiz.io/blog/cve-2026-114938-rce-java4shell-openjdk)
_Wiz Research · Nov 18 · score 0.689 · **CRITICAL 9.5** · ×9 reports · CVE-2026-114938_

Detect and mitigate Java4Shell (CVE-2026-114938), a critical 9.2 RCE vulnerability affecting OpenJDK and major Java-based applications.

`java` `rce` `cve-`

_also: [Sysdig](https://webflow.sysdig.com/blog/java4shell-cve-2026-114938-pre-auth-rce-in-openjdk), [Datadog Security Labs](https://securitylabs.datadoghq.com/articles/java4shell-remote-code-execution-in-openjdk-cve-2026-114938/), [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/17/critical-java-vulnerability-requires-immediate-patching), [Endor Labs](https://www.endorlabs.com/learn/java4shell-unauthenticated-rce-reported-in-openjdk-17-cve-2026-114938), [OX Security](https://www.ox.security/blog/java4shell-cve-2026-114938-rce-risk/)_

### 26. [NGINX2Root: Five Critical NGINX Flaws Expose Web Servers to Remote Code Execution](https://www.ox.security/blog/nginx2root-five-critical-nginx-flaws-expose-web-servers-to-remote-code-execution/)
_OX Security · Nov 18 · score 0.416 · **CRITICAL 9.5**_

Unauthenticated attackers can run code on NGINX servers through HTTP/2, HTTP/3, proxying and mail proxy setups. Administrators are urged to upgrade to 1.31.9 immediately. On November 18, 2026, F5 released fixes for five NGINX vulnerabilities, which researchers have named nginx2root. Xint&#8217;s res…

`f5`

### 27. [Perforce Puppet Enterprise: Perforce Puppet Enterprise Deserialization of Untrusted Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-115731)
_CISA KEV · Nov 18 · score 0.346 · **CRITICAL 9.5** · ×3 reports · CVE-2026-115731_

Perforce Puppet Enterprise contains a deserialization of untrusted data vulnerability in Puppet’s report-processing code that allows a client with any CA-signed agent certificate to execute arbitrary code on the Puppet Server as the service user by submitting a report containing a crafted rich-data …

`certificate` `ca` `exploit` `deserialization`

_also: [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/17/cisa-adds-one-known-exploited-vulnerability-catalog), [The Hacker News](https://thehackernews.com/2026/11/hackers-exploiting-critical-puppet-rce.html)_

### 28. [Vanderbilt University Research Electronic Data Capture (REDCap): Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-90817)
_CISA KEV · Nov 18 · score 0.320 · **CRITICAL 9.0** · CVE-2026-90817_

Vanderbilt University Research Electronic Data Capture (REDCap) contains a code injection vulnerability which could allow an unauthenticated attacker to execute arbitrary code on the server. An attacker could exploit this via crafted HTTP requests that access an unintended controller route from a pu…

`exploit`

### 29. [OX Security Launches OX Radar and Response Center to Show Companies Which Cyber Threats Actually Affect Them](https://www.ox.security/blog/ox-radar-response-center-launch/)
_OX Security · Nov 18 · score 0.242 · **CRITICAL 9.5**_

New capabilities monitor critical vulnerabilities and supply chain threats, automatically assessing customer exposure and guiding remediation NEW YORK, November 18, 2026 &#8212; OX Security, a leader in AI-native application protection, today announced the launch of OX Radar and Response Center, giv…

`supply chain` `teams`

### 30. [F5 Warns 6 Critical BIG-IP Flaws Can Crash Traffic in Specific Setups, May Allow RCE](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)
_The Hacker News · Nov 18 · score 0.210 · **CRITICAL 9.5**_

Six critical vulnerabilities in F5 BIG-IP allow an attacker to crash the Traffic Management Microkernel (TMM) without logging in, disrupting traffic until the TMM restarts. Each flaw needs a specific setup on a virtual server: an iRule that uses a particular command, or an APM policy that includes t…

`f5` `rce`

### 31. [Introducing OX Radar & Response Center: When News Breaks, Know If You’re Affected](https://www.ox.security/blog/introducing-ox-radar-response-center-when-news-breaks-know-if-youre-affected/)
_OX Security · Nov 18 · score 0.197 · **CRITICAL 9.5**_

TL;DR When a critical CVE drops, the first question every security team asks is simple: are we affected? Answering it is not as simple. For most teams, it still means emergency sweeps, every team pulled into a war room, and a full day lost before the answer lands. Today we&#8217;re introducing OX Ra…

`teams`

### 32. [Optimizely Supply Chain Attack Distributes Malware Across Global Brands](https://socket.dev/blog/optimizely-supply-chain-attack?utm_medium=feed)
_Socket Blog · Nov 18 · score 0.681 · **HIGH 8.5**_

Attackers exploited Optimizely to inject malicious JavaScript into major websites, delivering cryptocurrency clippers, card skimmers, and iOS malware.

`javascript` `supply chain`

### 33. [Risky Bulletin: Optimizely hijacked to deliver malware](https://risky.biz/RBNEWS635/)
_Risky Business News · Nov 18 · score 0.153 · **HIGH 8.5**_

Hackers hijack Optimizely to deliver malware through 178 popular websites, hackers breach Japanese supercomputers, Microsoft Edge to get a Lockdown Mode, and the EU sanctions NoName057.

`edge` `breach`

### 34. [Microsoft agent-framework Compromised: Credential Stealer Targets Azure and CI Pipelines](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi)
_Wiz Research · Nov 17 · score 1.329 · **CRITICAL 9.0**_

On November 17, 2026 at 20:35 UTC, versions 1.26.1 & 1.26.2 of the Microsoft PyPI package agent-framework were published with an added credential stealer. The package gets almost 200k downloads a month. The malicious versions have since been quarantined.

`pypi` `azure` `credential` `stealer`

### 35. [Microsoft’s agent-framework PyPI package Compromised with Credential Stealer](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer?utm_medium=feed)
_Socket Blog · Nov 17 · score 1.303 · **CRITICAL 9.0**_

Compromised agent-framework versions 1.26.1 and 1.26.2 on PyPI use .pth startup hooks to exfiltrate Azure, GitHub Actions, and CI/CD credentials.

`pypi` `github` `github actions` `ci/cd` `azure`

### 36. [OPTIMJACK: When Trusted JavaScript Becomes a Supply Chain Attack](https://www.reversinglabs.com/blog/optimjack-when-trusted-javascript-becomes-a-supply-chain-attack)
_ReversingLabs · Nov 17 · score 0.472 · **CRITICAL 9.5**_

How a vulnerability in Optimizely exposed visitors of at least 178 organizations’ websites to malicious code, revealing a critical blind spot in third-party software trust.

`javascript` `supply chain`

### 37. [Siemens Industrial Software Products](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-04)
_CISA Advisories · Nov 17 · score 0.316 · **CRITICAL 9.5** · ×2 reports · CVE-2026-111497_

View CSAF Summary On October 21, 2026, the Node.js project released security updates addressing a critical vulnerability in the Brotli decoder bundled with Node.js, commonly referred to as "Node2Shell" (tracked as CVE-2026-111497). The vulnerability is an out-of-bounds write that could allow a remot…

`node` `cve-`

_also: [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-03)_

### 38. [Researchers Claim Two RCE Exploits That Bypass Telegram’s New Android Defenses](https://thehackernews.com/2026/11/researchers-claim-two-rce-exploits-that.html)
_The Hacker News · Nov 17 · score 0.266 · **CRITICAL 9.0**_

A malicious widget can bypass the security filter that Telegram added to its Android app last week and run code outside it, according to NebuSec, a security company. Widgets are small interactive blocks that bots send inside chat messages, and their JavaScript runs on the user's phone. The researche…

`javascript` `rce`

### 39. [Siemens RUGGEDCOM APE1808](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-07)
_CISA Advisories · Nov 17 · score 0.226 · **CRITICAL 9.5** · CVE-2026-106175_

View CSAF Summary Fortinet has published information on a Double Free vulnerability in FortiOS. This advisory lists the related Siemens Industrial products. Siemens recommends to update Fortigate NGFW to V7.6.9 or later following the secure update recommendation procedure. Contact customer support t…

`fortinet` `cve-` `cvss`

### 40. [Siemens SIMATIC WinCC](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-09)
_CISA Advisories · Nov 17 · score 0.136 · **CRITICAL 9.0** · CVE-2026-59082_

View CSAF Summary Graphics Designer of SIMATIC WinCC before V8.2 contains an implicit active content execution vulnerability upon opening files, which could allow an attacker to cause arbitrary code execution on the device. Siemens is preparing fixes and recommends specific mitigations for products …

`v8` `cve-` `cvss`

### 41. [Siemens ROS#](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-06)
_CISA Advisories · Nov 17 · score 0.125 · **CRITICAL 9.5** · CVE-2026-109097_

View CSAF Summary ROS# before version 2.3.1 contains a code injection vulnerability that could allow an attacker that is able to pass a crafted message definition file to the user to inject arbitrary code into the generated program. Siemens has released a new version for ROS# and recommends to updat…

`cve-` `cvss`

### 42. [What Is Mythos and Why It Matters for Software Security | Endor Labs](https://www.endorlabs.com/learn/what-is-mythos-and-why-it-matters-for-software-security)
_Endor Labs · Nov 17 · score 0.101 · **CRITICAL 9.0**_

Learn what Mythos is, how it found zero-day bugs, and why Mythos could reshape software security and vulnerability prioritization

`zero-day`

### 43. [Siemens Simcenter Femap](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-10)
_CISA Advisories · Nov 17 · score 0.101 · **CRITICAL 9.5** · CVE-2026-64629_

View CSAF Summary Simcenter Femap is affected by an out of bounds read vulnerability that could be triggered when the application reads files in X_T format. This could allow an attacker to crash the application or execute arbitrary code. Siemens has released a new version for Simcenter Femap and rec…

`cve-` `cvss`

### 44. [N-able Patches 17 N-central Flaws as Attackers Exploit Earlier Bugs to Deploy Crypto Miners](https://thehackernews.com/2026/11/n-able-patches-17-n-central-flaws-as.html)
_The Hacker News · Nov 17 · score 0.063 · **CRITICAL 9.5**_

N-able has released a new security update to address additional critical security flaws impacting N-central. Describing N-central 2026.4 Hotfix 3 as a critical security update, the company said it includes a number of security patches and fixes that enhance the security of the Remote Monitoring and …

`exploit`

### 45. [BREAKING: Hijacked Releases of Microsoft’s Official agent-framework Steals Azure and CI Credentials](https://www.ox.security/blog/breaking-hijacked-releases-of-microsofts-official-agent-framework-steals-azure-and-ci-credentials/)
_OX Security · Nov 17 · score 0.343 · **HIGH 8.5**_

Two releases of Microsoft&#8217;s official agent-framework Python package were hijacked to harvest Azure and CI credentials. Traced by OX Radar, the supply chain attack executes automatically on Python startup&#8212;no import required. Overview A popular official Microsoft Python package, with 192,5…

`python` `supply chain` `azure`

### 46. [Hijacked Optimizely Scripts Served Card Skimmer and iOS Exploit Kits to CNN, BBC and Zoom Visitors](https://thehackernews.com/2026/11/hijacked-optimizely-scripts-served-card.html)
_The Hacker News · Nov 17 · score 0.096 · **HIGH 8.5**_

An attacker exploited a flaw in Optimizely Web Experimentation to plant malicious code in some of the scripts that customers' websites load from the service, Optimizely said early today. Visitors to sites run by at least 178 organizations, including CNN, the BBC and Zoom, received the code yesterday…

`zoom` `exploit`

### 47. [Microsoft Entra Connect Health flaw exploited to steal tenant data](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)
_BleepingComputer · Nov 21 · score 0.230_

Microsoft is warning organizations that it suffered a data breach after attackers exploited a vulnerability in its Entra Connect Health service to gain unauthorized access to administrator email addresses and tenant configuration information. [...]

`entra` `breach`

### 48. [Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host Memory on AMD Hosts](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html)
_The Hacker News · Nov 20 · score 0.493 · CVE-2026-99312_

A flaw in KVM, the hypervisor built into the Linux kernel, let researchers read about 127 GB of a cloud server's memory from inside a virtual machine of their own on DigitalOcean. On a shared server, that memory can include other customers' virtual machines. The flaw, tracked as CVE-2026-99312, affe…

`kvm` `linux` `kernel` `cve-`

### 49. [RUSTSEC-2026-0587: Vulnerability in wasmtime-wasi](https://rustsec.org/advisories/RUSTSEC-2026-0587.html)
_RustSec · Nov 20 · score 0.337_

WASI filesystem sandbox escape on Windows through a drive-prefixed path component

`windows`

### 50. [OPTIMJACK: Optimizely-Hosted Scripts Loaded a Crypto Clipper and Card Skimmer on 178 Organizations](https://www.stepsecurity.io/blog/optimjack-optimizely-hosted-scripts-crypto-clipper-card-skimmer)
_StepSecurity · Nov 20 · score 0.234_

Optimizely confirmed an attacker injected malicious JavaScript into customer projects. What the payload does, who was hit, and what to check.

`javascript`

### 51. [Vendor data breach exposes Chase, Visa, Mastercard customer info](https://www.bleepingcomputer.com/news/security/vendor-data-breach-exposes-chase-visa-mastercard-customer-info/)
_BleepingComputer · Nov 20 · score 0.208_

J.P. Morgan Chase warned it suffered a data breach after a cyberattack at a third-party service provider exposed customers' personal information and marketing data. [...]

`breach`

### 52. [N-able says recent security breach led to major service outage](https://www.bleepingcomputer.com/news/microsoft/n-able-says-recent-security-breach-led-to-major-service-outage/)
_BleepingComputer · Nov 20 · score 0.182_

N-able says attackers who breached one of its servers have caused a major outage affecting Mail Assure and SpamExperts Hosted Cloud services worldwide. [...]

`breach`

### 53. [Still tracking company passwords in spreadsheets? You’re flying blind.](https://www.bleepingcomputer.com/news/security/still-tracking-company-passwords-in-spreadsheets-youre-flying-blind/)
_BleepingComputer · Nov 20 · score 0.128_

Tracking company passwords in spreadsheets can leave IT administrators unaware of weak, reused, or compromised credentials stored and shared outside approved systems. NordPass explains how centralized password management can improve credential visibility, identify security risks, and simplify secure…

`credential`

### 54. [WhatsApp Patches 3 Security Flaws, Including Android Bug Suspected of Use in Scams](https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html)
_The Hacker News · Nov 20 · score 0.064 · CVE-2026-23871_

Meta-owned WhatsApp has addressed security vulnerabilities, including one impacting its Android app that it suspects may have been exploited in connection with scam messages. The vulnerability, tracked as CVE-2026-23871 (CVSS score: 3.5), has been described as a case of incomplete validation of exte…

`cve-` `cvss`

### 55. [GitHub Desktop now supports multiple accounts per host](https://github.blog/changelog/2026-11-19-github-desktop-now-supports-multiple-accounts-per-host)
_GitHub Changelog · Nov 20 · score 0.054_

GitHub Desktop now lets you sign in with more than one account on the same host, including GitHub.com, GitHub Enterprise Server, and GHE.com. This has been one of the most&#8230; The post GitHub Desktop now supports multiple accounts per host appeared first on The GitHub Blog .

`github`

### 56. [Security advisory permissions are now generally available](https://github.blog/changelog/2026-11-20-security-advisory-permissions-are-now-generally-available)
_GitHub Changelog · Nov 20 · score 0.053_

Organization owners can now let people work on repository security advisories, including private vulnerability reports, through custom repository roles. You no longer have to make them repository administrators or give&#8230; The post Security advisory permissions are now generally available appeare…

`github`

### 57. [Improvements on the pull request overview in public preview](https://github.blog/changelog/2026-11-19-improvements-on-the-pull-request-overview-in-public-preview)
_GitHub Changelog · Nov 20 · score 0.043_

Your feedback has helped improve the new pull request Overview page since its November 5, 2026 public preview. Here&#8217;s what&#8217;s new! Clearer merge status and next steps Failed optional checks&#8230; The post Improvements on the pull request overview in public preview appeared first on The G…

`github`

### 58. [GitHub Enterprise Server 3.23 release candidate](https://github.blog/changelog/2026-11-20-github-enterprise-server-3-23-release-candidate)
_GitHub Changelog · Nov 20 · score 0.037_

GitHub Enterprise Server (GHES) 3.23 is now available and introduces new capabilities across the platform. Here are a few highlights in the 3.23 release: When working in GitHub Projects, you&#8230; The post GitHub Enterprise Server 3.23 release candidate appeared first on The GitHub Blog .

`github`

### 59. [Risky Bulletin: "Windows Baseline Protection" coming to apps next year](https://risky.biz/RBNEWS636/)
_Risky Business News · Nov 20 · score 0.009_

A new Windows security feature will allow apps to check system security before running, hackers hit the European Commission’s HR platform, Ubuntu will ship AI-generated patches in Edge releases, and a ton of branded vulnerabilities.

`ubuntu` `windows` `edge`

### 60. [Promote `ptr_wise_atomic_memmove` to general private API function](https://discuss.python.org/t/promote-ptr-wise-atomic-memmove-to-general-private-api-function/110216)
_PyPI Security Announcements · Nov 20 · score 0.009_

Followup to Generalized ptr_wise_atomic_{memmove,memcpy} as part of public API - Ideas - Discussions on Python.org 2nd attempt in generalizing ptr_wise_atomic_* functions beyond _elementtree . static inline void _PyObject_ptr_wise_atomic_memmove(PyObject *a, PyObject **dest, PyObject **src, Py_ssize…

`python`

### 61. [Microsoft now automatically installs Windows 11 26H2 on unmanaged devices](https://www.bleepingcomputer.com/news/microsoft/microsoft-now-automatically-installs-windows-11-26h2-on-personal-and-unmanaged-pcs/)
_BleepingComputer · Nov 20 · score 0.006_

Starting this week, Microsoft has begun automatically upgrading eligible devices that aren't managed by an IT department to Windows 11 26H2. [...]

`windows`

### 62. [Windows 11 KB5132057 update released with 28 changes and fixes](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5132057-update-released-with-28-changes-and-fixes/)
_BleepingComputer · Nov 20 · score 0.006_

Microsoft released the KB5132057 November Windows 11 preview update, which comes with 28 changes, including improvements to Windows Search, Windows Hello, and the Run dialog. [...]

`windows`

### 63. [ROMULUS ClickFix Attacks Deliver RAT That Can Spy on Users and Control PCs](https://thehackernews.com/2026/11/romulus-clickfix-attacks-deliver-rat.html)
_The Hacker News · Nov 20 · score 0.006_

Threat actors have been observed using the ROMULUS ClickFix malware delivery platform to deliver a previously undocumented remote access trojan (RAT) that shares similarities with CNCMachineRMS. "ROMULUS likely operates as a delivery service, distributing CNCMachineRMS and Legion Loader through sepa…

`rat`

### 64. [Pin your favorite repositories to your dashboard](https://github.blog/changelog/2026-11-20-pin-your-favorite-repositories-to-your-dashboard)
_GitHub Changelog · Nov 20 · score 0.003_

Choose which repositories appear on the Dashboard with the new Favorite repositories section. If the new dashboard experience isn&#8217;t enabled, Top repositories remains unchanged. Select Edit or Add repositories to&#8230; The post Pin your favorite repositories to your dashboard appeared first on…

`github`

### 65. [Everything Is a Web Application, Including Your Firewall](https://thehackernews.com/2026/11/everything-is-web-application-including.html)
_The Hacker News · Nov 19 · score 0.298 · CVE-2026-109618, CVE-2026-109619_

One of the early targets of PHP2Shell exploitation was the firewall. On October 28, Palo Alto Networks confirmed that attackers were exploiting the two PHP vulnerabilities, CVE-2026-109618 and CVE-2026-109619, against PAN-OS management interfaces exposed to the internet. Both flaws let anyone execut…

`php` `palo alto` `firewall` `cve-`

### 66. [CISA Warns of 4 Exploited Flaws Linked to Ransomware, Cryptomining, and LLMjacking Attacks](https://thehackernews.com/2026/11/cisa-warns-of-4-exploited-flaws-linked.html)
_The Hacker News · Nov 19 · score 0.284_

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added four vulnerabilities impacting Synology DiskStation Manager (DSM), BerriAI LiteLLM, Apache Axis, and Vanderbilt University Research Electronic Data Capture (REDCap) to its Known Exploited Vulnerabilities (KEV) catalo…

`kev` `ransomware`

### 67. [Hardening GitHub Actions Against Insider Threats](https://socket.dev/blog/hardening-github-actions-against-insider-threats?utm_medium=feed)
_Socket Blog · Nov 19 · score 0.270_

A practical guide to securing CI/CD pipelines against stolen credentials, covering GitHub Actions, trusted publishing, release approvals, and revocation.

`github` `github actions` `ci/cd`

### 68. [[tl;dr sec] #355 - Cyber Chaos Monkey, Offsec Harness Index, Top 10 AWS Security Research of 2026](https://tldrsec.com/p/tldr-sec-355)
_tl;dr sec · Nov 19 · score 0.190_

Shopify's AI agent system that continuously attacks their production infra, list of open-source offensive AI agent harnesses, la creme de la cloud 2026

`aws` `shopify`

### 69. [Transport for London breach exposes 265,000 Oyster card users' data](https://www.bleepingcomputer.com/news/security/transport-for-london-breach-exposes-265-000-oyster-card-users-data/)
_BleepingComputer · Nov 19 · score 0.171_

Transport for London (TfL) has announced that around 265,000 Oyster photocard customers may have had their account details exposed in a data breach. [...]

`breach`

### 70. [Age of Entitlement: Privileges in Entra's access packages](https://securitylabs.datadoghq.com/articles/entra-access-packages-part-1-privileges/)
_Datadog Security Labs · Nov 19 · score 0.160_

This series will describe how everyday access package configurations within entitlement management can lead to scenarios where an attacker could elevate privileges. This post lays out the fundamentals of Microsoft Entra ID Governance's entitlement management, and why an attacker may target for privi…

`entra` `privilege escalation`

### 71. [Runtime security for Amazon EKS Auto Mode with Sysdig](https://webflow.sysdig.com/blog/runtime-security-for-amazon-eks-auto-mode)
_Sysdig · Nov 19 · score 0.148_

Sysdig integrates with Amazon EKS Auto Mode hands node management to AWS, giving you immutable, Bottlerocket-based nodes with read-only root filesystems and no kernel module loading. But the shared responsibility model still applies: what happens inside your workloads at runtime is on you. This post…

`node` `kubernetes` `aws` `eks` `kernel`

### 72. [Hackers Breach N-able Cloud Server, Disrupting Email Security Management Across 3 Regions](https://thehackernews.com/2026/11/n-able-confirms-hackers-accessed-cloud.html)
_The Hacker News · Nov 19 · score 0.140_

N-able on Wednesday disclosed that unknown threat actors gained unauthorized access to one of the servers in the Mail Assure and Spam Experts Hosted Cloud, causing it to disable management interfaces and APIs. "We have taken steps to mitigate the threat and are continuing to harden our services to r…

`breach`

### 73. [On embedders and Stable ABI](https://discuss.python.org/t/on-embedders-and-stable-abi/110197)
_PyPI Security Announcements · Nov 19 · score 0.130_

PEP 384 says that applications targeting the Stable ABI should link against libpython3.so when CPython is built as a shared library on Unix. On Linux, even an executable that just calls Py_GetVersion() fails to link with -lpython3 . I think we need to decide whether CPython should support this use c…

`python` `linux`

### 74. [phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution](https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html)
_The Hacker News · Nov 19 · score 0.121 · CVE-2026-126714_

PHP's default file-based session storage can be made to return objects an attacker chose, by cutting off a session write at the right moment. When combined with a second weakness, such as a suitable gadget chain in the app, those objects can allow the attacker to run code on the server. Today's PHP …

`php` `session` `cve-`

### 75. [Srsly Risky Biz: Regulatory relief for AI hacks is a good first step](https://risky.biz/SRB191/)
_Risky Business News · Nov 19 · score 0.083_

Tom Uren and Amberleigh Jack talk about the Trump administration’s AI task force asking for US federal regulatory agencies to go easy on organisations that fall victim to AI-powered cyber attacks. This makes sense, at least in the short term. But we’d like to see more expansive forward-looking polic…

`go `

### 76. [How to run AI SAST in CI/CD and on pull requests | Endor Labs](https://www.endorlabs.com/learn/ai-sast-in-ci-cd-and-pull-requests)
_Endor Labs · Nov 19 · score 0.071_

Run AI SAST where code gets reviewed. Scan placement, diff-aware PR scans, PR comments, merge policies, CI secrets, and metrics, with an example pipeline.

`ci/cd`

### 77. [Red Hat Enterprise Linux runner images now generally available](https://github.blog/changelog/2026-11-19-red-hat-enterprise-linux-runner-images-now-generally-available)
_GitHub Changelog · Nov 19 · score 0.058_

Red Hat Enterprise Linux (RHEL) 9 and RHEL 10 images for GitHub-hosted larger runners are now generally available. Originally introduced in public preview in June 2026 in partnership with Red&#8230; The post Red Hat Enterprise Linux runner images now generally available appeared first on The GitHub …

`github` `runner` `linux` `rhel`

### 78. [Enterprise Live Migrations from Azure DevOps generally available](https://github.blog/changelog/2026-11-19-enterprise-live-migrations-from-azure-devops-generally-available)
_GitHub Changelog · Nov 19 · score 0.058_

Enterprise Live Migrations (ELM) from Azure DevOps Services to GitHub Enterprise Cloud with data residency is now generally available. You can move your repositories while your teams keep working, then&#8230; The post Enterprise Live Migrations from Azure DevOps generally available appeared first on…

`github` `azure` `teams`

### 79. [S3 audit log streaming with OpenID Connect expands to GHE.com](https://github.blog/changelog/2026-11-19-s3-audit-log-streaming-with-openid-connect-expands-to-ghe-com)
_GitHub Changelog · Nov 19 · score 0.050_

You can now stream enterprise audit logs to Amazon S3 using OpenID Connect (OIDC) on GitHub Enterprise Cloud with data residency (GHE.com). This extends the existing github.com capability, letting you&#8230; The post S3 audit log streaming with OpenID Connect expands to GHE.com appeared first on The…

`github` `s3` `oidc`

### 80. [Wait for pull request events with GitHub CLI](https://github.blog/changelog/2026-11-18-wait-for-pull-request-events-with-github-cli)
_GitHub Changelog · Nov 19 · score 0.026_

GitHub CLI now supports GitHub Event Streams. With gh v2.105.0, you and your agents can wait for a pull request to change with a single command instead of polling it&#8230; The post Wait for pull request events with GitHub CLI appeared first on The GitHub Blog .

`github`
