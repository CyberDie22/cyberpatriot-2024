# (L1) Ensure 'Allow add-on installs from websites' is set to 'Disabled'

## Description

This vulnerability relates to a security configuration issue in Firefox that allows websites to automatically install add-ons without an allow list. When enabled, this setting poses a significant security risk as malicious add-ons can be installed automatically, potentially compromising user sessions, data, and modifying Firefox's behavior in harmful ways.

Add-ons are extensions of the browser that add new functionality to Firefox or change its appearance. These run in a user session, allowing them to manipulate data and alter the way Firefox interacts with other applications and user commands. If malicious add-ons are installed automatically, a user's security could be completely compromised.

The recommended state for this setting is: Disabled.

Note: If this setting is enabled, an allow list will be needed for approved add-ons.

## Audit

### Windows

1. Open the Group Policy Management Console (gpmc.msc).
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Addons\Allow add-on installs from websites
   ```
3. Verify that the setting is set to "Disabled".

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe).
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\InstallAddonsPermission
   ```
3. Verify that the "Default" value is set to 0 (REG_DWORD).

### Linux

Firefox policies on Linux are typically managed through a JSON configuration file. To audit the setting:

1. Check for the existence of the policy file:
   ```
   /usr/lib/firefox/distribution/policies.json
   ```
2. If the file exists, verify that it contains the following configuration:
   ```json
   {
     "policies": {
       "InstallAddonsPermission": {
         "Default": false
       }
     }
   }
   ```

## Remediation

### Windows

To establish the recommended configuration via Group Policy:

1. Ensure you have the necessary Firefox Group Policy template (firefox.admx/adml). If not, download it from: https://github.com/mozilla/policy-templates/releases
2. Open the Group Policy Management Console (gpmc.msc).
3. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Addons\Allow add-on installs from websites
   ```
4. Set the policy to "Disabled".

### Linux

To remediate this issue on Linux:

1. Create or edit the Firefox policy file:
   ```
   sudo nano /usr/lib/firefox/distribution/policies.json
   ```
2. Add or modify the content to include:
   ```json
   {
     "policies": {
       "InstallAddonsPermission": {
         "Default": false
       }
     }
   }
   ```
3. Save the file and exit the editor.
4. Restart Firefox for the changes to take effect.