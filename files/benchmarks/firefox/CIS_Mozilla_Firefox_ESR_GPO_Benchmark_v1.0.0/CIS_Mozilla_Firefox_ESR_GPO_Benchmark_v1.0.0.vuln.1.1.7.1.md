# (L1) Ensure 'TLS_RSA_WITH_3DES_EDE_CBC_SHA' is set to 'Enabled'

## Description

This policy setting controls the use of the TLS_RSA_WITH_3DES_EDE_CBC_SHA cipher suite in Mozilla Firefox. Cipher suites are a group of algorithms that help secure network connections. The recommended state for this setting is: Enabled (which means the cipher suite is disabled).

The Triple Data Encryption Algorithm (TDEA), also known as Triple DES (3DES), was deprecated by NIST in 2019. 3DES is now considered an insecure cipher suite and should not be used. Enabling this policy setting effectively disables the use of this weak cipher suite in Firefox, improving the overall security posture of the browser.

Disabling this cipher suite might impact compatibility with very old software and hardware that relies on 3DES. However, keeping it enabled represents a significant security risk due to the known weaknesses of the 3DES algorithm.

This configuration aligns with the CIS Control framework for encrypting sensitive data in transit, emphasizing the importance of using strong encryption for secure communications in modern environments.

## Audit

To audit this setting:

1. Open the Group Policy Management Console (gpmc.msc)
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Disabled Ciphers\TLS_RSA_WITH_3DES_EDE_CBC_SHA
   ```
3. Verify that the setting is configured as "Enabled"

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe)
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\DisabledCiphers
   ```
3. Verify that the "TLS_RSA_WITH_3DES_EDE_CBC_SHA" value exists and is set to 1 (DWORD)

## Remediation

### Windows:

To establish the recommended configuration via Group Policy:

1. Ensure you have the Mozilla Firefox Group Policy template (firefox.admx/adml) installed. If not, download it from: https://github.com/mozilla/policy-templates/releases
2. Open the Group Policy Management Console (gpmc.msc)
3. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Disabled Ciphers\TLS_RSA_WITH_3DES_EDE_CBC_SHA
   ```
4. Set the policy to "Enabled"
5. Run `gpupdate /force` on the target systems to apply the changes

### Linux:

For Linux systems running Firefox, you can disable the TLS_RSA_WITH_3DES_EDE_CBC_SHA cipher suite by creating or modifying the Firefox configuration file:

1. Locate the Firefox configuration file. It's typically in one of these locations:
   - `/etc/firefox/policies/policies.json` (system-wide)
   - `~/.mozilla/firefox/<profile>/user.js` (user-specific)
2. Add or modify the following content:

   ```json
   {
     "policies": {
       "DisabledCiphers": {
         "TLS_RSA_WITH_3DES_EDE_CBC_SHA": true
       }
     }
   }
   ```

3. Save the file and restart Firefox for the changes to take effect

Note: The exact location and method may vary depending on your Linux distribution and Firefox installation. Consult your system's documentation for specific details.