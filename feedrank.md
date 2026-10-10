# feedrank — 2026-10-10

_80 items, 5d window._

### 1. [Vikunja: Permissive Cross-domain Security Policy trusts every localhost origin which should not be trusted](https://github.com/advisories/GHSA-m687-p538-r5hp)
_GHSA — go · Oct 09 · score 1.077 · **CRITICAL 8.1** · ×16 reports · CVE-2026-57458, CVE-2026-62367, CVE-2026-62376_

Affected: code.vikunja.io/api. ## Summary Vikunja ships with `cors.origins` defaulting to `http://127.0.0.1:*` and `http://localhost:*`, and sends `Access-Control-Allow-Credentials: true`, so a page served from any port on the user's own machine may make credentialed cross-origin requests to the API…

`jwt` `token`

_also: [GHSA — go](https://github.com/advisories/GHSA-hjx8-qv73-f7cm), [GHSA — go](https://github.com/advisories/GHSA-4hv6-xc92-j86g), [GHSA — go](https://github.com/advisories/GHSA-wq92-8x3r-fm38), [GHSA — go](https://github.com/advisories/GHSA-vfxw-3x8p-2vjr), [GHSA — go](https://github.com/advisories/GHSA-39p5-2wrr-xh29)_

### 2. [Nginx UI: Unauthenticated signed-request body staging can exhaust temporary storage](https://github.com/advisories/GHSA-j3hg-9rp3-5hw9)
_GHSA — go · Oct 09 · score 0.998 · **CRITICAL 8.8** · ×10 reports · CVE-2026-107804, CVE-2026-107805, CVE-2026-107806_

Affected: github.com/0xJacky/Nginx-UI. ## Summary In Nginx UI versions 2.5.0 through 2.5.x, the node-signature authentication path staged an attacker-controlled request body in a temporary file and synchronized it to disk before validating the body digest and cryptographic signature. An unauthentica…

`node` `github`

_also: [GHSA — go](https://github.com/advisories/GHSA-9h23-53f4-q947), [GHSA — go](https://github.com/advisories/GHSA-p393-cf76-4jmr), [GHSA — go](https://github.com/advisories/GHSA-662p-52hx-cmh2), [GHSA — go](https://github.com/advisories/GHSA-45gv-9wjv-xh7p), [GHSA — go](https://github.com/advisories/GHSA-33rr-wq23-g6gg)_

### 3. [Credential-Stealing GitHub Actions Workflows Planted in Tens of Thousands of Repositories](https://thehackernews.com/2026/10/credential-stealing-github-actions.html)
_The Hacker News · Oct 09 · score 0.811 · **CRITICAL 9.0**_

Cybersecurity researchers have disclosed details of an ongoing credential-theft campaign that has compromised two high-profile open-source maintainer accounts to push a malicious workflow into over 340 repositories. "Using the account of Takashi Kitao, author of the 18,400-star game engine pyxel, th…

`github` `github actions` `credential`

### 4. [Citrix warns admins to patch new NetScaler RCE flaw immediately](https://www.bleepingcomputer.com/news/security/citrix-warns-admins-to-patch-new-netscaler-rce-flaw-immediately/)
_BleepingComputer · Oct 09 · score 0.582 · **CRITICAL 9.5**_

Citrix has warned IT administrators to patch systems immediately against a new critical vulnerability affecting NetScaler ADC networking appliances and NetScaler Gateway secure remote access solutions. [...]

`rce`

### 5. [Citrix Patches Critical NetScaler Flaw That Could Enable RCE in SAML Deployments](https://thehackernews.com/2026/10/citrix-patches-critical-netscaler-flaw.html)
_The Hacker News · Oct 09 · score 0.502 · **CRITICAL 9.5** · CVE-2026-107406_

Citrix has released patches for yet another critical security flaw impacting NetScaler ADC and NetScaler Gateway that could result in remote code execution or denial-of-service (DoS) under certain conditions. "CVE-2026-107406 is a memory overflow vulnerability that may lead to remote code execution …

`saml` `rce` `cve-`

### 6. [Researchers Publish Working Exploit for Pre-Auth AnyDesk Linux Flaw That Gives Root Access](https://thehackernews.com/2026/10/researchers-publish-working-exploit-for.html)
_The Hacker News · Oct 09 · score 0.412 · **CRITICAL 9.0**_

Security researchers have&nbsp;published a full working exploit&nbsp;for a pre-authentication remote code execution flaw in AnyDesk Linux that gives attackers root access before anyone approves the connection. AnyDesk patched the flaw in version 8.0.3 in June, but its&nbsp;changelog&nbsp;described t…

`linux` `exploit`

### 7. [Hackers get $1,262,000 for 98 zero-days at Pwn2Own Ireland](https://www.bleepingcomputer.com/news/security/hackers-earn-1262000-for-98-zero-days-at-pwn2own-ireland/)
_BleepingComputer · Oct 09 · score 0.312 · **CRITICAL 9.0**_

The Pwn2Own Ireland 2026 hacking contest has concluded, with hackers collecting $1,262,000 in rewards after exploiting 98 zero-day flaws. [...]

`zero-day`

### 8. [Contao: Cross-site scripting in the comments bundle](https://github.com/advisories/GHSA-628f-v4f6-p37r)
_GHSA — composer · Oct 09 · score 0.307 · **CRITICAL 9.3** · CVE-2026-107845_

Affected: contao/comments-bundle, contao/comments-bundle. An unauthenticated front end visitor can post a comment containing a XSS injection. The victim is any back end user who opens the Comments module, and moderation makes exposure certain rather than preventing it. No `Content-Security-Policy` h…

`session` `ca` `xss`

### 9. [TinaCMS admin preview iframe loads an attacker-controlled origin from the URL fragment](https://github.com/advisories/GHSA-x34j-47hf-4xg7)
_GHSA — npm · Oct 09 · score 0.248 · **CRITICAL 9.3** · CVE-2026-108261_

Affected: tinacms, @tinacms/app. ### Summary The TinaCMS admin builds its preview `<iframe src>` from the `/~/*` hash-router splat without checking that the value stays same-origin. A fragment with a doubled slash (`#/~//attacker.example/p`) becomes the protocol-relative URL `//attacker.example/p`, …

`token`

### 10. [pyLoad: Privilege revocation and password change through the REST API do not invalidate the user's session](https://github.com/advisories/GHSA-jq7h-wrvp-3rgx)
_GHSA — pip · Oct 09 · score 1.145 · **HIGH 8.1** · ×6 reports · CVE-2026-48484_

Affected: pyload-ng. An admin who revokes a user's privileges through the REST API does not actually revoke them, because the session carrying those privileges is never invalidated. pyLoad authorizes each request from values copied into the Flask session at login. set_session in webui/app/helpers.py…

`session`

_also: [GHSA — pip](https://github.com/advisories/GHSA-889w-m37p-88m5), [GHSA — pip](https://github.com/advisories/GHSA-p3pr-8f3m-4qp8), [GHSA — pip](https://github.com/advisories/GHSA-fr26-jjhm-638c), [GHSA — pip](https://github.com/advisories/GHSA-r44w-v6gf-x3p6), [GHSA — pip](https://github.com/advisories/GHSA-vq8p-m3wm-gv5f)_

### 11. [ageLANServer: Unbounded JSON Array Allocation in AoE3 Cloud `getFileURL` Endpoint Leads to Remote Denial of Service](https://github.com/advisories/GHSA-4jfq-pmq9-257h)
_GHSA — go · Oct 09 · score 0.430 · **HIGH 7.5** · CVE-2026-107839_

Affected: github.com/luskaner/ageLANServer/server. ### Summary The AoE3 `POST /game/cloud/getFileURL` handler in `luskaner/ageLANServer`'s bundled game server decodes an attacker-controlled `names` JSON array and immediately allocates response storage sized directly from the array's length (`make(i.…

`github` `session`

### 12. [Argo CD repo-server command injection via crafted SSH repository SOCKS5 proxy URL](https://github.com/advisories/GHSA-j6cw-g6p4-7hch)
_GHSA — go · Oct 09 · score 0.410 · **HIGH 8.8** · CVE-2026-55797_

Affected: github.com/argoproj/argo-cd/v2, github.com/argoproj/argo-cd/v3, github.com/argoproj/argo-cd/v3, github.com/argoproj/argo-cd/v3, github.com/argoproj/argo-cd/v3. ### Impact Argo CD runs a shell command in the repo-server when it clones or fetches an SSH Git repository that has a proxy URL. T…

`github` `ssh`

### 13. [yopass Prometheus metrics middleware allows remote memory exhaustion through unbounded method labels](https://github.com/advisories/GHSA-6r69-c6wg-7g8m)
_GHSA — go · Oct 09 · score 0.331 · **HIGH 7.5** · CVE-2026-107840_

Affected: github.com/jhaals/yopass. The Prometheus metrics middleware in pkg/server/server.go used r.Method directly as a label value on request counter and duration histogram metrics. Since the mux catch-all route matches any HTTP method, an unauthenticated attacker can send requests with arbitrary…

`go ` `github` `prometheus`

### 14. [Tina: Code injection via unescaped Git branch name in generated client source](https://github.com/advisories/GHSA-pwhx-cvv3-qj5c)
_GHSA — npm · Oct 09 · score 0.272 · **HIGH 8.2** · CVE-2026-108259_

Affected: @tinacms/cli. ### Summary `@tinacms/cli` inserts the raw Git branch value into the generated `client.ts` source without escaping or encoding. A Git-valid branch name can close the string literal and inject an arbitrary JavaScript expression that executes when the consumer build imports the…

`javascript`

### 15. [@tinacms/web-components: `tina-markdown` writes rich-text link URLs into `href` without scheme validation, allowing stored XSS](https://github.com/advisories/GHSA-c42q-qvc3-j6vg)
_GHSA — npm · Oct 09 · score 0.226 · **HIGH 7.6** · CVE-2026-108260_

Affected: @tinacms/web-components. ### Summary `<tina-markdown>` renders a rich-text AST into the DOM and, for `a` nodes, assigns the node's URL straight to the anchor's `href` with no scheme check. A link authored in the CMS as `javascript:…` renders as a live `javascript:` anchor, so a visitor who…

`node` `javascript` `xss`

### 16. [fast-jwt: Verifier cache accepts expired JWTs without iat.](https://github.com/advisories/GHSA-x937-hj6v-793p)
_GHSA — npm · Oct 08 · score 1.642 · **CRITICAL 9.8** · ×6 reports · CVE-2026-107719, CVE-2026-107720, CVE-2026-107721_

Affected: fast-jwt. ### Summary `cacheSet` only derives its `exp` cache deadline inside `hasIat` (`src/verifier.js:127-140`). JWT `iat` is optional. For a valid token with `exp` but no `iat`, `cacheSet` substitutes `clockTimestamp + clockTolerance + cacheTTL` (`src/verifier.js:142-146`). Later, the …

`jwt` `token`

_also: [GHSA — npm](https://github.com/advisories/GHSA-8wpc-h4q6-8fxv), [GHSA — npm](https://github.com/advisories/GHSA-ww5h-9m49-7xx4), [GHSA — npm](https://github.com/advisories/GHSA-687g-22h4-j4w4), [GHSA — npm](https://github.com/advisories/GHSA-5hjw-83fp-phq9), [GHSA — npm](https://github.com/advisories/GHSA-g3jj-5cmm-3hxx)_

### 17. [TensorLake npm SDK Compromised in ChainDrop Shai-Hulud Credential-Stealing Attack](https://socket.dev/blog/tensorlake-compromise?utm_medium=feed)
_Socket Blog · Oct 08 · score 1.120 · **CRITICAL 9.0** · ×3 reports_

Tensorlake npm SDK version 0.5.144 was compromised in a ChainDrop / Shai-Hulud attack, delivering credential-stealing malware.

`npm` `credential` `shai-hulud`

_also: [OX Security](https://www.ox.security/blog/shai-hulud-here-we-go-again-tensorlake-npm-package-hit-with-malware/), [The Hacker News](https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html)_

### 18. [PraisonAI: AgentOS defaults to network-exposed no-auth mode, allowing unauthenticated agent invocation and instruction disclosure](https://github.com/advisories/GHSA-6wjp-v33h-5cvq)
_GHSA — npm · Oct 08 · score 0.742 · **CRITICAL 9.9** · ×8 reports · CVE-2026-60085, CVE-2026-60091, CVE-2026-61426_

Affected: praisonai. ## Summary The AgentOS server in the `praisonai` TypeScript/npm package ships an insecure default: it binds `0.0.0.0`, sets no API key, and uses CORS `*` with credentials. The API-key middleware is only registered when an API key is configured, so the documented quickstart (`new…

`npm` `typescript`

_also: [GHSA — pip](https://github.com/advisories/GHSA-cv3g-hj65-pcfh), [GHSA — pip](https://github.com/advisories/GHSA-9mp3-24cc-77mg), [GHSA — pip](https://github.com/advisories/GHSA-hc5v-gxvj-58wh), [GHSA — pip](https://github.com/advisories/GHSA-5r6c-gj4g-r697), [GHSA — pip](https://github.com/advisories/GHSA-4w49-gwv8-fpjg)_

### 19. [Handlebars: JavaScript Injection via Unsafe Inline Embedding of Precompiled Templates](https://github.com/advisories/GHSA-xw65-4hp5-5hc7)
_GHSA — npm · Oct 08 · score 0.490 · **CRITICAL 9.8** · ×3 reports · CVE-2026-106444, CVE-2026-106445, CVE-2026-106446_

Affected: handlebars. ## Summary `Handlebars.precompile()` generates JavaScript source that is commonly embedded in browser `<script>` elements. Before the fix, static template text containing `</script>` was emitted unchanged. HTML parsers recognize `</script>` even inside a JavaScript string liter…

`javascript`

_also: [GHSA — npm](https://github.com/advisories/GHSA-8r5x-fm3f-whwj), [GHSA — npm](https://github.com/advisories/GHSA-p8wg-vrv2-v86f)_

### 20. [PraisonAI: SkillTools Executes Scripts Without Path Containment Validation](https://github.com/advisories/GHSA-c44f-37qr-gw3f)
_GHSA — pip · Oct 08 · score 0.456 · **CRITICAL 10.0** · ×5 reports · CVE-2026-61430, CVE-2026-61437, CVE-2026-61443_

Affected: praisonaiagents. ### Summary `SkillTools.run_skill_script()` accepts a `script_path` parameter and executes it via `subprocess.run()` without any path containment validation. While `FileTools` has `_validate_path()` with traversal detection, `SkillTools` performs none. An LLM-directed call…

`python`

_also: [GHSA — pip](https://github.com/advisories/GHSA-4gfv-wg42-7jw5), [GHSA — pip](https://github.com/advisories/GHSA-m6wp-h223-4c8g), [GHSA — pip](https://github.com/advisories/GHSA-2xv2-w8cq-5gxw), [GHSA — pip](https://github.com/advisories/GHSA-qg25-6gc4-48mg)_

### 21. [ISC BIND:  ISC BIND Data Processing Errors Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2015-5477)
_CISA KEV · Oct 08 · score 0.377 · **CRITICAL 9.0** · CVE-2015-5477_

ISC BIND contains a data processing errors vulnerability that could allow remote attackers to cause a denial of service via TKEY queries. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (…

`bind`

### 22. [FBI disrupts Chinese hacking tools used to breach critical infrastructure](https://www.bleepingcomputer.com/news/security/fbi-disrupts-chinese-hacking-tools-used-to-breach-critical-infrastructure/)
_BleepingComputer · Oct 08 · score 0.255 · **CRITICAL 9.5**_

The FBI has seized seven domains used by Chinese state-sponsored hackers known as Flax Typhoon to operate two hacking tools, MicroScan and FishHub, used in attacks that breached critical infrastructure and other organizations worldwide. [...]

`breach`

### 23. [Strapi Strapi: Strapi Cleartext Storage of Sensitive Information Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2023-22894)
_CISA KEV · Oct 08 · score 0.224 · **CRITICAL 9.0** · CVE-2023-22894_

Strapi contains a cleartext storage of sensitive information vulnerability that could allow attackers with access to the admin panel to discover sensitive user details via the query filter. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontin…

`cve-`

### 24. [ONLYOFFICE Docs: ONLYOFFICE Docs Server Path Traversal Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2021-3199)
_CISA KEV · Oct 08 · score 0.221 · **CRITICAL 9.0** · CVE-2021-3199_

ONLYOFFICE Docs contains a path traversal vulnerability that can occur when JWT is used, via a /.. sequence in an image upload parameter and could allow for remote code execution. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Pri…

`jwt`

### 25. [Tensorlake npm Package Compromised: A Worm With a Hostage Token That Wipes Your Machine If You Revoke It](https://www.stepsecurity.io/blog/tensorlake-npm-compromised-hostage-token-worm)
_StepSecurity · Oct 08 · score 1.039 · **HIGH 8.5**_

The malicious release was built from the project's own main branch and published with an npm provenance attestation.

`npm` `provenance` `token`

### 26. [MariaDB Connector/Node.js: SQL injection in the text protocol when the session uses NO_BACKSLASH_ESCAPES](https://github.com/advisories/GHSA-r3rv-jm3r-62q2)
_GHSA — npm · Oct 08 · score 0.528 · **HIGH 8.1** · ×4 reports · CVE-2026-107382, CVE-2026-107383, CVE-2026-107384_

Affected: mariadb, mariadb, mariadb, mariadb. ### Description When escaping string and binary parameters for the text protocol, the connector always escaped the quote character with a backslash, without ever consulting the session's NO_BACKSLASH_ESCAPES SQL mode. The server status flag was declared …

`node` `mariadb` `session` `sql injection`

_also: [GHSA — npm](https://github.com/advisories/GHSA-v6pj-gxxw-phfw), [GHSA — npm](https://github.com/advisories/GHSA-48qf-xh34-q73r), [GHSA — npm](https://github.com/advisories/GHSA-cx2f-j9fh-8g68)_

### 27. [JHipster: SQL Injection in the Parameter of JHipster-Generated Reactive (WebFlux + R2DBC) Applicationssort](https://github.com/advisories/GHSA-r223-96jv-q533)
_GHSA — npm · Oct 08 · score 0.468 · **HIGH 8.8** · ×2 reports · CVE-2026-107303, CVE-2026-107375_

Affected: generator-jhipster. # SQL Injection in the `sort` Parameter of JHipster-Generated Reactive (WebFlux + R2DBC) Applications - **Product**: jhipster/generator-jhipster (npm package `generator-jhipster`) - **Affected versions**: v7.0.0 through v9.2.0 - **Component**: generated reactive-applica…

`npm` `java` `sql injection`

_also: [GHSA — npm](https://github.com/advisories/GHSA-9ffp-22j7-56r2)_

### 28. [msgpack5: Many buffered values can exhaust the streaming decoder stack](https://github.com/advisories/GHSA-5x5g-h9x8-2fh9)
_GHSA — npm · Oct 08 · score 0.254 · **HIGH 7.5** · ×3 reports · CVE-2026-107297, CVE-2026-107298, CVE-2026-107300_

Affected: msgpack5. ### Impact The streaming decoder recursively invokes itself for every complete value remaining in a chunk. A single chunk containing many small valid MessagePack values can exhaust the JavaScript call stack and interrupt the process or stream. ### Patches The streaming decoder no…

`javascript`

_also: [GHSA — npm](https://github.com/advisories/GHSA-24ch-f2g6-9hhh), [GHSA — npm](https://github.com/advisories/GHSA-gcx5-hxj7-gpqq)_

### 29. [Excelize: Unchecked pivot-cache field index in extractPivotTableFields causes unrecoverable panic](https://github.com/advisories/GHSA-mx22-3794-2vpv)
_GHSA — go · Oct 08 · score 0.171 · **HIGH** · CVE-2026-107211_

Affected: github.com/xuri/excelize/v2. ### Summary extractPivotTableFields builds `order := pc.getPivotCacheFieldsName()` from xl/pivotCache/pivotCacheDefinitionN.xml's <cacheFields> list, then indexes it with values taken from a *separately parsed* xl/pivotTables/pivotTableN.xml part with zero cros…

`github`

### 30. [CairoSVG: Quadratic-time DoS parsing a crafted SVG <path>](https://github.com/advisories/GHSA-c3jg-qh8m-j3h2)
_GHSA — pip · Oct 08 · score 0.123 · **HIGH** · CVE-2026-107378_

Affected: cairosvg. ## Summary Rendering an untrusted SVG whose `<path d="...">` contains many segments is O(n²) CPU. A single `<path>` under 1 MiB burns tens of seconds. Two independent O(n²) sites in `cairosvg/path.py`: 1. **Tokenizer** — the path-data parser consumes the `d` string with a `while …

`node`

### 31. [Atlassian Data Center Flaw Draws Exploitation Attempts Within Two Hours of Public Details](https://thehackernews.com/2026/10/atlassian-data-center-flaw-draws.html)
_The Hacker News · Oct 07 · score 0.399 · **CRITICAL 9.5** · ×2 reports · CVE-2026-21589_

Threat actors have begun to exploit a newly disclosed critical security flaw impacting Atlassian Data Center products that could allow access to sensitive files under certain conditions. The arbitrary file access flaw, tracked as CVE-2026-21589 (CVSS score: 9.3) affects multiple products, including …

`atlassian` `jira` `confluence` `exploit` `cve-`

_also: [The Hacker News](https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html)_

### 32. [Ghost: Remote Code Execution via Bookmark Card Images](https://github.com/advisories/GHSA-788w-68h3-cvxp)
_GHSA — npm · Oct 07 · score 0.938 · **HIGH 8.8** · ×8 reports · CVE-2026-105642, CVE-2026-105643, CVE-2026-105644_

Affected: ghost. ### Impact An image processing library bundled with Ghost contained a vulnerability in its SVG handling. Any staff user, including Contributors, could create a bookmark card for an attacker-controlled website, resulting in arbitrary commands being run on the Ghost server. ### Vulner…

`docker`

_also: [GHSA — npm](https://github.com/advisories/GHSA-69qc-f5m6-889c), [GHSA — npm](https://github.com/advisories/GHSA-hqq2-xqr2-fmx2), [GHSA — npm](https://github.com/advisories/GHSA-9m4w-fmjw-fvjq), [GHSA — npm](https://github.com/advisories/GHSA-fwh9-qg68-vxp4), [GHSA — npm](https://github.com/advisories/GHSA-322m-ff4g-9vx9)_

### 33. [Payload: Remote Code Execution through first-register](https://github.com/advisories/GHSA-97rh-rhh2-7vjv)
_GHSA — npm · Oct 07 · score 0.434 · **HIGH 8.1** · CVE-2026-105858_

Affected: payload, payload. ### Impact A crafted request to the public first-register operation can be used to perform a RCE exploit. **You are affected if:** - You use local auth strategy and your application remains without an initial user created ## Patches In the patched version data submission …

`rce` `exploit`

### 34. [Kunstmaan CMS: MediaBundle extension blacklist bypass allows authenticated administrators to upload executable PHP files leading to remote code execution](https://github.com/advisories/GHSA-p279-5wcv-45vq)
_GHSA — composer · Oct 07 · score 0.428 · **HIGH 7.2** · CVE-2026-104890_

Affected: kunstmaan/media-bundle, kunstmaan/bundles-cms. ### Summary The MediaBundle blocks dangerous upload extensions with a blacklist that was matched case-sensitively, while the stored filename was lowercased afterwards. A file uploaded as `webshell.pHp` therefore bypassed the blacklist and was …

`php`

### 35. [Payload: SQL injection in SQLite/Postgres](https://github.com/advisories/GHSA-pj7x-6wpf-pgvp)
_GHSA — npm · Oct 07 · score 0.167 · **HIGH** · CVE-2026-105856_

Affected: @payloadcms/db-sqlite, @payloadcms/db-d1-sqlite, @payloadcms/db-postgres, @payloadcms/db-vercel-postgres, @payloadcms/db-sqlite. ### Impact An attacker who has read plus create or update access to a collection can submit a request that includes a SQL injection targeting a specific field pa…

`postgres` `sqlite` `sql injection`

### 36. [Next.js has Server-Side Request Forgery in Image Optimization](https://github.com/advisories/GHSA-cjq9-62q9-8jv4)
_GHSA — npm · Oct 07 · score 0.116 · **HIGH 6.5** · CVE-2026-94483_

Affected: next. ## Impact An attacker-controlled, allow-listed remote URL can lead to server-side request forgery (e.g. to private IPs) during Image Optimization. ## Workaround Audit allow-listed remote URLs in `images.remotePatterns` (see https://nextjs.org/docs/app/getting-started/images#remote-im…

`dns`

### 37. [hickory-resolver follows irrelevant CNAME records](https://github.com/advisories/GHSA-6f2x-v7q7-m7m5)
_GHSA — rust · Oct 05 · score 0.601 · **HIGH 7.5** · ×3 reports_

Affected: hickory-resolver. When the Hickory DNS resolver follows CNAME records, it sends queries that are not necessary to answer the original recursive query. If there are any CNAME records in the authority section or additional section of the response, queries will be sent for those names. If the…

`dns`

_also: [GHSA — rust](https://github.com/advisories/GHSA-6w6g-hm98-mhgm), [GHSA — rust](https://github.com/advisories/GHSA-5j98-2g5x-46v6)_

### 38. [New controls and chat improvements in Copilot for JetBrains](https://github.blog/changelog/2026-10-10-new-controls-and-chat-improvements-in-copilot-for-jetbrains)
_GitHub Changelog · Oct 10 · score 0.046_

This update brings more control over default models and MCP server in GitHub Copilot for JetBrains. It also makes diagnostics easier to address, improves chat navigation and account controls, and&#8230; The post New controls and chat improvements in Copilot for JetBrains appeared first on The GitHub…

`github`

### 39. [Contao: Cross-site request forgery in custom backend actions](https://github.com/advisories/GHSA-9ff2-p842-45wq)
_GHSA — composer · Oct 09 · score 0.604 · **MEDIUM 4.3** · ×3 reports · CVE-2026-107848, CVE-2026-107850, CVE-2026-107851_

Affected: contao/core-bundle, contao/core-bundle. `RequestTokenListener` is the only generic `REQUEST_TOKEN` validator in Contao and it only runs on POST. On the GET side the guard is local and declarative, and it only fires when an `act` parameter is present. Every back end action dispatched throug…

`token` `csrf`

_also: [GHSA — composer](https://github.com/advisories/GHSA-q6wp-fr43-gm9v), [GHSA — composer](https://github.com/advisories/GHSA-5974-gfqc-wrcm)_

### 40. [GhostAction Returns: Malicious “Security Audit” Workflows Now Mine Credentials from Entire Git Histories](https://www.stepsecurity.io/blog/ghostaction-returns)
_StepSecurity · Oct 09 · score 0.445_

GhostAction returns: compromised maintainers push a fake security-audit.yml workflow that steals CI/CD secrets and cloud credentials from GitHub repos.

`github` `ci/cd`

### 41. [FBI arrests another suspected ShinyHunters hacker after agency breach](https://www.bleepingcomputer.com/news/security/fbi-arrests-another-suspected-shinyhunters-hacker-after-agency-breach/)
_BleepingComputer · Oct 09 · score 0.388_

The FBI has arrested another suspected member of the ShinyHunters extortion group believed to be involved in the recent breach of FBI systems, Director Kash Patel announced Friday. [...]

`breach`

### 42. [New GhostAction Wave Hits Hundreds of Repos, Expanding Beyond CI/CD Secrets to Cloud Credentials](https://socket.dev/blog/ghostaction-cloud-credentials?utm_medium=feed)
_Socket Blog · Oct 09 · score 0.377_

A new GhostAction wave hits hundreds of GitHub repos, expanding CI/CD secret theft to cloud and AI credentials in source code and git history.

`github` `ci/cd`

### 43. [Max severity SonicWall SMA1000 flaw now exploited in attacks](https://www.bleepingcomputer.com/news/security/max-severity-sonicwall-sma1000-flaw-now-exploited-in-attacks/)
_BleepingComputer · Oct 09 · score 0.290 · CVE-2026-102255_

Attackers are exploiting a maximum-severity vulnerability in SonicWall SMA1000 appliances (CVE-2026-102255) that was patched on Tuesday, three days ago. [...]

`sonicwall` `cve-`

### 44. [Flax Typhoon Exploits Five Flaws as CISA Sets October 11 Deadline for Federal Agencies](https://thehackernews.com/2026/10/flax-typhoon-exploits-five-flaws-as.html)
_The Hacker News · Oct 09 · score 0.287 · CVE-2015-3306_

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Thursday added five security flaws to its Known Exploited Vulnerabilities (KEV) catalog, following their abuse by a China-linked threat actor known as Flax Typhoon. The vulnerabilities in question are listed below - CVE-2015-3306 (C…

`kev` `cve-` `cvss`

### 45. [Shiny for Python has path traversal in bookmark restore](https://github.com/advisories/GHSA-47c3-hpmg-7j6p)
_GHSA — pip · Oct 09 · score 0.244 · **MEDIUM** · CVE-2026-108258_

Affected: shiny. ### Impact Shiny for Python's bookmark-restore path accepted a client-supplied `_state_id_` query-string value and joined it into the server-side bookmark directory (`<cwd>/shiny_bookmarks/<id>`) without validating it. A value containing `..` path segments, or an absolute path, coul…

`python`

### 46. [pacioli: A submit consent marker licensed cancellation of caller-named pre-existing documents](https://github.com/advisories/GHSA-3hj7-6vmj-h8v4)
_GHSA — pip · Oct 09 · score 0.211 · **MEDIUM 5.7** · CVE-2026-107841_

Affected: pacioli-guard. ### Impact `pacioli-guard`'s document-layer consent gate requires a human-minted, single-use, document-bound and **act-bound** marker before a credential carrying `API Key Scope.require_consent` may submit or cancel a document. Because ERPNext performs further document write…

`credential`

### 47. [P7 DarkSword iOS Exploit Kit Adds Crypto Wallet Data Theft and Remote Commands](https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html)
_The Hacker News · Oct 09 · score 0.182_

Cybersecurity researchers have disclosed details of a previously unseen variant of the DarkSword iOS exploit kit called P7 DarkSword. "Compared with the variants we usually observe, P7 reduces its on-device footprint, adds on-device keychain and crypto-wallet theft, and adds two way C2 communication…

`keychain` `exploit`

### 48. [Germany arrests alleged core Qilin ransomware member after extradition](https://www.bleepingcomputer.com/news/security/germany-arrests-alleged-core-qilin-ransomware-member-after-extradition/)
_BleepingComputer · Oct 09 · score 0.175_

Germany has arrested a Russian national suspected of being a leading member of the Qilin ransomware group following extradition from Japan earlier this month. [...]

`ransomware`

### 49. [How to keep AI agents within their permissions](https://www.bleepingcomputer.com/news/security/how-to-keep-ai-agents-within-their-permissions/)
_BleepingComputer · Oct 09 · score 0.147_

AI agents can use valid credentials to perform actions beyond their assigned permissions, creating risks that traditional access controls may not prevent. Token Security explains how organizations can enforce agent-specific policies without sacrificing autonomy. [...]

`token`

### 50. [Attackers Exploit AhsayCBS Flaws to Deploy XMRig Miners Disguised as Microsoft Edge](https://thehackernews.com/2026/10/attackers-exploit-ahsaycbs-flaws-to.html)
_The Hacker News · Oct 09 · score 0.070 · CVE-2026-105133_

Threat actors have been observed exploiting two recently disclosed flaws in the AhsayCBS backup utility to seize control of affected devices and deploy web shells and XMRig cryptocurrency miners. Details of the flaws are below - CVE-2026-105133 (CVSS v4 score: 5.5) - An improper authentication vulne…

`java` `edge` `exploit` `cve-` `cvss`

### 51. [GitHub Copilot weekly releases — October 5](https://github.blog/changelog/2026-10-09-github-copilot-weekly-releases-october-5)
_GitHub Changelog · Oct 09 · score 0.043_

This week&#8217;s updates make Copilot easier to use across accounts and environments, with more control over what agents can access and how you manage their work. GitHub Copilot Claude Haiku&#8230; The post GitHub Copilot weekly releases — October 5 appeared first on The GitHub Blog .

`github`

### 52. [CodeQL 2.27.2 improves C++, Go, Rust, and JavaScript analysis](https://github.blog/changelog/2026-10-09-codeql-2-27-2-improves-c-go-rust-and-javascript-analysis)
_GitHub Changelog · Oct 09 · score 0.028_

CodeQL 2.27.2 is now available, adding a C++ regular-expression parser and analysis improvements across several languages. CodeQL is the static analysis engine behind GitHub code scanning, which helps you find&#8230; The post CodeQL 2.27.2 improves C++, Go, Rust, and JavaScript analysis appeared fir…

`javascript` `rust` `github`

### 53. [Microsoft: Outdated Windows devices will stop receiving security updates](https://www.bleepingcomputer.com/news/microsoft/microsoft-outdated-windows-devices-will-lose-security-protection-next-year/)
_BleepingComputer · Oct 09 · score 0.006_

Microsoft says devices running unsupported versions of Windows will stop receiving security updates after next year's Windows Update certificate rotation. [...]

`windows` `certificate`

### 54. [Three Teams Demonstrate Remote Hacks of Fully Patched Google Pixel 10 at Pwn2Own](https://thehackernews.com/2026/10/three-teams-demonstrate-remote-hacks-of.html)
_The Hacker News · Oct 09 · score 0.006_

Three research teams broke into Google's Pixel 10 on October 8 at Pwn2Own Ireland, a hacking contest in Cork whose rules require every target to be fully patched. The contest pays researchers to show working exploits and passes the flaws to the vendors. One of the three Pixel exploits earned Ikotas …

`teams`

### 55. [Pydantic AI Web chat UI (`Agent.to_web()`, `clai web`): the local chat endpoint does not validate the `Host` header](https://github.com/advisories/GHSA-q2xc-rrxj-58x9)
_GHSA — pip · Oct 08 · score 0.467 · **MEDIUM 6.8** · ×5 reports · CVE-2026-107289, CVE-2026-107291, CVE-2026-107292_

Affected: pydantic-ai, pydantic-ai, pydantic-ai-slim, pydantic-ai-slim. ### Summary The Pydantic AI development web chat UI (`Agent.to_web()`, `clai web`) does not validate the `Host` header of incoming requests. A website a developer visits can use DNS rebinding to make requests to a chat UI runnin…

`token` `dns` `csrf`

_also: [GHSA — pip](https://github.com/advisories/GHSA-3gh4-cghq-f8v4), [GHSA — pip](https://github.com/advisories/GHSA-v2xh-2vp8-57h8), [GHSA — pip](https://github.com/advisories/GHSA-4x9p-g9wm-8q7f), [GHSA — pip](https://github.com/advisories/GHSA-vmxc-h2x2-jmf3)_

### 56. [Indico: Incomplete Server-Side Request Forgery (SSRF) check](https://github.com/advisories/GHSA-2v95-h47v-g4x9)
_GHSA — pip · Oct 08 · score 0.426 · **MEDIUM 6.8** · ×4 reports · CVE-2026-107394, CVE-2026-107395, CVE-2026-107396_

Affected: indico. ### Impact Indico makes outgoing requests to user-provides URLs in various places. This is mostly intentional and part of Indico's functionality, but of course it is never intended to let you access "special" targets such as localhost or cloud metadata endpoints. The previous fix (…

`github` `edge` `ssrf` `cve-`

_also: [GHSA — pip](https://github.com/advisories/GHSA-6p4f-j8j6-463q), [GHSA — pip](https://github.com/advisories/GHSA-cw24-x4mj-fw3q), [GHSA — pip](https://github.com/advisories/GHSA-c4wc-ggrj-jg9v)_

### 57. [Coraza: Resource exhaustion via deferred file handle accumulation in multipart body processor](https://github.com/advisories/GHSA-rp9v-7xv3-r6g3)
_GHSA — go · Oct 08 · score 0.384 · **MEDIUM 5.9** · ×6 reports · CVE-2026-107825, CVE-2026-107833, CVE-2026-107834_

Affected: github.com/corazawaf/coraza/v3. ## Summary `defer temp.Close()` sits inside a `for` loop in the multipart processor. Go defers run at function return, not loop end, so every file part in the request holds an open fd until `ProcessRequest()` exits. Send enough parts and you hit `EMFILE`. Wi…

`go ` `github`

_also: [GHSA — go](https://github.com/advisories/GHSA-w253-m66g-rx24), [GHSA — go](https://github.com/advisories/GHSA-3c6w-j9xm-8h2h), [GHSA — go](https://github.com/advisories/GHSA-3wr7-993q-jrff), [GHSA — go](https://github.com/advisories/GHSA-g4qm-m288-5cp9), [GHSA — go](https://github.com/advisories/GHSA-x26q-wvhg-fh4m)_

### 58. [enshrined/svg-sanitize: Stored XSS via DTD Entity / HTML5 Named Character Reference Collision](https://github.com/advisories/GHSA-9rjx-3jch-6vjf)
_GHSA — composer · Oct 08 · score 0.380 · **MEDIUM 6.5** · ×3 reports · CVE-2026-107379, CVE-2026-107380, CVE-2026-107381_

Affected: enshrined/svg-sanitize. ## Summary A crafted SVG bypasses `enshrined/svg-sanitize`'s href validation and delivers a `javascript:` URL through the sanitizer unchanged. The bypass exploits a semantic mismatch between XML entity resolution (used during sanitization) and HTML5 Named Character …

`javascript` `packagist` `php` `xss`

_also: [GHSA — composer](https://github.com/advisories/GHSA-m9xh-6747-9r6f), [GHSA — composer](https://github.com/advisories/GHSA-v383-3rw5-q8rf)_

### 59. [music-metadata: MP4 stsd sample-entry size==0 causes a synchronous infinite loop (DoS) — unreleased regression on master](https://github.com/advisories/GHSA-f94x-6692-553q)
_GHSA — npm · Oct 08 · score 0.307 · **MEDIUM 6.2** · ×3 reports · CVE-2026-107389, CVE-2026-107391, CVE-2026-107392_

Affected: music-metadata. ### Summary `StsdAtom.get()` in `lib/mp4/AtomToken.ts` parses an MP4 `stsd` (sample description) box's entry table by advancing a cursor with `off += size - 4`, where `size` is a 32-bit, attacker-controlled per-entry length read straight from the file. When `size == 0`, tha…

`node`

_also: [GHSA — npm](https://github.com/advisories/GHSA-5gfj-9q3v-qfp3), [GHSA — npm](https://github.com/advisories/GHSA-8j4c-6x6g-rq3j)_

### 60. [amqp091-go: Pre-negotiation frame limit is not enforced to 4KB](https://github.com/advisories/GHSA-w6r9-248c-frg8)
_GHSA — go · Oct 08 · score 0.263 · **MEDIUM** · CVE-2026-107386_

Affected: github.com/rabbitmq/amqp091-go. ## Summary The frame-size mitigation released in `amqp091-go` v1.13.0 can be bypassed before `connection.tune` completes. A malicious or compromised AMQP peer can send only a seven-byte body-frame header containing a large attacker-controlled `uint32` payloa…

`github` `rabbitmq`

### 61. [ARTEX AI Pentesting Tool Used in Data Theft Attacks on South Korean Financial Firms](https://thehackernews.com/2026/10/artex-ai-pentesting-tool-used-in-data.html)
_The Hacker News · Oct 08 · score 0.220_

Cybersecurity researchers have disclosed details of a targeted campaign aimed at South Korean financial organizations that used an artificial intelligence (AI) pen testing tool named ARTEX to carry out the attacks. The activity, per CrowdStrike Intelligence, was active from late September to early O…

`crowdstrike` `exfiltration`

### 62. [Ransomware attack disrupts Japan's IDCF Cloud used by govt clients](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/)
_BleepingComputer · Oct 08 · score 0.205_

IDC Frontier, a major Japanese cloud and digital infrastructure company, disclosed that its IDCF Cloud service was targeted in a ransomware attack that caused an outage at a data center cluster serving the eastern part of the country. [...]

`ransomware`

### 63. [MonsterCloud Owner Accused of Billing Over $19M While Secretly Paying Ransoms to Decrypt Data](https://thehackernews.com/2026/10/monstercloud-owner-accused-of-billing.html)
_The Hacker News · Oct 08 · score 0.162_

The U.S. Department of Justice (DoJ) on Wednesday announced charges against a 50-year-old U.S. and Israeli national for allegedly defrauding ransomware victims by secretly paying the attackers to obtain decryptors while claiming to use proprietary tools to recover their data. Zohar Pinhasi (aka Zack…

`ransomware`

### 64. [DEW #170 - Zack on a podcast, Hunting DNS and Citrix 0days](https://www.detectionengineering.net/p/dew-170-zack-on-a-podcast-hunting)
_Detection Engineering Weekly · Oct 08 · score 0.158_

i&#8217;m baaaaack

`dns`

### 65. [LangChain: MongoDBChatMessageHistory query injection can allow cross-session access](https://github.com/advisories/GHSA-m6rx-h84q-8r95)
_GHSA — npm · Oct 08 · score 0.156 · **MEDIUM** · CVE-2026-106119_

Affected: @langchain/mongodb. ## Impact `MongoDBChatMessageHistory` did not enforce the documented string type for session identifiers at runtime. In affected applications, a structured session identifier could be interpreted as a MongoDB query condition rather than as a literal identifier. Applicat…

`mongodb` `session`

### 66. [ThreatsDay: Ransomware Affiliate Betrayal, WhatsApp RAT, Exposed Hacker Tools and 12 More Stories](https://thehackernews.com/2026/10/threatsday-ransomware-affiliate.html)
_The Hacker News · Oct 08 · score 0.151_

The crooks have trust problems of their own. One ransomware affiliate decided to keep the profits for himself. Elsewhere, an attacker left a server exposed, complete with tools and traces of an intrusion. Apparently, keeping things secure is a problem on both sides of the fence. The rest of the week…

`ransomware` `rat`

### 67. [Wazza Phishkit Targets Banking, Government, and Manufacturing Across the US, EU, and Australia](https://thehackernews.com/2026/10/wazza-phishkit-targets-banking.html)
_The Hacker News · Oct 08 · score 0.143_

Phishing kits are no longer limited to copying a familiar login page and waiting for a victim to enter credentials. Attackers are increasingly building filtering, session management, and traffic controls into the infrastructure that delivers the phishing page itself. ANY.RUN has identified Wazza, a …

`session`

### 68. [StepSecurity Now Inventories AI Agent Skills in Your GitHub Repositories and on Developer Machines](https://www.stepsecurity.io/blog/stepsecurity-now-inventories-ai-agent-skills-in-your-github-repositories-and-on-developer-machines)
_StepSecurity · Oct 08 · score 0.110_

Inventory the AI agent skills on developer machines and in your GitHub repositories: which agent loads them, what they can execute, and where they came from.

`github`

### 69. [RUSTSEC-2026-0333: Vulnerability in noyalib](https://rustsec.org/advisories/RUSTSEC-2026-0333.html)
_RustSec · Oct 08 · score 0.108_

Resource budgets not enforced on the typed deserialization path

`deserialization`

### 70. [UAC-0099 Targets Ukrainian Government Personnel With ASHVEIN RAT Hiding Commands in HTML](https://thehackernews.com/2026/10/uac-0099-targets-ukrainian-government.html)
_The Hacker News · Oct 08 · score 0.106_

The Russia-aligned threat actor known as UAC-0099 has been attributed to a previously undocumented .NET infostealer and remote access trojan (RAT) codenamed ASHVEIN. According to TrendAI, the malware has been put to use in attacks targeting Ukrainian government personnel. The cybersecurity company i…

`.net` `rat`

### 71. [How one bug bounty researcher chooses the features they investigate](https://github.blog/security/how-one-bug-bounty-researcher-chooses-the-features-they-investigate/)
_GitHub Security Blog · Oct 08 · score 0.068_

As we kick off Cybersecurity Awareness Month, the GitHub Bug Bounty team spotlights @vaib25vicky, exploring their methodology, techniques, and experiences hacking on GitHub. The post How one bug bounty researcher chooses the features they investigate appeared first on The GitHub Blog .

`github`

### 72. [16 Malicious Firefox Extensions Pose as Rabby and OKX Wallets to Steal Recovery Phrases](https://thehackernews.com/2026/10/16-malicious-firefox-extensions-pose-as.html)
_The Hacker News · Oct 08 · score 0.065_

Cybersecurity researchers have discovered a cluster of 16 malicious Mozilla Firefox extensions that are capable of stealing cryptocurrency wallet recovery phrases and private keys. "The extensions masquerade as wallet portals, desktop utilities, and browser tools, but their code intercepts recovery …

`firefox`

### 73. [Triage role users or higher can now archive pull requests](https://github.blog/changelog/2026-10-08-triage-role-users-or-higher-can-now-archive-pull-requests)
_GitHub Changelog · Oct 08 · score 0.048_

Users with the triage role or higher in a repository can now archive and unarchive pull requests. Previously, archiving was limited to repository administrators, requiring trusted triagers to hand routine&#8230; The post Triage role users or higher can now archive pull requests appeared first on The…

`github`

### 74. [Copilot code review: New organization billing options and controls](https://github.blog/changelog/2026-10-08-copilot-code-review-new-organization-billing-options-and-controls)
_GitHub Changelog · Oct 08 · score 0.026_

This release adds new billing and license controls for Copilot code review admins: Billing: Organization owners can bill Copilot code reviews from members with a Copilot license to the organization&#8217;s&#8230; The post Copilot code review: New organization billing options and controls appeared fi…

`github`

### 75. [Screen readers can navigate timelines as lists](https://github.blog/changelog/2026-10-08-screen-readers-can-navigate-timelines-as-lists)
_GitHub Changelog · Oct 08 · score 0.002_

Screen readers can now navigate issue and pull request timelines as a list. When you move through a timeline, assistive technology can announce the list structure, item count, current position,&#8230; The post Screen readers can navigate timelines as lists appeared first on The GitHub Blog .

`github`

### 76. [Draft pull requests count toward pull request limits](https://github.blog/changelog/2026-10-08-draft-pull-requests-count-toward-pull-request-limits)
_GitHub Changelog · Oct 08 · score 0.002_

Maintainers are seeing more low-quality contributions in their repositories and need better ways to manage them. You can now configure pull request limits to also include draft pull requests. Previously,&#8230; The post Draft pull requests count toward pull request limits appeared first on The GitHu…

`github`

### 77. [Eight Malicious npm Packages Downloaded 40,767 Times Deliver Overlord RAT and Stealer](https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html)
_The Hacker News · Oct 07 · score 0.400_

Cybersecurity researchers have disclosed details of a long-running npm supply chain malware campaign that pushes information stealers and remote access trojans (RAT) to compromised hosts. The campaign has been codenamed MALFEX by CloudSEK and Checkmarx. The activity is assessed to be the work of a l…

`npm` `supply chain` `stealer` `rat`

### 78. [FBI Warns FortiBleed Remains Active After Amassing 86,644 Fortinet Device Credentials](https://thehackernews.com/2026/10/fbi-warns-fortibleed-remains-active.html)
_The Hacker News · Oct 07 · score 0.215_

The U.S. Federal Bureau of Investigation (FBI) and Secret Service (USSS) on Tuesday warned that the FortiBleed credential harvesting campaign remains an active threat aimed at internet-facing Fortinet FortiGate firewalls and secure socket layer (SSL) virtual private network (VPN) gateways. "The camp…

`credential` `ssl` `vpn` `fortinet`

### 79. [100+ Compromised Websites Use Fake Cloudflare Checks to Deliver LunexStealer](https://thehackernews.com/2026/10/100-compromised-websites-use-fake.html)
_The Hacker News · Oct 07 · score 0.171_

The Computer Emergency Response Team of Ukraine (CERT-UA) has identified more than 100 compromised websites that have been injected with malicious JavaScript to serve an information-stealing malware called LunexStealer (aka Psychedelic Stealer). The activity, which was observed by the agency in Sept…

`javascript` `cloudflare` `stealer`

### 80. [16 Malicious Firefox Extensions Steal Cryptocurrency Wallet Credentials](https://socket.dev/blog/firefox-crypto-wallet-stealers?utm_medium=feed)
_Socket Blog · Oct 07 · score 0.111_

Socket found 16 malicious Firefox extensions designed to steal crypto wallet recovery phrases and private keys using cloned Rabby and OKX interfaces.

`firefox`
