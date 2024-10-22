# (L1) Ensure 'Minimum SSL version enabled' is set to 'Enabled: TLS 1.2'

## Description

This vulnerability assessment pertains to a critical configuration issue in Mozilla Firefox related to the minimum TLS/SSL protocol version used for secure communications. The current configuration allows for the negotiation of connections using outdated and insecure versions of TLS/SSL (such as SSLv2, SSLv3, TLS 1.0, TLS 1.1), instead of enforcing the more secure TLS 1.2 protocol as the minimum standard.

**Vulnerability Details:**

- **Vulnerable Component:** Mozilla Firefox browser
- **Vulnerability Type:** Protocol Version Negotiation Vulnerability
- **Impact:** Potential compromise of data confidentiality and integrity during communications. Attackers may exploit vulnerabilities in older protocols to intercept and decrypt sensitive information.
- **Exploitability:** The vulnerability is exploitable if the system is configured to allow negotiation of outdated versions of TLS/SSL.

Failing to enforce TLS 1.2 as the minimum acceptable protocol significantly increases the attack surface and exposes the system to various known vulnerabilities associated with older protocol versions.

## Audit

To verify the current configuration:

1. Open the Group Policy Management Console.
2. Navigate to the following path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox
   ```
3. Locate and check the setting for "Minimum SSL version enabled".
4. Confirm that it is set to "Enabled: TLS 1.2".

Alternatively, you can check the registry:

1. Open the Registry Editor.
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```
3. Verify that the "SSLVersionMin" value (REG_SZ) is set to "tls1.2".

## Remediation

To implement the recommended configuration:

### Windows:

1. Download and install the additional Group Policy template (firefox.admx/adml) if not already present.
2. Open the Group Policy Management Console.
3. Navigate to the following path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox
   ```
4. Locate and double-click on "Minimum SSL version enabled".
5. Set the policy to "Enabled".
6. In the options, select "TLS 1.2" as the minimum version.
7. Click "Apply" and then "OK".
8. Run `gpupdate /force` in an elevated command prompt to apply the changes.

### Linux:

For Linux systems, the process may vary depending on the distribution and Firefox installation method. However, you can generally follow these steps:

1. Locate the Firefox configuration file, typically found at:
   ```
   ~/.mozilla/firefox/<profile>/prefs.js
   ```
   or
   ```
   /etc/firefox/pref/firefox.js
   ```
2. Add or modify the following line:
   ```
   user_pref("security.tls.version.min", 3);
   ```
   (Note: 3 corresponds to TLS 1.2)
3. Save the file and restart Firefox.

For system-wide configuration on Linux:

1. Create or edit the file:
   ```
   /usr/lib/firefox/defaults/pref/local-settings.js
   ```
2. Add the following content:
   ```javascript
   pref("security.tls.version.min", 3);
   ```
3. Save the file and restart Firefox on all affected systems.

After applying these changes, verify the configuration to ensure TLS 1.2 is set as the minimum protocol version for all Firefox instances in your environment.