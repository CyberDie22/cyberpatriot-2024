# (L1) Ensure 'Extension Update' is set to 'Enabled'

## Description

This policy setting configures Firefox to automatically download and install extension updates as they become available. The recommended state for this setting is: Enabled.

Enabling automatic extension updates is a best practice for security. It ensures that extensions are kept up-to-date with the latest security patches, mitigating known software bugs and vulnerabilities. Outdated extensions can contain vulnerabilities that malicious actors may exploit, making timely updates crucial for maintaining a secure browsing environment.

## Audit

To audit this setting:

### Windows:
1. Open the Group Policy Management Console (gpmc.msc).
2. Navigate to the following UI path:
   `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Extensions\Extension Update`
3. Verify that the setting is set to "Enabled".

Alternatively, you can check the registry:
1. Open the Registry Editor (regedit.exe).
2. Navigate to the following key:
   `HKLM\SOFTWARE\Policies\Mozilla\Firefox`
3. Verify that the "ExtensionUpdate" value exists and is set to 1 (REG_DWORD).

### Linux:
1. Check the Firefox configuration file (usually located at `/etc/firefox/policies/policies.json`).
2. Look for the "ExtensionUpdate" policy and ensure it is set to true.

## Remediation

To implement the recommended configuration:

### Windows:
1. Open the Group Policy Management Console (gpmc.msc).
2. Navigate to the following UI path:
   `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Extensions\Extension Update`
3. Set the policy to "Enabled".

Note: If the Group Policy path does not exist, you may need to download and install the additional Firefox Group Policy template (firefox.admx/adml) from Mozilla's official website.

### Linux:
1. Edit the Firefox configuration file (usually located at `/etc/firefox/policies/policies.json`).
2. Add or modify the "ExtensionUpdate" policy:
   ```json
   {
     "policies": {
       "ExtensionUpdate": true
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect.

Implementing this policy ensures that Firefox extensions are kept up-to-date automatically, enhancing the overall security posture of the browser.