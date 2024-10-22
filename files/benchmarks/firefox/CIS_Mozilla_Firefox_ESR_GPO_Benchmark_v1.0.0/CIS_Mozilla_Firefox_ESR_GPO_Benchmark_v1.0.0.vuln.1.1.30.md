# (L1) Ensure 'Disable Forget Button' is set to 'Enabled'

## Description

This policy setting determines whether the Forget button is available in Mozilla Firefox. This feature, also known as eCleaner, allows a user to quickly delete browser data from a selected time frame without affecting the rest of the data. The recommended state for this setting is: Enabled.

Disabling the Forget button can have significant implications for computer forensics and investigations. When this feature is unavailable, it becomes challenging to isolate specific browsing data for analysis, making incident response more time-consuming and difficult to manage. This configuration issue affects all users of Firefox on systems with the incorrect policy, and is especially relevant for organizations where computer forensics or system administration is critical.

The severity of this vulnerability is considered Medium to High, depending on the organization's needs for forensic capabilities.

## Audit

To audit this setting:

1. Open the Group Policy Management Console (gpmc.msc).
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Disable Forget Button
   ```
3. Verify that the setting is configured as "Enabled".

Alternatively, you can check the registry:

**Windows:**
1. Open the Registry Editor (regedit.exe).
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```
3. Verify that the "DisableForgetButton" value exists and is set to 1 (DWORD).

**Linux:**
Firefox policies on Linux are typically managed through a JSON file. Check the following locations for a policy file:
- `/etc/firefox/policies/policies.json`
- `/usr/lib/firefox/distribution/policies.json`

Ensure the file contains the following configuration:
```json
{
  "policies": {
    "DisableForgetButton": true
  }
}
```

## Remediation

To remediate this issue:

**Windows:**
1. Download the necessary Group Policy template (firefox.admx/adml) from: https://github.com/mozilla/policy-templates/releases
2. Copy the .admx file to `C:\Windows\PolicyDefinitions` and the .adml file to the appropriate language subfolder.
3. Open the Group Policy Management Console (gpmc.msc).
4. Navigate to:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Disable Forget Button
   ```
5. Set the policy to "Enabled".
6. Run `gpupdate /force` to apply the changes.

**Linux:**
1. Create or edit the policy file at `/etc/firefox/policies/policies.json` (system-wide) or `/usr/lib/firefox/distribution/policies.json` (for specific Firefox installation).
2. Add or modify the following content:
   ```json
   {
     "policies": {
       "DisableForgetButton": true
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect.

After applying these changes, verify the settings as described in the Audit section to ensure they have been applied correctly.