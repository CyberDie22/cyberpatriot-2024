# (L1) Ensure 'Locked' is set to 'Enabled'

## Description

This policy setting controls whether the Firefox browser deletes user data upon closing. When properly configured, it ensures that browsing history, cookies, cache, and other potentially sensitive information are automatically cleared when the browser is shut down. 

The vulnerability arises when this setting is incorrectly configured (i.e., set to "Disabled" or not properly implemented). This misconfiguration can lead to:

1. Unintentional preservation of user data, which may violate privacy policies or data retention regulations.
2. Potential loss of critical forensic evidence in the event of a security incident or investigation.

The impact of this vulnerability is particularly significant for organizations that rely on browser data for forensic analysis or those that must comply with strict data privacy regulations.

## Audit

To verify the correct configuration:

### Windows:

1. Open the Group Policy Management Console (gpmc.msc).
2. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Clear data when browser is closed
3. Verify that the 'Locked' setting is set to 'Enabled'.

Alternatively, check the registry:

1. Open the Registry Editor (regedit.exe).
2. Navigate to: HKLM\SOFTWARE\Policies\Mozilla\Firefox\SanitizeOnShutdown
3. Verify that the 'Locked' value is set to 1 (REG_DWORD).

### Linux:

Firefox policies on Linux are typically managed through a JSON configuration file.

1. Check for the existence of the policy file:
   ```
   ls /etc/firefox/policies/
   ```
2. If present, examine the contents of the `policies.json` file:
   ```
   cat /etc/firefox/policies/policies.json
   ```
3. Look for a configuration similar to:
   ```json
   {
     "policies": {
       "SanitizeOnShutdown": {
         "Locked": true
       }
     }
   }
   ```

## Remediation

To establish the recommended configuration:

### Windows:

1. Ensure the necessary Firefox Group Policy template (firefox.admx/adml) is installed. It can be downloaded from: https://github.com/mozilla/policy-templates/releases
2. Open the Group Policy Management Console (gpmc.msc).
3. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Clear data when browser is closed
4. Set the 'Locked' setting to 'Enabled'.

### Linux:

1. Create or edit the Firefox policy file:
   ```
   sudo mkdir -p /etc/firefox/policies
   sudo nano /etc/firefox/policies/policies.json
   ```
2. Add or modify the following configuration:
   ```json
   {
     "policies": {
       "SanitizeOnShutdown": {
         "Locked": true
       }
     }
   }
   ```
3. Save the file and exit the editor.
4. Ensure the file has the correct permissions:
   ```
   sudo chmod 644 /etc/firefox/policies/policies.json
   ```

After applying these changes, restart Firefox for the new policy to take effect.