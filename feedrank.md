# feedrank — 2026-11-07

_80 items, 5d window._

### 1. [SonicWall SonicOS SSLVPN: SonicWall SonicOS SSLVPN Use of Single-factor Authentication Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-19868)
_CISA KEV · Nov 06 · score 1.927 · **CRITICAL 9.0** · ×2 reports · CVE-2026-19868_

SonicWall SonicOS SSLVPN contains a use of single-factor authentication vulnerability that may allow a user with valid credentials for an alternate authentication method to bypass SAML authentication controls. Successful exploitation may also bypass SAML-enforced multi-factor authentication (MFA). R…

`saml` `mfa` `sonicwall`

_also: [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/06/cisa-adds-one-known-exploited-vulnerability-catalog)_

### 2. [LXD has restricted project bypass leading to arbitrary command execution](https://github.com/advisories/GHSA-47w9-6r3f-938g)
_GHSA — go · Nov 06 · score 1.440 · **CRITICAL 9.9** · ×11 reports · CVE-2026-12411, CVE-2026-28385, CVE-2026-9639_

Affected: github.com/canonical/lxd. Reported from https://github.com/lxc/incus/security/advisories/GHSA-48q5-w887-33wv ### Summary Instance snapshots ignore the `restricted.containers.lowlevel=block` setting; allowing for arbitrary command execution on the Incus server by abusing lowlevel hooks such…

`github` `qemu`

_also: [GHSA — go](https://github.com/advisories/GHSA-7mr3-28h5-m5vx), [GHSA — go](https://github.com/advisories/GHSA-qx75-2p3r-pwm5), [GHSA — go](https://github.com/advisories/GHSA-j93m-3j9p-m5m8), [GHSA — go](https://github.com/advisories/GHSA-pjff-c2wc-f6jm), [GHSA — go](https://github.com/advisories/GHSA-fmc8-p6q7-75cc)_

### 3. [Shai-Hulud Descendant Surfaces in Malicious Ruby Gem That Steals Credentials and Poisons AI Tools](https://socket.dev/blog/shai-hulud-descendant-malicious-ruby-gem?utm_medium=feed)
_Socket Blog · Nov 06 · score 1.426 · **CRITICAL 9.0** · ×2 reports_

A malicious Ruby gem runs a credential-stealing worm during installation, poisons AI coding tools, and can wipe files when a stolen GitHub token is revoked.

`ruby` `gem ` `github` `token` `credential`

_also: [StepSecurity](https://www.stepsecurity.io/blog/malicious-files-find-what-supply-chain-attacks-leave-behind-in-your-github-repositories-and-on-developer-machines)_

### 4. [Installing the Fix for an Exploited WordPress Flaw Can Expose Some Sites One Last Time](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)
_The Hacker News · Nov 06 · score 0.676 · **CRITICAL 9.5**_

Some WordPress sites can still be attacked while they install the fix for an actively exploited flaw, according to Umut Bayram, the Picus Security researcher who found it. The update that installs the fix still unpacks its files using the site's old, unpatched code, so an attacker who strikes at the…

`actively exploited`

### 5. [Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It](https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html)
_The Hacker News · Nov 06 · score 0.335 · **CRITICAL 9.0** · CVE-2026-83844_

A fix for CVE-2026-83844, a remote code execution flaw in Windows Paint, is now in the Microsoft Store. Paint gets this fix only through a Store update, not through Windows updates. The fixed build, 11.2609.401.0, was the newest Paint build in all ten countries The Hacker News checked today. The fla…

`windows` `rce` `cve-`

### 6. [Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs](https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html)
_The Hacker News · Nov 06 · score 0.228 · **CRITICAL 9.0**_

A backdoor has been found hiding in the web server that runs Control Web Panel (CWP), a free panel for managing Linux hosting servers, researchers at QiAnXin's XLab said this week. The backdoored web server executes commands that attackers send via web requests, and those requests never appear in it…

`linux` `backdoor`

### 7. [OSAC operator: Kubeconfig credential-plugin execution and SSRF in console proxy](https://github.com/advisories/GHSA-5w5g-j6hw-6p8f)
_GHSA — go · Nov 06 · score 0.670 · **HIGH** · CVE-2026-62284_

Affected: github.com/osac-project/osac-operator. ### Impact The console-proxy's RemoteConfigResolver parses kubeconfig data from Kubernetes Secrets using clientcmd.RESTConfigFromKubeConfig without sanitizing the resulting rest.Config. A kubeconfig containing an exec plugin stanza (under users[].user…

`go ` `github` `kubernetes` `credential` `ssrf`

### 8. [Fake security tools on GitHub push backdoors and infostealers](https://www.bleepingcomputer.com/news/security/fake-security-tools-on-github-push-backdoors-and-infostealers/)
_BleepingComputer · Nov 06 · score 0.512 · **HIGH 8.5**_

Cybersecurity professionals are being targeted with infected security projects on GitHub that deploy a backdoor and information stealer malware. [...]

`github` `stealer` `backdoor`

### 9. [Experts Demonstrate Barracuda Email Security Gateway Chain Enabling Root Access Without Login](https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html)
_The Hacker News · Nov 06 · score 0.426 · **HIGH 8.0** · ×2 reports · CVE-2026-116606_

Two flaws in Barracuda's Email Security Gateway, an email-filtering appliance, can be chained to run commands on it as root, its highest level of access, with no login required. The company released patches on Monday, and the security firm watchTowr detailed the attack chain on Thursday. One flaw, C…

`barracuda` `cve-`

_also: [The Hacker News](https://thehackernews.com/2026/11/barracuda-flaws-could-be-chained-to.html)_

### 10. [OpenAI's new GPT-6 Cyber AI finds 81 Firefox flaws, 948 Linux bugs](https://www.bleepingcomputer.com/news/security/openais-new-gpt-6-cyber-ai-finds-81-firefox-flaws-948-linux-bugs/)
_BleepingComputer · Nov 06 · score 0.167 · **HIGH 7.5**_

OpenAI has revealed GPT-6 Cyber, a new artificial intelligence model that has discovered 81 previously unknown high-severity Firefox vulnerabilities and developed working exploits for 948 distinct Linux kernel flaws. [...]

`linux` `kernel` `firefox`

### 11. [kaniko can send the build's Azure (Entra ID) access token to lookalike ACR registry hosts](https://github.com/advisories/GHSA-5q7h-w9jf-cx97)
_GHSA — go · Nov 05 · score 1.053 · **CRITICAL 9.3** · CVE-2026-105769_

Affected: github.com/chainguard-dev/kaniko. ### Summary kaniko before v1.25.20 can send a Microsoft Entra ID (Azure AD) access token for Azure Resource Manager to a registry host an attacker controls. A Dockerfile that references an image on a lookalike host, such as `FROM x.azurecr.io.attacker.com/…

`github` `container` `docker` `azure` `entra`

### 12. [Zyxel GS1900 Patch Fails to Block Zero-Day Exploit Allowing Root Command Execution](https://thehackernews.com/2026/11/zyxel-gs1900-patch-fails-to-block-zero.html)
_The Hacker News · Nov 05 · score 0.975 · **CRITICAL 9.5**_

Zyxel GS1900 network switches that received the vendor's earlier fix for an actively exploited flaw are still open to the exploit attackers used, researchers at Binarly found. The exploit lets anyone who can reach a switch's web management interface run commands on it without logging in. Zyxel has r…

`zero-day` `exploit` `actively exploited`

### 13. [Apple Multiple Products: Apple Multiple Products Improper Authentication Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2024-27834)
_CISA KEV · Nov 05 · score 0.807 · **CRITICAL 9.0** · ×2 reports · CVE-2024-27834_

Apple iOS, iPadOS, macOS, Safari, tvOS and watchOS 10.5 contain an improper authentication vulnerability which could allow an attacker with arbitrary read and write capability to bypass pointer authentication. Required action: Apply mitigations in accordance with vendor instructions, ensuring compli…

`macos` `apple` `safari`

_also: [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-patched-apple-flaw-to.html)_

### 14. [OpenSSH Issues Emergency Fix for Flaw Letting Long Passwords Bypass SSH Auth on Alpine Linux](https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html)
_The Hacker News · Nov 05 · score 0.465 · **CRITICAL 9.5**_

Attackers can log in to accounts that have no password, such as SSH key-only accounts, on some Alpine Linux servers running the standard openssh-server package. They need network access to the server, an account name, and a password between 257 and 1,024 bytes long. OpenSSH, which rates the flaw cri…

`linux` `alpine` `ssh` `openssh`

### 15. [ThreatsDay: Apache OFBiz RCE, DreamHost Breach, DeFi Site Hijacks + 17 More Stories](https://thehackernews.com/2026/11/threatsday-apache-ofbiz-rce-dreamhost.html)
_The Hacker News · Nov 05 · score 0.235 · **CRITICAL 9.0**_

How much damage can someone do without breaking much? Quite a lot, it seems. A stolen login can open doors across several systems. A trusted setting can be used to lock people out. Even a simple file copy can reach places it shouldn't. And while new tools are helping find security holes faster, some…

`rce` `breach`

### 16. [Banks: Unsafe importlib.import_module of attacker-controlled Tool.import_path in CompletionExtension allows RCE](https://github.com/advisories/GHSA-64vx-6h2c-rjh7)
_GHSA — pip · Nov 05 · score 0.225 · **HIGH 7.5** · CVE-2026-61536_

Affected: banks. ## Summary `banks` parses `Tool` JSON objects from the rendered body of `{% completion %}` blocks and later resolves their `import_path` field through `importlib.import_module(...)` + `getattr(...)` to obtain the callable that handles a tool call. There is no allowlist or sanitizati…

`python` `rce`

### 17. [Critical Rails Flaw Lets Attackers Write Server Files via Crafted ImageMagick Uploads](https://thehackernews.com/2026/11/critical-rails-flaw-lets-attackers.html)
_The Hacker News · Nov 04 · score 0.196 · **CRITICAL 9.5**_

A critical flaw in Ruby on Rails could allow an unauthenticated attacker to write arbitrary files on an app's server by uploading a crafted file if the app processes uploads using ImageMagick. The Rails project disclosed the flaw in&nbsp;an advisory&nbsp;and fixed it in versions 8.1.4.1 and 8.0.5.2.…

`ruby`

### 18. [Risky Bulletin: Hackers brick Chinese EVs in Russia](https://risky.biz/RBNEWS629/)
_Risky Business News · Nov 04 · score 0.173 · **CRITICAL 9.0**_

Hackers brick Chinese EVs in Russia, a second wave of hacks defrost European supermarket freezers, the US boots Acronis from government networks and the major distros patch a Linux kernel RCE.

`linux` `kernel` `rce`

### 19. [Google Issues Patches for Critical Android Flaw That Could Allow RCE Without User Interaction](https://thehackernews.com/2026/11/google-patches-critical-android-flaw.html)
_The Hacker News · Nov 04 · score 0.124 · **CRITICAL 9.5** · CVE-2026-58868_

A critical Android flaw could allow an attacker to run code on a phone without any user action remotely, Google said in its&nbsp;November security bulletin. The flaw, CVE-2026-58868, affects Android 14 through 17. Phones get the fix with security patch level 2026-11-01 or later, which phone makers a…

`rce` `cve-`

### 20. [PolinRider Returns: Hijacked npm Packages Use Ethereum Blockchain to Conceal Malware Infrastructure](https://www.ox.security/blog/polinrider-returns-hijacked-npm-packages-use-ethereum-blockchain-to-conceal-malware-infrastructure/)
_OX Security · Nov 04 · score 0.744 · **HIGH 8.5**_

Overview OX Security researchers identified malicious releases of legitimate npm packages compromised in a campaign linked to the PolinRider malware family. The injected code uses the Ethereum blockchain as a dead drop for command-and-control (C2) infrastructure. When an affected package is imported…

`npm`

### 21. [APT29-Linked Hackers Hijack Web Analytics Script to Deliver iOS and Android Exploits](https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html)
_The Hacker News · Nov 04 · score 0.613 · **HIGH 8.5**_

The Russia-linked threat actor known as APT29 is presumed to be behind a large-scale watering hole campaign targeting iOS and Android users through compromised websites, fake domains, and a supply chain attack involving a Ukrainian web analytics service called Plerdy SEO Tracker. "The injected JavaS…

`javascript` `supply chain`

### 22. [CISA Confirms Hackers Exploiting WordPress Core Flaw During Software Upgrades](https://thehackernews.com/2026/11/cisa-confirms-hackers-exploiting.html)
_The Hacker News · Nov 04 · score 0.435 · **HIGH 7.5** · CVE-2026-119977_

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a security flaw in WordPress Core to the Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The high-severity vulnerability, tracked as CVE-2026-119977 (CVSS score: 8.1), is a case of Time-…

`kev` `cve-` `cvss`

### 23. [SonicWall Won't Patch EoL GMS Flaws That Could Expose Files, Alter Database Records](https://thehackernews.com/2026/11/sonicwall-wont-patch-eol-gms-flaws-that.html)
_The Hacker News · Nov 04 · score 0.273 · **HIGH 8.0** · CVE-2026-109593_

SonicWall has warned of two vulnerabilities impacting end-of-life Global Management System (GMS) systems that it said will not be patched. Details of the security flaws, which affect SonicWall GMS 9.5.2 and earlier versions, are below - CVE-2026-109593 (CVSS score: 9.1) - An unauthenticated file rea…

`sonicwall` `cve-` `cvss`

### 24. [China-Aligned Hackers Hijack Sogou Input Method DNS Requests to Deploy DarkVigil Backdoor](https://thehackernews.com/2026/11/china-aligned-hackers-hijack-sogou.html)
_The Hacker News · Nov 04 · score 0.224 · **HIGH 8.5**_

A China-aligned threat actor known as SlippyNunchucks has been attributed to a Domain Name System (DNS) hijacking operation abusing insecure HTTP communications in Windows versions of Sogou Input Method as part of a surveillance campaign designed to deploy an implant called DarkVigil (aka FDMTP). Th…

`windows` `dns` `backdoor`

### 25. [Elo JavaScript emitter has sandbox escape to arbitrary Node.js / browser code execution via unfiltered `.constructor` member access](https://github.com/advisories/GHSA-33r5-xmm8-v6x5)
_GHSA — npm · Nov 03 · score 1.240 · **CRITICAL 9.8** · ×3 reports · CVE-2026-44265, CVE-2026-44266, CVE-2026-44267_

Affected: @enspirit/elo. ### Summary An unauthenticated attacker who controls a string passed to any Elo JavaScript-emission path — `defaultFormats.elo.parse()`, the `bin/elo` CLI, or the live browser playground at `elo-lang.org/try` — can execute arbitrary code in the host JavaScript runtime. A pay…

`node` `javascript`

_also: [GHSA — npm](https://github.com/advisories/GHSA-7w38-ggh5-v542), [GHSA — npm](https://github.com/advisories/GHSA-x9rp-7wh3-2rj5)_

### 26. [Attackers Exploit Critical Siemens IoT2050 Flaw to Plant Remote Command Backdoors](https://thehackernews.com/2026/11/attackers-exploit-critical-siemens.html)
_The Hacker News · Nov 03 · score 0.349 · **CRITICAL 9.5** · CVE-2026-58115_

A maximum-severity security flaw impacting Siemens SIMATIC IoT2050 Advanced devices has come under active exploitation, VulnCheck has revealed. The vulnerability, tracked as CVE-2026-58115 (CVSS score: 10.0), is a case of missing authentication for a critical function that could be exploited by an u…

`exploit` `cve-` `cvss`

### 27. [Red Hat Patches 9.8-Rated Linux TCP RCE Flaw While Ubuntu Releases Fixes for Testing](https://thehackernews.com/2026/11/red-hat-patches-98-rated-linux-tcp-rce.html)
_The Hacker News · Nov 03 · score 0.161 · **CRITICAL 9.0** · CVE-2026-98432_

Fixed kernels for a&nbsp;use-after-free vulnerability in the Linux kernel's IPv4 TCP code&nbsp;are now available for Red Hat Enterprise Linux 8, 9, and 10, while Ubuntu's fixes for its three newest long-term-support releases remain in its opt-in testing channel with no date for a regular update. The…

`linux` `kernel` `ubuntu` `rce` `cve-`

### 28. [Hardening GitHub Actions Against Outside Threats](https://socket.dev/blog/hardening-github-actions-against-outside-threats?utm_medium=feed)
_Socket Blog · Nov 03 · score 1.135 · **HIGH 8.5**_

A practical guide to securing GitHub Actions against supply chain attacks, covering malicious pull requests, credential theft, dependency risks, and release pipelines.

`github` `github actions` `supply chain` `credential`

### 29. [cPGuard Update Channel Hijacked to Backdoor Linux Servers and Collect Password Hashes](https://thehackernews.com/2026/11/cpguard-update-channel-hijacked-to.html)
_The Hacker News · Nov 03 · score 0.387 · **HIGH 8.5**_

An attacker broke into the update system of the cPGuard security tool on November 2 and used it to send a malicious script to customers' Linux servers. The script installed a backdoor and collected password hashes and other sensitive files from servers that ran it, cPGuard maker OPSSHIELD said in an…

`linux` `backdoor`

### 30. [praktor: Path traversal in Telegram file uploads allows writing outside the agent workspace uploads/ directory (stored instruction injection)](https://github.com/advisories/GHSA-48v2-6jcm-fc99)
_GHSA — go · Nov 03 · score 0.328 · **HIGH 8.2** · CVE-2026-62331_

Affected: github.com/mtzanidakis/praktor. ### Impact A remote Telegram user can write files to arbitrary paths inside an agent's persistent workspace volume (`praktor-wk-<workspace>`, mounted at `/workspace/agent`), escaping the documented `uploads/` directory. The attacker controls the Telegram doc…

`github`

### 31. [Stanza: RCE via pickle deserialization in the lemmatizer](https://github.com/advisories/GHSA-gh9r-c94j-cmp5)
_GHSA — pip · Nov 03 · score 0.153 · **HIGH 7.8** · CVE-2026-115878_

Affected: stanza. ## TL;DR Loading an attacker-supplied lemma `.pt` runs arbitrary code as the loading user. Since 1.14.0 the lemmatizer stores `pos_dict` as a gzip-compressed pickle in the checkpoint's `dicts` field (a `bytes` value). `torch.load(weights_only=True)` treats `bytes` as a primitive an…

`checkpoint` `rce` `deserialization`

### 32. [Attackers Target Unpatched CryptoPayment Gateway Flaw That Can Expose Wallet Credentials](https://thehackernews.com/2026/11/attackers-target-unpatched.html)
_The Hacker News · Nov 03 · score 0.125 · **HIGH 8.0** · CVE-2026-81648_

Threat actors are attempting to exploit an unpatched maximum-severity security vulnerability in the CryptoPayment Gateway WordPress plugin, according to findings from Defused Cyber. The vulnerability in question is CVE-2026-81648, which carries a CVSS score of 10.0. Successful exploitation of the fl…

`exploit` `cve-` `cvss`

### 33. [⚡ Weekly Recap: Critical CVEs, Linux DDoS Botnet, Device-Code Phishing, Android Spyware and More](https://thehackernews.com/2026/11/weekly-recap-critical-cves-linux-ddos.html)
_The Hacker News · Nov 02 · score 0.288 · **CRITICAL 9.5**_

Some attacks this week didn't need much of a trick. A fake support call, a trusted extension, a shared link, or a device with no password. Small things that people barely think about. Yet each was enough to cause serious trouble. Then there were the bigger messes. Billions stolen, hidden networks of…

`linux`

### 34. [SD JWT JS: Tampered disclosures silently dropped instead of rejected](https://github.com/advisories/GHSA-f9j6-8p6x-r9j6)
_GHSA — npm · Nov 02 · score 0.275 · **HIGH** · CVE-2026-62374_

Affected: @sd-jwt/decode, @sd-jwt/core. ## Summary When one Disclosure in an SD-JWT presentation is tampered so its digest no longer matches the Issuer-signed `_sd` array, `@sd-jwt/decode` 0.19.0 does **not** reject the presentation. It silently drops the unmatched Disclosure and returns a **reduced…

`jwt` `credential`

### 35. [Google Disrupts 1.3 Million-Device Android Botnet, Says TV Box Maker Sold Criminal Access](https://thehackernews.com/2026/11/google-disrupts-13-million-device.html)
_The Hacker News · Nov 02 · score 0.143 · **HIGH 8.5**_

A botnet of more than 1.3 million Android devices, mostly TV set-top boxes, lost control of its servers in late October in a takedown led by Google. Google says&nbsp;it is highly confident that device maker Videostrong intentionally put a backdoor in the boxes and sold access to criminals. They used…

`backdoor`

### 36. [SonicWall warns of new SSL-VPN MFA bypass flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-new-ssl-vpn-mfa-bypass-flaw-exploited-in-attacks/)
_BleepingComputer · Nov 07 · score 0.537_

SonicWall has released security updates to fix seven vulnerabilities in SonicOS firewalls, including an SSL-VPN authentication bypass flaw exploited in attacks. [...]

`mfa` `ssl` `vpn` `sonicwall` `authentication bypass`

### 37. [Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)
_The Hacker News · Nov 07 · score 0.150_

Passwords and API keys that developers typed into commands they approved in Claude Code are sitting in public GitHub repositories, where anyone can read them. When a user selects "Yes, and don't ask again," Anthropic's AI coding assistant can save the command, word-for-word, including the secret, in…

`github`

### 38. [Copilot code review: API management and review overview updates](https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates)
_GitHub Changelog · Nov 07 · score 0.074_

You can now manage GitHub Copilot code review settings through the REST and GraphQL APIs, from enterprise policy down to individual repositories. Copilot&#8217;s review overview comment is now more compact,&#8230; The post Copilot code review: API management and review overview updates appeared firs…

`github`

### 39. [CVE-2026-123158 (*sshole): OpenSSH Password Authentication Bypass on Alpine Linux](https://www.stepsecurity.io/blog/cve-2026-123158-sshhole-openssh-musl-password-bypass)
_StepSecurity · Nov 06 · score 1.043 · ×3 reports · CVE-2026-123158_

CVE-2026-123158 (*sshole) enables an OpenSSH authentication bypass on Alpine Linux. Review lab results, exposure conditions, fixes, and mitigations.

`linux` `alpine` `openssh` `authentication bypass` `cve-`

_also: [OX Security](https://www.ox.security/blog/openssh-authentication-bypass-cve-2026-123158/), [The Hacker News](https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html)_

### 40. [listmonk: SQL Injection in `/api/subscribers/export` bypasses table access control, leaking admin password hashes and SMTP credentials](https://github.com/advisories/GHSA-xgjr-7j9q-2h4r)
_GHSA — go · Nov 06 · score 0.619 · **MEDIUM 5.5** · CVE-2026-62361_

Affected: github.com/knadh/listmonk. ### Summary A SQL injection vulnerability in `GET /api/subscribers/export` allows an authenticated user with the `subscribers:sql_query` permission to bypass the table access control that exists on the regular query endpoint (`GET /api/subscribers`) and read arbi…

`github` `exfiltration` `sql injection` `privilege escalation`

### 41. [OpenSSH auth bypass bug hits Alpine Linux, OperWRT](https://risky.biz/RBNEWS630/)
_Risky Business News · Nov 06 · score 0.401_

An OpenSSH authentication bypass bug hits Alpine Linux and OpenWRT, hackers attempt to raise fridge temperatures at French blood banks, a French bank gets hacked for $133 million, and the Thai opposition has been targeted with spyware.

`linux` `alpine` `openssh` `authentication bypass`

### 42. [Chainalysis says breach exposed credentials for all customers](https://www.bleepingcomputer.com/news/security/chainalysis-says-breach-exposed-credentials-for-all-customers/)
_BleepingComputer · Nov 06 · score 0.371_

Blockchain intelligence firm Chainalysis says a recent attack on its systems and internal tools has exposed credentials and live tokens for all customers. [...]

`breach`

### 43. [Chainalysis Breach Exposes All Users' Credentials, Forces Shutdown of Key Services](https://thehackernews.com/2026/11/chainalysis-breach-exposes-all-users.html)
_The Hacker News · Nov 06 · score 0.256_

Blockchain analysis firm Chainalysis has revealed that its ongoing investigation into the agentic cyber attack targeting its systems also exposed names, usernames, password hashes and live tokens for all users. "While we investigated, we removed access to Reactor and Data Solutions," the company sai…

`breach`

### 44. [Runaway AI hacking agent behind WorkOS breach after escaping sandbox](https://www.bleepingcomputer.com/news/security/runaway-ai-hacking-agent-behind-workos-breach-after-escaping-sandbox/)
_BleepingComputer · Nov 06 · score 0.165_

WorkOS says an AI-powered hacking agent that breached its internal sales application and accessed customer information was operated by a security researcher who claims the tool escaped its testing environment and unintentionally attacked the company. [...]

`breach`

### 45. [10 Snyk Alternatives for Engineering & Security Teams (2027) | Endor Labs | Endor Labs](https://www.endorlabs.com/learn/snyk-alternatives)
_Endor Labs · Nov 06 · score 0.133_

Compare 10 Snyk alternatives for SCA, SAST and container scanning, with reachability, AI capabilities and fit by team size, build system and compliance needs.

`container` `teams`

### 46. [RUSTSEC-2026-0443: Vulnerability in actix-files](https://rustsec.org/advisories/RUSTSEC-2026-0443.html)
_RustSec · Nov 06 · score 0.123_

Hidden file disclosure through Windows short names

`windows`

### 47. [@GitHub in Slack and Teams is generally available and more](https://github.blog/changelog/2026-11-06-github-copilot-in-slack-and-teams-is-generally-available)
_GitHub Changelog · Nov 06 · score 0.082_

Turn conversations into code with @GitHub in Slack and Teams! Investigate bugs, create issues, implement changes, and open pull requests&#8212;all without leaving your conversation. What&#8217;s new Build and review together&#8230; The post @GitHub in Slack and Teams is generally available and more …

`github` `slack` `teams`

### 48. [Usage metrics API adds code review details and addressed rate](https://github.blog/changelog/2026-11-05-usage-metrics-api-adds-code-review-details-and-addressed-rate)
_GitHub Changelog · Nov 06 · score 0.079_

The enterprise and organization repository-level Copilot usage metrics reports now show what happens to Copilot code review feedback. A new copilot_code_review object on each repos-1-day row reports how many Copilot-reviewed&#8230; The post Usage metrics API adds code review details and addressed ra…

`github`

### 49. [GitHub Copilot weekly releases — November 2](https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2)
_GitHub Changelog · Nov 06 · score 0.045_

This week, Copilot comes to JetBrains Air and Xcode&#8217;s coding assistant, with updates to help you manage pull requests, settings, and agent sessions. GitHub Copilot app Set up Agent Merge&#8230; The post GitHub Copilot weekly releases — November 2 appeared first on The GitHub Blog .

`github`

### 50. [Copilot impact dashboard adds chat and VS Code agent usage](https://github.blog/changelog/2026-11-06-copilot-impact-dashboard-adds-chat-and-vs-code-agent-usage)
_GitHub Changelog · Nov 06 · score 0.037_

The Agent adoption chart in the Copilot impact dashboard now includes Copilot Chat and the VS Code Agents window, so you can see engagement across nine Copilot experiences. The adoption&#8230; The post Copilot impact dashboard adds chat and VS Code agent usage appeared first on The GitHub Blog .

`github`

### 51. [GeoNode has Stored XSS in Documents metadata abstract field](https://github.com/advisories/GHSA-r4hm-p9f9-fj9v)
_GHSA — pip · Nov 06 · score 0.016 · **MEDIUM 6.3** · CVE-2026-55649_

Affected: GeoNode. The abstract metadata of documents is not sanitised. It’s possible to store arbitrary HTML (and JS) that will be executed when visiting the page.

`xss`

### 52. [OpenAI Launches GPT-6 Cyber After AI Helps Find 81 Firefox Flaws, 948 Linux Exploits](https://thehackernews.com/2026/11/openai-launches-gpt-6-cyber-after-ai.html)
_The Hacker News · Nov 06 · score 0.007_

OpenAI on Thursday unveiled GPT‑6 Cyber, which it described as a major step forward in security research that brings together stronger cybersecurity capabilities with a step-change improvement in model alignment. The new model is "more capable at finding and fixing vulnerabilities, and far more reli…

`linux` `firefox`

### 53. [The Flood is Coming And The Pipes Were Already Full](https://thehackernews.com/2026/11/the-flood-is-coming-and-pipes-were.html)
_The Hacker News · Nov 06 · score 0.006_

An update on Athena, and some unsolicited predictions on what's coming next On Saturday, Dario Amodei published We Must Pace the Frontier. I agree with him. Go read it if you haven't. I've spent the summer looking at what these models find, and the gap he describes between what they can do and what …

`go `

### 54. [Usage metrics API flags telemetry and version gaps](https://github.blog/changelog/2026-11-05-usage-metrics-api-flags-telemetry-and-version-gaps)
_GitHub Changelog · Nov 06 · score 0.003_

The Copilot usage metrics API now shows which users are missing client telemetry or are running IDE or extension versions below the usage metrics minimums. New per-user fields appear in&#8230; The post Usage metrics API flags telemetry and version gaps appeared first on The GitHub Blog .

`github`

### 55. [Researchers Bypass ChatGPT Lockdown Mode to Exfiltrate Chats Without User Interaction](https://thehackernews.com/2026/11/researchers-bypass-chatgpt-lockdown.html)
_The Hacker News · Nov 05 · score 0.334_

Cybersecurity researchers have disclosed details of a now-patched vulnerability that could be exploited to bypass Lockdown Mode protections in OpenAI ChatGPT. Lockdown Mode was introduced by the artificial intelligence (AI) company in June 2026 as an optional setting to minimize data exfiltration ri…

`exfiltration`

### 56. [GitHub to Block pull_request_target Workflows by Default Starting December 2](https://socket.dev/blog/github-to-block-pull-request-target?utm_medium=feed)
_Socket Blog · Nov 05 · score 0.324_

GitHub is tightening GitHub Actions security with new restrictions on privileged pull request workflows. Here's what changes and how maintainers are affected.

`github` `github actions`

### 57. [OpenAI AI Pipeline Generates 948 Linux Root Escalation Exploits in 30-Hour Run](https://thehackernews.com/2026/11/openai-ai-pipeline-generates-948-linux.html)
_The Hacker News · Nov 05 · score 0.309_

OpenAI on Wednesday detailed a pipeline that employed an upcoming cyber-focused artificial intelligence (AI) model to validate and patch 948 local privilege escalation vulnerabilities in Linux for $1.2 million in API costs. "Our prototype identified and analyzed 2,308 candidate Linux kernel findings…

`linux` `kernel` `privilege escalation`

### 58. [[tl;dr sec] #353 - A Thousand Fewer Paths to Root, Kubernetes Security Logging, Post-AI Security Floor](https://tldrsec.com/p/tldr-sec-353)
_tl;dr sec · Nov 05 · score 0.304_

OpenAI's pipeline found 948 LPEs in Linux, how to build a comprehensive security logging platform for k8s clusters, 3 security priorities in a world with powerful AI

`kubernetes` `k8s` `linux`

### 59. [OpenSSH flaw lets attackers log into password-disabled Linux accounts](https://www.bleepingcomputer.com/news/security/openssh-flaw-lets-attackers-log-into-password-disabled-linux-accounts/)
_BleepingComputer · Nov 05 · score 0.252_

A newly disclosed OpenSSH vulnerability dubbed "*sshole" allows attackers to log in to certain Alpine Linux and other musl-based Linux accounts that are configured to block password authentication, simply by entering an oversized password. [...]

`linux` `alpine` `musl` `openssh`

### 60. [CVE-2026-109518: apt Flaw Lets Attackers Swap Packages After Verification and Run Code as Root](https://www.stepsecurity.io/blog/cve-2026-109518-apt-package-swap-root)
_StepSecurity · Nov 05 · score 0.190 · CVE-2026-109518_

Understand CVE-2026-109518, patch vulnerable APT clients, and use Harden-Runner to find HTTP package downloads and investigate CI/CD activity.

`ci/cd` `runner` `cve-`

### 61. [RUSTSEC-2026-0437: Vulnerability in azure_security_keyvault_certificates](https://rustsec.org/advisories/RUSTSEC-2026-0437.html)
_RustSec · Nov 05 · score 0.102_

Rejected authentication challenges can poison the Key Vault scope cache

`key vault`

### 62. [RUSTSEC-2026-0438: Vulnerability in azure_security_keyvault_secrets](https://rustsec.org/advisories/RUSTSEC-2026-0438.html)
_RustSec · Nov 05 · score 0.102_

Rejected authentication challenges can poison the Key Vault scope cache

`key vault`

### 63. [RUSTSEC-2026-0439: Vulnerability in azure_security_keyvault_keys](https://rustsec.org/advisories/RUSTSEC-2026-0439.html)
_RustSec · Nov 05 · score 0.102_

Rejected authentication challenges can poison the Key Vault scope cache

`key vault`

### 64. [Apple to Start Scanning Publicly Shared iCloud Photos and Files for Harmful Content](https://thehackernews.com/2026/11/apple-to-start-scanning-publicly-shared.html)
_The Hacker News · Nov 05 · score 0.055_

Apple has revealed that it plans to start checking public iCloud links for harmful content starting with iOS 27.3, iPadOS 27.3, macOS 27.3, and visionOS 27.3. The change specifically applies to scenarios where users share iCloud content, such as photos in iCloud Photos or files in iCloud Drive, by s…

`macos` `apple`

### 65. [New pull request overview page in public preview](https://github.blog/changelog/2026-11-05-new-pull-request-overview-page-in-public-preview)
_GitHub Changelog · Nov 05 · score 0.046_

On a long pull request, checking what&#8217;s blocking often means scrolling past dozens of comments and timeline events just to reach the merge box. And once you&#8217;re there, you still&#8230; The post New pull request overview page in public preview appeared first on The GitHub Blog .

`github`

### 66. [Secret scanning upgrades detectors, adds SpaceX as partner](https://github.blog/changelog/2026-11-05-secret-scanning-upgrades-detectors-adds-spacex-as-partner)
_GitHub Changelog · Nov 05 · score 0.045_

This update expands secret scanning&#8217;s detection coverage: New partner: SpaceX is now a secret scanning partner. New detector: GitHub now detects starlink_public_api_v2_secret. Upgraded detectors: Alibaba, AWS, Google, OpenVSX, Pydantic Services,&#8230; The post Secret scanning upgrades detecto…

`github` `aws`

### 67. [RUSTSEC-2026-0442: Unsoundness in arrow-data](https://rustsec.org/advisories/RUSTSEC-2026-0442.html)
_RustSec · Nov 05 · score 0.007_

Apache Arrow Rust: Improper validation of RunEndEncoded arrays allows out of bounds reads

`rust`

### 68. [Arc: DuckDB I/O aliases bypass database RBAC after CVE-2026-47735](https://github.com/advisories/GHSA-93cm-2v4m-c56c)
_GHSA — go · Nov 04 · score 0.662 · **MEDIUM 6.5** · ×2 reports · CVE-2026-55098_

Affected: github.com/basekick-labs/arc. ### Summary The fix for CVE-2026-47735 (released 2026.06.1) is incomplete. It added a DuckDB sandbox (`SET GLOBAL allowed_directories=[<storage root>]; SET GLOBAL enable_external_access=false`) and an Arc SQL-layer denylist of the **literal** functions `read_p…

`github` `token` `ssrf` `cve-`

_also: [GHSA — go](https://github.com/advisories/GHSA-m3qr-fvp4-78xj)_

### 69. [Xen Hypervisor Flaws Let One Malicious VM Read and Write Any Other VM's Memory](https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html)
_The Hacker News · Nov 04 · score 0.362_

Two flaws in the Xen hypervisor allow a malicious guest virtual machine (VM) to read and write the memory of other VMs on the same host, including dom0. Dom0 is the VM that, by default, has full permissions and manages the others. Patches are out, and there is no known mitigation, the Xen Project sa…

`xen`

### 70. [Introducing Sysdig AI Defense: See, stop, and prove what agents do](https://webflow.sysdig.com/blog/introducing-sysdig-ai-defense)
_Sysdig · Nov 04 · score 0.150_

Sysdig AI Defense is runtime security and governance for every AI agent your teams run, from the laptop where an agent starts its work to the cloud where its actions land. It starts by showing you what’s there. It finds the agents, MCP servers, skills and plugins your people use, including the ones …

`teams`

### 71. [Docker Sandboxes vulnerability lets AI agents access sensitive files outside their sandbox (CVE-2026-103916) | Endor Labs](https://www.endorlabs.com/learn/docker-sandboxes-vulnerability-lets-ai-agents-access-sensitive-files-outside-their-sandbox-cve-2026-103916)
_Endor Labs · Nov 04 · score 0.143 · CVE-2026-103916_

I discovered a vulnerability in Docker Sandboxes that lets AI coding agents bypass file access restrictions, potentially exposing cloud credentials and other sensitive files on a developer's computer through a routine copy command.

`docker` `cve-`

### 72. [odf-kit: HTML injection leading to XSS in odtToHtml() and odsToHtml() via unescaped style attribute values](https://github.com/advisories/GHSA-3cgg-c5pp-57h6)
_GHSA — npm · Nov 04 · score 0.129 · **MEDIUM 6.1** · CVE-2026-113787_

Affected: odf-kit. ### Summary ODF style attribute values are interpolated into `style="..."` attributes without HTML-escaping in **both** of odf-kit's to-HTML renderers (`odtToHtml` and `odsToHtml`). A double-quote character inside an attacker-controlled style value breaks out of the attribute, all…

`xss`

### 73. [What one organization revealed about AI agent risk](https://webflow.sysdig.com/blog/a-first-look-under-the-hood-of-ai-agents)
_Sysdig · Nov 04 · score 0.109_

One company monitored AI agent activity for a month. See what Sysdig AI Defense found, from unapproved agents to unlogged credential reads.

`credential`

### 74. [Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root](https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html)
_The Hacker News · Nov 04 · score 0.097_

A flaw in APT, the package manager for Debian and Ubuntu, allows an attacker who can modify package downloads to swap a checked package for their own. The attacker's code then runs as root, according to advisories that&nbsp;Debian,&nbsp;Ubuntu, and&nbsp;APT's developers&nbsp;published on November 4.…

`ubuntu` `debian`

### 75. [GitHub Copilot is now available in Xcode’s coding assistant](https://github.blog/changelog/2026-11-04-github-copilot-is-now-available-in-xcodes-coding-assistant)
_GitHub Changelog · Nov 04 · score 0.032_

You can now work with GitHub Copilot directly in Xcode&#8217;s built-in coding assistant, bringing Copilot into your native Xcode workflow. The integration is now in public preview, available starting with&#8230; The post GitHub Copilot is now available in Xcode&#8217;s coding assistant appeared fir…

`github`

### 76. [CodeQL 2.27.4 improves accuracy and query metadata](https://github.blog/changelog/2026-11-04-codeql-2-27-4-improves-accuracy-and-query-metadata)
_GitHub Changelog · Nov 04 · score 0.024_

CodeQL is the static analysis engine behind GitHub code scanning, which finds and remediates security issues in your code. We&#8217;ve recently released CodeQL 2.27.4 with query accuracy improvements across several&#8230; The post CodeQL 2.27.4 improves accuracy and query metadata appeared first on …

`github`

### 77. [Composer 2.11 Adds Dependency Cooldowns](https://socket.dev/blog/composer-dependency-cooldowns?utm_medium=feed)
_Socket Blog · Nov 03 · score 0.479_

Composer 2.11 adds dependency cooldowns, joining package managers that delay new releases to reduce supply chain risks while allowing urgent security updates.

`composer` `supply chain`

### 78. [Chainstack Reports Production Systems Breach Exposing Customer Data and Password Hashes](https://thehackernews.com/2026/11/chainstack-reports-production-systems.html)
_The Hacker News · Nov 03 · score 0.246_

Blockchain infrastructure provider Chainstack on Tuesday disclosed that it was targeted in a cyber attack that allowed an unauthorized party to gain access to some parts of its infrastructure. The incident is assessed to be part of a large-scale, artificial intelligence (AI)-powered attack campaign …

`breach`

### 79. [Synology NAS Devices Targeted in Ransomware Attacks Exploiting Patched DSM Flaw](https://thehackernews.com/2026/11/synology-nas-devices-targeted-in.html)
_The Hacker News · Nov 03 · score 0.241_

Synology is urging customers to update the DiskStation Manager (DSM) software powering its Network Attached Storage (NAS) devices following ransomware attacks. The Taiwanese vendor said it observed threat actors exploiting a vulnerability patched in December 2024 to target devices running outdated v…

`ransomware`

### 80. [Binance Reveals How Fake Job Interviews and AI Tool Abuse Led to $6.43 Billion Theft](https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html)
_The Hacker News · Nov 03 · score 0.158_

Binance on Tuesday said the record-setting theft of $6.43 billion in assets from the world's largest cryptocurrency exchange was the culmination of a "sophisticated, multi-stage campaign" that involved the use of a tampered Homebrew installation and recruitment-themed social engineering attack targe…

`breach`
