# feedrank — 2026-11-28

_79 items, 5d window._

### 1. [OSGeo GeoServer: OSGeo GeoServer XML Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-120705)
_CISA KEV · Nov 27 · score 2.094 · **CRITICAL 9.5** · ×8 reports · CVE-2026-120705, CVE-2026-129243, CVE-2026-132165_

OsGeo GeoServer contains an XML injection vulnerability that allows an unauthenticated remote attacker to cause the server to read local text files accessible to the GeoServer process or fetch attacker-specified HTTP or HTTPS URLs via a crafted ID parameter in the WFS 2.0 GetFeatureById stored query…

`cve-`

_also: [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-129243), [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-132165), [StepSecurity](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165), [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/27/cisa-adds-three-known-exploited-vulnerabilities-catalog), [The Hacker News](https://thehackernews.com/2026/11/drupal-warns-of-new-highly-critical.html)_

### 2. [Unpatched Cacti zero-day with public PoC gives remote code execution](https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/)
_BleepingComputer · Nov 27 · score 1.227 · **CRITICAL 9.0**_

A zero-day vulnerability in the Cacti network monitoring platform has been publicly disclosed, along with a proof-of-concept exploit that lets unauthenticated attackers execute commands on vulnerable servers. [...]

`zero-day` `exploit`

### 3. [Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access](https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html)
_The Hacker News · Nov 27 · score 1.124 · **CRITICAL 9.0**_

Details have emerged about a new zero-day vulnerability in Cacti, an open-source network monitoring tool, that could be exploited to achieve remote code execution. The proof-of-concept (PoC) exploit, which has yet to be assigned a CVE identifier, has been tracked as 4HTTP2SHELL and 4HTTP2ROOT. "I fo…

`session` `rce` `zero-day` `exploit`

### 4. [New NFS2ROOT Linux flaw can let attackers gain root privileges](https://www.bleepingcomputer.com/news/security/new-nfs2root-linux-flaw-can-let-attackers-gain-root-privileges/)
_BleepingComputer · Nov 27 · score 0.632 · **CRITICAL 9.5** · CVE-2026-99362_

​A 12-year-old critical vulnerability in the Linux kernel's Network File System (NFS) server, tracked as CVE-2026-99362, allows remote attackers to gain root privileges. [...]

`linux` `kernel` `cve-`

### 5. [Drupal warns of new site takeover flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/drupal-warns-of-new-access-bypass-flaw-exploited-in-attacks/)
_BleepingComputer · Nov 27 · score 0.497 · **CRITICAL 9.5**_

The Drupal security team says attackers are exploiting a second critical vulnerability that lets them breach and hijack unpatched websites. [...]

`breach`

### 6. [Hackers Trojanize Official Q-Dir and DesktopOK Downloads to Deliver Remote Access Malware](https://thehackernews.com/2026/11/hackers-trojanize-official-q-dir-and.html)
_The Hacker News · Nov 27 · score 0.723 · **HIGH 8.5**_

Cybersecurity researchers have disclosed details of a software supply chain attack that has tampered with Q-Dir and DesktopOK installation files distributed via the official SoftwareOK website. "Evidence indicates that malicious files were generated not only when users downloaded the programs direct…

`supply chain`

### 7. [Hewlett Packard Enterprise (HPE) Juniper Session Smart Conductor and Session Smart Router: Hewlett Packard Enterprise (HPE) Juniper Session Smart Conductor and Session Smart Router OS Command Injection Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-103406)
_CISA KEV · Nov 26 · score 1.230 · **CRITICAL 9.0** · ×3 reports · CVE-2023-25914, CVE-2023-25915, CVE-2025-41450_

Hewlett Packard Enterprise (HPE) Juniper Session Smart Conductor and Session Smart Router contain an OS command injection vulnerability that could allow a remote attacker to execute arbitrary commands as root via a specially crafted salt minion ID. Required action: Apply mitigations in accordance wi…

`juniper` `session`

_also: [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog), [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-10-vulnerabilities.html)_

### 8. [Remus malware steals Gmail messages via fake Google Sheets extension](https://www.bleepingcomputer.com/news/security/remus-malware-steals-gmail-messages-via-fake-google-sheets-extension/)
_BleepingComputer · Nov 26 · score 0.227 · **CRITICAL 9.0**_

The Remus infostealer is stealing Gmail messages through a stealthy malicious Chrome extension, a capability the malware operators marketed as a zero-day exploit in Google's email service. [...]

`chrome` `zero-day` `exploit`

### 9. [Vates Xen Orchestra: Vates Xen Orchestra Improper Validation of Specified Type of Input Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-133469)
_CISA KEV · Nov 25 · score 1.165 · **CRITICAL 9.8** · ×2 reports · CVE-2026-133469_

Vates Xen Orchestra contains an improper validation of specified type of input vulnerability that could allow an unauthenticated attacker to bypass authentication and perform actions with administrative privileges via a specially crafted authentication token containing an empty JSON object. Required…

`xen` `token`

_also: [GHSA — npm](https://github.com/advisories/GHSA-2r3w-c2vx-fv5g)_

### 10. [Hackers Exploited CVSS 10.0 Hex.pm RCE Flaw to Compromise 6 Package Registry Servers](https://thehackernews.com/2026/11/hackers-exploited-cvss-100-hexpm-rce.html)
_The Hacker News · Nov 25 · score 0.624 · **CRITICAL 9.0**_

An attacker ran operating system commands on Monday on six production servers of Hex.pm, the package registry that Elixir and Erlang developers fetch their dependencies from. The flaw used in the attack had been in the registry's code since February 2016, and the team that maintains the service had …

`rce` `cvss`

### 11. [TastyIgniter permits Path Traversal in Media Upload](https://github.com/advisories/GHSA-rj59-9f77-mvg5)
_GHSA — composer · Nov 25 · score 0.489 · **CRITICAL 9.1** · ×4 reports · CVE-2026-69177, CVE-2026-69178, CVE-2026-69179_

Affected: tastyigniter/tastyigniter. ### Summary Arbitrary file write outside `media/uploads/` ### Details It is possible to perform Path Traversal in Media Manager file upload function as admin. ### PoC - login as admin - upload a image but in the request, change the path from `/` to `/../../`. Req…

`linux` `token` `chromium` `csrf`

_also: [GHSA — composer](https://github.com/advisories/GHSA-7wwv-x6mc-pxqx), [GHSA — composer](https://github.com/advisories/GHSA-743w-g9pf-8p94), [GHSA — composer](https://github.com/advisories/GHSA-mqg7-fw3f-mhp7)_

### 12. [Credential Remediation Is Slow When You Don’t Know What Will Break](https://thehackernews.com/2026/11/credential-remediation-is-slow-when-you.html)
_The Hacker News · Nov 25 · score 0.376 · **CRITICAL 9.5**_

TL;DR More than 64% still valid after four years: GitGuardian’s State of Secrets Sprawl 2026 found that most valid secrets discovered in 2022 still worked in January 2026, because teams stall on what a revoke will break. Validity-only triage misses 46% of critical secrets: Prioritize by impact inste…

`credential` `teams`

### 13. [@waline/client vulnerable to stored XSS through unsanitized comment edit previews](https://github.com/advisories/GHSA-crj3-q72p-ggqm)
_GHSA — npm · Nov 25 · score 0.347 · **CRITICAL 9.3** · CVE-2026-64670_

Affected: @waline/client. ### Summary `@waline/client` renders the comment editor's live preview with `marked` and no sanitizer (`utils/markdown.ts`), and the preview is injected with `v-html`. When a comment is edited, the editor is seeded with the comment's raw, un-sanitized body (`orig`). Only ad…

`session` `xss`

### 14. [WordPress Blocks Six Backdoored WP Connect Plugins Before Malicious Releases Go Live](https://thehackernews.com/2026/11/wordpress-blocks-six-backdoored-wp.html)
_The Hacker News · Nov 25 · score 0.220 · **CRITICAL 9.0**_

WordPress has removed six WordPress plugins developed by WP Connect after they were backdoored on November 22, 2026, to enable arbitrary code execution on sites that have them installed, following a suspected compromise of the developer's account. The WordPress plugins team has proactively detected …

`go `

### 15. [livewire-powergrid: SQL injection via sortDirection in naturalSort queries](https://github.com/advisories/GHSA-7fgc-3h6c-698r)
_GHSA — composer · Nov 25 · score 0.242 · **HIGH 7.6** · CVE-2026-65971_

Affected: power-components/livewire-powergrid. ## [Description] The public Livewire property `sortDirection` is interpolated **verbatim** into a raw SQL `ORDER BY` clause and is not restricted to `asc`/`desc`, allowing arbitrary SQL injection through `POST /livewire/update`. **Data flow** - **Source…

`php` `sql injection`

### 16. [CISA Adds Two Known Exploited Vulnerabilities to Catalog](https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog)
_CISA Advisories · Nov 24 · score 1.227 · **CRITICAL 9.5** · ×3 reports · CVE-2026-133968, CVE-2026-134624_

CISA has added two new vulnerabilities to its Known Exploited Vulnerabilities (KEV) Catalog , based on evidence of active exploitation. CVE-2026-133968 Project MONAI MONAI Label Path Traversal Vulnerability &nbsp; CVE-2026-134624 N-able Mail Assure (SpamExperts) Server-Side Request Forgery (SSRF) Vu…

`kev` `ssrf` `cve-`

_also: [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html), [The Hacker News](https://thehackernews.com/2026/11/n-able-discloses-critical-mail-assure.html)_

### 17. [ruflo MCP bridge allows unauthenticated remote code execution in default Docker Compose deployments](https://github.com/advisories/GHSA-c4hm-4h84-2cf3)
_GHSA — npm · Nov 24 · score 0.619 · **CRITICAL 10.0** · CVE-2026-59726_

Affected: ruflo. The MCP bridge shipping in ruflo/docker-compose.yml exposed POST /mcp with no authentication. The docker-compose defaults bound the bridge and MongoDB to all interfaces. Combined, an unauthenticated network attacker could invoke tools/call → terminal_execute inside the bridge contai…

`node` `container` `docker` `mongodb`

### 18. [VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html)
_The Hacker News · Nov 24 · score 0.608 · **CRITICAL 9.5** · CVE-2026-123903_

Broadcom has shipped patches to address 23 vulnerabilities impacting VMware ESX, vCenter, Workstation, Fusion, and Avi Load Balancer, including one critical bug that could be abused to bypass authentication. The critical vulnerability, tracked as CVE-2026-123903, is rated 9.8 out of 10.0 on the CVSS…

`vmware` `vcenter` `zero-day` `cve-` `cvss`

### 19. [Socket Releases Free Patches for 100% of Critical CVEs in RubyGems](https://socket.dev/blog/free-patches-critical-ruby-cves?utm_medium=feed)
_Socket Blog · Nov 24 · score 0.498 · **CRITICAL 9.5**_

Fix critical RubyGems vulnerabilities without upgrading dependencies. Free security patches are now available with more ways to install and deploy them.

`rubygems`

### 20. [Idunno AntiCsrf: Idunno AntiCsrf Deserialization of Untrusted Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-131914)
_CISA KEV · Nov 24 · score 0.394 · **CRITICAL 9.5** · ×2 reports · CVE-2026-131914_

Idunno AntiCsrf contains a deserialization of untrusted data vulnerability that allows an unauthenticated remote attacker to execute arbitrary code via object injection. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transi…

`deserialization`

_also: [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-critical-aspnet-anti.html)_

### 21. [AutomationDirect C-More EA9 Programming Software](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-01)
_CISA Advisories · Nov 24 · score 0.367 · **CRITICAL 9.5** · CVE-2026-127280_

View CSAF Summary Successful exploitation of this vulnerability could allow attackers to corrupt application memory and cause instability or a crash, potentially leading to arbitrary code execution, if a user is convinced to open a malicious file. The following versions of AutomationDirect C-More EA…

`cve-` `cvss`

### 22. [Danfoss AK-SM 8xxA Series](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03)
_CISA Advisories · Nov 24 · score 0.324 · **CRITICAL 9.5** · CVE-2026-129713_

View CSAF Summary Successful exploitation of this vulnerability could allow an attacker to execute arbitrary code with webserver privileges. The following versions of Danfoss AK-SM 8xxA Series are affected: AK-SM8xxA &lt;=5.4.0 (CVE-2026-129713) CVSS Vendor Equipment v3 9.8 Danfoss AK-SM8xxA 1 Vulne…

`cve-` `cvss`

### 23. [Iran-Aligned Volant Manticore Uses IPFS-Based KuboShell Backdoor in Espionage Campaigns](https://thehackernews.com/2026/11/iran-aligned-volant-manticore-uses-ipfs.html)
_The Hacker News · Nov 24 · score 0.269 · **CRITICAL 9.5**_

A previously undocumented Iran-aligned cyber espionage group called Volant Manticore has targeted telecommunications companies, airlines, and critical infrastructure in Cyprus. Central to the group's operations is a backdoor called KuboShell that uses the InterPlanetary File System (IPFS) for comman…

`backdoor`

### 24. [Optimizely Web Experimentation: Optimizely Web Experimentation External Control of Critical State Data Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-132224)
_CISA KEV · Nov 24 · score 0.234 · **CRITICAL 9.0** · CVE-2026-132224_

Optimizely Web Experimentation contains an external control of critical state data vulnerability in its account signup flow that could allow an attacker to impersonate existing customer users and modify Project JavaScript. Successful exploitation can result in attacker-controlled JavaScript being di…

`javascript`

### 25. [soapbar: verify_envelope_bsp accepts an unauthenticated embedded certificate (signature forgery / authentication bypass)](https://github.com/advisories/GHSA-859w-52fx-hcm6)
_GHSA — pip · Nov 24 · score 0.704 · **HIGH 8.2** · CVE-2026-64855_

Affected: soapbar. ### Impact `verify_envelope_bsp()` derived its trust anchor from the message it was verifying. It read the X.509 certificate out of the caller-untrusted `wsse:BinarySecurityToken`, validated **only** that certificate's not-before / not-after dates, and then verified the signature …

`certificate` `ca` `x.509` `authentication bypass`

### 26. [nginx2root (CVE-2026-123007): HTTP/2 Flaw Lets Attackers Run Code on Unpatched nginx Servers](https://www.stepsecurity.io/blog/cve-2026-123007-nginx-http2-rce)
_StepSecurity · Nov 24 · score 0.500 · **HIGH 8.0** · CVE-2026-123007_

nginx 1.31.9 and 1.30.7 fix an HTTP/2 flaw that a public exploit turns into unauthenticated code execution. See what stopped the exploit in our lab, how to patch and confirm the fix, and how to find nginx on developer machines.

`exploit` `cve-`

### 27. [AVideo API FFmpeg process permits OS command injection via notifyCode/callback](https://github.com/advisories/GHSA-g9x9-q7qj-6mv5)
_GHSA — composer · Nov 24 · score 0.433 · **HIGH 8.1** · ×2 reports · CVE-2026-63304, CVE-2026-63305_

Affected: wwbn/avideo. ### Summary The standalone FFmpeg execution endpoint `plugin/API/standAlone/ffmpeg.json.php` builds a shell command string that is passed to `execAsync()` and run via `nohup sh -c "<command>"`. When the decrypted `codeToExec` payload produces a non-empty `avideoPath`, the endp…

`php`

_also: [GHSA — composer](https://github.com/advisories/GHSA-j44m-77cc-p3cc)_

### 28. [github.com/insomniacslk/dhcp permits denial of service through a malformed IPv4 payload length](https://github.com/advisories/GHSA-jp3c-6v3g-mpxv)
_GHSA — go · Nov 24 · score 0.245 · **HIGH**_

Affected: github.com/insomniacslk/dhcp. In github.com/insomniacslk/dhcp/dhcpv4/nclient4, BroadcastRawUDPConn.ReadFrom does not validate that the IPv4 payload length is sufficient to hold a UDP header before calculating the DHCP payload length. A frame with an IPv4 total-length field specifying fewer…

`github`

### 29. [Critical binary-parser Flaw Enables JavaScript Injection via Malicious Parser Definitions](https://thehackernews.com/2026/11/critical-binary-parser-flaw-enables.html)
_The Hacker News · Nov 23 · score 0.264 · **CRITICAL 9.5** · CVE-2026-134814_

A critical security flaw has been disclosed in the popular binary-parser library that could allow an attacker who controls parser definitions to execute arbitrary code. The vulnerability, tracked as CVE-2026-134814 (CVSS score: 9.2 / 8.1), is a case of code injection impacting binary-parser versions…

`javascript` `cve-` `cvss`

### 30. [Hackers Exploit Critical ScreenConnect Flaw to Hijack MSP Technician PCs Without Warning](https://thehackernews.com/2026/11/hackers-exploit-critical-screenconnect.html)
_The Hacker News · Nov 23 · score 0.124 · **CRITICAL 9.5** · CVE-2026-84869_

Threat actors are exploiting a now-patched security flaw in ConnectWise ScreenConnect to target managed service provider (MSP) servers. The activity revolves around CVE-2026-84869 (CVSS score: 9.9), a critical ScreenConnect client flaw that allows a guest to transfer and execute a malicious payload …

`exploit` `cve-` `cvss`

### 31. [13 Malicious NuGet Packages Target .NET Developers With Fake Job Assessments](https://socket.dev/blog/malicious-nuget-packages-fake-job-assessments?utm_medium=feed)
_Socket Blog · Nov 23 · score 0.740 · **HIGH 8.5**_

Socket researchers uncovered 13 malicious NuGet packages linked to fake developer job assessments, DLL side-loading, credential theft, and GitHub-based malware.

`.net` `nuget` `github` `credential`

### 32. [Klever Go counts bitmap padding bits toward BLS quorum, allowing blocks with insufficient signatures](https://github.com/advisories/GHSA-f9h7-4mmq-vgcq)
_GHSA — go · Nov 23 · score 0.128 · **HIGH** · CVE-2026-58262_

Affected: github.com/klever-io/klever-go. ## Summary When validating an incoming block header, `HeaderSigVerifier.verifyConsensusSize` counts *every* set bit in `PubKeysBitmap` — including bits that correspond to no validator (the padding bits of the final byte, which exist whenever the consensus gr…

`go ` `github`

### 33. [New Boston Scientific data breach exposes personal, medical info](https://www.bleepingcomputer.com/news/security/new-boston-scientific-data-breach-exposes-personal-medical-info/)
_BleepingComputer · Nov 27 · score 0.381_

Medical technology company Boston Scientific is sending data breach notices to individuals affected by a cyberattack on the firm. [...]

`breach`

### 34. [Your Firewall Isn't Enough: The Hidden Risk of Unmanaged VMs](https://www.bleepingcomputer.com/news/security/your-firewall-isnt-enough-the-hidden-risk-of-unmanaged-vms/)
_BleepingComputer · Nov 27 · score 0.303_

Forgotten virtual machines, unpatched servers, and excessive access permissions can create security blind spots across IT infrastructure. ISPsystem explains how centralized infrastructure management, access controls, and resource lifecycle automation can help reduce these risks. [...]

`firewall`

### 35. [Microsoft removes WSUS server role in Windows Server 2028](https://www.bleepingcomputer.com/news/microsoft/microsoft-removes-wsus-server-role-in-windows-server-2028/)
_BleepingComputer · Nov 27 · score 0.264_

Microsoft will remove the WSUS server role from Windows Server 2028, the next major release of its server operating system. [...]

`windows` `windows server`

### 36. [Microsoft pushes emergency hotpatch to fix Windows Server crashes](https://www.bleepingcomputer.com/news/microsoft/new-out-of-band-oob-emergency-hotpatch-fixes-windows-server-2025-crashes/)
_BleepingComputer · Nov 27 · score 0.258_

Microsoft has released an emergency hotpatch update to address Windows Server 2025 crashes triggered after installing this month's security hotpatch update (KB5131077). [...]

`windows` `windows server`

### 37. [SAP confirms security incident after suspicious GitHub activity](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/)
_BleepingComputer · Nov 27 · score 0.214_

SAP has confirmed to BleepingComputer that it took urgent action to protect its customers after detecting suspicious activity in its IT environment. [...]

`github`

### 38. [Malwarebytes Antivirus: Get 50% off during Black Friday 2026](https://www.bleepingcomputer.com/news/security/malwarebytes-antivirus-get-50-percent-off-during-black-friday-2026/)
_BleepingComputer · Nov 27 · score 0.206_

Malwarebytes' 2026 Black Friday and Cyber Monday sale is now live, offering 50% off security subscriptions for individuals, families, and small businesses, including its antivirus software, VPN, identity theft protection, and personal data removal services. [...]

`vpn`

### 39. [RUSTSEC-2026-0603: Vulnerability in dryoc](https://rustsec.org/advisories/RUSTSEC-2026-0603.html)
_RustSec · Nov 27 · score 0.195_

X25519 accepts low-order public keys, yielding session keys computable without a private key

`session`

### 40. [US Air Force cloud platform reportedly hacked in latest federal breach](https://www.bleepingcomputer.com/news/security/us-air-force-cloud-platform-reportedly-hacked-in-latest-federal-breach/)
_BleepingComputer · Nov 27 · score 0.178_

Hackers have reportedly breached the US Air Force's Cloud One computing platform, adding to a recent wave of cyberattacks affecting US government agencies, including the FBI, CIA, and Treasury Department. [...]

`breach`

### 41. [Microsoft Store App Found Delivering Vinci RAT Capable of Remote System Control](https://thehackernews.com/2026/11/microsoft-store-app-found-delivering.html)
_The Hacker News · Nov 27 · score 0.158_

Cybersecurity researchers have disclosed details of a cyber attack in which a threat actor leveraged a Microsoft Store application to deliver a remote access trojan (RAT) called Vinci RAT. The intrusion, according to eSentire, begins with a redirection to a bogus site for a sniping tool ("snipp.code…

`rat`

### 42. [1Password Hacked, Customer Data and Source Code Stolen in GitHub Account Breach](https://thehackernews.com/2026/11/1password-hacked-customer-data-and.html)
_The Hacker News · Nov 26 · score 0.409_

Popular password management software 1Password on Wednesday disclosed a security incident involving its backend systems that led to the unauthorized access of some customer information, but emphasized that customer password vaults and other secrets were not accessed. "While we took immediate steps t…

`github` `1password` `breach`

### 43. [Risky Bulletin: Hackers breach Erlang and Elixir package manager](https://risky.biz/RBNEWS639/)
_Risky Business News · Nov 26 · score 0.339_

Erlang and Elixir’s package manager gets hacked, FinCEN investigates a security breach, 1Password got owned through an employee’s GitHub account, and Russia will try to build a GitHub clone. Again.

`github` `1password` `breach`

### 44. [13 Malicious NuGet Packages Turn Fake .NET Job Assessments Into Malware Delivery Traps](https://thehackernews.com/2026/11/13-malicious-nuget-packages-turn-fake.html)
_The Hacker News · Nov 26 · score 0.218_

Cybersecurity researchers have discovered 13 malicious NuGet packages that are designed to target Windows .NET developers under the guise of a fake take-home job assessment. "Most of the packages pose as WinUI 3 and WPF [Windows Presentation Foundation] button controls," Socket security researcher K…

`.net` `nuget` `windows`

### 45. [Fake paid expert interviews impersonate brands to steal Google logins](https://www.bleepingcomputer.com/news/apple/fake-paid-expert-interviews-impersonate-brands-to-steal-google-logins/)
_BleepingComputer · Nov 26 · score 0.206_

An ongoing phishing campaign dubbed "GoodGuys" impersonates major brands, including Google, Nvidia, Accenture, and SpaceX, to steal corporate Google and Okta credentials using fake invitations to paid expert interviews and webinars. [...]

`okta`

### 46. [North Korea-Linked PolinRider Poisons Over 7,600 GitHub Repositories to Spread Malware](https://thehackernews.com/2026/11/north-korea-linked-polinrider-poisons.html)
_The Hacker News · Nov 26 · score 0.178_

The threat actors behind the PolinRider campaign have compromised over 7,600 GitHub repositories, in some cases planting a Python loader capable of delivering next-stage payloads, as evidence emerges that the activity may have started as far back as February 2025. "These are real developers, not thr…

`python` `github`

### 47. [NordVPN Black Friday Deal: Get 78% off VPN plans in 2026](https://www.bleepingcomputer.com/news/security/nordvpn-black-friday-deal-get-78-percent-off-vpn-plans-in-2026/)
_BleepingComputer · Nov 26 · score 0.173_

NordVPN's 2026 Black Friday and Cyber Monday deal is now live, offering savings of up to 78% on VPN subscriptions, plus three extra months of protection. [...]

`vpn`

### 48. [Most Wanted: The Phishing Kits and Techniques Getting Past Security Controls](https://thehackernews.com/2026/11/most-wanted-phishing-kits-and.html)
_The Hacker News · Nov 26 · score 0.158_

Every phishing attack has to get past email security, web filtering, and safe browsing before it reaches an employee. Some kits manage that far more often than others, and those are the kits that security teams need to know about. At Push Security, we measure this as breakthrough rate: The share of …

`teams`

### 49. [A new npm package for Web3 and MEV developers shipped a clean tarball and pulled its payload from GitHub at install time.  | Endor Labs](https://www.endorlabs.com/learn/web3-mev-error-decoder-a-clean-npm-package-that-installs-malicious-payload-from-github)
_Endor Labs · Nov 25 · score 0.484_

A new npm package for Web3 and MEV developers shipped a clean tarball and pulled its payload from GitHub at install time. A same-name decoy on the registry made the dependency look routine.

`npm` `github`

### 50. [Com-Affiliated Hackers Hijack Cloud Accounts via Vishing for Data Theft and Extortion](https://thehackernews.com/2026/11/com-affiliated-hackers-hijack-cloud.html)
_The Hacker News · Nov 25 · score 0.400_

Palo Alto Networks Unit 42 has disclosed that it's tracking and has responded to "numerous waves of vishing attacks" orchestrated by Com-affiliated threat actors since August 2026 that have led to data theft and extortion attempts. The attacks have targeted financial services, healthcare, and legal …

`palo alto`

### 51. [RUSTSEC-2026-0600: Vulnerability in kube-client](https://rustsec.org/advisories/RUSTSEC-2026-0600.html)
_RustSec · Nov 25 · score 0.342_

`openssl-tls` trusts OpenSSL&apos;s default CA store in addition to the configured cluster CA

`tls` `openssl` `ca`

### 52. [Risky Bulletin: Hackers breach CIA OSINT system](https://risky.biz/RBNEWS638/)
_Risky Business News · Nov 25 · score 0.249_

Hackers breach the CIA’s OSINT platform, cybersecurity firm Radware gets hacked, the US investigates Iran over 50 ship hacks and threat actors exploit an Azure API bug to access cloud environments.

`azure` `exploit` `breach`

### 53. [The Take-Home Test That Runs on Your Work Laptop: Inside the AccuraSoftHire Fake Interview Campaign](https://www.stepsecurity.io/blog/accurasofthire-fake-interview-developer-machines)
_StepSecurity · Nov 25 · score 0.247_

Binance says its $6.34 billion theft began when an engineer ran a fake interview assignment on his work computer. JFrog has now exposed a fake company, AccuraSoftHire, built to run the same trick. We decoded the attacker's server history from a public Ethereum wallet and found npm packages from the …

`npm`

### 54. [GitHub Security Advisory backlog: why SCA must detect at the repository | Endor Labs](https://www.endorlabs.com/learn/githubs-advisory-queue)
_Endor Labs · Nov 25 · score 0.215_

GitHub and NVD review queues are backed up. Learn what sits in the gap, why detection has to start at the repository, and what to ask your SCA vendor.

`github`

### 55. [laradocs  Command injection via unescaped Node.js binary path in KaTeX SSR](https://github.com/advisories/GHSA-h746-qpxh-ph7g)
_GHSA — composer · Nov 25 · score 0.189 · **MEDIUM 6.4** · CVE-2026-65973_

Affected: petebishwhip/laradocs. ### Summary Local command injection (CWE-78) in server-side KaTeX rendering via an unescaped Node.js binary path in a `proc_open()` command string. ### Affected versions >= 0.4.0, < 1.0.0 ### Patched versions >= 1.0.0 (fixed in commit `100cb1e`) ### Impact When rende…

`node` `php`

### 56. [How “don’t ask again” in Claude Code leaks secrets on GitHub: The click that keeps on giving](https://webflow.sysdig.com/blog/how-dont-ask-again-in-claude-code-leaks-secrets-on-github-the-click-that-keeps-on-giving)
_Sysdig · Nov 25 · score 0.086_

`github`

### 57. [Copilot code review billing will default to the organization](https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization)
_GitHub Changelog · Nov 25 · score 0.029_

If you haven&#8217;t chosen how to bill Copilot code review for members with a Copilot license, those reviews will be billed to your organization starting December 30, 2026. To keep&#8230; The post Copilot code review billing will default to the organization appeared first on The GitHub Blog .

`github`

### 58. [etcd: CRL enforcement bypass on gRPC listener when `--listen-client-http-urls` is configured](https://github.com/advisories/GHSA-3wh4-j44w-pg92)
_GHSA — go · Nov 24 · score 0.397 · **MEDIUM 6.5** · CVE-2026-59818_

Affected: go.etcd.io/etcd/v3, go.etcd.io/etcd/v3. ### Impact _What kind of vulnerability is it? Who is impacted?_ When etcd is configured with `--listen-client-http-urls` to split the HTTP and gRPC client endpoints onto separate listeners, the `--client-crl-file` Certificate Revocation List is not e…

`certificate`

### 59. [Okta Links ShinyHunters-Associated Vishing Group to New INCEPTION Data Leak Site](https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html)
_The Hacker News · Nov 24 · score 0.393_

A threat cluster previously assessed to be affiliated with the ShinyHunters extortion crew may have rebranded and continued operations under a new name called INCEPTION, according to Okta's Threat Intelligence team. The cluster, dubbed O-UNC-053, is characterized by the use of voice phishing (aka vi…

`okta` `data leak`

### 60. [GitHub CLI gh codespace jupyter may allow code execution via unvalidated URLs from malicious Codespaces](https://github.com/advisories/GHSA-8cg3-r6g9-fpg2)
_GHSA — go · Nov 24 · score 0.300 · **MEDIUM 4.4** · CVE-2026-59831_

Affected: github.com/cli/cli/v2. ### Summary A security vulnerability has been identified in GitHub CLI that could allow remote code execution when users connect to a malicious Codespace using the `gh codespace jupyter` command. The command opens JupyterLab by launching a URL in the user's browser, …

`github`

### 61. [Schneider Electric EcoStruxure Power Build Rapsody software](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-02)
_CISA Advisories · Nov 24 · score 0.211_

View CSAF Summary Schneider Electric is aware of a vulnerability in its EcoStruxure™ Power Build Rapsody product. The EcoStruxure™ Power Build Rapsody is used to enter or import the single line diagram, to get the extensive bill of material of your switchboard, including all devices, connection item…

`exploit`

### 62. [Microsoft Fixes Azure API Management Classic Flaw as Actor Targets Customer Secrets](https://thehackernews.com/2026/11/microsoft-fixes-azure-api-management.html)
_The Hacker News · Nov 24 · score 0.137_

Norway's National Security Authority (NSM) has disclosed that it became aware of a security vulnerability in Microsoft's Azure API Management (APIM) that has affected multiple businesses in the country, including energy companies Equinor and Skagerak Energi. "An unknown actor has been actively looki…

`azure`

### 63. [Evo Agentic Development Security and Evo Dependency Firewall Inside NVIDIA OpenShell](https://snyk.io/blog/secure-ai-coding-agents-nvidia-openshell/)
_Snyk · Nov 24 · score 0.121_

See how Evo ADS and Dependency Firewall secure Claude Code in NVIDIA OpenShell, from screening agent skills and code to controlling package installs.

`firewall`

### 64. [OpenAI and Cisco Unveil AI-Assisted Linux Security Tool to Block Exploits Before Patching](https://thehackernews.com/2026/11/openai-and-cisco-unveil-ai-assisted.html)
_The Hacker News · Nov 24 · score 0.098_

OpenAI and Cisco have teamed up to launch Shirudo (meaning "shield" in Japanese), an open-source Linux runtime that allows artificial intelligence (AI) agents to defend systems without downtime. "It lets agents write dynamic eBPF controls to shield systems from exploits, giving defenders more time t…

`cisco` `linux`

### 65. [Google Researcher Shows How a Single Bit Change in .NET Files Bypassed Windows Code Integrity](https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html)
_The Hacker News · Nov 24 · score 0.091 · CVE-2026-87268_

A quirk in how the .NET Framework loads a program file let a local attacker run untrusted code past two separate protections on Windows built to block it, Google Project Zero researcher James Forshaw showed in a write-up published yesterday. The same loading behavior bypassed Oracle VirtualBox's pro…

`.net` `windows` `cve-`

### 66. [WHMCS SQL Injection Could Expose Customer Data and Admin Password Hashes without Login](https://thehackernews.com/2026/11/whmcs-sql-injection-flaw-could-expose.html)
_The Hacker News · Nov 24 · score 0.084_

A flaw in WHMCS's shopping cart, the billing and automation platform many web hosting companies use to run their businesses, could allow anyone on the internet to retrieve customer records and administrator password hashes from an installation's database. No login is needed. The company disclosed th…

`sql injection`

### 67. [Cakephp twig-view unserialize Twig filter allows arbitrary object deserialization](https://github.com/advisories/GHSA-48qj-5wxh-m8hc)
_GHSA — composer · Nov 24 · score 0.007 · **MEDIUM** · CVE-2026-59192_

Affected: cakephp/twig-view, cakephp/twig-view. ### Impact The `unserialize` filter has no restriction on which classes are allowed. This can be used as a deserialization remote-code-execution gadget. ### Patches 1.3.3 and 2.1.2 contain a fix for this issue. The fix may impact backwards compatibilit…

`php` `deserialization`

### 68. [2027 SOC Budget Reset: 5 Priorities to Cut Costs and Reduce Cyber Risk](https://thehackernews.com/2026/11/2027-soc-budget-reset-5-priorities-to.html)
_The Hacker News · Nov 24 · score 0.004_

What if your biggest SOC budget problem isn't how much you spend, but how much analyst time you lose? According to ANY.RUN's estimates, SOC teams could recover 450 analyst hours per 1,000 investigated alerts through faster threat analysis and IOC research. That's a significant opportunity as manual …

`teams`

### 69. [More predictable notifications on GitHub.com](https://github.blog/changelog/2026-11-24-more-predictable-notifications-on-github-com)
_GitHub Changelog · Nov 24 · score 0.002_

Starting December 1, 2026, we&#8217;re migrating notifications on GitHub.com over the course of a week to make subscriptions more predictable, correct unexpected behavior, and support the growing scale of activity.&#8230; The post More predictable notifications on GitHub.com appeared first on The Gi…

`github`

### 70. [Agentic Attacks: In The Wild](https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks)
_Wiz Research · Nov 23 · score 0.206_

Agentic offensive frameworks like ARTEX are driving a surge in cloud intrusions. Wiz Research shares cases from the wild, including both sides of one attack via the operator's leaked logs, an update on Black October, and the detections that catch these noisy, machine-speed attacks.

`in the wild`

### 71. [Hackers Exploited GL.iNet Cloud Flaw to Install Malware on Routers and KVM Devices](https://thehackernews.com/2026/11/hackers-exploited-glinet-cloud-flaw-to.html)
_The Hacker News · Nov 23 · score 0.127_

Hackers exploited a vulnerability in GL.iNet's GoodCloud remote management service to install malware on some customer routers and KVM devices, the maker of travel routers and remote-access KVM hardware said in a security notice updated today. The company identified and fixed the flaw on Friday and …

`kvm`

### 72. [Plug and Pray: Your AI Agents Are Taking Orders From Strangers](https://www.ox.security/blog/plug-and-pray-your-ai-agents-are-taking-orders-from-strangers/)
_OX Security · Nov 23 · score 0.125_

OX Security analyzed 542,207 components across npm, PyPI, MCP servers and Agent Skills. The findings demonstrate how the attack surface is expanding from code that runs to instructions that agents follow. We all learned the USB rule years ago. Don&#8217;t plug in a drive you just found somewhere. Yo…

`npm` `pypi`

### 73. [⚡ Weekly Recap: VMware 0-Day, Java4Shell, NGINX2Root, Ruby2Shell, and a Whole Lot of Shell Trouble](https://thehackernews.com/2026/11/weekly-recap-vmware-0-day-java4shell.html)
_The Hacker News · Nov 23 · score 0.085_

A stolen key. A trusted message. A routine update. None of these looks like the start of a major security problem. That's partly why they work. Attackers don't always need to break down a door. Sometimes they just use one that's already open. This week's stories show how quickly a small opening can …

`vmware` `breach`

### 74. [Webworm Suspected of Modifying SoftEther VPN to Evade Detection and Hide Remote Access](https://thehackernews.com/2026/11/webworm-suspected-of-modifying.html)
_The Hacker News · Nov 23 · score 0.080_

The China-aligned threat actor known as Webworm is suspected to be using a custom version of the open-source SoftEther VPN Bridge tool in an attempt to remove recognizable detection fingerprints, while disguising it as network-monitoring software to establish covert remote access to compromised netw…

`vpn`

### 75. [Issue statuses and repository boards are in public preview](https://github.blog/changelog/2026-11-23-issue-statuses-and-repository-boards-are-in-public-preview)
_GitHub Changelog · Nov 23 · score 0.029_

Open or closed doesn&#8217;t always tell you where an issue stands. You can now use more specific statuses to give your team and agents shared context about what&#8217;s in flight&#8230; The post Issue statuses and repository boards are in public preview appeared first on The GitHub Blog .

`github`

### 76. [Code coverage uploads now flag invalid report formats](https://github.blog/changelog/2026-11-23-code-coverage-uploads-now-flag-invalid-report-formats)
_GitHub Changelog · Nov 23 · score 0.017_

The GitHub Code Quality upload-code-coverage action now checks that your coverage report is in Cobertura XML format. If it isn&#8217;t in a supported format, the upload step fails and the&#8230; The post Code coverage uploads now flag invalid report formats appeared first on The GitHub Blog .

`github`

### 77. [RUSTSEC-2026-0595: Unsoundness in parquet](https://rustsec.org/advisories/RUSTSEC-2026-0595.html)
_RustSec · Nov 23 · score 0.004_

Apache Arrow Rust: Bloom filters written as plaintext when writing encrypted Parquet

`rust`

### 78. [Secret scanning reduces false positives for Slack](https://github.blog/changelog/2026-11-23-secret-scanning-reduces-false-positives-for-slack)
_GitHub Changelog · Nov 23 · score 0.001_

Secret scanning now reduces false-positive detections for Slack secrets. False positives reduced The following detector improvements reduce false-positive matches for supported secrets. Provider Secret type Improvement Slack slack_incoming_webhook_url Exclude URLs&#8230; The post Secret scanning red…

`github` `slack`

### 79. [Usage reports will include a user ID column starting December 1](https://github.blog/changelog/2026-11-23-usage-reports-will-include-a-user-id-column-starting-december-1)
_GitHub Changelog · Nov 23 · score 0.001_

Starting December 1, 2026, usage reports that include a username column will also include a user_id column next to it. Every column after username will move one position to the&#8230; The post Usage reports will include a user ID column starting December 1 appeared first on The GitHub Blog .

`github`
