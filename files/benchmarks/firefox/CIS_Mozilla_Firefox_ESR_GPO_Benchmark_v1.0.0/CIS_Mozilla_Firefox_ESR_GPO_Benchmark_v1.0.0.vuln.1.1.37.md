# (L1) Ensure 'Maximum SSL version enabled' is set to 'Enabled: TLS 1.3'

## Description

This vulnerability relates to the configuration of the maximum TLS (Transport Layer Security) version supported by Mozilla Firefox. If the 'Maximum SSL version enabled' Group Policy is not correctly set to TLS 1.3, the system may allow the use of older, less secure TLS versions.

Older TLS versions (e.g., TLS 1.0, TLS 1.1) have known vulnerabilities that can allow attackers to:
- Eavesdrop on communications
- Modify data in transit
- Impersonate servers

TLS 1.3 incorporates significant improvements in security, including better threat mitigation strategies and strengthened cryptographic mechanisms.

The severity of this vulnerability depends on the potential impact of compromised connections. It should be assessed in the context of the application and data sensitivity, and whether older TLS versions might still be used on the same network.

## Audit

To audit this setting:

### Windows

1. Open the Group Policy Management Console
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Maximum SSL version enabled
   ```
3. Verify that the setting is configured as "Enabled: TLS 1.3"

Alternatively, you can check the registry:

1. Open the Registry Editor
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```
3. Verify that the "SSLVersionMax" value (REG_SZ) is set to "tls1.3"

### Linux

Firefox on Linux typically doesn't use Group Policy. However, you can check the Firefox configuration:

1. Open Firefox
2. In the address bar, type `about:config`
3. Search for `security.tls.version.max`
4. Verify that the value is set to 4 (which corresponds to TLS 1.3)

## Remediation

### Windows

To set the recommended configuration via Group Policy:

1. Ensure you have the necessary ADMX/ADML files for Firefox. If not, download them from the official Mozilla website.
2. Open the Group Policy Management Console
3. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Maximum SSL version enabled
   ```
4. Set the policy to "Enabled: TLS 1.3"

If you need to set this manually in the registry:

1. Open the Registry Editor
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```
3. Create a new String Value (REG_SZ) named "SSLVersionMax"
4. Set its value to "tls1.3"

### Linux

On Linux systems:

1. Locate the Firefox configuration file. This is typically in:
   ```
   ~/.mozilla/firefox/<profile>/prefs.js
   ```
2. Add or modify the following line:
   ```
   user_pref("security.tls.version.max", 4);
   ```
3. Save the file and restart Firefox

For system-wide configuration:

1. Create or edit the file:
   ```
   /etc/firefox/syspref.js
   ```
2. Add the following line:
   ```
   pref("security.tls.version.max", 4);
   ```
3. Save the file. This will apply to all users on the system.

Remember to test these changes thoroughly in a controlled environment before applying them widely, as they may impact compatibility with some websites or services that don't support TLS 1.3.