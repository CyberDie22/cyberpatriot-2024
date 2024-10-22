# (L1) Ensure 'Do not allow preferences to be changed' is set to 'Enabled'

## Description

This configuration setting determines whether Firefox will provide geographic location information to websites. The recommended state for this setting is: Enabled.

The policy "Do not allow preferences to be changed" for the Firefox Location permission, when set to "Enabled", prevents users from modifying Firefox's location settings. This effectively disables the ability of web applications to request a user's location.

**Impact:**
- Critical functionality loss: Websites requiring location access (e.g., Google Maps, navigation apps) will not function correctly.
- User frustration: Applications requiring location access will fail to work as intended for all users.
- Potential security implications: Users may attempt to circumvent the policy, introducing unintended security risks.

**Rationale:** Geo-location services can expose private information to remote websites.

## Audit

### Windows:

1. Open the Group Policy Management Console (gpmc.msc).
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Permissions\Location\Do not allow preferences to be changed
   ```
3. Verify that the setting is set to "Enabled".

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe).
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Permissions\Location
   ```
3. Verify that the "Locked" value exists and is set to 1 (REG_DWORD).

### Linux:

On Linux systems, Firefox policies are typically managed through a JSON file. To audit the setting:

1. Locate the policy file, usually at `/etc/firefox/policies/policies.json`.
2. Check for the following configuration:
   ```json
   {
     "policies": {
       "Permissions": {
         "Location": {
           "Locked": true
         }
       }
     }
   }
   ```

## Remediation

### Windows:

1. Download the Firefox Group Policy template (firefox.admx/adml) from: https://github.com/mozilla/policy-templates/releases
2. Install the template in your Group Policy Central Store or local machine.
3. Open the Group Policy Management Console (gpmc.msc).
4. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Permissions\Location\Do not allow preferences to be changed
   ```
5. Set the policy to "Enabled".

### Linux:

1. Create or edit the file `/etc/firefox/policies/policies.json`.
2. Ensure it contains the following configuration:
   ```json
   {
     "policies": {
       "Permissions": {
         "Location": {
           "Locked": true
         }
       }
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect.

Note: Ensure that this policy aligns with your organization's security requirements and user needs, as it can significantly impact the functionality of web applications that rely on location services.